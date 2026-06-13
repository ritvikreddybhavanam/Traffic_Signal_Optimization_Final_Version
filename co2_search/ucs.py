import heapq


def ucs(graph, start, goal):

    pq = [(0, start, [start])]

    visited = set()

    while pq:

        cost, node, path = heapq.heappop(pq)

        if node == goal:
            return path, cost

        if node not in visited:

            visited.add(node)

            for neighbor, edge_cost in graph[node].items():

                heapq.heappush(
                    pq,
                    (
                        cost + edge_cost,
                        neighbor,
                        path + [neighbor]
                    )
                )

    return None, float("inf")