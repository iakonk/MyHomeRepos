"""
Runs with time complexity of O(V+E).

Particularly useful for one thing:
finding the shortest path on unweighted graphs

Starts at node 0 and adds all neighbours to a queue.
"""
import collections


n = 10 # num of nodes in a graph
graph = {}


def bfs(start_node, end_node):
    prev = solve(start_node) # who the parent of i was
    return reconstructPath(start_node, end_node, prev)


def solve(at):
    queue = collections.deque()
    queue.append(at)

    visited = [False] * n
    visited[at] = True
    prev = [None] * n

    while queue:
        node = queue.pop()
        neighbours = graph[node]
        for next in neighbours:
            if not visited[next]:
                queue.append(next)
                visited[next] = True
                prev[next] = node
    return prev


def reconstructPath(start_node, end_node, prev):
    path = []
    