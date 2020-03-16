from Calculator import Calculator

def test_add_empty_returns_zero()-> None:
    assert Calculator.Add("") == 0

def test_add_number_returns_number()-> None:
    assert Calculator.Add("1") == 1
