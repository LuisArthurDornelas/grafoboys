import networkx as nx
import matplotlib.pyplot as plt
from art import text2art

print(text2art("Grafo Boys", font="small"))

# Pergunta se o grafo é direcionado
is_dirigido = input("O grafo é direcionado? (s/n): ").lower() == 's'

# Pergunta se o grafo é valorado
is_valorado = input("O grafo é valorado? (s/n): ").lower() == 's'

# Cria o grafo correspondente ao tipo
if is_dirigido:
    grafo = nx.DiGraph()
else:
    grafo = nx.Graph()

# Solicita a entrada de vértices
print("\nDigite os vertices do grafo: ")
while(True):
    v = input() 
    if not v:   
        break 
    grafo.add_node(v)

# Solicita a entrada de arestas
print("\nDigite as arestas do grafo(x y peso): ")
while(True):
    a = input()
    if not a:
        break 

    a1, a2, *peso = a.split()
    peso = float(peso[0]) if peso else 1.0

    if is_valorado:
        grafo.add_edge(a1, a2, weight=peso)
    else:
        grafo.add_edge(a1, a2)

# Imprime o grafo
pos = nx.spring_layout(grafo)
labels = nx.get_edge_attributes(grafo, 'weight')
nx.draw_networkx_nodes(grafo, pos, node_color='r', node_size=500)
nx.draw_networkx_edges(grafo, pos, edge_color='b', arrows=True)
nx.draw_networkx_labels(grafo, pos, font_size=20, font_family='sans-serif')
nx.draw_networkx_edge_labels(grafo, pos, edge_labels=labels, font_size=16)
plt.axis('off')
plt.show()

# Imprime ordem e tamanho do grafo
print("Ordem do grafo:", grafo.order())
print("Tamanho do grafo:", grafo.size())

# Imprime os vértices adjacentes a cada vértice
for v in grafo.nodes():
    print("Vértices adjacentes a", v, ":", list(grafo.neighbors(v)))

# Solicita a entrada de um vértice para imprimir o grau
print("\nDigite um vertice: ")
while(True):
    v = input()
    if not v:
        break 
    print("Grau do vértice ", v,": ", grafo.degree(v))
    print("Lista de vértices adjacentes a", v, ": ")
    if is_dirigido:
        print("Entrada:", list(grafo.predecessors(v)))
        print("Saída:", list(grafo.successors(v)))
    else:
        print(list(grafo.neighbors(v)))
    print("\nDigite um vertice: ")


# Solicita a entrada de um par de vértices para imprimir se eles são adjacentes, menor caminho e custo do menor caminho
while(True):
    print("\nDigite um par vertices(x y): ")
    print("(Ou digite 'finalizar' para ver o raio e diâmetro):")


    v = input()
    if v.lower() == "finalizar":
        break 

    v1, v2 = v.split()
    
    # Verifica se são adjacentes
    if grafo.has_edge(v1, v2):
        print("O vértice", v1, "é adjacente ao vértice", v2)
    else:
        print("O vértice", v1, "não é adjacente ao vértice", v2)
    if not is_dirigido:
        if nx.has_path(grafo, v1, v2):
            menor_caminho = nx.shortest_path(grafo, source=v1, target=v2, weight='weight') if is_valorado else nx.shortest_path(grafo, source=v1, target=v2)
            print("Menor caminho entre os vértices: ", str(menor_caminho))

            custo_menor_caminho = nx.shortest_path_length(grafo, source=v1, target=v2, weight='weight')
            print("Peso do menor caminho entre os vértices: ", custo_menor_caminho)
        else:
            print("Não  há caminho entre os vértices!")
    else:
        if nx.has_path(grafo.reverse(), v2, v1):
            menor_caminho = nx.shortest_path(grafo, source=v1, target=v2, weight='weight') if is_valorado else nx.shortest_path(grafo, source=v1, target=v2)
            print("Menor caminho entre os vértices: ", menor_caminho)

            custo_menor_caminho = nx.shortest_path_length(grafo, source=v1, target=v2, weight='weight')
            print("Peso do menor caminho entre os vértices: ", custo_menor_caminho)
        else:
            print("Não  há caminho entre os vértices!")
   
    # Calcula o menor caminho e o custo do menor caminho (caso o grafo seja valorado)

# Calcula e imprime o raio e o diâmetro do grafo
try:
    raio = nx.radius(grafo)
except nx.NetworkXError:
    print ("O grafo tem raio infinito!")

try:
    diametro = nx.diameter(grafo)
except nx.NetworkXError:
        print ("O grafo tem diâmetro infinito!")

