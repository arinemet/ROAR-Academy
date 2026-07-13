import numpy as np


def set_array(L, rows, cols, order="C"):
  if len(L) != rows * cols:
    raise ValueError("L must contain exactly rows * cols elements")
  if order not in ("C", "F"):
    raise ValueError("order must be 'C' or 'F'")

  return np.array(L).reshape((rows, cols), order=order)
