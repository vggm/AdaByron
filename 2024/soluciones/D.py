

if __name__ == '__main__':

  while True:
    
    entrada = input()
    if entrada == '0 0 0':
      break
    
    N, M, V = list(map(int, entrada.split()))
    
    mmatrix = {}
    
    while True:
      
      consulta = input()
      if consulta == 'FIN':
        print('---')
        break
      
      accion, *resto = consulta.split()
      
      if accion == 'set':
        i, j, v = resto        
        i, j, v = int(i), int(j), int(v)
        
        mini = min(i, j)
        i, j = i-mini, j-mini
        
        mmatrix[(i,j)] = v
               
        
      elif accion == 'get':
        i, j = resto        
        i, j = int(i), int(j)  
        
        mini = min(i, j)
        i, j = i-mini, j-mini   
        
        if mmatrix.get((i,j)) is None:
          print(V)
        
        else:
          print(mmatrix[(i,j)])
                     

      