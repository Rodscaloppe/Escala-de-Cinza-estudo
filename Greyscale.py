testes = int(input())
casos = testes
resultadosFinais = []

while(testes != 0):
  comando = input()
  rgb = input()

  lista = rgb.split()

  red = int(lista[0])
  green = int(lista[1])
  blue = int(lista[2])

  if (comando == "mean"):
    media = (red + green + blue) / 3
    resultadosFinais.append(int(media))
    
  elif (comando == "eye"):
    resultado = (red * 0.3) + (green * 0.59) + (blue * 0.11)
    resultadosFinais.append(int(resultado))

  elif (comando == "min"):
    minimo = int(min(lista))
    resultadosFinais.append(minimo)

  elif(comando == "max"):
    maximo = int(max(lista))
    resultadosFinais.append(maximo)

  else:
    print("Comando Inválido")
    
  testes -= 1

i = 1
for x in resultadosFinais:
  print("Caso #" + str(i) + ": " + str(resultadosFinais[i-1]))
  i += 1

  