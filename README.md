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
- **Escape Sequences**: Suporte a `\n`, `\t`, `\"`, `\\` em strings

## Estrutura do Projeto

```
bencao/
├── Compilador.g4              # Gramática ANTLR4 da linguagem
├── CompiladorLexer.py         # Lexer gerado automaticamente
├── CompiladorParser.py        # Parser gerado automaticamente  
├── CompiladorListener.py      # Listener base gerado pelo ANTLR4
├── CompiladorBaseVisitor.py   # Visitor base gerado pelo ANTLR4
├── driver.py                  # Script principal do compilador
├── SemanticAnalyzer.py        # Analisador semântico (Listener Pattern)
├── CodeGeneratorLLVM.py       # Gerador de código LLVM-IR (Visitor Pattern)
├── ast_visualizer.py          # Visualizador da AST com Graphviz
├── exemplos/                  # Exemplos de programas
│   ├── triangulo.txt          # Classificação de triângulos
│   ├── pascal.txt             # Triângulo de Pascal
│   ├── fibonacci.txt          # Sequência de Fibonacci
│   └── fatorial.txt           # Cálculo de fatorial
├── requirements.txt           # Dependências Python
└── README.md                  # Este arquivo
```

## Arquitetura do Compilador

### Padrões de Design Utilizados

#### 1. **Listener Pattern** (Análise Semântica)
- **Arquivo**: `SemanticAnalyzer.py`
- **Herança**: `CompiladorListener`
- **Função**: Percorre a AST automaticamente via `ParseTreeWalker`
- **Métodos**: `enterDeclaracao()`, `exitFator()`, `exitExprAritmetica()`, etc.

#### 2. **Visitor Pattern** (Geração de Código)
- **Arquivo**: `CodeGeneratorLLVM.py`
- **Herança**: `CompiladorBaseVisitor`
- **Função**: Controle manual da travessia da AST
- **Métodos**: `visitPrograma()`, `visitCondicional()`, `visitExpr()`, etc.

### Por que Dois Padrões Diferentes?

- **Listener**: Ideal para análise semântica (verificação de tipos, escopo)
- **Visitor**: Ideal para geração de código (controle da ordem de processamento)

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

Conteúdo do `requirements.txt`:
```
antlr4-python3-runtime==4.13.2
llvmlite>=0.42.0
graphviz>=0.20.1
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
# Classificação de triângulos
python driver.py exemplos/triangulo.txt

# Triângulo de Pascal  
python driver.py exemplos/pascal.txt

# Sequência de Fibonacci
python driver.py exemplos/fibonacci.txt

# Cálculo de fatorial
python driver.py exemplos/fatorial.txt
```

## Fases do Compilador

### 1. **Análise Léxica**
- **Responsável**: `CompiladorLexer.py` (gerado automaticamente)
- **Função**: Tokenização do código fonte
- **Tokens**: Identificadores, números, strings, operadores, palavras-chave
- **Recursos**: Comentários (`--`), strings com escape sequences

### 2. **Análise Sintática**
- **Responsável**: `CompiladorParser.py` (gerado automaticamente)
- **Função**: Construção da Árvore Sintática Abstrata (AST)
- **Saída**: Parse tree navegável
- **Visualização**: Geração automática de `ast.png`

### 3. **Análise Semântica** 
- **Responsável**: `SemanticAnalyzer.py` (Listener Pattern)
- **Função**: Verificação de tipos e escopo
- **Verificações**:
  - Declaração de variáveis
  - Compatibilidade de tipos em operações
  - Uso de variáveis não declaradas
  - Tipo correto em atribuições

### 4. **Geração de Código LLVM-IR**
- **Responsável**: `CodeGeneratorLLVM.py` (Visitor Pattern)
- **Função**: Tradução para código intermediário LLVM
- **Recursos**:
  - Controle de fluxo (if/else, loops)
  - Expressões aritméticas e lógicas
  - Funções de I/O (printf/scanf)
  - Múltiplos targets de arquitetura

### 5. **Compilação Nativa** 
- **Responsável**: `driver.py` (integração com toolchain)
- **Ferramentas**: LLC (assembly) + Clang (linking)
- **Saída**: Executável nativo para a plataforma

## Saídas Geradas

Para cada arquivo compilado:

```
exemplos/triangulo.txt → 
├── triangulo.ll       # Código LLVM-IR intermediário
├── triangulo.s        # Assembly nativo (se LLC disponível)
├── triangulo.o        # Código objeto (se Clang disponível)
├── triangulo          # Executável final
├── ast.dot            # Descrição textual da AST
└── ast.png            # Visualização gráfica da AST
```

## Linguagem Suportada

### Estrutura do Programa
```pascal
variaveis
    nome:tipo;
    valor:int;

// Comandos do programa
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
se valor ~= 0 entao  -- diferente
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
    escreva("Verdadeiro\n");
senao
    escreva("Falso\n");
fim
```

#### Loops
```pascal
enquanto contador <= 10 faca
    escreva(contador);
    escreva(" ");
    contador = contador + 1;
fim
```

### Entrada/Saída
```pascal
escreva("Digite um número:\n");
leia(numero);
escreva("Resultado: ");
escreva(numero * 2);
escreva("\n");
```

### Escape Sequences em Strings
```pascal
escreva("Primeira linha\nSegunda linha\n");
escreva("Texto com \"aspas\" e tab:\taquí\n");
escreva("Barra invertida: \\\n");
```

Sequências suportadas:
- `\n` → nova linha
- `\t` → tab
- `\r` → carriage return
- `\\` → barra invertida literal
- `\"` → aspas duplas literal

