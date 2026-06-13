from co2_search.road_network import RoadNetwork
from co2_search.bfs import bfs
from co2_search.dfs import dfs
from co2_search.ucs import ucs
from co2_search.greedy import greedy_search
from co2_search.astar import astar


def demonstrate_search():

    network = RoadNetwork()

    graph = network.get_graph()

    heuristic = network.get_heuristic()

    start = "A"
    goal = "F"

    print("\n===================================")
    print("CO2 SEARCH ALGORITHMS")
    print("===================================")

    print("\nBFS")
    print(
        "Path:",
        " -> ".join(
            bfs(graph, start, goal)
        )
    )

    print("\nDFS")
    print(
        "Path:",
        " -> ".join(
            dfs(graph, start, goal)
        )
    )

    path, cost = ucs(
        graph,
        start,
        goal
    )

    print("\nUCS")
    print("Path:", " -> ".join(path))
    print("Cost:", cost)

    path = greedy_search(
        graph,
        heuristic,
        start,
        goal
    )

    print("\nGreedy")
    print("Path:", " -> ".join(path))

    path, cost = astar(
        graph,
        heuristic,
        start,
        goal
    )

    print("\nA*")
    print("Path:", " -> ".join(path))
    print("Cost:", cost)