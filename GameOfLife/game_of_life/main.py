from .grid import Grid
from .utils import timed, load_pattern_from_txt, clear_screen
import time
import logging

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='GameOfLife/logs/simulation.log', filemode='a')
stats = {'start_time': None, 'end_time': None}

@timed
def main():
    import time as timemodule
    
    # Example usage
    rows, cols = 20, 20
    grid = Grid(rows, cols)
    
    # Pass blinker.txt pattern to load_pattern function in grid class
    glider_pattern = load_pattern_from_txt("GameOfLife/patterns/glider.txt")
    blinker_pattern = load_pattern_from_txt("GameOfLife/patterns/blinker.txt")
    other_pattern = load_pattern_from_txt("GameOfLife/patterns/other.txt")
    
    pattern = input("Choose pattern (glider/blinker/other): ").strip().lower()
    if pattern == "glider":
        pattern = glider_pattern
    elif pattern == "blinker":
        pattern = blinker_pattern
    elif pattern == "other":
        pattern = other_pattern
    else:
        print("Invalid pattern choice. Defaulting to glider.")
        pattern = glider_pattern
        
    offset_row = input("Enter offset row (default centered, use 0 if other was chosen): ").strip()
    offset_col = input("Enter offset column (default centered, use 0 if other was chosen): ").strip()
    offset_row = int(offset_row) if offset_row.isdigit() else int(rows / 2) - len(pattern) + 1
    offset_col = int(offset_col) if offset_col.isdigit() else int(cols / 2) - len(pattern[0]) + 1
    
    grid.load_pattern(pattern, offset_row=offset_row, offset_col=offset_col)
    
    print("Initial Grid:")
    grid.display()
    
    generation = 0
    
    stats['start_time'] = timemodule.time()
    try: 
        while grid.is_grid_alive():
            clear_screen()
            print(f"Generation {generation}")
            print("=" * 80)
            grid.display()
            print("=" * 80)
            print("Press Ctrl+C to stop the simulation.")
            time.sleep(0.2)
            grid.evolve()
            generation += 1
    
        print("Simulation ended because all cells are dead.")
        logging.info(f"All cells are dead at generation {generation}.")
    
    except KeyboardInterrupt:
        logging.info(f"Simulation stopped by user at generation {generation}.")
        print(f"Simulation stopped by user at {generation} generation(s).")
        print("Final Grid State:")
        grid.display()
        print("=" * 80)
        
    stats['end_time'] = timemodule.time()
    logging.info(f"Simulation ran for {stats['end_time'] - stats['start_time']} seconds.")
          
if __name__ == "__main__":
    main()