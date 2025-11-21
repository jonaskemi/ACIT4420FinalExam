# Smart Courier Optimizer

A Python-based courier delivery route optimization system that calculates optimal delivery routes based on distance, priority, and transport mode preferences.

## Overview

Smart Courier Optimizer helps delivery services plan efficient routes by:
- Validating delivery data using regex patterns
- Calculating optimal routes using the Haversine formula
- Supporting multiple transport modes (Car, Bicycle, Walking)
- Providing detailed cost, time, and CO2 emission calculations
- Logging execution times and validation results

## Project Structure

```
SmartCourier/
|-- data/
|   |-- deliveries.csv              # Input delivery data
|   \-- transport_modes.json        # Transport mode specifications
|-- output/ 
|   |-- valid.csv                   # Validated deliveries
|   |-- rejected.csv                # Invalid deliveries
|   |-- optimized_route.csv         # Distance-optimized route
|   |-- optimized_route_mode.csv    # Route with all transport options
|   |-- final_route.csv             # Final route with selected mode
|   \-- run.log                     # Execution logs
|-- smart_courier/
|   |-- __init__.py
|   |-- main.py                     # Main entry point with CLI menu
|   |-- validation.py               # Input validation functions
|   |-- optimizer.py                # Route optimization algorithms
|   \-- utils.py                    # Utility functions (logging, timing)
|-- tests/
|   -- validation_test.py           # Pytest unit tests
|-- requirements.txt
|-- setup.py
|-- README.md
```

## Installation

### Prerequisites
- Python 3.7 or higher
- Virtual environment (recommended)

### Install Dependencies

Install the package and its dependencies:

```bash
pip install -e .
```

Or install dependencies manually:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

Run the main application:

```bash
python -m smart_courier.main
```

### Interactive Menu

The application provides an interactive CLI menu with the following options:

1. **Start Validation and Optimization Process**
   - Validate delivery data from CSV
   - Calculate optimized routes
   - Generate route summaries for different transport modes
   - Save final route with selected transport mode

2. **Reset Output Files**
   - Clear all output CSV files
   - Recommended before new optimization runs

3. **Open Output Files Manually**
   - View any generated output file

4. **Exit**

### Input Data Format

Create a CSV file with the following format ([data/deliveries.csv](data/deliveries.csv)):

```c
customer,latitude,longitude,priority,weight_kg
oslomet,59.91975231772749,10.735437671046288,high,20
northfish,68.13330290294708,13.436546727334079,medium,45
oilers,58.95400253440023,5.690332621833003,low,12.4
```

**Validation Rules:**
- `customer`: Non-empty string with printable characters
- `latitude`: Float between -90 and 90
- `longitude`: Float between -180 and 180
- `priority`: Must be "High", "Medium", or "Low" (case-insensitive)
- `weight_kg`: Positive number

### Transport Modes

The system supports three transport modes defined in [data/transport_modes.json](data/transport_modes.json):

| Mode     | Speed (km/h) | Cost (NOK/km) | CO2 (g/km) |
|----------|--------------|---------------|------------|
| Car      | 50           | 4             | 120        |
| Bicycle  | 15           | 0             | 0          |
| Walking  | 5            | 0             | 0          |

## Features

### Validation System
- Regex-based validation using [`validate_priority`](smart_courier/validation.py), [`validate_customer_name`](smart_courier/validation.py), etc.
- Invalid entries are logged to [output/rejected.csv](output/rejected.csv)
- Valid entries are saved to [output/valid.csv](output/valid.csv)

### Route Optimization
- Uses Haversine formula for distance calculation (see [`haversine`](smart_courier/optimizer.py))
- Priority-based routing (High > Medium > Low)
- Nearest-neighbor algorithm for route planning
- Returns to depot after all deliveries

### Performance Logging
- All functions wrapped with [`@timed`](smart_courier/utils.py) decorator
- Execution times logged to [output/run.log](output/run.log)
- Statistics printed at end of each run

## Testing

Run the test suite using pytest:

```bash
pytest tests/validation_test.py
```

Or run all tests:

```bash
pytest
```

### Test Coverage

Tests are provided for validation functions in [tests/validation_test.py](tests/validation_test.py):
- Customer name validation
- Priority validation (High/Medium/Low)
- Latitude validation (-90 to 90)
- Longitude validation (-180 to 180)
- Weight validation (positive numbers)

## Output Files

### valid.csv
Contains deliveries that passed validation checks.

### rejected.csv
Contains deliveries that failed validation with original data preserved.

### optimized_route.csv
Shows the optimized route with distances between stops:
```cs
from_customer,to_customer,distance_km
```

### optimized_route_mode.csv
Shows route metrics for all three transport modes:
```cs
from_customer,to_customer,distance_km,mode_of_transport,time_hrs,cost,emissions_kgCO2
```

### final_route.csv
Final route using the selected transport mode:
```cs
from_customer,to_customer,distance_km,mode_of_transport,time_hrs,cost,emissions_kgCO2
```

### run.log
Structured log file using logging module

## Example Workflow

1. Prepare your delivery data in CSV format
2. Run the application: `python -m smart_courier.main`
3. Select option 1 to start validation
4. Review validated and rejected deliveries
5. Proceed to optimization
6. View route summaries for all transport modes
7. Select your preferred transport mode
8. Review the final optimized route

## Module Reference

### [`validation.py`](smart_courier/validation.py)
Contains regex patterns and validation functions for input data.

### [`optimizer.py`](smart_courier/optimizer.py)
Core optimization logic including:
- [`haversine`](smart_courier/optimizer.py): Distance calculation
- [`calculate_distance`](smart_courier/optimizer.py): Route optimization
- [`calculate_transport_modes`](smart_courier/optimizer.py): Multi-mode analysis
- [`save_final_route`](smart_courier/optimizer.py): Output generation

### [`utils.py`](smart_courier/utils.py)
Helper functions:
- [`timed`](smart_courier/utils.py): Decorator for execution timing
- [`view_csv_file`](smart_courier/utils.py): CSV file display utility

### [`main.py`](smart_courier/main.py)
Entry point with interactive CLI menu and workflow orchestration.

## Error Handling

The application handles:
- File not found errors
- Invalid CSV format
- Invalid data types
- Out-of-range coordinates
- Invalid priority values
- Negative weights

All errors are logged and invalid entries are saved to [output/rejected.csv](output/rejected.csv).

## Development

To extend the system:
- Add new transport modes to [data/transport_modes.json](data/transport_modes.json)
- Modify validation rules in [`validation.py`](smart_courier/validation.py)
- Implement new optimization algorithms in [`optimizer.py`](smart_courier/optimizer.py)
- Add new tests in the `tests/` directory

## License

This project was developed as part of a Python scripting course final exam.