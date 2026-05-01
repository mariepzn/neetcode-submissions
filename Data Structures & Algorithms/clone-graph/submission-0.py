"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew={}

        if not node:
            return
        if node.val is None:
            return [[]]
        def bfs(node):
            q=deque([node])
            new_node=Node(node.val)
            oldToNew[node]=new_node
            while q:

                cur = q.popleft()
                for nei in cur.neighbors:
                    if nei not in oldToNew:
                        q.append(nei)
                        new_nei=Node(nei.val)
                        oldToNew[nei]=new_nei
                    oldToNew[cur].neighbors.append(oldToNew[nei])
                

        bfs(node)
        return oldToNew[node]        