# Statistics Calculator

## Overview
A modular Python package that calculates and displays basic statistics (average, maximum, minimum) from a list of numeric values. The package is designed to be both a standalone CLI tool and a reusable library for other Python projects.

## Features
- **Core Statistics Module**: Reusable functions for calculating statistics
- **CLI Interface**: Interactive command-line tool for quick calculations
- **Type-safe**: Full type hints for better IDE support
- **Flexible Input**: Accepts both integers and floats
- **Data Classes**: Clean, structured output using Python dataclasses

### Statistics Calculated
- Count of values
- Total sum
- Average (mean)
- Maximum value
- Minimum value

## Project Structure
```
.
├── src/
│   └── statistics_calculator/
│       ├── __init__.py       # Package exports
│       ├── core.py           # Core statistics logic
│       └── cli.py            # Command-line interface
├── stats.py                  # CLI entry point
├── example_usage.py          # Examples of using the module
└── replit.md                # Project documentation
```

## Usage

### As a CLI Tool
Run the interactive script and enter numbers when prompted:
```bash
python stats.py
```

You can enter numbers in two formats:
- Space-separated: `5 10 15 20 25`
- Comma-separated: `5, 10, 15, 20, 25`

### As a Reusable Module
Import and use the statistics functions in your own Python scripts:

```python
from statistics_calculator import calculate_statistics

# Calculate statistics for any numeric list
scores = [85, 92, 78, 90, 88]
stats = calculate_statistics(scores)

if stats:
    print(f"Average: {stats.average:.2f}")
    print(f"Max: {stats.maximum}")
    print(f"Min: {stats.minimum}")
```

See `example_usage.py` for more detailed examples including:
- Test score analysis
- Temperature tracking
- Sales data analysis

## API Reference

### `calculate_statistics(values)`
Calculates statistics for a sequence of numbers.

**Parameters:**
- `values` (Sequence[Union[int, float]]): List or sequence of numeric values

**Returns:**
- `Statistics` object with count, average, maximum, minimum, and total
- `None` if the input list is empty

### `Statistics` Class
A dataclass containing:
- `count`: Number of values
- `average`: Mean value
- `maximum`: Highest value
- `minimum`: Lowest value
- `total`: Sum of all values

## Recent Changes
- 2025-10-29: Refactored into modular package structure
  - Separated core logic from CLI interface
  - Added type hints and dataclasses
  - Created reusable module that can be imported
  - Added example usage script demonstrating real-world use cases
- 2025-10-28: Initial project creation with basic statistics functionality
