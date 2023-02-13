import pytest
from main import inc, dec


def test_answer_inc():
    assert inc(3) == 4

def test_answer_dec():
    assert dec(3) == 4