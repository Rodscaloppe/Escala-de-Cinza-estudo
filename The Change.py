while True:
  angulo = int(input())
  if (angulo == 360 or angulo >= 0 and angulo <= 89):
    print("Bom Dia!!")
  elif (angulo >= 90 and angulo <= 179):
    print("Boa Tarde!!")
  elif (angulo >= 180 and angulo <= 269):
    print("Boa Noite!!")
  else:
    print("De Madrugada!!")
