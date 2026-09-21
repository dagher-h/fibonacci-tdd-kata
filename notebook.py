import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return


@app.cell(hide_code=True)
def _():
    return


@app.function
def fibonacci(n: int) -> int:
    """Return the n-th Fibonacci number."""
    pass


@app.cell
def _():
    def test_fibonacci_base_cases():
        assert fibonacci(0) == 0
        assert fibonacci(1) == 1

    def test_fibonacci_small_values():
        assert fibonacci(2) == 1
        assert fibonacci(5) == 5

    def test_fibonacci_larger_value():
        assert fibonacci(10) == 55

    return


if __name__ == "__main__":
    app.run()
