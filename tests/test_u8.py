import pytest

from helang.u8 import U8
from helang.exceptions import CyberSubtractionException


a = U8([5, 3, 6])
b = U8([2, 6, 7])
c = U8([2])
a_b = [3, -3, -1]
b_a = [-3, 3, 1]
a_c = [3, 1, 4]
b_c = [0, 4, 5]


def test_u8_compare():
    assert a == a
    assert a == a.value
    assert a != b


def test_u8_subtraction():
    assert a-b == a_b
    assert b-a == b_a
    assert a-c == a_c
    assert b-c == b_c

    try:
        c - a
        pytest.fail('illegal operation: number - vector')
    except CyberSubtractionException:
        ...
