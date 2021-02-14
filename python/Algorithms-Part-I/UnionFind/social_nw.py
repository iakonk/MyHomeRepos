class UnionFind(object):
    def __init__(self, N):
        self.id = [id for id in range(N)]
        self.size = 0

    def union(self, p, q):
        pass

    def connected(self, p, q):
        return self.id[p] == self.id[q]


class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next


n1 = Node(6, 6)
n2 = Node(6, 6)

print(n1.next is n2)