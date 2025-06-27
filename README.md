# Compilador - Projeto de Compiladores

Este projeto implementa um compilador completo utilizando ANTLR4 que realiza análise léxica, sintática, semântica e geração de código LLVM-IR. O compilador processa uma linguagem personalizada e gera código intermediário executável.

##  Estrutura do Projeto

- `Compilador.g4`: Arquivo de gramática ANTLR4 que define a linguagem
- `CompiladorLexer.py`, `CompiladorParser.py`, `CompiladorListener.py`: Arquivos gerados automaticamente pelo ANTLR4
- `driver.py`: Script principal que executa todas as fases do compilador
- `SemanticAnalyzer.py`: Analisador semântico que verifica tipos e declarações
- `CodeGeneratorLLVM.py`: Gerador de código LLVM-IR
- `ast_visualizer.py`: Visualizador da Árvore de Derivação (AST) com Graphviz
- `exemplos/`: Diretório com exemplos de código (triangulo.txt, pascal.txt, etc.)
- `requirements.txt`: Lista de dependências Python necessárias

##  Pré-requisitos

- Python 3.8 ou superior
- [ANTLR4](https://www.antlr.org/) versão 4.13.2 ou superior
- [Graphviz](https://graphviz.org/) para visualização da AST
- [LLVM](https://llvm.org/) para execução do código gerado (opcional)

### Instalação das Dependências

1. Instale as dependências Python:
```bash
pip install -r requirements.txt
```

2. Instale o Graphviz:
```bash
# Windows (via Chocolatey)
choco install graphviz

# macOS (via Homebrew)
brew install graphviz

# Ubuntu/Debian
sudo apt-get install graphviz

# Ou via pip
pip install graphviz
```

##  Como Executar

### 1. Gerar os Arquivos do Parser (se necessário)

Se você modificou a gramática, regenere os arquivos:

```bash
# Com ANTLR4 instalado globalmente
antlr4 -Dlanguage=Python3 Compilador.g4

# Ou usando o JAR diretamente
java -jar antlr/antlr-4.13.2-complete.jar -Dlanguage=Python3 Compilador.g4
```

### 2. Executar o Compilador

O compilador processa automaticamente todas as fases:

```bash
# Executar com um arquivo de exemplo
python driver.py exemplos/triangulo.txt
python driver.py exemplos/pascal.txt
```

### 3. Saídas Geradas

O compilador gera automaticamente:
- **Tokens**: Lista de tokens reconhecidos
- **AST Visual**: `ast.dot` e `ast.png` (árvore sintática visual)
- **Código LLVM-IR**: `arquivo.ll` (código intermediário)
- **Logs**: Análise semântica detalhada

##  Fases do Compilador

### 1. **Análise Léxica**
- Reconhece tokens da linguagem
- Reporta erros léxicos com posição

### 2. **Análise Sintática** 
- Constrói a árvore sintática (AST)
- Detecta erros de sintaxe
- Gera visualização da AST

### 3. **Análise Semântica**
- Verifica tipos de dados
- Valida declarações de variáveis
- Detecta incompatibilidades de operadores

### 4. **Geração de Código LLVM-IR**
- Gera código intermediário LLVM
- Suporte a operações aritméticas e lógicas
- Geração de funções e variáveis

##  Exemplos

O diretório `exemplos/` contém arquivos de teste:

- **`triangulo.txt`**: Programa que calcula área de triângulo
- **`pascal.txt`**: Exemplo com estruturas condicionais e loops
- **`divstring.txt`**: Teste de erro semântico (divisão por string)
- **`divzero.txt`**: Teste de divisão por zero

### Exemplo de Execução

```bash
$ python driver.py exemplos/triangulo.txt

***************** INPUT *****************
programa
    var x: int;
    var y: int;
    var z: int;
    
    x = 10;
    y = 20;
    z = x + y * 2;
    
    print z;
fim

***************** ANÁLISE LÉXICA *****************
<PROGRAMA, 'programa', Linha 1, Coluna 0>
<VAR, 'var', Linha 2, Coluna 4>
...

***************** ANÁLISE SINTÁTICA *****************
(programa ...)

***************** GERAÇÃO DA ÁRVORE VISUAL *****************
Arquivo 'ast.dot' gerado!
Imagem 'ast.png' gerada com sucesso!

***************** ANÁLISE SEMÂNTICA *****************
[Semântico] Variável 'x' declarada com tipo 'int'
[Semântico] Análise semântica concluída com sucesso!

***************** GERAÇÃO DE CÓDIGO LLVM-IR *****************
[CodeGen] Código LLVM-IR gerado com sucesso!

***************** CÓDIGO LLVM-IR *****************
; ModuleID = "main"
target triple = "unknown-unknown-unknown"
...

***************** COMPILAÇÃO CONCLUÍDA *****************
```

##  Tratamento de Erros

O compilador detecta e reporta:

- **Erros Léxicos**: Caracteres inválidos
- **Erros Sintáticos**: Estruturas malformadas  
- **Erros Semânticos**: Tipos incompatíveis, variáveis não declaradas

### Exemplo de Erro Semântico:
```bash
$ python driver.py exemplos/divstring.txt

[ERRO SEMÂNTICO] Operação '/' exige operandos inteiros, mas recebeu 'int' e 'string'.
```

##  Tecnologias Utilizadas

- **ANTLR4**: Geração de lexer e parser
- **Python 3.8+**: Linguagem de implementação
- **llvmlite**: Geração de código LLVM-IR
- **Graphviz**: Visualização da AST
- **subprocess**: Integração com ferramentas externas

##  Gramática da Linguagem

A linguagem suporta:

### Declarações
```
var nome: tipo;        // Declaração de variável
```

### Tipos de Dados
- `int`: Números inteiros
- `string`: Cadeias de caracteres

### Operadores
- **Aritméticos**: `+`, `-`, `*`, `/`
- **Comparação**: `<`, `>`, `<=`, `>=`
- **Igualdade**: `==`, `~=`
- **Lógicos**: `&&`, `||`

### Estruturas de Controle
```
se (condicao) entao
    // comandos
senao
    // comandos
fim

enquanto (condicao) faca
    // comandos
fim
```

### Entrada/Saída
```
read nome;            // Leitura
print expressao;      // Escrita
```

##  Licença

Este projeto está licenciado sob a [MIT License](LICENSE).


##  Créditos

- **Autores Principais**: [@Namem](https://github.com/Namem) e [@cmigos1](https://github.com/cmigos1)
- **Orientador**: [@edwilsonferreira](https://github.com/edwilsonferreira)