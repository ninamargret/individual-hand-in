from Calculator import Calculator
import pytest 

def test_add_empty_returns_zero() -> None:
    assert Calculator.Add("") == "0"

def test_add_number_returns_number() -> None:
    assert Calculator.Add("1") == "1"

def test_add_two_numbers_returns_sum_of_numbers() -> None:
    assert Calculator.Add("1,2") == "3"

def test_add_unknown_numbers_returns_sum_of_numbers() -> None:
    assert Calculator.Add("1,2,3,4,5") == "15"

def test_add_unknown_numbers_returns_sum_of_numbers_vol2() -> None:
    assert Calculator.Add("10,2,5,22,1,1") == "41"

def test_add_unknown_numbers_returns_sum_of_numbers_vol3() -> None:
    assert Calculator.Add("10,2,5,22,1,1,105,342") == "488"

def test_add_new_line_returns_sum_of_numbers() -> None:
    assert Calculator.Add("1\n2,3") == "6"

def test_add_ignore_numbers_bigger_than_1000() -> None:
    assert Calculator.Add("1001,2") == "2"

def test_add_negative_number_return_error() -> None:
    with pytest.raises(Exception, match=r"Negatives not allowed: -1"):
        Calculator.Add("-1,2")

def test_add_negative_number_return_error() -> None:
    with pytest.raises(Exception, match=r"Negatives not allowed: -4,-5"):
        Calculator.Add("2,-4,3,-5")

def test_add_negative_number_return_error_vol2() -> None:
    with pytest.raises(Exception, match=r"Negatives not allowed: -4,-5,-12,-10"):
        Calculator.Add("2,-4,3,-5,-12,3,-10")

def test_add_with_delimiter_return_only_sum_of_numbers() -> None:
    assert Calculator.Add("//X\n1X2") == "3"

def test_add_with_delimiter_return_only_sum_of_numbers_vol2() -> None:
    assert Calculator.Add("//%\n1%2%3") == "6"
