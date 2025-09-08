"""Clase 03"""

# import pandas as pd
# import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

import inspect
from src.core.main import run_exercises_from_main

graph_config = {
    "font_size": 10,
    "node_color": "moccasin",
    "width": 2,
    "edge_color": "grey",
    "with_labels": True,
}


def show_graph_data(graph: nx.Graph):
    print(f"Vertices: {graph.order()} | Nodos: {graph.nodes()}")
    print(f"Enlaces: {graph.edges()} | Cantidad : {graph.number_of_edges()}")


def print_graph():
    plt.axis("off")
    plt.show()


def ejercicio_1():
    """Ejercicio 1"""
    fig, ax = plt.subplots(figsize=(5, 5))
    graph = nx.Graph()
    nodes = [(1, 2), (1, 3), (1, 5), (2, 3), (3, 4), (4, 5)]
    graph.add_edges_from(nodes)
    nx.draw(graph, **graph_config, ax=ax)
    print_graph()


def ejercicio_2():
    """Ejercicio 2"""
    fig, ax = plt.subplots(figsize=(5, 5))
    graph = nx.Graph()
    nodes = [
        ("Palermo", "Chacabuco", 0.5),
        ("Palermo", "Obelisco", 0.7),
        ("Palermo", "Enrique", 2.5),
        ("Chacabuco", "Obelisco", 2.0),
        ("Obelisco", "San Martin", 1.7),
        ("San Martin", "Enrique", 5.0),
    ]
    graph.add_weighted_edges_from(nodes)
    pos = nx.shell_layout(graph)

    # Loading nodes
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_labels(graph, pos)
    labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edges(graph, pos, style="dotted", ax=ax)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    show_graph_data(graph)
    print_graph()


def list_to_edges(edges: list[int]) -> list[tuple[int, int]]:
    return list(zip(edges, edges[1:]))


def ejercicio_3():
    """Ejercicio 3"""
    fig, ax = plt.subplots(figsize=(5, 5))
    edges = [
        (1, 2, {"label": "a"}),
        (1, 4, {"label": "i"}),
        (2, 3, {"label": "b"}),
        (4, 3, {"label": "h"}),
        (3, 5, {"label": "c"}),
        (3, 6, {"label": "f"}),
        (5, 6, {"label": "e"}),
        (6, 7, {"label": "g"}),
    ]
    graph = nx.Graph(edges)
    graph.add_edge(4, 4)
    graph.add_edge(5, 5)
    pos = nx.spring_layout(graph, k=2)
    labels = nx.get_edge_attributes(graph, "label")
    nx.draw(graph, pos, with_labels=True)
    shortest_path = list_to_edges(nx.algorithms.shortest_path(graph, 1, 7))
    nx.draw_networkx_edges(graph, pos, edgelist=shortest_path, edge_color="lime")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    print_graph()


def ejercicio_4():
    """Utilizar el algoritmo de Dijkstra para determinar en el grafo ponderado siguiente un camino de longitud mínima entre los vértices Z y A. Construir el grafo"""
    fig, ax = plt.subplots(figsize=(7, 7))
    edges = [
        # Primer extremo
        ("A", "D", 5),
        ("A", "G", 2),
        ("A", "B", 4),
        ("D", "G", 1),
        ("G", "B", 1),
        # Segundo extremo
        ("Z", "E", 3),
        ("Z", "F", 2),
        ("Z", "C", 1),
        ("E", "F", 1),
        ("F", "C", 1),
        # Conexiones medias
        ("E", "D", 2),
        ("C", "B", 5),
    ]
    graph = nx.Graph()
    graph.add_weighted_edges_from(edges)
    labels = nx.get_edge_attributes(graph, "weight")
    pos = {
        "A": (2, 0),  # Derecha arriba
        "B": (1, -1),  # Centro arriba
        "G": (1, 0),  # Centro
        "D": (1, 1),  # Centro izquierda
        "Z": (-2, 0),  # Izquierda
        "E": (-1, 1),  # Izquierda arriba
        "F": (-1, 0),  # Izquierda abajo
        "C": (-1, -1),  # Centro abajo
    }
    nx.draw(graph, pos, with_labels=True)
    shortest_path_data = nx.dijkstra_path(graph, "A", "Z")
    shortest_path = list(nx.utils.pairwise(shortest_path_data))
    nx.draw_networkx_edges(graph, pos, edgelist=shortest_path, edge_color="lime")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    print_graph()


