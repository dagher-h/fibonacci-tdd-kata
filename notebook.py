import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    # Fibonacci Kata (TDD)

    An iterative Fibonacci function built with the Red-Green-Refactor cycle.
    Use the widget below to compute F(n) interactively.
    """)
    return


@app.function
def fibonacci(n: int) -> int:
    """Return the n-th Fibonacci number.

    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) for n >= 2.
    Uses an iterative approach in O(n) time and O(1) space.
    """
    if n < 0:
        raise ValueError("fibonacci is not defined for negative n")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


@app.cell
def _(mo):
    n_input = mo.ui.number(start=0, stop=50, value=10, label="n")
    n_input
    return (n_input,)


@app.cell
def _(mo, n_input):
    mo.md(f"""
    **fibonacci({n_input.value}) = {fibonacci(n_input.value)}**
    """)
    return


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
