"""
https://leetcode.com/discuss/interview-question/436073/

You are given an undirected connected graph.
An articulation point (or cut vertex) is defined as a vertex which,
when removed along with associated edges, makes the graph disconnected
(or more precisely, increases the number of connected components in the graph).
The task is to find all articulation points in the given graph.

Input:
The input to the function/method consists of three arguments:

numNodes, an integer representing the number of nodes in the graph.
numEdges, an integer representing the number of edges in the graph.
edges, the list of pair of integers - A, B representing an edge between the nodes A and B.
Output:
Return a list of integers representing the critical nodes.

Tarjan`s algo: leetcode/hard/crit_connections.py
"""
import collections


def dfs(at, graph, visited_nodes):
    """ O(V+E) """
    visited_nodes[at] = True
    all_conn = graph[at]
    for conn in all_conn:
        if not visited_nodes[conn]:
            dfs(conn, graph, visited_nodes)
    return visited_nodes


def is_graph_connected(graph):
    visited_nodes = [False] * len(graph)
    dfs(0, graph, visited_nodes)
    return all(visited_nodes)


def make_graph(edges):
    """ {
        0: 1, 2,
        1: 0, 2, 3, 4
        2: 0, 3
    }"""
    graph = collections.defaultdict(list)
    for from_, to_ in edges:
        graph[from_].append(to_)
        graph[to_].append(from_)
    return graph


def brute_force(edges):
    """ DFS is running inside the loop of connections and each connection represents 2 edges
        O( 2E * (V+E))
    """
    graph = make_graph(edges)

    c_conn = []
    for from_, to_ in edges:
        # remove one edge from the graph
        if from_ in graph:
            graph[from_].remove(to_)
        if to_ in graph:
            graph[to_].remove(from_)

        is_connected = is_graph_connected(graph)
        if not is_connected:
            c_conn.append(from_)

        # add edges back
        if from_ in graph:
            graph[from_].append(to_)
        if to_ in graph:
            graph[to_].append(from_)
    return c_conn


edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
assert sorted(brute_force(edges)) == [2, 3, 5]
