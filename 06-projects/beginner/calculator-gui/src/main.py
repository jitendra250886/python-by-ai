"""Calculator GUI application.

A simple four-operation calculator implemented with Tkinter. This module
exposes a small evaluation helper that can be tested without a GUI and a
`run()` function that starts the graphical interface.
"""

from __future__ import annotations

import tkinter as tk
from dataclasses import dataclass


@dataclass
class CalculatorState:
    """State for the calculator expression."""

    expression: str = ""

    def append(self, value: str) -> None:
        self.expression += value

    def clear(self) -> None:
        self.expression = ""


def evaluate_expression(expr: str) -> str:
    """Safely evaluate a simple arithmetic expression.

    Supports digits and the operators +, -, *, / and parentheses. If the
    expression is invalid, returns a user-friendly error message instead
    of raising an exception.
    """

    # Basic safety: allow only digits, operators, dot and parentheses.
    allowed_chars = set("0123456789+-*/(). ")
    if any(ch not in allowed_chars for ch in expr):
        return "Error"

    try:
        # Use Python's eval in a restricted environment. For a production
        # system, consider using a dedicated expression parser instead.
        result = eval(expr, {"__builtins__": {}}, {})  # type: ignore[arg-type]
    except Exception:
        return "Error"

    return str(result)


def run() -> None:
    """Start the Tkinter calculator GUI."""

    state = CalculatorState()

    root = tk.Tk()
    root.title("Python Calculator")
    root.resizable(False, False)

    display_var = tk.StringVar(value="")

    display = tk.Entry(
        root,
        textvariable=display_var,
        font=("Segoe UI", 18),
        justify="right",
        bd=8,
        relief="sunken",
    )
    display.grid(row=0, column=0, columnspan=4, padx=8, pady=8, sticky="nsew")

    def on_press(char: str) -> None:
        if char == "C":
            state.clear()
            display_var.set("")
        elif char == "=":
            result = evaluate_expression(state.expression)
            state.expression = result if result != "Error" else ""
            display_var.set(result)
        else:
            state.append(char)
            display_var.set(state.expression)

    buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", ".", "C", "+"],
        ["(", ")", "=", ""],
    ]

    for r, row in enumerate(buttons, start=1):
        for c, label in enumerate(row):
            if not label:
                continue  # skip empty placeholder cell
            btn = tk.Button(
                root,
                text=label,
                width=4,
                height=2,
                font=("Segoe UI", 14),
                command=lambda ch=label: on_press(ch),
            )
            btn.grid(row=r, column=c, padx=4, pady=4, sticky="nsew")

    # Make grid cells expand nicely if the window is resized.
    for i in range(4):
        root.columnconfigure(i, weight=1)
    for i in range(len(buttons) + 1):
        root.rowconfigure(i, weight=1)

    root.mainloop()


if __name__ == "__main__":
    run()
