from calculator_binary import Calculator_Binary

#

def test_add():
    assert Calculator_Binary.add(1,2) == bin(3)
    assert Calculator_Binary.add(-500, 400) == bin(-100)
    assert Calculator_Binary.add(0, 0) == bin(0)
    
