from parameterized import parameterized
from main import isBalance2
from main import My_Stack
import pytest

test_list = [
['(((([{}]))))', True],
['[([])((([[[]]])))]{()}', True],
['{{[()]}}', True],
['}{}', False],
['{{[(])]}}', False],
['[[{())}]', False],
['[([])((([[[]]d])))]{()}', False]
]

@parameterized.expand(test_list)
def test_isBalance2(string: str, res: bool):
    assert isBalance2(string) == res

@parameterized.expand(test_list)
def test_isBalance(string: str, res: bool):
    stack = My_Stack()
    for i in string:
        stack.push(i)
    assert stack.isBalance() == res