class FloydWarshall:
    
    def run(self, graph):
        num_nodes = len(graph)  # Menentukan jumlah node dalam graf
        dist = [[float('inf')] * num_nodes for _ in range(num_nodes)]
        
        # Inisialisasi jarak antar node
        for u in range(num_nodes):
            for v in range(num_nodes):
                if u == v:
                    dist[u][v] = 0  # Jarak dari node ke dirinya sendiri adalah 0
                elif graph[u][v] != 0:
                    dist[u][v] = graph[u][v]  # Jika ada edge dari u ke v, inisialisasi jaraknya dengan bobot edge tersebut

        # Algoritma Floyd-Warshall: Menghitung jarak terpendek antara semua pasangan node
        for k in range(num_nodes):  # K adalah node perantara yang digunakan untuk mencari jalur lebih pendek
            for i in range(num_nodes):  # i adalah node asal
                for j in range(num_nodes):  # j adalah node tujuan
                    # Jika jarak langsung dari i ke j lebih besar daripada jarak melalui node k
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        return dist





