class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def run(self, n, operations):
        uf = UnionFind(int(n))  # Inisialisasi UnionFind dengan n elemen
        results = []
        
        for op in operations:
            if op[0] == "union":
                uf.union(int(op[1]), int(op[2]))
            elif op[0] == "connected":
                result = uf.connected(int(op[1]), int(op[2]))
                results.append(result)
        return results