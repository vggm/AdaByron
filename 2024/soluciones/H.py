
# gasolineras
from collections import defaultdict
from heapq import heappush, heappop


Query = tuple[int, int, int]
MAdy = list[dict[int, int]]

def resolve(neighbours: MAdy, query: Query, fuel_cost: list[int]):
  max_fuel, src, dst = query
  
  # every state starts with the cost of inf
  visited = defaultdict(lambda : float('inf'))
  stack = []
  heappush(stack, (0, 0, src))
  while stack:
    current_cost, fuel, city = heappop(stack)
    
    if visited[(city, fuel)] < current_cost:
      continue
    
    visited[(city, fuel)] = current_cost
    
    if city == dst:
      print(current_cost)
      return  
    
    if fuel < max_fuel:
      heappush(stack, (current_cost + fuel_cost[city], fuel+1, city))
    
    for neighbor, distance in neighbours[city].items():
      if (fuel >= distance  # fuel must be greater or equal than distance 
        and visited[(neighbor, fuel-distance)] > current_cost):  # the cost of that state is greater than the new one
        heappush(stack, (current_cost, fuel-distance, neighbor))

  print('IMPOSIBLE')
    

if __name__ == '__main__':
  
  try:
    
    while True:
    
      entrada = input()
      if entrada == '':
        break
      
      nodes, edges = list(map(int, entrada.split()))
      precios = list(map(int, input().split()))
      
      # Para luego poder acceder a la i-esima ciudad sin tener que restarle 1.
      # Ej.: combustible de la ciudad 1 es precios[1] en lugar de precios[1-1]
      precios.insert(0, 0)
      
      # Cada ciudad es la posicion i-esima del array. Ciudad 1 = mady[1]
      # La posicion 0 sera siempre un map vacio, las ciudades empiezan en 1
      mady = [{} for _ in range(nodes + 1)]
      
      for _ in range(edges):
        u, v, d = list(map(int, input().split()))
        mady[u][v] = d
        mady[v][u] = d
      
      queries = int(input())
      for _ in range(queries):
        query = list(map(int, input().split()))
        resolve(mady, query, precios)
        
      print('---')
    
  except EOFError:
    pass
    