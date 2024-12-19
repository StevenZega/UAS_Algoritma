class BellmanFord:
    def run(self, graph, num_nodes=None):
        # Jika jumlah node tidak diberikan, tentukan berdasarkan jumlah key dalam graph
        if num_nodes is None:
            num_nodes = len(graph) 

        # Pastikan num_nodes adalah integer
        if isinstance(num_nodes, str):  
            num_nodes = int(num_nodes)

        # Inisialisasi jarak dari node sumber ke semua node lainnya sebagai tak terhingga 
        dist = {node: float('inf') for node in range(num_nodes)}
        dist[0] = 0  

        # Ulangi sebanyak num_nodes - 1 kali
        for _ in range(num_nodes - 1):
            # Periksa setiap node u
            for u in range(num_nodes):
                # Periksa setiap v dan bobotnya dari node u
                for v, weight in graph.get(u, []):
                    # Jika jarak dari u ke v lebih kecil melalui edge (u, v), perbarui jarak v
                    if dist[u] + weight < dist[v]:
                        dist[v] = dist[u] + weight

        # Cek siklus negatif
        for u in range(num_nodes):
            for v, weight in graph.get(u, []):
                # Jika jarak masih bisa diperkecil, berarti ada siklus negatif
                if dist[u] + weight < dist[v]:
                    raise ValueError("Graph contains a negative weight cycle")

        # Kembalikan jarak terpendek dari node 0 ke semua node
        return dist
