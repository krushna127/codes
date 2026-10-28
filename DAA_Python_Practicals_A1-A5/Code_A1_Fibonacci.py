# Code-A1: Fibonacci Numbers
iteration_counter = 0
recursion_counter = 0

def fibonacci_iteration(n):
    global iteration_counter
    iteration_counter = 0
    series = []
    previous, current = 0, 1
    for _ in range(n):
        series.append(previous)
        previous, current = current, previous + current
        iteration_counter += 1
    return series

def fibonacci_recursion(n):
    global recursion_counter
    recursion_counter += 1
    if n <= 1:
        return n
    return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)

def main():
    global recursion_counter
    try:
        n = int(input("Enter the number of terms: "))
        if n < 0:
            print("Please enter a non-negative number.")
            return
    except ValueError:
        print("Please enter a valid integer.")
        return

    print("\nFibonacci Series using Iteration:", fibonacci_iteration(n))
    print("Total Iterative Steps:", iteration_counter)
    print("Time Complexity: O(n)")
    print("Space Complexity: O(n) including output list; O(1) auxiliary space")
    print("=" * 80)

    recursion_counter = 0
    series = [fibonacci_recursion(i) for i in range(n)]
    print("Fibonacci Series using Recursion:", series)
    print("Total Recursive Function Calls:", recursion_counter)
    print("Time Complexity: O(2^n) for naive recursion")
    print("Space Complexity: O(n) recursion stack")

if __name__ == "__main__":
    main()
