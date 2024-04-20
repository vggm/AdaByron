
# gasolineras

from collections import deque
from heapq import heappush, heappop


Query = tuple[int, int, int]
MAdy = list[dict[int, int]]

def resolve(mady: MAdy, query: Query, precio_combustible: list[int]):
  comb_max, src, dst = query
  
  result = float('inf')
  visited = {}
  # visited = set()
  stack = []
  heappush(stack, (0, 0, src, -1))
  while stack:
    c, g, v, l = heappop(stack)
    
    if visited.get((v, g)) is not None:
      if visited[(v, g)] < c:
        continue
    
    visited[(v, g)] = c
    
    # if (v, g) in visited:
    #   continue
    # visited.add((v, g))
    
    if v == dst:
      return c
    
    if g < comb_max:
      heappush(stack, (c + precio_combustible[v], g+1, v, l))
    
    for ady, dist in mady[v].items():
      if ady != l and dist <= g:
        heappush(stack, (c, g-dist, ady, v))
  
  return result
    

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
      mady = [{} for _ in range(nodes + 1)]
      
      for _ in range(edges):
        u, v, d = list(map(int, input().split()))
        mady[u][v] = d
        mady[v][u] = d
      
      queries = int(input())
      for _ in range(queries):
        query = list(map(int, input().split()))
        response = resolve(mady, query, precios)
        print('IMPOSIBLE' if response == float('inf') else response)
  except EOFError:
    pass 
    
    