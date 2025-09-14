"""Clase 05"""

from rich.console import Console

import networkx as nx
import matplotlib.pyplot as plt
import inspect
from src.core.main import run_exercises_from_main

NODES = [
    ("A", "B", 5),
    ("A", "D", 6),
    ("B", "C", 5),
    ("B", "E", 6),
    ("B", "G", 7),
    ("C", "G", 2),
    ("D", "F", 5),
    ("D", "G", 9),
    ("E", "A", 3),
    ("E", "D", 2),
    ("F", "G", 9),
]

GRAPH = nx.Graph()
GRAPH.add_weighted_edges_from(NODES)

console = Console()

print = console.print


def neighbors_of(graph, node):
    """Get neighbors of a node"""
    return list(graph.neighbors(node))


def edges_of(graph, node, _as=list):
    """Get edges of a node"""
    return _as(graph.edges(node))


def ejercicio_1():
    """Ejercicio 1"""
    pos = nx.bfs_layout(GRAPH, start="A")
    nx.draw(GRAPH, pos, with_labels=True)
    edge_labels = nx.get_edge_attributes(GRAPH, "weight")
    nx.draw_networkx_edge_labels(GRAPH, pos, edge_labels=edge_labels)
    plt.axis("off")
    # 1. Emitir los vecinos de 'B'
    print("Vecinos de B:", neighbors_of(GRAPH, "B"))
    print("-" * 40, "\n", style="dim")
    # 2. Emitir la lista de aristas de cada nodo
    edges = list(GRAPH.degree)
    print("Lista de aristas de cada nodo:", edges)
    # 3. Convertir a diccionario la lista anterior
    print("-" * 40, "\n", style="dim")
    edges_dict = dict(GRAPH.degree)
    print("Diccionario de aristas:", edges_dict)
    print("-" * 40, "\n", style="dim")
    # 4. Crear la matriz de adyacencia y emitirla
    matrix = nx.adjacency_matrix(GRAPH).todense()
    print("Matriz de adyacencia:")
    print(matrix)
    # 5. Crear la matriz de incidencia y emitirla
    matrix = nx.incidence_matrix(GRAPH).todense()
    print("Matriz de incidencia:")
    print(matrix)
    # 6. Emitir la longitud desde 'A' hasta el objetivo
    length = nx.algorithms.shortest_path_length(
        GRAPH, source="A", target="G", weight="weight"
    )
    print("Longitud desde 'A' hasta 'G':", length)
    # 7. Emitir el promedio de la ruta más corta usando el método de floyd-warshall
    shortest = nx.average_shortest_path_length(
        GRAPH, weight="weight", method="floyd-warshall"
    )
    print("Promedio de la ruta más corta:", shortest)
    # 8. Emitir la ruta ponderada más corta entre 'A' y 'G' usando el algoritmo de Dijkstra
    path = nx.dijkstra_path(GRAPH, source="A", target="G", weight="weight")
    print("Ruta ponderada más corta entre 'A' y 'G':", path)
    # 9. Emitir la longitud de la ruta ponderada entre 'A' y 'G'
    length = nx.path_weight(GRAPH, path, weight="weight")
    print("Longitud de la ruta ponderada entre 'A' y 'G':", length)
    # 10. Emitir la longitud de la ruta desde el nodo 'C'
    length = nx.shortest_path_length(GRAPH, source="C", target="G", weight="weight")
    print("Longitud de la ruta desde el nodo 'C':", length)
    # 11. Emita el radio del grafo
    radius = nx.radius(GRAPH)
    print("Radio del grafo:", radius)
    # 12. Emita el diámetro del grafo
    diameter = nx.diameter(GRAPH)
    print("Diámetro del grafo:", diameter)
    # 13. Emita la excentricidad
    eccentricity = nx.eccentricity(GRAPH)
    print("Excentricidad del grafo:", eccentricity)
    # 14. Emita el centro del grafo
    center = nx.center(GRAPH)
    print("Centro del grafo:", center)
    # 15. Emita la periferia del grafo
    periphery = nx.periphery(GRAPH)
    print("Periferia del grafo:", periphery)
    # 16. Emita la densidad
    density = nx.density(GRAPH)
    print("Densidad del grafo:", density)
    # 17. Dibujar el grafo y emitir con matplotlib
    plt.show()
    # 18. Convertir en grafo dirigido
    directed_graph = nx.DiGraph()
    directed_graph.add_weighted_edges_from(NODES)
    # 19. Dibujar el grafo
    pos = nx.forceatlas2_layout(directed_graph)
    nx.draw(directed_graph, pos, with_labels=True)
    edge_labels = nx.get_edge_attributes(directed_graph, "weight")
    nx.draw_networkx_edge_labels(directed_graph, pos, edge_labels=edge_labels)
    plt.axis("off")
    plt.show()

    return directed_graph


def main():
    """Run all exercises"""
    module = inspect.currentframe()
    run_exercises_from_main(module)


if __name__ == "__main__":
    main()
