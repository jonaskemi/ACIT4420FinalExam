import time
import logging
from functools import wraps
import re
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='GameOfLife/logs/simulation.log', filemode='a')

def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(f"Function {func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

class PatternLoadError(Exception):
    pass

def load_pattern_from_txt(filepath):
    """Load pattern from TXT file and convert to 2D grid."""
    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()
        
        grid = []
        
        for line in lines:
            line = line.strip()
            
            # Skip empty lines
            if not line:
                continue
            
            # Use regex to validate line contains only O and .
            if not re.match(r'^[O.]+$', line):
                logging.error("Invalid pattern line: %s", line)
                raise PatternLoadError(f"Invalid pattern line: {line}")
            
            # Convert O to 1, . to 0
            row = [1 if cell == 'O' else 0 for cell in line]
            grid.append(row)
        
        if not grid:
            logging.error("Error loading pattern from file: No valid pattern found")
            raise PatternLoadError("No valid pattern found in file")
        
        return grid
    
    except FileNotFoundError:
        logging.error("Error loading pattern from file: %s", filepath)
        raise PatternLoadError(f"Pattern file not found: {filepath}")
    except Exception as e:
        logging.error("Error loading pattern: %s", e)
        raise PatternLoadError(f"Error loading pattern: {e}")
    
def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')    