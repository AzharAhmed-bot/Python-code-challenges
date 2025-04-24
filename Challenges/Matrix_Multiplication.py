import numpy as np

def matrix_mult(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
  # your code here
  np_a=np.array(a)
  np_b=np.array(b)
  # np back to array
  result=(np_a @ np_b).tolist()
  return result




print(matrix_mult([[1,2],[3,2]],[[3,2],[1,1]]))