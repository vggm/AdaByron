

def resolve(pesos: list[int], viajes: int):

  n = len(pesos)

  def puede_transportar(total: int) -> bool:
    i, k = 0, 0
    while i < n:
      curr = pesos[i]
      j = i + 1
      while j < n and curr + pesos[j] <= total:
        curr += pesos[j]
        j += 1
      i = j
      k += 1
    return k <= viajes

  suma, maximo = 0, 0
  for peso in pesos:
    maximo = max(maximo, peso)
    suma += peso

  l, r = maximo, suma
  while l <= r:
    m = (l+r) // 2
    if puede_transportar(m):
      r = m - 1
    else:
      l = m + 1

  return l


if __name__ == '__main__':

  while True:
    entrada = input()
    if entrada == '0 0':
        break
    
    n_nums, viajes = list(map(int, entrada.split()))
    nums = list(map(int, input().split()))
    
    print(resolve(nums, viajes))
