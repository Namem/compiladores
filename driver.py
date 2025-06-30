import sys
import platform
from llvmlite import binding
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker, InputStream, Token
from antlr4.error.ErrorListener import ErrorListener
from CompiladorLexer import CompiladorLexer
from CompiladorParser import CompiladorParser
from SemanticAnalyzer import AnalisadorSemantico
from CodeGeneratorLLVM import LLVMCodeGenerator
from ast_visualizer import ASTVisualizer

# Listener customizado para erros
class MeuErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.erros = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        erro = f"\033[91mERRO SINTÁTICO [Linha {line}, Coluna {column}]: {msg}\033[0m"
        self.erros.append(erro)
        print(erro)

def get_target_triple():
    """Detecta automaticamente o target triple do sistema"""
    machine = platform.machine().lower()
    system = platform.system().lower()
    
    # Mapear arquitetura
    if machine in ['x86_64', 'amd64']:
        arch = 'x86_64'
    elif machine in ['i386', 'i686']:
        arch = 'i386'
    elif machine in ['arm64', 'aarch64']:
        arch = 'aarch64'
    elif machine.startswith('arm'):
        arch = 'arm'
    elif machine.startswith('mips'):
        arch = 'mips'
    elif machine.startswith('riscv'):
        arch = machine  # riscv32 ou riscv64
    else:
        arch = 'unknown'
    
    # Mapear sistema
    if system == 'linux':
        return f"{arch}-unknown-linux-gnu"
    elif system == 'windows':
        return f"{arch}-pc-windows-msvc"
    elif system == 'darwin':  # macOS
        return f"{arch}-apple-darwin"
    elif system == 'freebsd':
        return f"{arch}-unknown-freebsd"
    else:
        return f"{arch}-unknown-unknown"

def print_system_info():
    """Imprime informações do sistema detectado"""
    target = get_target_triple()
    print(f"\033[96m[Sistema] Arquitetura: {platform.machine()}\033[0m")
    print(f"\033[96m[Sistema] Sistema: {platform.system()} {platform.release()}\033[0m")
    print(f"\033[96m[Sistema] Target Triple: {target}\033[0m")
    return target

