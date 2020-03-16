from Calculator import Calculator

def test_add_empty_returns_zero()-> None:
    assert Calculator.Add("") == 0

def test_add_number_returns_number()-> None:
    assert Calculator.Add("1") == 1

def test_add_two_numbers_returns_sum_of_numbers()-> None:
    assert Calculator.Add("1,2") == 3

def test_add_unknown_numbers_returns_sum_of_numbers()-> None:
    assert Calculator.Add("1,2,3,4,5") == 15


