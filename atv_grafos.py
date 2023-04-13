import networkx as nx
import matplotlib.pyplot as plt
from art import text2art


def startNaoValorado():

    print("\nDigite os vertices do grafo: ")
    while(True):
        v = input() 
        if not v:   
            break 
        grafo.add_node(v)

    print("\nDigite as arestas do grafo: ")
    while(True):
        a = input()
        if not a:
            break 

        a1, a2 = a.split()
        grafo.add_edge(a1, a2)

    nx.draw(grafo, with_labels=True)
    labels = nx.get_edge_attributes(grafo, 'weight')
    nx.draw_networkx_edge_labels(grafo, pos=nx.spring_layout(grafo), edge_labels=labels)
    plt.show()

def startValorado():

    print("\nDigite os vertices do grafo: ")
    while(True):
        v = input() 
        if not v:   
            break 
        grafo.add_node(v)

    print("\nDigite as arestas do grafo junto com o peso\nno formato (aresta1 aresta2 peso): ")
    while(True):
        a = input()
        if not a:
            break 

        a1, a2, p = a.split()
        grafo.add_edge(a1, a2, weight=float(p))

    nx.draw(grafo, with_labels=True)
    labels = nx.get_edge_attributes(grafo, 'weight')
    nx.draw_networkx_edge_labels(grafo, pos=nx.spring_layout(grafo), edge_labels=labels)
    plt.show()

print(text2art("GrafoBoys"))

direcionado = input("Grafo direcionado? Y para sim e N para não:")
if(direcionado.lower() == 'y'):
    grafo = nx.DiGraph()
else:
    grafo = nx.Graph()

valorado = input("Grafo valorado? Y para sim e N para não:")
if(valorado.lower() == 'y'):
    startValorado()
else:
    startNaoValorado()


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
plt.show() """
