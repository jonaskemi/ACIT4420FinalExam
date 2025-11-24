from .utils import timed
from .rules import Rules
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='logs/simulation.log', filemode='a')

class GridSizeError(Exception):
    pass

class PatternSizeError(Exception):
    pass


class Grid:
    def __init__(self, rows, cols):
        if rows <= 0 or cols <= 0:
            logging.error("Invalid grid size - must be positive integers")
            raise GridSizeError("Grid size must be positive integers.")
        self.rows = rows
        self.cols = cols
        self.grid = self.create_empty_grid()

    def create_empty_grid(self):
        return [[0 for _ in range(self.cols)] for _ in range(self.rows)]
    
    @timed
    # Load pattern from file
    def load_pattern(self, pattern, offset_row=0, offset_col=0):
        if not pattern or not pattern[0]:
            raise PatternSizeError("Pattern cannot be empty.")
        
        pattern_rows = len(pattern)
        pattern_cols = len(pattern[0])
    
        # Check if pattern fits in the grid
        if (offset_row + pattern_rows > self.rows) or (offset_col + pattern_cols > self.cols):
            logging.error(f"Pattern size: {pattern_rows}x{pattern_cols}, Grid: {self.rows}x{self.cols}, Offset: ({offset_row},{offset_col})")
            raise PatternSizeError(f"Pattern ({pattern_rows}x{pattern_cols}) does not fit in grid ({self.rows}x{self.cols}) at offset ({offset_row},{offset_col}).")
            
        
        for r in range(pattern_rows):
            for c in range(pattern_cols):
                self.grid[offset_row + r][offset_col + c] = pattern[r][c]
                
    def display(self):
        for row in self.grid:
            print(" ".join([' O ' if cell else ' . ' for cell in row]))
        print()
        
    def get_cell(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.grid[row][col]
        return 0  # Treat out-of-bounds as dead cells
    
    def set_cell(self, row, col, state):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.grid[row][col] = state
            
    def evolve(self):
        self.grid = Rules.evolve_grid(self.grid)
        
    def is_grid_alive(self):
        return any(cell == 1 for row in self.grid for cell in row)
            
    def clear(self):
        self.grid = self.create_empty_grid()