import subprocess
from antlr4.tree.Trees import Trees

class ASTVisualizer:
    def visualizar(self, tree, parser):
        dot_string = Trees.toStringTree(tree, None, parser)

        # Gera o arquivo .dot
        with open("ast.dot", "w") as f:
            f.write("digraph G {\n")
            f.write(self.converter_para_dot(dot_string))
            f.write("\n}")
        
        print("\033[92mArquivo 'ast.dot' gerado!\033[0m")

        # Gera o PNG automaticamente usando Graphviz
        try:
            subprocess.run(["dot", "-Tpng", "ast.dot", "-o", "ast.png"], check=True)
            print("\033[92mImagem 'ast.png' gerada com sucesso!\033[0m")
        except Exception as e:
            print("\033[91mErro ao gerar PNG com Graphviz:\033[0m", e)

    def converter_para_dot(self, tree_str):
        tree_str = tree_str.replace("(", " ( ").replace(")", " ) ").split()
        stack = []
        edges = []
        count = 0
        node_ids = {}

        for token in tree_str:
            if token == "(":
                continue
            elif token == ")":
                stack.pop()
            else:
                node_id = f"n{count}"
                node_ids[token + str(count)] = node_id
                count += 1
                label = token.replace('"', '\\"')
                edges.append(f'{node_id} [label="{label}"];')
                if stack:
                    edges.append(f"{stack[-1]} -> {node_id};")
                stack.append(node_id)

        return "\n".join(edges)
