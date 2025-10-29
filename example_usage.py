import sys
sys.path.insert(0, 'src')

from statistics_calculator import calculate_statistics


def main():
    print("Example 1: Calculate statistics for a list of test scores")
    test_scores = [85, 92, 78, 90, 88, 95, 82]
    stats = calculate_statistics(test_scores)
    
    if stats:
        print(f"Test Scores: {test_scores}")
        print(stats)
        print(f"Class average: {stats.average:.1f}%\n")
    
    print("Example 2: Calculate statistics for temperatures")
    temperatures = [72.5, 68.3, 75.1, 71.9, 69.8]
    stats = calculate_statistics(temperatures)
    
    if stats:
        print(f"Temperatures (°F): {temperatures}")
        print(f"Average: {stats.average:.1f}°F")
        print(f"High: {stats.maximum}°F")
        print(f"Low: {stats.minimum}°F\n")
    
    print("Example 3: Calculate statistics for sales data")
    sales = [1250, 2100, 1850, 1920, 2350, 1680]
    stats = calculate_statistics(sales)
    
    if stats:
        print(f"Daily Sales ($): {sales}")
        print(f"Total: ${stats.total:,.2f}")
        print(f"Average: ${stats.average:,.2f}")
        print(f"Best day: ${stats.maximum:,.2f}")
        print(f"Worst day: ${stats.minimum:,.2f}")


if __name__ == "__main__":
    main()
