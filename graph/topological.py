import ast

class TopologicalSort:
    def run(self, graph):
        # Jika graph berupa string, ubah menjadi dictionary
        if isinstance(graph, str):
            try:
                graph = ast.literal_eval(graph)
            except (ValueError, SyntaxError):
                raise ValueError("Invalid graph format. It should be a valid dictionary or adjacency list.")
        
        # Pastikan graph adalah dictionary
        if not isinstance(graph, dict):
            raise ValueError("Graph should be a dictionary with node as key and list of neighbors as value.")
        
        visited = set()  # Menyimpan node yang sudah dikunjungi
        result = []  

        # Fungsi DFS untuk mengunjungi node dan menambahkannya ke hasil
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph.get(node, []):
                dfs(neighbor)
            result.append(node)

        # Lakukan DFS untuk setiap node yang belum dikunjungi
        for node in graph:
            if node not in visited:
                dfs(node)

        return result[::-1]  # Balikkan hasil DFS untuk mendapatkan urutan yang benar



