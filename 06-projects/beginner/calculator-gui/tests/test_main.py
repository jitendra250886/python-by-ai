import pytest

from calculator_gui.src import main as calc_main  # type: ignore[import]


@pytest.mark.parametrize(
    "expr, expected",
    [
        ("1+1", "2"),
        ("2*3", "6"),
        ("10/2", "5.0"),
        ("2+3*4", "14"),
        ("(2+3)*4", "20"),
    ],
)
def test_evaluate_expression_basic(expr: str, expected: str) -> None:
    assert calc_main.evaluate_expression(expr) == expected


@pytest.mark.parametrize("expr", ["1/0", "abc", "2+", "__import__('os')"])
def test_evaluate_expression_errors(expr: str) -> None:
    assert calc_main.evaluate_expression(expr) == "Error"
