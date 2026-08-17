import sys
import importlib
from io import StringIO

import pytest

sys.path.append("../.")
fibonacci = importlib.import_module("fibonacci-python")
### todo add tests


def test_calc(capsys):

    a = 0
    b = 1
    runFor = 3

    fibonacci.calc(a=a, b=b, runFor=runFor)
    captured = capsys.readouterr()
    assert a == a
    assert "1" in captured.out
    assert "2" in captured.out
    assert "3" in captured.out
    assert "5" not in captured.out

    a = 3
    b = 5
    runFor = 2

    fibonacci.calc(a=a, b=b, runFor=runFor)
    captured = capsys.readouterr()
    assert a == a
    assert "8" in captured.out
    assert "13" in captured.out
    assert "21" not in captured.out

    a = 7
    b = 8
    runFor = 2

    fibonacci.calc(a=a, b=b, runFor=runFor)
    captured = capsys.readouterr()
    assert a == a
    assert "15" in captured.out
    assert "23" in captured.out
    assert "38" not in captured.out


def test_options(monkeypatch, capsys):
    
    
    optionsDataSet = {
    "EndTimer": {"val": True, "infoShort": " Want to Run End timer?"},
    "TimeEndTimer": {"val": 2, "infoShort": "Set EndTimer Length in sek."},
    "PrintEndResult": {"val": True, "infoShort": "Print Result in Console"},
    "SaveEndResult": {"val": True, "infoShort": "Save Result as in Text File "},
    "startValA": {"val": 0, "infoShort": "Start Val A"},
    "startValB": {"val": 1, "infoShort": "Start Val B"},
    "PresetNumberRuns": {
        "val": 1000,
        "infoShort": "Number of Run if preset if no input ",
    },}
    

    testData = optionsDataSet
    
    testInput =  StringIO("i")
    monkeypatch.setattr("sys.stdin", testInput)
    fibonacci.optionsLoader()
    # Eof for While True Loop
    with pytest.raises(EOFError) as eof:
        fibonacci.options(data=testData)
    captured = capsys.readouterr()
    assert ("Info") in captured.out

      

    testInput =  StringIO("u")
    monkeypatch.setattr("sys.stdin", testInput)
    fibonacci.optionsLoader()
    # Eof for While True Loop
    with pytest.raises(EOFError) as eof:
        fibonacci.options(data=testData)
    captured = capsys.readouterr()
    assert ("Update") in captured.out




    testInput = StringIO("h")
    monkeypatch.setattr("sys.stdin", testInput)
    fibonacci.optionsLoader()
    # Eof for While True Loop
    with pytest.raises(EOFError) as eof:
      fibonacci.options(data=testData)
    captured = capsys.readouterr()
    assert "Help" in captured.out
    
    



    
def test_setup(monkeypatch, capsys):
    
    optionsDataSet = {
    "EndTimer": {"val": True, "infoShort": " Want to Run End timer?"},
    "TimeEndTimer": {"val": 2, "infoShort": "Set EndTimer Length in sek."},
    "PrintEndResult": {"val": True, "infoShort": "Print Result in Console"},
    "SaveEndResult": {"val": True, "infoShort": "Save Result as in Text File "},
    "startValA": {"val": 0, "infoShort": "Start Val A"},
    "startValB": {"val": 1, "infoShort": "Start Val B"},
    "PresetNumberRuns": {
        "val": 1000,
        "infoShort": "Number of Run if preset if no input ",
    },}
    

    testData = optionsDataSet
    testInput = StringIO("5")
    monkeypatch.setattr("sys.stdin", testInput)
    fibonacci.setup(data =testData)
    captured = capsys.readouterr()
    assert "Runs Fibonacci.Set for 5 times." in captured.out

    testInput = StringIO("0")
    monkeypatch.setattr("sys.stdin", testInput)
    fibonacci.setup(data =testData)
    captured = capsys.readouterr()
    assert "Runs Fibonacci.Set for 0 times." in captured.out

    testInput = StringIO("s")
    monkeypatch.setattr("sys.stdin", testInput)
    fibonacci.optionsLoader()
    with pytest.raises(EOFError) as eof:
      fibonacci.setup(data =testData)
    captured = capsys.readouterr()
    assert "Update witch Option ?" in captured.out

    testInput = StringIO("o")
    monkeypatch.setattr("sys.stdin", testInput)
    fibonacci.optionsLoader()
    with pytest.raises(EOFError) as eof:
     fibonacci.setup(data =testData)
    captured = capsys.readouterr()
    assert "Options" in captured.out

    testInput = StringIO("q")
    monkeypatch.setattr("sys.stdin", testInput) 
    with  pytest.raises(SystemExit) as exc:
     fibonacci.setup(data =testData)
    assert exc.value.code == 0






    
   


