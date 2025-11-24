import pytest
from game_of_life.grid import Grid

def test_grid_initialization():
    grid = Grid(5, 5)
    assert grid.rows == 5
    assert grid.cols == 5
    assert all(cell == 0 for row in grid.grid for cell in row)
    
def test_load_pattern():
    grid = Grid(5, 5)
    pattern = [
        [1, 0, 0],
        [0, 1, 1],
        [1, 1, 0]
    ]
    grid.load_pattern(pattern, offset_row=1, offset_col=1)
    
    expected_grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    
    assert grid.grid == expected_grid
    
def test_load_pattern_out_of_bounds():
    grid = Grid(5, 5)
    pattern = [
        [1, 1],
        [1, 1]
    ]
    with pytest.raises(Exception):
        grid.load_pattern(pattern, offset_row=4, offset_col=4)
        
def test_set_and_get_cell():
    grid = Grid(3, 3)
    grid.set_cell(1, 1, 1)
    assert grid.get_cell(1, 1) == 1
    assert grid.get_cell(0, 0) == 0
    assert grid.get_cell(3, 3) == 0  # Out of bounds should return 0
    
def test_clear_grid():
    grid = Grid(3, 3)
    grid.set_cell(1, 1, 1)
    grid.clear()
    assert all(cell == 0 for row in grid.grid for cell in row)
    
if __name__ == "__main__":
    pytest.main()