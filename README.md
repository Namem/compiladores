# Mini LUA

Este repositório contém a implementação de um compilador desenvolvido como parte de um projeto acadêmico. O compilador é construído utilizando ferramentas como ANTLR para geração de analisadores léxicos e sintáticos, e é escrito predominantemente em Python.

## Estrutura do Projeto

- `grammar/`: Contém os arquivos de gramática utilizados pelo ANTLR para gerar os analisadores léxico e sintático.
- `compilador/`: Diretório principal do compilador, contendo os módulos responsáveis pelas diversas fases da compilação.
- `src/`: Código-fonte adicional que dá suporte ao compilador.
- `testes/`: Conjunto de testes para verificar a correção e robustez do compilador.
- `.antlr/`: Arquivos gerados automaticamente pelo ANTLR a partir das gramáticas definidas.

## Tecnologias Utilizadas

- **Python**: Linguagem principal utilizada no desenvolvimento do compilador.
- **ANTLR**: Ferramenta para geração de analisadores léxicos e sintáticos a partir de gramáticas definidas.
- **Java**: Utilizado em conjunto com o ANTLR para a geração dos analisadores.

## Como Executar

1. Certifique-se de ter o [Python](https://www.python.org/downloads/) instalado em sua máquina.
2. Instale o ANTLR seguindo as instruções disponíveis na [documentação oficial](https://www.antlr.org/).
3. Clone este repositório:
   ```bash
   git clone https://github.com/Namem/compiladores.git
   ```
4. Navegue até o diretório do projeto:
   ```bash
   cd compiladores
   ```
5. Gere os analisadores léxico e sintático utilizando o ANTLR:
   ```bash
   antlr4 -Dlanguage=Python3 grammar/Compilador.g4 -o .antlr
   ```
6. Execute o compilador:
   ```bash
   python driver.py Seuexemplo.txt
   ```

## Exemplos de Código Suportado

A gramática implementada permite a criação de programas com comandos como leitura, escrita, atribuição, estruturas condicionais e laços de repetição. Veja alguns exemplos abaixo:

### Leitura e Escrita
```txt
leia(x);
escreva("Resultado:");
escreva(x);
```

### Atribuição e Expressões
```txt
x = 5 + 3 * 2;
y = (x - 4) / 2;
```

### Condicional
```txt
se x > 10 entao
    escreva("Maior que 10");
senao
    escreva("Menor ou igual a 10");
fim
```

### Repetição
```txt
enquanto x < 10 faca
    escreva(x);
    x = x + 1;
fim
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests com sugestões, correções ou melhorias.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
