import networkx as nx
import matplotlib.pyplot as plt

grafo = nx.Graph()

print("\nDigite os vertices do grafo: ")
while(True):
    v = input() 
    if not v:   
        break 
    grafo.add_nodes_from(v)
        

print("\nDigite as arestas do grafo(x y): ")
while(True):
    a = input()
    if not a:
        break 

    a1, a2 = a.split()
    grafo.add_edge(a1, a2)

nx.draw(grafo, with_labels=True)
plt.show()

# Imprimir ordem e tamanho do grafo
print("Ordem do grafo:", grafo.order())
print("Tamanho do grafo:", grafo.size())

# Aqui ele pega todos os vertices do grafo e fala a quais vertices ele é adjacente
for v in grafo.nodes():
    print("Vértices adjacentes a", v, ":", list(grafo.neighbors(v)))

# Aqui vai pegar vertices como input e mostrar o grau(até q enter seja apertado duas vezes)
print("\nDigite um vertice: ")
while(True):
    v = input()
    if not v:
        break 
    print("Grau do vértice ", v,": ", grafo.degree(v))

# Vai pegar um par de vertices como input e printar:
while(True):
    print("\nDigite um par vertices(x y): ")

    v = input()
    if not v:
        break 

    v1, v2 = v.split()
    
    # Se eles sao adjecentes
    if grafo.has_edge(v1, v2):
        print("O vértice", v1, "é adjacente ao vértice", v2)

    else:
        print("O vértice", v1, "não é adjacente ao vértice", v2)

    # A rota do caminho mais curto entre eles
    menor_caminho = nx.shortest_path(grafo, source=v1, target=v2, weight='weight')

    # O custo do caminho mais curto entre eles
    custo_menor_caminho = nx.shortest_path_length(grafo, source=v1, target=v2, weight='weight')

    print("O menor caminho é:", menor_caminho)
    print("O custo do menor caminho é:", custo_menor_caminho)