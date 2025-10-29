from typing import List, Union, Sequence
from .core import calculate_statistics


def parse_input(user_input: str) -> List[float]:
    if ',' in user_input:
        values = [float(x.strip()) for x in user_input.split(',') if x.strip()]
    else:
        values = [float(x) for x in user_input.split() if x]
    return values


def print_statistics(values: Sequence[Union[int, float]]) -> None:
    if not values:
        print("Error: No values provided")
        return
    
    stats = calculate_statistics(values)
    if stats is None:
        print("Error: Unable to calculate statistics")
        return
    
    print("\n" + "="*40)
    print("BASIC STATISTICS")
    print("="*40)
    print(f"Count:   {stats.count}")
    print(f"Total:   {stats.total:.2f}")
    print(f"Average: {stats.average:.2f}")
    print(f"Maximum: {stats.maximum}")
    print(f"Minimum: {stats.minimum}")
    print("="*40 + "\n")


def run_interactive():
    print("Enter numbers separated by spaces (or comma-separated):")
    user_input = input("> ")
    
    try:
        values = parse_input(user_input)
        
        if not values:
            print("Error: No valid numbers provided")
            return
        
        print_statistics(values)
        
    except ValueError:
        print("Error: Please enter valid numbers only")
