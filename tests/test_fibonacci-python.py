import sys
import importlib
from io import StringIO

## sys.path.append('../.')
fibonacci = importlib.import_module("fibonacci-python")
### todo


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


# def test_options(monkeypatch, capsys):
#     testInput = StringIO("Text (Listed Only).: h")
#     monkeypatch.setattr("sys.stdin", testInput)
#     fibonacci.setup()
#     fibonacci.options()
#     captured = capsys.readouterr()

#     assert "Help" in captured.out
#     assert "Help" in captured.out
