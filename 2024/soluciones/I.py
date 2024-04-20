


def resolve2(nums: list[int], viajes: int):
    if viajes == len(nums):
        return max(nums)
    
    if viajes == 1:
        return sum(nums)

    
    

def resolve(nums: list[int], viajes):
    
    if len(nums) == viajes:
        print(max(nums))
        return
    
    media = sum(nums) // viajes
    
    maximo, temp = 0, 0
    for n in nums:
        if n >= media:
            maximo = n
            continue
            
        temp += n
        if temp >= media:
            if temp < maximo:
                maximo = temp
            temp = 0
    
    print(maximo)


if __name__ == '__main__':

  while True:
    entrada = input()
    if entrada == '0 0':
        break
    
    n_nums, viajes = list(map(int, entrada.split()))
    nums = list(map(int, input().split()))
    
    print(resolve(nums, viajes))