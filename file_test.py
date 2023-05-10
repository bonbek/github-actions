import pytest

def test_calc_addition():
  # Addition of 2 and 4
    output = 2+4
    assert output == 6

def test_calc_substraction():
  # Substraction of 2 and 4
    output = 2-4
    assert output == -2

def test_calc_multiply():
  # Fonction test du résultat de 2*4
    output = 2*4
    assert output == 8

def test_coucou():
  # Fonction test si la résultat renvoie 'hello'
    output='hello'
    assert output == 'hello'  
