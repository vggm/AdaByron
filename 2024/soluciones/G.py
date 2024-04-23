

def get_parameters(nums: list[int], cantidad: int):
  maximo = max(nums)
  maximo = max(nums)
  temp = sum(nums[:cantidad])
  
  if maximo in nums[:cantidad]:
    max_sum = temp
    for i, n in enumerate(nums[:cantidad][::-1]):
      if n == maximo:
        count = cantidad - 1 - i
        break
  else:
    max_sum = 0
    count = 0
  
  return maximo, max_sum, count, temp


def resolve(nums: list[int], cantidad: int):
  
  maximo, max_sum, count, temp = get_parameters(nums, cantidad)
  result = 0
    
  for i, n in enumerate(nums[cantidad:], start=cantidad):
    if n == maximo:
      count = cantidad
    
    temp += n - nums[i-cantidad]
    if temp >= max_sum and count > 0:
      max_sum = temp
      result = i - cantidad + 1 
    
    count -= 1 if count > 0 else 0
  
  print(result + 1)


if __name__ == '__main__':

  try:
    while True:
      entrada = input()
      if entrada == '0 0':
          break
      
      n_nums, total = list(map(int, entrada.split()))
      
      nums = list(map(int, input().split()))
      
      resolve(nums, total)
  except:
    pass