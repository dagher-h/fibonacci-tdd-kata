import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")

with app.setup:
    import marimo as mo
    import matplotlib.pyplot as plt

    from fibonacci_kata import fibonacci


@app.cell
def _():
    mo.md(r"""
    # Fibonacci Explorer

    Pick a range below and see the Fibonacci numbers over it,
    both as a list and as a chart. This notebook consumes the
    published fibonacci_kata package — it does not reimplement
    the function.
    """)
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
    indices = list(range(lo, hi + 1))
    values = [fibonacci(n) for n in indices]
    values
    return indices, values


@app.cell
def _(indices, values):
    fig, ax = plt.subplots()
    ax.bar(indices, values, color="#4c72b0")
    ax.set_xlabel("n")
    ax.set_ylabel("fibonacci(n)")
    ax.set_title("Fibonacci numbers over the selected range")
    fig
    return


if __name__ == "__main__":
    app.run()
