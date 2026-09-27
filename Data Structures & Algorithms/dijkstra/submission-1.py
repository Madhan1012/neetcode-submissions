import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        adj = [[] for _ in range(n)]

        for u, v, w in edges:
            adj[u].append((v, w))

        dist = {i: float("inf") for i in range(n)}
        dist[src] = 0

        heap = [(0, src)]

        while heap:
            d, node = heapq.heappop(heap)

            if d > dist[node]:
                continue

            for nei, weight in adj[node]:
                new_dist = d + weight

                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    heapq.heappush(heap, (new_dist, nei))

        for node in dist:
            if dist[node] == float("inf"):
                dist[node] = -1

        return dist