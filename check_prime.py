# -*- coding: utf-8 -*-
"""Check_Prime.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19OZ0EV959S16hsim764wivSGZTYJG8Yg
"""

def check_prime(n):
  """
  Checks if a given integer is prime or not.

  Args:
    n: An integer.

  Returns:
    True if n is prime, False otherwise.
  """

  if n <= 1:
    return False

  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False

  return True

check_prime(11)

