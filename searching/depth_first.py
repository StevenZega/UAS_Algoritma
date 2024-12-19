class DepthFirst:
    def run(self, graph, start):
        visited = set()  # Buat set untuk menyimpan node yang sudah dikunjungi
        stack = [start]  # Inisialisasi tumpukan (stack) dengan node awal
        result = []  # List untuk menyimpan urutan traversal

        while stack:
            # Ambil node terakhir dari tumpukan
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)    # Jika node belum dikunjungi Tandai sebagai dikunjungi
                
                # Tambahkan node ke hasil traversal
                result.append(vertex)
                
                # Tambahkan semua tetangga node ke tumpukan
                stack.extend(graph.get(vertex, []))
        
        return result
