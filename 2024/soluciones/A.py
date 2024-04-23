
def counter():
  n = 0
  while True:
    yield n + 1


def recursive(in1: list[str], in2: list[str], i: int, j: int, matrix: list[list[int]]):
  
  if i < 0 or j < 0:
    return 0
  
  if matrix[i][j] != 0:
    return matrix[i][j]
  
  if in1[i] == in2[j]:
    matrix[i][j] = recursive(in1, in2, i-1, j-1, matrix) + 1
    return matrix[i][j]
  
  matrix[i][j] = max(recursive(in1, in2, i-1, j, matrix), recursive(in1, in2, i, j-1, matrix))
  return matrix[i][j]
  

def resolve(palabras: list[str], entrada: list[str]):
  result = []
  N, M = len(palabras), len(entrada)
  i, j = N-1, M-1
  
  matrix = [[0 for _ in range(M)] for _ in range(N)]
  recursive(palabras, entrada, i, j, matrix)
  for row in matrix:
    print(*row)
  
  count = matrix[i][j]
  while count > 0 and (i, j >= 0):
    cell_value = matrix[i][j]
    if palabras[i] == entrada[j]:
      result.append(palabras[i])
      count -= 1
      i, j = i-1, j-1
      continue
    
    if j - 1 >= 0 and cell_value == matrix[i][j-1]:
      j -= 1
    else:
      i -= 1
  
  print(*result[::-1]) 


if __name__ == '__main__':

  try:
    while True:
      palabras = input()
      if palabras == '':
        break
      
      entrada = input()
      
      resolve(palabras.split(), entrada.split())
  except EOFError:
    pass
    
    