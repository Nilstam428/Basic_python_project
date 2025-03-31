# Auto-generated Python script - 2025-03-31
# Question: Write a Python function to solve the knapsack problem using dynamic programming

```python
def knapsack(weights, values, capacity):
    n = len(weights)
    # Create a 2D DP array where dp[i][w] represents the maximum value
    # that can be achieved with the first i items and capacity w
    dp = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    # Build the table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # If the weight of the ith item is less than or equal to the current capacity
                # we have two options: either include the item or not include it
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                # If the weight of the ith item is more than the current capacity
                # we cannot include it, so we take the value from the previous row
                dp[i][w] = dp[i - 1][w]

    # The maximum value that can be achieved with the given capacity
    return dp[n][capacity]

# Example usage:
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7
print(knapsack(weights, values, capacity))  # Output: 9
``` 

# If this code contains a function or class but no execution code,
# here's a simple test to run it:

def test_solution():
    print("Testing the solution...")
    # Add test code here if needed
    print("Test completed!")

if __name__ == "__main__":
    test_solution()
