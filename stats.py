def calculate_statistics(values):
    if not values:
        return None
    
    total = sum(values)
    count = len(values)
    average = total / count
    maximum = max(values)
    minimum = min(values)
    
    return {
        'average': average,
        'max': maximum,
        'min': minimum,
        'count': count
    }

def print_statistics(values):
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
    print(f"Count:   {stats['count']}")
    print(f"Average: {stats['average']:.2f}")
    print(f"Maximum: {stats['max']}")
    print(f"Minimum: {stats['min']}")
    print("="*40 + "\n")

def main():
    print("Enter numbers separated by spaces (or comma-separated):")
    user_input = input("> ")
    
    try:
        if ',' in user_input:
            values = [float(x.strip()) for x in user_input.split(',') if x.strip()]
        else:
            values = [float(x) for x in user_input.split() if x]
        
        if not values:
            print("Error: No valid numbers provided")
            return
        
        print_statistics(values)
        
    except ValueError:
        print("Error: Please enter valid numbers only")

if __name__ == "__main__":
    main()
