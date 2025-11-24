# Conway's Game of Life Simulator

A Python-based implementation of Conway's Game of Life, a cellular automaton where cells evolve based on rules applied to a grid.

## Overview

Conway's Game of Life Simulator provides:
- Pattern loading from text files using regex parsing
- Grid evolution
- Visual display of cell generations in the terminal
- Logging of simulation performance and events
- Support for classic patterns (Blinker, Glider, etc.)
- Error handling for invalid patterns and grid configurations

```
GameOfLife/
|-- patterns/
|   |-- blinker.txt                 # 3x3 blinker pattern
|   |-- glider.txt                  # 3x3 glider pattern
|   \-- other.json                  # Currently a 20x20 puffer train
|-- logs/ 
|   \-- simulation.log
|-- game_of_life/
|   |-- __init__.py
|   |-- main.py                     # Main entry point with CLI menu
|   |-- grid.py                     # Grid management
|   |-- rules.py                    # Evolution rules
|   \-- utils.py                    # Utility functions (logging, timing)
|-- tests/
|   -- grid_test.py                 # Pytest unit tests
|-- requirements.txt
|-- setup.py
|-- README.md
```

## Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup

1. **Navigate to the GameOfLife directory**:
   ```bash
   cd CODE/GameOfLife
   ```

2. **Install the package in development mode**:
   ```bash
   pip install -e .
   ```

   This will install all dependencies from [`requirements.txt`](requirements.txt).

## Usage

### Running the Simulator

Due to poor file path handling, the packages can't be run on their own, and only through the main python files located outside the folder holding the Game Of Life package.

```bash
python CODE/main.py  
```
Select option 2 for Game of Life

### Interactive Menu

1. **Choose a pattern**:
   - Glider: Cluster of cells that travels diagonally (3x3)
   - Blinker: Alternating 3 cells from horizontal to vertical line (3x3)
   - Other: Custom pattern (out of box: puffer train) (20x20)

2. **Set grid position**:
   - Enter offset row/column
   - Default: Pattern centered on grid

3. **Watch evolution**:
   - Grid updates automatically each generation
   - Press `Ctrl+C` to stop simulation
   - Simulation ends when all cells die

## Example Workflow

1. Prepare pattern in .txt format
2. Run the main file in CODE folder: `python main.py`
3. Select Game Of Life package
4. Select Pattern
5. Input offset row and column
6. Watch generations evolve
7. Watch them go extinct or keyboard interrupt

### Example Session

```
Choose pattern (glider/blinker/other): glider
Enter offset row (default centered, use 0 if other was chosen): 2
Enter offset column (default centered, use 0 if other was chosen): 2

Generation 0
========================================
· · · · · · · · · · · · · · · · · · · ·
· · · · · · · · · · · · · · · · · · · ·
· · · O · · · · · · · · · · · · · · · ·
· · · · O · · · · · · · · · · · · · · ·
· · O O O · · · · · · · · · · · · · · ·
...
========================================
Press Ctrl+C to stop
```

## Pattern File Format

Pattern files use simple text format with `O` for alive cells and `.` for dead cells:

**blinker.txt**:
```
.O.
.O.
.O.
```

**glider.txt**:
```
.O.
..O
OOO
```
## Features

### Core Functionality
- **Grid Management**: Create and manipulate 2D cellular grids
- **Pattern Loading**: Load initial states from `.txt` pattern files
- **Evolution Engine**: Apply Conway's Game of Life rules to evolve cells
- **Display**: Animated terminal visualization of generations

## Key Functions and Classes

### Grid Class ([`grid.py`](game_of_life/grid.py))
- `__init__(rows, cols)`: Initialize grid with dimensions
- `load_pattern(pattern, offset_row, offset_col)`: Load pattern at position
- `display()`: Render grid to terminal
- `evolve()`: Evolve grid to next generation
- `is_grid_alive()`: Check if any cells are alive

### Rules Class ([`rules.py`](game_of_life/rules.py))
- `count_neighbors(grid, row, col)`: Count live neighbors for a cell
- `evolve_grid(grid)`: Apply Conway's rules to entire grid
- `will_live(is_alive, live_neighbors)`: Determine cell survival

### Utility Functions ([`utils.py`](game_of_life/utils.py))
- `@timed`: Decorator for performance logging
- `load_pattern_from_txt(filepath)`: Parse pattern files with regex
- `clear_screen()`: Clear terminal display

## Conway's Game of Life Rules

1. **Survival**: Live cell with 2-3 neighbors survives
2. **Death**: Live cell with <2 or >3 neighbors dies
3. **Birth**: Dead cell with exactly 3 neighbors becomes alive

## Testing

Run unit tests with pytest:

```bash
pytest tests/grid_test.py -v
```

### Test Coverage
- Grid initialization
- Pattern loading with offsets
- Boundary checking
- Cell state management
- Grid clearing

## Error Handling

### Custom Exceptions
- **GridSizeError**: Invalid grid dimensions
- **PatternSizeError**: Pattern doesn't fit in grid
- **PatternLoadError**: Invalid pattern file format

### Example Error Messages
```
GridSizeError: Grid size must be positive integers.
PatternSizeError: Pattern does not fit in the grid at the given offset.
PatternLoadError: Invalid pattern line: X.O
```

## Logging

Simulation events are logged to [`logs/simulation.log`](logs/simulation.log):

```
2025-11-24 14:30:15 - INFO - Function load_pattern took 0.0012 seconds
2025-11-24 14:30:15 - INFO - Function main took 12.4567 seconds
```

## Development

To extend the system:
- Add more patterns (Gosper Glider Gun, Pulsar, etc.) to [`patterns/`] folder.
- Add functionality to check the [`patterns/`] folder for files, and list them for the user.
- Add color-coded cell age visualization [`game_of_lige/rules.py`]

## Author

**Jonas Lysfjord Kemi**  
OsloMet - Oslo Metropolitan University  
Course: Scripting with Python (H-25)

## License

This project was developed as part of a Python scripting course final exam.

---

**Note**: Due to file path handling, packages should be run through the main launcher (`main.py`) rather than individually.