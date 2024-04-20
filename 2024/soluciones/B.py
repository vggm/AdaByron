

def resolve(n: int, precios: list[int]):
  suma = sum(precios)
  total = precios[0] * n
  print(suma-total)


if __name__ == '__main__':

  N = int(input())
  
  for _ in range(N):
    cunas = int(input())
    precios = list(map(int, input().split()))
    resolve(cunas, precios)