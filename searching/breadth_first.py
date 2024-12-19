class BreadthFirst:
    def run(self, graph, start):
        visited = set()  # membuat set untuk menyimpan node yang sudah dikunjungi
        queue = [start]   # Inisialisasi antrian dengan node awal
        result = []   # menyimpan urutan traversal

        while queue:
            # Ambil node pertama dari antrian
            vertex = queue.pop(0)
            
            # Jika node belum dikunjungi
            if vertex not in visited:
                # Tandai sebagai dikunjungi
                visited.add(vertex)
                
                # Tambahkan node ke hasil traversal
                result.append(vertex)
                
                # Tambahkan semua tetangga node ke antrian
                queue.extend(graph.get(vertex, []))
        
        return result
