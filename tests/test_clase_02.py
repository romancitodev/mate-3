"""Tests for clase 02"""

import pytest
from src.clase_02 import *


def test_ejercicio_1():
    """Test ejercicio 1"""
    assert ejercicio_1() is None

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
