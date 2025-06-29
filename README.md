# MiniLua - Projeto de Compiladores

Este projeto implementa um compilador completo utilizando ANTLR4 que realiza análise léxica, sintática, semântica e geração de código LLVM-IR. O compilador processa uma linguagem personalizada e gera código intermediário executável que pode ser compilado para assembly nativo.

## Características Principais

- **Compilador Completo**: Análise léxica, sintática, semântica e geração de código
- **Geração LLVM-IR**: Código intermediário otimizado e portável
- **Compilação Nativa**: Geração automática de executáveis via LLVM/Clang
- **Estruturas de Controle**: Condicionais (`se/senao`) e loops (`enquanto`)
- **Expressões Complexas**: Operadores aritméticos, lógicos e de comparação
- **Entrada/Saída**: Comandos `leia()` e `escreva()` para interação
- **Visualização AST**: Geração automática de diagramas da árvore sintática
- **Detecção de Erros**: Relatórios detalhados de erros em todas as fases

## Estrutura do Projeto

```
bencao/
├── Compilador.g4              # Gramática ANTLR4 da linguagem
├── CompiladorLexer.py         # Lexer gerado automaticamente
├── CompiladorParser.py        # Parser gerado automaticamente  
├── CompiladorBaseVisitor.py   # Visitor base para percorrer AST
├── driver.py                  # Script principal do compilador
├── SemanticAnalyzer.py        # Analisador semântico
├── CodeGeneratorLLVM.py       # Gerador de código LLVM-IR
├── ast_visualizer.py          # Visualizador da AST com Graphviz
├── exemplos/                  # Exemplos de programas
│   ├── triangulo.txt          # Classificação de triângulos
│   ├── pascal.txt             # Triângulo de Pascal
│   ├── divstring.txt          # Teste de erro semântico
│   └── divzero.txt            # Teste de divisão por zero
├── requirements.txt           # Dependências Python
└── README.md                  # Este arquivo
```

## Pré-requisitos

### Software Necessário
- **Python 3.8+**: Linguagem de implementação
- **ANTLR4 4.13.2+**: Geração de lexer/parser
- **Graphviz**: Visualização da AST
- **LLVM/Clang**: Compilação para executável (opcional)

### Instalação das Dependências

#### 1. Dependências Python
```bash
pip install -r requirements.txt
```

#### 2. Graphviz (Visualização AST)
```bash
# Ubuntu/Debian
sudo apt-get install graphviz

# macOS (Homebrew)
brew install graphviz

# Windows (Chocolatey)
choco install graphviz
```

#### 3. LLVM/Clang (Compilação Nativa)
```bash
# Ubuntu/Debian
sudo apt-get install llvm clang

# macOS (Homebrew)
brew install llvm

# Windows
# Baixar de https://releases.llvm.org/
```

## Como Executar

### 1. Gerar Parser (se modificou a gramática)
```bash
# Com ANTLR4 instalado
antlr4 -Dlanguage=Python3 Compilador.g4

# Ou com JAR
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 Compilador.g4
```

### 2. Compilar e Executar Programas
```bash
# Compilação completa (todas as fases)
python driver.py exemplos/triangulo.txt

# Execução do programa gerado
./exemplos/triangulo
```

### 3. Exemplos Disponíveis
```bash
# Classificação de triângulos (condicionais aninhadas)
python driver.py exemplos/triangulo.txt

# Triângulo de Pascal (loops aninhados)
python driver.py exemplos/pascal.txt

# Teste de erro semântico
python driver.py exemplos/divstring.txt
```

## Fases do Compilador

### 1. **Análise Léxica**
- Tokenização completa do código fonte
- Detecção de erros léxicos com localização precisa
- Suporte a comentários (`--`) e strings com escape sequences

### 2. **Análise Sintática**
- Construção da Árvore Sintática Abstrata (AST)
- Detecção de erros de sintaxe
- Geração automática de visualização (`ast.png`)

### 3. **Análise Semântica**
- Verificação de tipos de dados
- Validação de declarações de variáveis
- Detecção de operações incompatíveis
- Análise de escopo

### 4. **Geração de Código LLVM-IR**
- Código intermediário otimizado
- Suporte completo a estruturas de controle
- Geração de funções `printf`/`scanf` para I/O
- Target específico para arquitetura

### 5. **Compilação Nativa**
- Compilação automática para assembly (.s)
- Linking para executável nativo
- Suporte multiplataforma (x86_64, ARM, etc.)

## Saídas Geradas

Para cada arquivo compilado, o sistema gera:

```
exemplos/triangulo.txt → 
├── triangulo.ll       # Código LLVM-IR
├── triangulo.s        # Assembly nativo
├── triangulo          # Executável
├── ast.dot            # Descrição da AST
└── ast.png            # Visualização da AST
```

## Linguagem Suportada

### Estrutura do Programa
```pascal
variaveis
    nome:tipo;
    valor:int;

// Corpo do programa
comando1;
comando2;
```

### Tipos de Dados
- **`int`**: Números inteiros (32-bit)
- **`string`**: Cadeias de caracteres UTF-8

### Declarações
```pascal
variaveis
    contador:int;
    mensagem:string;
```

### Operadores

#### Aritméticos
```pascal
resultado = a + b * c - d / e;
```

#### Comparação
```pascal
se a < b entao
se x >= y entao
se nome == "teste" entao
```

#### Lógicos
```pascal
se a > 0 && b < 10 entao
se x == 1 || y == 2 entao
```

