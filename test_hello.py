# test_hello.py
from hello import add

def test_add():
    assert add(2, 3) == 2
    assert add(-1, 1) == 0