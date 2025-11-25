# CODE - Python Scripting Final Exam Project

A comprehensive Python project showcasing two independent applications: **SmartCourier** (package delivery optimization) and **GameOfLife** (Conway's cellular automaton simulator). This project demonstrates advanced Python concepts including file handling, modular design, metaprogramming, error handling, and regular expressions.

## Project Overview

This repository contains two complete Python packages, each solving distinct problems while implementing the same core programming principles:

1. **SmartCourier** - A delivery route optimization system
2. **GameOfLife** - Conway's Game of Life simulator

Both packages are accessible through a unified CLI launcher that provides easy navigation between the applications.

## Project Structure

```
CODE/
|-- main.py                         # Main CLI launcher
|-- README.md                       # This file
|-- SmartCourier/                   # Package delivery optimizer
|   |-- smart_courier/
|   |   |-- __init__.py
|   |   |-- main.py
|   |   |-- validation.py
|   |   |-- optimizer.py
|   |   \-- utils.py
|   |-- data/
|   |-- output/
|   |-- tests/
|   |-- requirements.txt
|   |-- setup.py
|   \-- README.md                   # SmartCourier documentation
\-- GameOfLife/                     # Conway's Game of Life
    |-- game_of_life/
    |   |-- __init__.py
    |   |-- main.py
    |   |-- grid.py
    |   |-- rules.py
    |   \-- utils.py
    |-- patterns/
    |-- logs/
    |-- tests/
    |-- requirements.txt
    |-- setup.py
    \-- README.md                   # GameOfLife documentation
```

## Quick Start

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone or download this repository**

2. **Install SmartCourier package**:
   ```bash
   cd CODE/SmartCourier
   pip install -e .
   cd ..
   ```

3. **Install GameOfLife package**:
   ```bash
   cd GameOfLife
   pip install -e .
   cd ..
   ```

### Running the Application

From the `CODE/` directory, run:

```bash
python main.py
```

You'll see a menu like this:

```
============================================================
               WELCOME TO CODE PROJECT
============================================================

Main Menu:
----------------------------------------
1. SmartCourier - Package Delivery System
2. GameOfLife - Conway's Game of Life Simulator
3. Exit
----------------------------------------

Enter your choice (1-3):
```

## Package Summaries

### 1. SmartCourier - Package Delivery Optimizer

A route optimization system for courier services that:
- Validates delivery data using regex patterns
- Calculates optimal routes using the Haversine formula
- Supports multiple transport modes (Car, Bicycle, Walking)
- Generates detailed cost, time, and CO2 emission reports

**Key Features:**
- CSV file validation with regex
- Priority-based route optimization
- Multi-modal transport analysis
- Comprehensive logging and reporting

📖 **[View SmartCourier Documentation](SmartCourier/README.md)**

### 2. GameOfLife - Conway's Game of Life Simulator

A cellular automaton simulator implementing Conway's Game of Life:
- Loads patterns from text files
- Real-time terminal visualization
- Customizable grid sizes and starting positions
- Classic patterns included (Blinker, Glider)

**Key Features:**
- Pattern parsing with regex validation
- Grid evolution
- Interactive terminal display
- Performance logging

📖 **[View GameOfLife Documentation](GameOfLife/README.md)**

## Usage Examples

### SmartCourier Workflow

```bash
python main.py
# Select option 1

# Interactive menu:
# 1. Validate and optimize deliveries
# 2. Reset output files
# 3. View output files
# 4. Exit
```

### GameOfLife Workflow

```bash
python main.py
# Select option 2

# Interactive prompts:
# - Choose pattern (glider/blinker/other)
# - Set grid position
# - Watch real-time evolution
# - Press Ctrl+C to stop
```

## Testing

### Run All Tests
```bash
# Test SmartCourier
python -m pytest smartcourier/tests/ -v
```

```bash
# Test GameOfLife
python -m pytest gameoflife/tests/ -v
```

### Test Coverage

Both packages include comprehensive unit tests:
- **SmartCourier**: Validation functions, regex patterns
- **GameOfLife**: Grid operations, pattern loading, evolution rules


## Dependencies

Both packages use minimal dependencies:
- **pytest** - Testing framework
- **Python standard library** - All core functionality

Install all dependencies:
```bash
pip install pytest
```

## Documentation

- 📄 [SmartCourier README](SmartCourier/README.md) - Detailed package documentation
- 📄 [GameOfLife README](GameOfLife/README.md) - Complete simulator guide

## Author

**Jonas Lysfjord Kemi**  
OsloMet - Oslo Metropolitan University  
Course: Scripting with Python (H-25)

## License

This project was developed as part of a Python scripting course final exam.

---

**Note**: Due to file path handling, packages should be run through the main launcher (`main.py`) rather than individually.