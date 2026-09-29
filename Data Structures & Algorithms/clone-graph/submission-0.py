"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        toNode = {}
        toNode[node] = Node(node.val)
        q = deque([node])

        while q:
            curr = q.popleft()
            for nei in curr.neighbors:
                if nei not in toNode:
                    toNode[nei] = Node(nei.val)
                    q.append(nei)
                toNode[curr].neighbors.append(toNode[nei])
        return toNode[node]