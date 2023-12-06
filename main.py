"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew ={}  # hashmap

        def dfs(node):  # clone
            if node in oldToNew:  # if node is in hashmap, we already made a clone of  it
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        # return if node is not null, otherwise, return None
        return dfs(node) if node else None