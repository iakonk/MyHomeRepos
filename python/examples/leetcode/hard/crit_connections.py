class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        import collections

        def dfs(at, parent, bridges, id):
            id += 1
            visited[at] = True
            low[at] = ids[at] = id

            for to in graph[at]:
                if to == parent: continue
                if not visited[to]:
                    dfs(to, at, bridges, id)
                    low[at] = min(low[at], low[to])
                    if ids[at] < low[to]:
                        bridges.append([at, to])
                else:
                    low[at] = min(low[at], ids[to])
            return bridges

        visited = [False] * n
        ids = [0] * n
        low = [0] * n
        graph = collections.defaultdict(list)

        for conn in connections:
            from_, to_ = conn
            graph[from_].append(to_)
            graph[to_].append(from_)

        bridges = []
        for node in graph:
            if not visited[node]:
                dfs(node, -1, bridges, -1)
        return bridges


ans = Solution().criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]])
assert ans == [[1, 3]]
