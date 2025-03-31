# Auto-generated Python script - 2025-03-31
# Question: Write a Python function to perform matrix multiplication

```python
def matrix_multiply(A, B):
    """
    Multiplies two matrices A and B.

    Parameters:
    A (list of list of int/float): The first matrix.
    B (list of list of int/float): The second matrix.

    Returns:
    list of list of int/float: The resulting matrix after multiplication.
    """

    # Get the number of rows in A and B, and the number of columns in B
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    # Ensure the matrices can be multiplied
    if cols_A != rows_B:
        raise ValueError("Number of columns in A must be equal to number of rows in B")

    # Initialize the resulting matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result
```

# If this code contains a function or class but no execution code,
# here's a simple test to run it:

def test_solution():
    print("Testing the solution...")
    # Add test code here if needed
    print("Test completed!")

if __name__ == "__main__":
    test_solution()