### Estruturas de Controle

#### Condicionais
```pascal
se condicao entao
    escreva("Verdadeiro");
senao
    escreva("Falso");
fim
```

#### Loops
```pascal
enquanto contador <= 10 faca
    escreva(contador);
    contador = contador + 1;
fim
```

### Entrada/Saída
```pascal
escreva("Digite um número:");
leia(numero);
escreva("Resultado: ");
escreva(numero * 2);
```

## Exemplos Completos

### 1. Classificação de Triângulos
```pascal
variaveis 
a:int;
b:int;
c:int;

escreva("Digite o primeiro lado:");
leia(a);
escreva("Digite o segundo lado:");
leia(b);
escreva("Digite o terceiro lado:");
leia(c);

se a == b && b == c entao
    escreva("Equilatero");
senao
    se a == b || a == c || b == c entao
        escreva("Isosceles");
    senao
        escreva("Escaleno");
    fim
fim
```

### 2. Triângulo de Pascal
```pascal
variaveis
    linha:int;
    i:int;
    j:int;
    valor:int;
    n:int;

escreva("Digite o numero de linhas:");
leia(n);
linha = 0;

enquanto linha <= n faca
    i = 0;
    enquanto i <= linha faca
        valor = 1;
        j = 0;
        enquanto j < i faca
            valor = valor * (linha - j);
            valor = valor / (j + 1);
            j = j + 1;
        fim
        
        escreva(valor);
        i = i + 1;
    fim
    linha = linha + 1;
fim
```

## Tratamento de Erros

### Erros Léxicos
```
[ERRO LÉXICO] Caractere inválido '#' na linha 5, coluna 12
```

### Erros Sintáticos
```
[ERRO SINTÁTICO] Token inesperado 'fim' na linha 8, coluna 0
Esperado: 'entao'
```

### Erros Semânticos
```
[ERRO SEMÂNTICO] Operação '/' exige operandos inteiros, mas recebeu 'int' e 'string'.
[ERRO SEMÂNTICO] Variável 'x' não foi declarada.
[ERRO SEMÂNTICO] Incompatibilidade de tipos na atribuição: esperado 'int', recebido 'string'.
```

## Exemplo de Execução Completa

```bash
$ python driver.py exemplos/triangulo.txt

***************** INPUT *****************
variaveis 
a:int;
b:int;
c:int;

escreva("Digite o primeiro lado:");
leia(a);
...

***************** ANÁLISE LÉXICA *****************
<VARIAVEIS, 'variaveis', Linha 1, Coluna 0>
<IDENT, 'a', Linha 2, Coluna 0>
<DOIS_PONTOS, ':', Linha 2, Coluna 1>
...

***************** ANÁLISE SINTÁTICA *****************
Parse tree gerada com sucesso!

***************** GERAÇÃO DA ÁRVORE VISUAL *****************
Arquivo 'ast.dot' gerado!
Imagem 'ast.png' gerada com sucesso!

***************** ANÁLISE SEMÂNTICA *****************
[Semântico] Variável 'a' declarada com tipo 'int'
[Semântico] Variável 'b' declarada com tipo 'int'
[Semântico] Variável 'c' declarada com tipo 'int'
[Semântico] Análise semântica concluída com sucesso!

***************** GERAÇÃO DE CÓDIGO LLVM-IR *****************
[CodeGen] Código LLVM-IR gerado com sucesso!
[CodeGen] Target: x86_64-unknown-linux-gnu

***************** CÓDIGO LLVM-IR *****************
; ModuleID = "meu_modulo"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
...

***************** COMPILAÇÃO NATIVA *****************
[Compile] Encontrado LLC: llc
[Compile] Encontrado Clang: clang
[Compile] Gerando assembly: exemplos/triangulo.s
[Compile] Gerando código objeto: exemplos/triangulo.o
[Compile] Gerando executável: exemplos/triangulo
[Compile] Executável gerado com sucesso!
[Info] Execute com: ./exemplos/triangulo

***************** COMPILAÇÃO CONCLUÍDA *****************
```

### Execução do Programa
```bash
$ ./exemplos/triangulo
Digite o primeiro lado:
3
Digite o segundo lado:
4
Digite o terceiro lado:
5
Escaleno
```

## Arquitetura Técnica

### Padrões de Design
- **Visitor Pattern**: Para percorrer e processar a AST
- **Strategy Pattern**: Para diferentes targets de compilação
- **Factory Pattern**: Para criação de tipos LLVM

### Tecnologias Core
- **ANTLR4**: Geração automática de lexer/parser
- **llvmlite**: Interface Python para LLVM-IR
- **Graphviz**: Renderização de grafos para AST
- **subprocess**: Integração com toolchain LLVM

### Targets Suportados
- **x86_64-unknown-linux-gnu**: Linux 64-bit
- **x86_64-pc-windows-msvc**: Windows 64-bit
- **aarch64-unknown-linux-gnu**: ARM64 Linux
- **i386-unknown-linux-gnu**: Linux 32-bit

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Créditos

- **Desenvolvedores**: 
  - [@Namem](https://github.com/Namem) - Análise Sintática e Semântica
  - [@cmigos1](https://github.com/cmigos1) - Geração de Código e Compilação
- **Orientador**: [@edwilsonferreira](https://github.com/edwilsonferreira)
- **Instituição**: Instituto Federal de Mato Grosso - IFMT
- **Disciplina**: Compiladores - 2025.1

---

**Compilador totalmente funcional com geração de código nativo!**