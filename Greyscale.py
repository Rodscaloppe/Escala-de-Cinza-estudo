testes = int(input())

while(testes != 0):
  comando = input()
  rgb = input()

  lista = rgb.split()

  red = lista[0] # 20
  green = lista[1] # 70
  blue = lista[2] # 50

  if (comando == "mean"):
    media = (int(red) + int(green) + int(blue)) / 3
    print(int(media))
  elif (comando == "eye"):
    resultado = (int(red) * 0.3) + (int(green) * 0.59) + (int(blue) * 0.11)
    print(int(resultado))
  else:
    print("Comando Inválido")
    
  testes -= 1