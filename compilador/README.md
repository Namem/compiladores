# Compilador Simples baseado em Lua

Este projeto é um compilador feito em Python com ANTLR, inspirado na linguagem Lua, como parte do curso de Construção de Compiladores.

## Funcionalidades

- Tipos primitivos: `int`, `string`
- Entrada/Saída: `leia()`, `escreva()`
- Controle de fluxo: `se...entao...senao`, `enquanto...faca`
- Expressões aritméticas: `+`, `-`, `*`, `/`
- Expressões lógicas: `&&`, `||`, `!`, `==`
- Expressões relacionais: `>`, `<`

## Como Executar

1. Instale o runtime do ANTLR para Python:
    ```bash
    pip install -r requirements.txt
    ```

2. Gere o lexer e o parser:
    ```bash
    antlr4 -Dlanguage=Python3 Compilador.g4
    ```

3. Execute o compilador em um arquivo de exemplo:
    ```bash
    python driver.py exemplos/triangulo.txt
    ```

4. Visualize a árvore sintática (AST):
    ```bash
    dot -Tpng ast.dot -o ast.png
    ```

## Estrutura de Pastas

