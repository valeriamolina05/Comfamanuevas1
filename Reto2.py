#ENTRADAS DEL PROBLEMA
mesdeAño=input("Digita el mes: ")

#EVALUANDO CAMINOS
if mesdeAño =="marzo" or mesdeAño == "abril" or mesdeAño == "mayo":
    print("Estás en primavera")
elif mesdeAño =='junio' or mesdeAño == 'julio' or mesdeAño == 'agosto':
    print("Estás en verano")
elif mesdeAño == 'septiembre' or mesdeAño == 'octubre' or mesdeAño == 'noviembre':
    print("Estás en otoño")
elif mesdeAño =='diciembre' or mesdeAño == 'enero' or mesdeAño == 'febrero':
    print("Estás en invierno")
else:
    print("Mes no valido")