## Exemplos Completos

### 1. Classificação de Triângulos
```pascal
variaveis 
a:int;
b:int;
c:int;

escreva("Digite o primeiro lado:\n");
leia(a);
escreva("Digite o segundo lado:\n");
leia(b);
escreva("Digite o terceiro lado:\n");
leia(c);

se a == b && b == c entao
    escreva("Equilatero\n");
senao
    se a == b || a == c || b == c entao
        escreva("Isosceles\n");
    senao
        escreva("Escaleno\n");
    fim
fim
```

### 2. Sequência de Fibonacci
```pascal
variaveis
    n:int;
    i:int;
    primeiro:int;
    segundo:int;
    proximo:int;

escreva("Digite o numero de termos da sequencia de Fibonacci:\n");
leia(n);

se n >= 1 entao
    primeiro = 0;
    escreva("Fibonacci: ");
    escreva(primeiro);
    escreva(" ");
    
    se n >= 2 entao
        segundo = 1;
        escreva(segundo);
        escreva(" ");
        
        i = 3;
        enquanto i <= n faca
            proximo = primeiro + segundo;
            escreva(proximo);
            escreva(" ");
            
            primeiro = segundo;
            segundo = proximo;
            i = i + 1;
        fim
    fim
    escreva("\n");
senao
    escreva("Numero deve ser maior que 0\n");
fim
```

### 3. Cálculo de Fatorial
```pascal
variaveis
    numero:int;
    fatorial:int;
    i:int;

escreva("Digite um numero: ");
leia(numero);

fatorial = 1;
i = numero;

enquanto i > 1 faca
    fatorial = fatorial * i;
    i = i - 1;
fim

escreva("Fatorial de ");
escreva(numero);
escreva(" = ");
escreva(fatorial);
escreva("\n");
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
$ python driver.py exemplos/fibonacci.txt

***************** INPUT *****************
variaveis
    n:int;
    i:int;
    primeiro:int;
    segundo:int;
    proximo:int;
...

***************** ANÁLISE LÉXICA *****************
[Lexer] Análise léxica concluída com sucesso!

***************** ANÁLISE SINTÁTICA *****************
[Parser] Parse tree gerada com sucesso!

***************** GERAÇÃO DA ÁRVORE VISUAL *****************
[Visualizer] Arquivo 'ast.dot' gerado!
[Visualizer] Imagem 'ast.png' gerada com sucesso!

***************** ANÁLISE SEMÂNTICA *****************
[Semântico] Variável 'n' declarada com tipo 'int'
[Semântico] Variável 'i' declarada com tipo 'int'
[Semântico] Variável 'primeiro' declarada com tipo 'int'
[Semântico] Variável 'segundo' declarada com tipo 'int'
[Semântico] Variável 'proximo' declarada com tipo 'int'
[Semântico] Análise semântica concluída com sucesso!

***************** GERAÇÃO DE CÓDIGO LLVM-IR *****************
[CodeGen] Código LLVM-IR gerado com sucesso!
[CodeGen] Target: x86_64-unknown-linux-gnu

***************** COMPILAÇÃO NATIVA *****************
[Compile] Encontrado LLC: llc
[Compile] Encontrado Clang: clang
[Compile] Gerando assembly: exemplos/fibonacci.s
[Compile] Gerando código objeto: exemplos/fibonacci.o
[Compile] Gerando executável: exemplos/fibonacci
[Compile] Executável gerado com sucesso!
[Info] Execute com: ./exemplos/fibonacci

***************** COMPILAÇÃO CONCLUÍDA *****************
```

### Execução do Programa
```bash
$ ./exemplos/fibonacci
Digite o numero de termos da sequencia de Fibonacci:
10
Fibonacci: 1 1 2 3 5 8 13 21 34 55
```

## Arquitetura Técnica Detalhada

### Tecnologias Core
- **ANTLR4**: Geração automática de lexer/parser a partir da gramática
- **llvmlite**: Interface Python para geração de LLVM-IR
- **Graphviz**: Renderização de grafos para visualização da AST
- **subprocess**: Integração com toolchain LLVM (LLC + Clang)

### Targets de Compilação Suportados
- **x86_64-unknown-linux-gnu**: Linux 64-bit (padrão)
- **x86_64-pc-windows-msvc**: Windows 64-bit
- **aarch64-unknown-linux-gnu**: ARM64 Linux
- **i386-unknown-linux-gnu**: Linux 32-bit

### Data Layouts por Arquitetura
```python
# x86_64 Linux/Unix
"e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

# x86_64 Windows
"e-m:w-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

# ARM64
"e-m:e-i8:8:32-i16:16:32-i64:64-i128:128-n32:64-S128"
```

## Métricas do Projeto

- **Linhas de Código**: ~1500 (Python) + ~150 (Gramática)
- **Regras Gramaticais**: 25+ 
- **Tokens Definidos**: 30+
- **Fases de Compilação**: 5 completas
- **Exemplos Funcionais**: 4+ programas
- **Tipos de Erro Detectados**: 15+ diferentes
- **Padrões de Design**: 2 (Listener + Visitor)

## Créditos

- **Desenvolvedores**: 
  - [@Namem](https://github.com/Namem) - Análise Sintática e Semântica
  - [@cmigos1](https://github.com/cmigos1) - Geração de Código e Compilação
- **Orientador**: [@edwilsonferreira](https://github.com/edwilsonferreira)
- **Instituição**: Universidade Federal de Mato Grosso (IFMT)
- **Disciplina**: Compiladores - 2024.1
