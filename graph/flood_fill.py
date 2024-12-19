import ast

class FloodFill:
    def run(self, *params):
        # Pastikan menerima 4 parameter
        if len(params) != 4:
            raise ValueError("FloodFill algorithm requires 4 parameters: grid, x, y, new_color.")
        
        # Konversi string menjadi list grid jika grid berupa string
        try:
            grid = params[0]
            if isinstance(grid, str):  # Jika grid berupa string, konversi menjadi list
                grid = ast.literal_eval(grid)
        except Exception as e:
            raise ValueError(f"Error processing grid: {e}")
        
        # Konversi koordinat dan warna
        x = int(params[1]) 
        y = int(params[2]) 
        new_color = int(params[3]) 

        # Validasi grid
        if not isinstance(grid, list):
            raise ValueError("Grid must be a list.")
        if not all(isinstance(row, list) for row in grid):
            raise ValueError("Grid must be a 2D list (list of lists).")
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError("Coordinates x and y must be integers.")
        if not isinstance(new_color, int):
            raise ValueError("New color must be an integer.")
        
        # Memeriksa apakah koordinat berada dalam grid
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
            raise ValueError("Starting coordinates are out of bounds.")

        original_color = grid[x][y]
        if original_color == new_color:
            return grid  # Jika warna sama, tidak perlu diubah

        # Fungsi rekursif untuk flood fill
        def dfs(x, y):
            if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
                return
            if grid[x][y] != original_color:
                return
            grid[x][y] = new_color
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        dfs(x, y)
        return grid



