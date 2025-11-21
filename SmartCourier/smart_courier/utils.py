import csv
import time
import logging
from functools import wraps

def view_csv_file(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        count = 0
        for row in reader:
            if count == 0:
                print("\n" +", ".join(row))
                print("-" * len(", ".join(row)))
                count += 1
                continue
            print(", ".join(row))
            count += 1
            
def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(f"Function {func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper