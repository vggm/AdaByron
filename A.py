
def resolve(palabras: list[str], entrada: list[str]):
  n, m = len(palabras), len(entrada)
  dp = [[-1] * (m+1) for _ in range(n+1)]
  for i in range(n+1):
    dp[i][0] = 0
  for j in range(m+1):
    dp[0][j] = 0

  def rec(i, j):

    if dp[i][j] != -1:
      return dp[i][j]

    if palabras[i-1] == entrada[j-1]:
      dp[i][j] = rec(i-1, j-1) + 1
    else:
      dp[i][j] = max(rec(i-1, j), rec(i, j-1))

    return dp[i][j]
  rec(n, m)

  ''' Mostrar Matriz '''
  '''col = ['~'] + palabras
  for v in [' ', '~'] + entrada:
    print(v[0], end=' ')
  print()
  for i, row in enumerate(dp):
    print(col[i][0], end=' ')
    for v in row:
      print(v if v != -1 else 'X', end=' ')
    print()
  print()'''
  ''' - Fin Mostrar Matriz - '''

  res = []
  i, j = n, m
  total = dp[n][m]
  while total:
    curr = dp[i][j]
    if dp[i-1][j] != curr and dp[i][j-1] != curr:
      i, j = i-1, j-1
      total -= 1
      res.append(palabras[i])

    elif dp[i-1][j] == curr:
      i -= 1

    else:
      j -= 1

  print(*res[::-1])


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
    
    