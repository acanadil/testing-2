from calculator import Calculator

#

def test_add():
    assert Calculator.add(1,2) == bin(3.0)
    assert Calculator.add(-500, 400) == bin(-100.0)
    assert Calculator.add(0, 0) == bin(0.0)
    
