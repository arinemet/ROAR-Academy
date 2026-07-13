import numpy as np

def swap_rows(M, a, b):
  if not (0 <= a < M.shape[0] and 0 <= b < M.shape[0]):
    raise IndexError("row index out of range")

  result = M.copy()
  result[[a, b], :] = result[[b, a], :]
  return result

def swap_cols(M, a, b):
  if not (0 <= a < M.shape[1] and 0 <= b < M.shape[1]):
    raise IndexError("column index out of range")

  result = M.copy()
  result[:, [a, b]] = result[:, [b, a]]
  return result
