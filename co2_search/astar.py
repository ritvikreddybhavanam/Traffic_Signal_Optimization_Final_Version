import heapq


def astar(graph, heuristic, start, goal):
    """
    A* Search Algorithm

    graph:
    {
        "A": {"B": 4, "D": 3},
        "B": {"A": 4, "C": 5}
    }

    heuristic:
    {
        "A": 10,
        "B": 7
    }
    """

    priority_queue = []

    heapq.heappush(
        priority_queue,
        (
            heuristic[start],
            0,
            start,
            [start]
        )
    )

    visited = set()

    while priority_queue:

        f_cost, g_cost, current_node, path = heapq.heappop(
            priority_queue
        )

        if current_node == goal:
            return path, g_cost

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, edge_cost in graph[current_node].items():

            if neighbor not in visited:

                new_g = g_cost + edge_cost

                new_f = (
                    new_g
                    + heuristic[neighbor]
                )

                heapq.heappush(
                    priority_queue,
                    (
                        new_f,
                        new_g,
                        neighbor,
                        path + [neighbor]
                    )
                )

    return [], float("inf")