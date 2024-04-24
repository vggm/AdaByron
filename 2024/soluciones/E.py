
from collections import deque


Neighbours = dict[int, list[int]]
ALT = tuple[int, int, int]


def get_distances(neighbours: Neighbours, src: int) -> list[int]:
  total_nodes = len(neighbours)
  distance = [float('inf')] * (total_nodes + 1)
  distance[src] = 0
  
  stack = deque([(0, src)])
  while stack:
    d, node = stack.popleft()
    
    for neighbor in neighbours[node]:
      if d < distance[neighbor]:
        distance[neighbor] = d+1
        stack.append((d+1, neighbor))
  
  return distance


def resolve(neighbours: Neighbours, alt: ALT):
  total_nodes = len(neighbours)
  A, L, T = alt
  
  A_distance = get_distances(neighbours, A)
  L_distance = get_distances(neighbours, L)
  T_distance = get_distances(neighbours, T)
  
  result = float('inf')
  for node in range(1, total_nodes + 1):
    s = A_distance[node] + L_distance[node] + T_distance[node]
    if s < result:
      result = s
  
  return result


if __name__ == '__main__':
  
  try:
    while True:
      entrada = input()
      if entrada == '':
        break
      
      nodes, edges, A, L, T = list(map(int, entrada.split()))
      
      neighbours = [[] for _ in range(nodes + 1)]
      
      for _ in range(edges):
        src, dst = list(map(int, input().split()))
        neighbours[src].append(dst)
        neighbours[dst].append(src)
  
      print(resolve(neighbours, (A, L, T)))
  
  except EOFError:
    pass
    