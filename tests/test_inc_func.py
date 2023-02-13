import pytest
from main import inc


def test_answer():
    assert inc(3) == 4