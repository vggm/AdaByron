
from collections import defaultdict
from collections import deque
from heapq import heappush


def resolve4(nums: list[int], cantidad: int):
  result = 0
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
    
  for i, n in enumerate(nums[cantidad:], start=cantidad):
    if n == maximo:
      count = cantidad
    
    temp += n - nums[i-cantidad]
    if temp >= max_sum and count > 0:
      max_sum = temp
      result = i - cantidad + 1 
    
    count -= 1
  
  print(result + 1)


def resolve3(nums: list[int], cantidad: int):
  maximo = max(nums[:cantidad])
  curr = deque(nums[:cantidad])
  temp = sum(curr)
  stack = []
  heappush(stack, (temp, len(stack), set(curr)))
  
  for n in nums[cantidad:]:
    maximo = max(n, maximo)
    temp += n - curr.popleft()
    curr.append(n)
    heappush(stack, (temp, len(stack), set(curr)))

  result = 0
  for _, index, s in stack:
    if maximo in s:
      result = index
      break

  print(result + 1)
  

def resolve2(nums: list[int], cantidad: int):
  
  maximo = max(nums)
  temp = sum(nums[:cantidad])
  max_sum = temp if maximo in nums[:cantidad] else 0
  result = 0
  
  for i, n in enumerate(nums[cantidad:], start=cantidad):
    temp += n - nums[i-cantidad]
    if temp >= max_sum and maximo in nums[i-cantidad:i+1]:
      result = i - cantidad + 1
      max_sum = temp
  
  print(result + 1)


def resolve(nums: list[int], cantidad: int):
    paginas_index = defaultdict(deque)
    for i, n in enumerate(nums):
      paginas_index[n].append(i)
    
    maximo = max(list(paginas_index.keys()))
    
    resultado, max_sum = 0, 0
    for indice in paginas_index[maximo]:
        
        for c in range(cantidad):
            start, end = indice - c, indice + cantidad - c
            if 0 <= start and end <= len(nums):
                temp = sum(nums[start:end])
                if temp >= max_sum:
                    max_sum = temp
                    resultado = start
                    
    print(resultado + 1)


if __name__ == '__main__':

  try:
    while True:
      entrada = input()
      if entrada == '0 0':
          break
      
      n_nums, total = list(map(int, entrada.split()))
      
      nums = list(map(int, input().split()))
      
      resolve4(nums, total)
  except:
    pass