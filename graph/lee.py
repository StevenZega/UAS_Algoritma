from collections import deque

class Lee:
    def __init__(self):
        pass 

    def run(self, grid, start_x, start_y, end_x, end_y):
        # Validasi input untuk grid
        if not isinstance(grid, list) or len(grid) == 0:
            raise ValueError("Grid must be a non-empty list of lists")
        if not all(isinstance(row, list) for row in grid):
            raise ValueError("Each row in grid must be a list")
        if not all(isinstance(cell, int) for row in grid for cell in row):
            raise ValueError("Grid must only contain integers")

        rows = len(grid)
        cols = len(grid[0])
        
        # Pastikan start_x, start_y, end_x, end_y adalah integer
        start_x = int(start_x)
        start_y = int(start_y)
        end_x = int(end_x)
        end_y = int(end_y)

        # Cek apakah titik awal dan titik tujuan berada dalam grid yang valid
        if not (0 <= start_x < rows and 0 <= start_y < cols):
            raise ValueError("Start coordinates are out of bounds")
        if not (0 <= end_x < rows and 0 <= end_y < cols):
            raise ValueError("End coordinates are out of bounds")
        if grid[start_x][start_y] == 1 or grid[end_x][end_y] == 1:
            raise ValueError("Start or End coordinates are blocked by an obstacle")

        # Arah pergerakan dalam 4 arah (atas, bawah, kiri, kanan)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Queue untuk BFS
        queue = deque([(start_x, start_y)])
        
        # Menyimpan jarak dari titik start
        distances = [[-1 for _ in range(cols)] for _ in range(rows)]
        distances[start_x][start_y] = 0

        # Menyimpan path untuk merekonstruksi jalur
        parent = [[None for _ in range(cols)] for _ in range(rows)]

        # Proses BFS untuk mencari jalur
        while queue:
            current_x, current_y = queue.popleft()
            # Jika kita mencapai titik tujuan
            if (current_x, current_y) == (end_x, end_y):
                break

            for dx, dy in directions:
                new_x, new_y = current_x + dx, current_y + dy
                # Cek apakah posisi baru valid
                if 0 <= new_x < rows and 0 <= new_y < cols:
                    if grid[new_x][new_y] == 0 and distances[new_x][new_y] == -1:
                        # Tandai posisi ini telah dikunjungi
                        distances[new_x][new_y] = distances[current_x][current_y] + 1
                        parent[new_x][new_y] = (current_x, current_y)
                        queue.append((new_x, new_y))

        # Rekonstruksi jalur dari titik tujuan ke titik start
        path = []
        if distances[end_x][end_y] != -1:
            current = (end_x, end_y)
            while current != (start_x, start_y):
                path.append(current)
                current = parent[current[0]][current[1]]
            path.append((start_x, start_y))
            path.reverse()
        
        return path  



