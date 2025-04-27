# Compilador Simples

Este projeto é um compilador baseado em uma linguagem inspirada no Lua, desenvolvido em Python usando ANTLR.

## Funcionalidades

- Tipos: `int`, `string`
- Entrada/Saída: `leia()`, `escreva()`
- Controle de fluxo: `se...entao...senao`, `enquanto...faca`
- Operadores: `+`, `-`, `*`, `/`, `&&`, `||`, `!`, `==`

## Como executar

1. Gere o parser:
    ```bash
    antlr4 -Dlanguage=Python3 Compilador.g4
    ```

2. Rode o driver:
    ```bash
    python driver.py exemplos/pascal.txt
    ```

## Visualizar a AST

Após executar, será gerado o arquivo `ast.dot`. Para visualizar:

```bash
dot -Tpng ast.dot -o ast.png
