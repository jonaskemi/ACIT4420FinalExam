class Rules:
    @staticmethod
    def count_neighbors(grid, row, col):
        rows = len(grid)
        cols = len(grid[0])
        
        # 8 directions
        directions = [
            (-1, -1), (-1, 0), (-1, 1),  # Top row
            (0, -1),           (0, 1),    # Middle row (left, right)
            (1, -1),  (1, 0),  (1, 1)     # Bottom row
        ]
        
        count = 0
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            # Check bounds and if cell is alive
            if 0 <= new_row < rows and 0 <= new_col < cols:
                count += grid[new_row][new_col]
        
        return count
    
    @staticmethod
    def will_live(is_alive: bool, live_neighbors: int) -> bool:
        if is_alive:
            return live_neighbors in (2, 3)  # Survival: 2-3 neighbors
        else:
            return live_neighbors == 3        # Birth: exactly 3 neighbors
        
    @staticmethod
    def next_state(current_state: int, live_neighbors: int) -> int:
        is_alive = current_state == 1
        return 1 if Rules.will_live(is_alive, live_neighbors) else 0
    
    @staticmethod
    def evolve_grid(grid):
        rows = len(grid)
        cols = len(grid[0])
        
        # Create new grid
        new_grid = [[0 for _ in range(cols)] for _ in range(rows)]
        
        for row in range(rows):
            for col in range(cols):
                neighbors = Rules.count_neighbors(grid, row, col)
                new_grid[row][col] = Rules.next_state(grid[row][col], neighbors)
        
        return new_grid