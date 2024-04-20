

def resolve2(nums: list[int], total: int, cantidad: int):
  
  start, end = -1, 0
  for i, (n, s) in enumerate(zip(nums, sorted(nums))):
    if n != s:
      if start == -1:
        start = i
        end = i
      else:
        end = i
  
  print(0 if start == -1 else end - start + 1)


def resolve(nums: list[int], total, cantidad):
  resultado = [0] * (total+1)
  
  for i, n1 in enumerate(nums):
    if i == cantidad-1:
      continue
    
    n2 = nums[i+1]
    if n1 > n2:
      resultado[n1] = 1
      resultado[n2] = 1
  
  print(sum(resultado))


if __name__ == '__main__':

  try:
    while True:
      entrada = input()
      if entrada == '0 0':
          break
      
      total, cantidad = list(map(int, entrada.split()))
      nums = list(map(int, input().split()))
      
      resolve2(nums, total, cantidad)
  except:
    pass