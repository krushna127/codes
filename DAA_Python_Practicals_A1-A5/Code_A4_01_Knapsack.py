# Code-A4: 0/1 Knapsack using Dynamic Programming

def knapsack(capacity, weights, values):
    n = len(weights)
    if len(values) != n:
        raise ValueError("Weights and values must have the same length.")
    if capacity < 0 or any(w < 0 for w in weights):
        raise ValueError("Capacity and weights must be non-negative.")

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]
                dp[i][w] = max(include, exclude)
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]

def main():
    try:
        n = int(input("Enter number of items: "))
        if n < 0:
            print("Number of items cannot be negative.")
            return
        values = list(map(int, input("Enter values of items separated by spaces: ").split()))
        weights = list(map(int, input("Enter weights of items separated by spaces: ").split()))
        if len(values) != n or len(weights) != n:
            print(f"Please enter exactly {n} values and {n} weights.")
            return
        capacity = int(input("Enter capacity of knapsack: "))
        print("\nMaximum value in knapsack =", knapsack(capacity, weights, values))
        print("Time Complexity: O(nW)")
        print("Space Complexity: O(nW)")
    except ValueError as e:
        print("Invalid input:", e)

if __name__ == "__main__":
    main()
