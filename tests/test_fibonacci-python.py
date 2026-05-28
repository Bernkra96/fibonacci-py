import sys
import importlib
## sys.path.append('../.')
fibonacci = importlib.import_module("fibonacci-python")
### todo 

def test_calc(capsys): 
    
   
    a = 3
    b = 5
    runFor = 2

    fibonacci.calc(a = a , b = b, runFor = runFor)
    captured = capsys.readouterr()
    assert a == a
    assert "8" in captured.out 
    # assert "13" in captured.out 
    assert "21" not in captured.out 