def main(argv):
    if len(argv) < 2:
        print("Uso: python driver.py <arquivo_fonte>")
        sys.exit(1)

    # Mostrar informações do sistema
    print("\n\033[96m***************** INFORMAÇÕES DO SISTEMA *****************\033[0m")
    target_triple = print_system_info()

    # Ler entrada
    try:
        with open(argv[1], 'r', encoding='utf-8') as f:
            input_text = f.read()
    except FileNotFoundError:
        print(f"\033[91mERRO: Arquivo '{argv[1]}' não encontrado.\033[0m")
        sys.exit(1)

    print("\n\033[96m***************** INPUT *****************\033[0m")
    print(input_text)

    # 1) ANÁLISE LÉXICA
    print("\n\033[92m***************** ANÁLISE LÉXICA *****************\033[0m")
    input_stream = InputStream(input_text)
    lexer = CompiladorLexer(input_stream)

    # Adicionar listener de erro ao lexer
    lexer_error_listener = MeuErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(lexer_error_listener)

    stream = CommonTokenStream(lexer)

    # Verificar erros léxicos
    stream.fill()
    if lexer_error_listener.erros:
        print("\n\033[91mO programa foi encerrado devido a erro(s) léxicos.\033[0m")
        sys.exit(1)

    # Mostrar Tokens
    print("\n\033[92m***************** TOKENS *****************\033[0m")
    for token in stream.tokens:
        if token.type != Token.EOF:
            token_name = lexer.symbolicNames[token.type] if token.type < len(lexer.symbolicNames) else f"UNKNOWN_{token.type}"
            print(f"<{token_name}, '{token.text}', Linha {token.line}, Coluna {token.column}>")

    # 2) ANÁLISE SINTÁTICA
    print("\n\033[93m***************** ANÁLISE SINTÁTICA *****************\033[0m")
    parser = CompiladorParser(stream)
    parser_error_listener = MeuErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(parser_error_listener)

    tree = parser.programa()

    if parser_error_listener.erros:
        print("\n\033[91mO programa foi encerrado devido a erro(s) sintáticos.\033[0m")
        sys.exit(1)

    # Árvore sintática
    print("\n\033[93m***************** ÁRVORE SINTÁTICA *****************\033[0m")
    print(tree.toStringTree(recog=parser))

    # Gerar visualização da árvore usando ast_visualizer.py
    print("\n\033[93m***************** GERAÇÃO DA ÁRVORE VISUAL *****************\033[0m")
    try:
        visualizer = ASTVisualizer()
        visualizer.visualizar(tree, parser)
    except Exception as e:
        print(f"\033[93m[AST] Aviso: Erro na geração da árvore visual: {e}\033[0m")

    # 3) ANÁLISE SEMÂNTICA
    print("\n\033[94m***************** ANÁLISE SEMÂNTICA *****************\033[0m")
    semantic = AnalisadorSemantico()
    walker = ParseTreeWalker()
    walker.walk(semantic, tree)
    
    if semantic.errors:
        for err in semantic.errors: 
            print(err)
        print("\n\033[91mO programa foi encerrado devido a erro(s) semânticos.\033[0m")
        sys.exit(1)

    # Mostrar logs semânticos
    if hasattr(semantic, 'logs'):
        for log in semantic.logs:
            print(f"[Semântico] {log}")

    print("\033[92m[Semântico] Análise semântica concluída com sucesso!\033[0m")

    # 4) GERAÇÃO DE CÓDIGO LLVM-IR
    print("\n\033[95m***************** GERAÇÃO DE CÓDIGO LLVM-IR *****************\033[0m")
    try:
        # Usar apenas uma instância do gerador com Visitor pattern
        generator = LLVMCodeGenerator(semantic.symbols, target_triple=target_triple)
        
        # Usar visit em vez de walker
        result = generator.visit(tree)
        llvm_ir = generator.finalize()

        print("\033[92m[CodeGen] Código LLVM-IR gerado com sucesso!\033[0m")
        print(f"\033[96m[CodeGen] Target: {target_triple}\033[0m")
        print("\n\033[95m***************** CÓDIGO LLVM-IR *****************\033[0m")
        print(llvm_ir)

        # 5) INICIALIZAÇÃO DO LLVM
        print("\n\033[96m***************** INICIALIZAÇÃO LLVM *****************\033[0m")
        try:
            binding.initialize()
            binding.initialize_native_target()
            binding.initialize_native_asmprinter()
            print("\033[92m[LLVM] Inicialização concluída com sucesso!\033[0m")
        except Exception as e:
            print(f"\033[93m[LLVM] Aviso: Erro na inicialização LLVM: {e}\033[0m")

        # Salvar o IR em arquivo
        output_file = argv[1].replace('.txt', '.ll')
        try:
            with open(output_file, 'w') as f:
                f.write(str(llvm_ir))
            print(f"\033[92m[Output] Código LLVM-IR salvo em: {output_file}\033[0m")
        except Exception as e:
            print(f"\033[93m[Output] Aviso: Não foi possível salvar o arquivo: {e}\033[0m")

        # 6) COMPILAÇÃO PARA CÓDIGO NATIVO (Opcional)
        print("\n\033[97m***************** GERAÇÃO DE CÓDIGO NATIVO *****************\033[0m")
        
        # Tentar compilar com diferentes ferramentas
        asm_file = argv[1].replace('.txt', '.s')
        obj_file = argv[1].replace('.txt', '.o')
        exe_file = argv[1].replace('.txt', '.exe' if sys.platform == 'win32' else '')
        
        try:
            import subprocess
            
            # Lista de possíveis comandos LLC
            llc_commands = ['llc', 'llc.exe', 'llc-18', 'llc-17', 'llc-16', 'llc-15']
            clang_commands = ['clang', 'clang.exe', 'clang-18', 'clang-17', 'clang-16', 'clang-15']
            
            llc_found = None
            clang_found = None
            
            # Tentar encontrar LLC
            for cmd in llc_commands:
                try:
                    result = subprocess.run([cmd, '--version'], capture_output=True, text=True)
                    if result.returncode == 0:
                        llc_found = cmd
                        print(f"\033[92m[Compile] Encontrado LLC: {cmd}\033[0m")
                        break
                except FileNotFoundError:
                    continue
            
            # Tentar encontrar Clang
            for cmd in clang_commands:
                try:
                    result = subprocess.run([cmd, '--version'], capture_output=True, text=True)
                    if result.returncode == 0:
                        clang_found = cmd
                        print(f"\033[92m[Compile] Encontrado Clang: {cmd}\033[0m")
                        break
                except FileNotFoundError:
                    continue
            
            if llc_found and clang_found:
                # 1. LLVM-IR para Assembly (usando target específico)
                print(f"\033[93m[Compile] Gerando assembly: {asm_file}\033[0m")
                result = subprocess.run([llc_found, output_file, '-o', asm_file, f'-mtriple={target_triple}'], 
                                      capture_output=True, text=True)
                if result.returncode == 0:
                    print(f"\033[92m[Compile] Assembly gerado com sucesso!\033[0m")
                    
                    # 2. Assembly para objeto
                    print(f"\033[93m[Compile] Gerando arquivo objeto: {obj_file}\033[0m")
                    result = subprocess.run([clang_found, '-c', asm_file, '-o', obj_file], 
                                          capture_output=True, text=True)
                    if result.returncode == 0:
                        print(f"\033[92m[Compile] Arquivo objeto gerado com sucesso!\033[0m")
                        
                        # 3. Linking para executável
                        print(f"\033[93m[Compile] Gerando executável: {exe_file}\033[0m")
                        result = subprocess.run([clang_found, obj_file, '-o', exe_file], 
                                              capture_output=True, text=True)
                        if result.returncode == 0:
                            print(f"\033[92m[Compile] Executável gerado com sucesso!\033[0m")
                            print(f"\033[96m[Info] Execute com: ./{exe_file}\033[0m")
                        else:
                            print(f"\033[93m[Compile] Erro no linking: {result.stderr}\033[0m")
                    else:
                        print(f"\033[93m[Compile] Erro na compilação: {result.stderr}\033[0m")
                else:
                    print(f"\033[93m[Compile] Erro no LLC: {result.stderr}\033[0m")
            
            elif clang_found and not llc_found:
                # Tentar compilar direto com clang (se suportar LLVM-IR)
                print(f"\033[93m[Compile] LLC não encontrado, tentando clang diretamente...\033[0m")
                result = subprocess.run([clang_found, output_file, '-o', exe_file, f'--target={target_triple}'], 
                                      capture_output=True, text=True)
                if result.returncode == 0:
                    print(f"\033[92m[Compile] Executável gerado com sucesso!\033[0m")
                    print(f"\033[96m[Info] Execute com: ./{exe_file}\033[0m")
                else:
                    print(f"\033[93m[Compile] Clang não conseguiu compilar LLVM-IR diretamente\033[0m")
                    print(f"\033[93m[Compile] {result.stderr}\033[0m")
                    print_manual_instructions(target_triple)
            else:
                print_manual_instructions(target_triple)
                
        except Exception as e:
            print(f"\033[93m[Compile] Erro na compilação: {e}\033[0m")
            print_manual_instructions(target_triple)

    except Exception as e:
        print(f"\033[91m[CodeGen] ERRO na geração de código: {e}\033[0m")
        sys.exit(1)

    print("\n\033[92m***************** COMPILAÇÃO CONCLUÍDA *****************\033[0m")

def print_manual_instructions(target_triple=None):
    """Imprime instruções para compilação manual"""
    print(f"\033[93m[Compile] Ferramentas LLVM não encontradas ou não funcionais.\033[0m")

if __name__ == '__main__':
    main(sys.argv)
