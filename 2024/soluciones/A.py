
def resolve(palabras: list[str], entrada: list[str]):
  output = []
  palabra_indice = {p: i for i, p in enumerate(palabras)}
  
  i = 0
  for e in entrada:
    if e in palabras[i:]:
      output.append(e)
      i = palabra_indice[e]
  
  print(*output)

if __name__ == '__main__':

  try:
    while True:
      palabras = input()
      if palabras == '':
        break
      
      entrada = input()
      
      resolve(palabras.split(), entrada.split())
  except:
    pass
    
    