def ejercicio_5():
    """El plano muestra los puntos de conexión y las posibles líneas telefónicas en una urbanización. La zona quedará comunicada cuando dos puntos cualesquiera estén conectados. En rojo está indicado el precio de cada línea en miles de dólares. Calcular el diseño de la red más barata que conecte la zona."""
    fig, ax = plt.subplots(figsize=(7, 7))
    nodes = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]
    edges = [
        ("a", "b", 6),
        ("a", "c", 9),
        ("a", "d", 3),
        ("b", "e", 12),
        ("b", "c", 10),
        ("c", "e", 3),
        ("c", "f", 2),
        ("c", "d", 4),
        ("d", "f", 15),
        ("d", "g", 10),
        ("e", "h", 4),
        ("e", "i", 11),
        ("e", "f", 8),
        ("f", "i", 10),
        ("f", "g", 9),
        ("g", "j", 13),
        ("h", "k", 20),
        ("h", "l", 11),
        ("h", "i", 7),
        ("i", "l", 11),
        ("i", "j", 15),
        ("j", "l", 11),
        ("j", "m", 9),
        ("k", "n", 6),
        ("k", "l", 13),
        ("l", "n", 12),
        ("l", "m", 5),
        ("m", "n", 5),
    ]
    graph = nx.Graph()
    graph.add_nodes_from(nodes)
    graph.add_weighted_edges_from(edges)
    mst = nx.minimum_spanning_tree(graph)

    pos = {
        "a": (0, 5),
        "b": (5, 10),
        "c": (5, 5),
        "d": (5, 0),
        "e": (10, 10),
        "f": (10, 5),
        "g": (10, 0),
        "h": (15, 10),
        "i": (15, 5),
        "j": (15, 0),
        "k": (20, 10),
        "l": (20, 5),
        "m": (20, 0),
        "n": (25, 5),
    }
    nx.draw_networkx(graph, pos, node_color="lightblue", node_size=500)
    nx.draw_networkx_edges(graph, pos, edge_color="grey", ax=ax)
    labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    nx.draw_networkx_edges(mst, pos, edge_color="lime")

    print(f"Radio: {nx.radius(graph)}")
    print(f"Diametro: {nx.diameter(graph)}")
    print(f"Excentricidad: {nx.eccentricity(graph)}")
    print(f"Centro: {nx.center(graph)}")
    print(f"Periferia: {nx.periphery(graph)}")
    print(f"Densidad: {nx.density(graph)}")

    print_graph()


def ejercicio_6():
    """Sea G = (V,A) el grafo ponderado de 8 vértices, los cuales etiquetamos de A a H que representan poblaciones entre las cuales se implementará un medio de transporte. Los valores representan cantidad de combustible a utilizar. Determinar qué cantidad de combustible se necesitará utilizar en una ruta que conecte las poblaciones A y H, corresponde encontrar el camino más corto de A a H."""
    edges = [
        ("A", "B", 4),
        ("A", "E", 5),
        ("B", "C", 8),
        ("C", "D", 7),
        ("C", "G", 8),
        ("D", "E", 8),
        ("D", "F", 9),
        ("E", "F", 5),
        ("F", "G", 6),
        ("F", "H", 11),
        ("G", "H", 11),
    ]
    graph = nx.DiGraph()
    graph.add_weighted_edges_from(edges)
    shortest_path = nx.dijkstra_path_length(
        graph, source="A", target="H", weight="weight"
    )
    print(f"Combustible: {shortest_path}")


def ejercicio_7():
    """Se considera el grafo ponderado G de�nido por la siguiente tabla, donde los vértices representan ciudades y las aristas representan rutas existentes entre las poblaciones. Los pesos indican longitudes en Kms."""
    edges = [
        ("A", "B", 20),
        ("A", "F", 34),
        ("A", "I", 45),
        ("B", "C", 20),
        ("B", "F", 10),
        ("B", "I", 26),
        ("C", "D", 28),
        ("C", "I", 22),
        ("D", "G", 18),
        ("D", "H", 19),
        ("D", "I", 13),
        ("E", "F", 22),
        ("E", "G", 12),
        ("E", "H", 25),
        ("F", "G", 30),
        ("F", "I", 12),
        ("G", "H", 16),
        ("G", "I", 14),
        ("H", "I", 32)
    ]
    graph = nx.Graph()
    graph.add_weighted_edges_from(edges)
    src = dict(nx.single_source_dijkstra_path(graph, "A"))
    print(src)
    src = dict(nx.single_source_dijkstra_path_length(graph, "A"))
    print(src)

    delta = nx.dijkstra_path_length(graph, "A", "B") + nx.dijkstra_path_length(graph, "G", "H")
    print(f"{68 - delta} kms para la nueva ruta")

def main():
    """Run all exercises"""
    module = inspect.currentframe()
    run_exercises_from_main(module)


if __name__ == "__main__":
    main()
