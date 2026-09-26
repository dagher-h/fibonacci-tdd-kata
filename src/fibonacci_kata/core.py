def fibonacci(n: int) -> int:
    """Return the n-th Fibonacci number for n >= 0."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("fibonacci expects a non-negative integer")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
