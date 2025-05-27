# Compilador - Projeto de Compiladores

Este projeto consiste na implementação de um compilador utilizando a ferramenta ANTLR4. Ele realiza a análise léxica, sintática e semântica de uma linguagem definida, além de gerar a Árvore de Derivação (AST) correspondente.

## 📁 Estrutura do Projeto

- `Compilador.g4`: Arquivo de gramática ANTLR4 que define a linguagem.
- `CompiladorLexer.py`, `CompiladorParser.py`, `CompiladorListener.py`: Arquivos gerados automaticamente pelo ANTLR4 a partir da gramática.
- `driver.py`: Script principal que executa o compilador.
- `ast_visualizer.py`: Script para visualização da Árvore de Derivação (AST).
- `exemplos/`: Diretório contendo exemplos de código na linguagem definida.
- `requirements.txt`: Lista de dependências necessárias para executar o projeto.

## ✅ Pré-requisitos

- Python 3.6 ou superior
- [ANTLR4](https://www.antlr.org/) instalado e configurado no sistema
- Instalar as dependências Python listadas em `requirements.txt`:

```bash
pip install -r requirements.txt
```

## 🚀 Como Executar

1. Gere os arquivos do analisador léxico e sintático a partir da gramática:

```bash
antlr4 -Dlanguage=Python3 Compilador.g4
```

2. Execute o compilador com um arquivo de entrada:

```bash
python driver.py exemplos/exemplo1.txt
```

3. Para visualizar a Árvore de Derivação (AST):

```bash
python ast_visualizer.py exemplos/exemplo1.txt
```

## 🧪 Exemplos

O diretório `exemplos/` contém arquivos de exemplo que podem ser utilizados para testar o compilador. Basta executar os scripts mencionados acima com o caminho para o arquivo de exemplo desejado.

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).


## 👥 Créditos

- **Autores Principais**: [@Namem](https://github.com/Namem) e [@cmigos1](https://github.com/cmigos1)
- **Orientador**: [@edwilsonferreira](https://github.com/edwilsonferreira)