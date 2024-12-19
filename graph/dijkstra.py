import heapq
import ast

class Dijkstra:
    def __init__(self):
        pass
    
    def run(self, graph, start_node):
        # Pastikan graph adalah dictionary yang valid
        if isinstance(graph, str):
            try:
                # Mengonversi string menjadi list of tuples
                graph = ast.literal_eval(graph)
            except Exception as e:
                raise ValueError(f"Error processing graph: {e}")
        
        # Membuat graph adjacency list dari list of tuples
        adj_list = {}
        for u, v, w in graph:
            if u not in adj_list:
                adj_list[u] = {}
            adj_list[u][v] = w
            if v not in adj_list:
                adj_list[v] = {}
            adj_list[v][u] = w  # Assuming undirected graph, add reverse edge

        # Mengonversi start_node ke integer jika diteruskan sebagai string
        start_node = int(start_node)

        # Inisialisasi jarak dari start_node ke semua node
        distances = {node: float('inf') for node in adj_list}
        distances[start_node] = 0
        
        # Menyimpan node yang akan diproses, diurutkan berdasarkan jarak terpendek
        priority_queue = [(0, start_node)]  # (jarak, node)
        
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            
            # Lewati jika jarak yang diambil lebih besar dari yang sudah ditemukan
            if current_distance > distances[current_node]:
                continue
            
            # Proses semua tetangga dari node saat ini
            for neighbor, weight in adj_list[current_node].items():
                distance = current_distance + weight
                
                # Jika jarak ke tetangga lebih pendek, perbarui jarak dan masukkan ke priority queue
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances
