


if __name__ == '__main__':
  while True:
    entrada = input()
    if entrada == '':
      break
    
    N, C, A, L, T = list(map(int, entrada.split()))
    
    graph = {i: [] for i in range(N)}
    
    for _ in range(C):
      src, dst = list(map(int, input().split()))
      graph[src].append(dst)
      graph[dst].append(src)
    
    