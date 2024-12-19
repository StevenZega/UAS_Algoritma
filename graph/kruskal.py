class Kruskal:
    class UnionFind:
        def __init__(self, n):
            # Inisialisasi parent dan rank (tingkat kedalaman pohon)
            self.parent = list(range(n))  # Setiap node adalah induk dari dirinya sendiri
            self.rank = [0] * n  # Rank dimulai dengan 0 untuk semua node

        def find(self, u):
            # Fungsi untuk menemukan akar dari set yang mengandung u
            if self.parent[u] != u:
                self.parent[u] = self.find(self.parent[u])  # Path compression untuk efisiensi
            return self.parent[u]

        def union(self, u, v):
            # Menggabungkan dua set yang berbeda, u dan v
            root_u = self.find(u)
            root_v = self.find(v)
            if root_u != root_v:
                # Menggabungkan pohon dengan peringkat (rank) lebih kecil ke pohon dengan peringkat lebih tinggi
                if self.rank[root_u] > self.rank[root_v]:
                    self.parent[root_v] = root_u
                elif self.rank[root_u] < self.rank[root_v]:
                    self.parent[root_u] = root_v
                else:
                    self.parent[root_v] = root_u  # Pilih root_u sebagai root baru jika peringkat sama
                    self.rank[root_u] += 1  # Tingkatkan rank dari root_u

    def kruskal(self, num_nodes, edges):
        # Pastikan num_nodes adalah integer dan edges adalah list dari tuple
        num_nodes = int(num_nodes) 
        if isinstance(edges, str):  # Jika edges diberikan sebagai string, konversikan ke list of tuples
            edges = eval(edges) 

        uf = self.UnionFind(num_nodes)  # Membuat objek UnionFind untuk mengelola komponen yang terhubung
        mst = []  # Menyimpan hasil Minimum Spanning Tree (MST)

        # Mengurutkan edges berdasarkan bobot (edge[2] adalah bobot)
        edges.sort(key=lambda edge: edge[2])

        # Proses setiap edge dalam urutan bobot terkecil
        for u, v, weight in edges:
            # Jika u dan v tidak berada dalam set yang sama
            if uf.find(u) != uf.find(v):
                uf.union(u, v)  # Gabungkan komponen u dan v
                mst.append((u, v, weight))  # Tambahkan edge (u, v, weight) ke MST

        return mst  # Kembalikan MST yang telah terbentuk

    def run(self, num_nodes, edges):
        return self.kruskal(num_nodes, edges)
