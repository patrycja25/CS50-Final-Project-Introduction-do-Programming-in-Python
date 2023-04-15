from project import number_5, number_3
from prettytable import PrettyTable


# ten test działa
def test_number_5():
    assert number_5() == "Thank you for using my program. See you next time. 🙂"


def test_number_3():
    result = number_3()
    # Check if the result is a PrettyTable object
    assert isinstance(result, PrettyTable)


def test_number_n():
    result = number_3()

    # Check if the table formatting is correct
    assert result.right_padding_width == 5
    