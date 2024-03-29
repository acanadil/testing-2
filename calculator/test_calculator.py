from calculator import Calculator

#

def test_add():
    assert Calculator.add(1,2) == 3.0
    assert Calculator.add(-500, 400) == -100.0
    assert Calculator.add(0, 0) == 0.0

def test_subtract():
    assert Calculator.subtract(1, 2) == -1.0
    assert Calculator.subtract(2, 1) == 1.0
    assert Calculator.subtract(1.0, 2.0) == -1.0
    assert Calculator.subtract(0, 2.0) == -2.0
    assert Calculator.subtract(2.0, 0.0) == 2.0
    assert Calculator.subtract(-4, 2.0) == -6.0

def test_multiply():
    assert Calculator.multiply(3, 5) == 15.0
    assert Calculator.multiply(-2, 15) == -30.0

def test_divide():
    assert Calculator.divide(1, 2) == 0.5
    assert Calculator.divide(1.0, 2.0) == 0.5
    assert Calculator.divide(0, 2.0) == 0
    assert Calculator.divide(-4, 2.0) == -2.0
    assert Calculator.divide(2.0, 0.0) == 'Can\'t divide by 0'
    
