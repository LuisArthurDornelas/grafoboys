# > Interagir com o sistema, inserindo vertices e arestas 
# um por um ou tudo de uma só vez;

# > Criar grafos:
#    - Direcionados
#    - Não direcionados
#    - Valorados
#    - Não valorados

# > Imprimir grafo em formato livre ou grafico;

# > Exibir ordem e tamanho do grafo;

# > Exibir a informação da lista de vértices adjacentes;
# > Se o grafo for direcionado, o sistema deverá informar a lista 
# de vértices adjacentes de entrada e de saída de um dado vértice;

# > Para um dado vertice, informar o seu grau;
# > Se o grafo for direcionado, informar grau de adjacência de entrada e de saída do vértice;

# > Dado um par de vértices, retornar:
#   - Se os dois vértices são adjacentes ou não
#   - Caminha mais curto entre eles
#   - Valor do custo de menor caminho
#   - Sequencia de vertices do menor caminho

import networkx as nx
import matplotlib.pyplot as plt

print("   ____            __         ____                   ")
print("  / __| __ __ _ / _| ___   | __ )  ___  _   _ ___  ")
print(" | |  | '__/ _` | | / _ \  |  _ \ / _ \| | | / __| ")
print(" | || | | | (_| |  _| (_) | | |_) | (_) | |_| \_ \ ")
print("  \____|_|  \__,_|_|  \___/  |____/ \___/ \__, |___/ ")
print("                                          |___/      ")

grafo = nx.Graph()

print("\nDigite os vertices do grafo: ")
while(True):
    v = input() 
    if not v:   
        break 
    grafo.add_nodes_from(v)
        

print("\nDigite as arestas do grafo: ")
while(True):
    a = input()
    if not a:
        break 

    a1, a2 = a.split()
    grafo.add_edge(a1, a2)

nx.draw(grafo, with_labels=True)
plt.show()

""" # cria um novo grafo
G = nx.Graph()

# adiciona os nós
G.add_nodes_from([1, 2, 3])

# adiciona as arestas
G.add_edges_from([(1, 2), (2, 3)])

# desenha o grafo
nx.draw(G, with_labels=True)
plt.show()

# customiza o gráfico
options = {
    'node_color': 'pink',
    'node_size': 500,
    'width': 2,
    'font_size': 16,
    'with_labels': True,
    'edge_color': 'purple'
}

# desenha o grafo com as opções customizadas
nx.draw(G, **options)
plt.show() """