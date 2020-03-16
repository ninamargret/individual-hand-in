from Calculator import Calculator

def test_add_empty_returns_zero()-> None:
    assert Calculator.Add("") == 0

def test_add_number_returns_number()-> None:
    assert Calculator.Add("1") == 1

def test_add_two_numbers_returns_sum_of_numbers()-> None:
    assert Calculator.Add("1,2") == 3

def test_add_unknown_numbers_returns_sum_of_numbers()-> None:
    assert Calculator.Add("1,2,3,4,5") == 15

def test_add_unknown_numbers_returns_sum_of_numbers_vol2()-> None:
    assert Calculator.Add("10,2,5,22,1,1") == 41

def test_add_unknown_numbers_returns_sum_of_numbers_vol3()-> None:
    assert Calculator.Add("10,2,5,22,1,1,105,342") == 488

def test_add_new_line_returns_sum_of_numbers() -> None:
    assert Calculator.Add("1\n2,3") == 6

