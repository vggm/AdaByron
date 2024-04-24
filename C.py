from collections import Counter


VERDE = '#'
GRIS = '.'
AMARILLO = '-'


def resolve(N: int, nums: list[int], att: list[int]) -> None:
  apariciones = Counter(nums)
  output = [GRIS] * N 
  
  for i, (s, a) in enumerate(zip(nums, att)):
    if s == a:
      output[i] = VERDE
      apariciones[s] -= 1
  
  for i, (s, a) in enumerate(zip(nums, att)):
    if apariciones[a] > 0 and output[i] != VERDE:
      output[i] = AMARILLO
      apariciones[a] -= 1
      
  print(''.join(output))


if __name__ == '__main__':
    
  while True:
    N = int(input())
    if N == 0:
      break
    
    numeros = list(map(int, input().split()))
    intento = list(map(int, input().split()))
    
    resolve(N, numeros, intento)
    
    