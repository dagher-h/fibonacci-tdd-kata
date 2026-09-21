import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return


@app.function
def fibonacci(n: int) -> int:
    """Return the n-th Fibonacci number."""
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


@app.cell
def test_fibonacci():
    def test_base_cases():
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1

    def test_small_values():
        assert fibonacci(2) == 1
        assert fibonacci(5) == 5

    def test_larger_value():
        assert fibonacci(10) == 55

    test_base_cases()
    test_small_values()
    test_larger_value()
    return


if __name__ == "__main__":
    app.run()
