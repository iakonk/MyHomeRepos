"""
DFS runs with the complexity of O(V+E)
Usually performs tasks:
- count connected components
- determine connectivity
- find bridges/articulation points
- compute minimum spanning tree
"""

n = 10 # number of nodes
graph = [[], []] # list of edges
visited = [False] * n # track of visited nodes


def dfs(at):
    if visited[at]: return
    visited[at] = True
    neighbours = graph[at]
    for next in neighbours:
        dfs(next)


start_node = 0
dfs(start_node)

# Connected components:
# Algorithm:
# start a DFS at every node (except it is already been visited) and mark all reachable nodes with the lowest id,
# reachable from that node.
n = 10 # number of nodes in the graph
graph = [[], []]
components = [0] * n
visited = [False] * n


def findComponents():
    count = 0
    for i in range(n):
        if not visited[i]:
            count += 1
            dfs(i, count)
    return count


def dfs(at, count):
    visited[at] = True
    components[at] = count
    for next in graph[at]:
        dfs(next, count)