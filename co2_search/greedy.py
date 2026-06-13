import heapq


def greedy_search(
        graph,
        heuristic,
        start,
        goal):

    pq = [
        (
            heuristic[start],
            start,
            [start]
        )
    ]

    visited = set()

    while pq:

        _, node, path = heapq.heappop(pq)

        if node == goal:
            return path

        if node not in visited:

            visited.add(node)

            for neighbor in graph[node]:

                heapq.heappush(
                    pq,
                    (
                        heuristic[neighbor],
                        neighbor,
                        path + [neighbor]
                    )
                )

    return None