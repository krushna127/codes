# Code-A3: Fractional Knapsack using Greedy Method

def fractional_knapsack(capacity, items):
    if capacity < 0:
        raise ValueError("Capacity must be non-negative.")
    if any(weight <= 0 for value, weight in items):
        raise ValueError("Each item must have a positive weight.")

    items = sorted(items, key=lambda item: item[0] / item[1], reverse=True)
    total_value = 0.0
    selected = []
    remaining = capacity

    for value, weight in items:
        if remaining <= 0:
            break
        if weight <= remaining:
            total_value += value
            remaining -= weight
            selected.append((value, weight, 1.0))
        else:
            fraction = remaining / weight
            total_value += value * fraction
            selected.append((value, weight, fraction))
            remaining = 0
    return total_value, selected

def main():
    try:
        n = int(input("Enter number of items: "))
        if n < 0:
            print("Number of items cannot be negative.")
            return
        items = []
        print("Enter value and weight of each item:")
        for i in range(n):
            value, weight = map(float, input(f"Item {i + 1} (value weight): ").split())
            items.append((value, weight))
        capacity = float(input("Enter capacity of knapsack: "))
        maximum, selected = fractional_knapsack(capacity, items)
        print(f"\nMaximum value in knapsack = {maximum:.4f}")
        print("Selected portions (value, weight, fraction taken):")
        for item in selected:
            print(item)
        print("Time Complexity: O(n log n)")
        print("Space Complexity: O(n)")
    except ValueError as e:
        print("Invalid input:", e)

if __name__ == "__main__":
    main()
