from factoriales import *

def test_comparativa():
    for i in range(1,900):
        assert fact(i) == factR(i)

def test_resultado():
    assert fact(5) == 120
    assert fact(6) == 720
    assert fact(7) == 5040
    
    
def test_iterativa():
    for i in range(1000):
        fact(900)
        
def test_recursiva():
    for i in range(1000):
        factR(900)


