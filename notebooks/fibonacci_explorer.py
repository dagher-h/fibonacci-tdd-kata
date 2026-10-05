import marimo

__generated_with = "0.10.6"
app = marimo.App(width="medium")

with app.setup:
    import marimo as mo


@app.function
def fibonacci(n: int) -> int:
    """Return the n-th Fibonacci number for n >= 0."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("fibonacci expects a non-negative integer")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


@app.cell
def _():
    mo.md(
        r"""
        # Fibonacci Explorer

        Pick a range below and see the Fibonacci numbers over it.
        Move the sliders and the results update automatically.
        """
    )
    return


@app.cell
def _():
    start = mo.ui.slider(0, 30, value=0, label="Range start")
    end = mo.ui.slider(0, 30, value=15, label="Range end")
    mo.hstack([start, end])
    return end, start


@app.cell
def _(end, start):
    lo, hi = sorted((start.value, end.value))
    rows = [{"n": n, "fibonacci(n)": fibonacci(n)} for n in range(lo, hi + 1)]
    mo.ui.table(rows, selection=None)
    return


if __name__ == "__main__":
    app.run()
