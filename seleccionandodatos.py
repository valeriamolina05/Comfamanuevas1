#ENTRADAS DEL PROBLEMA
niveldeAgua=int(input("Digita el nivel del agua: "))

#EVALUANDO CAMINOS MULTIPLES (MAS DE 2)
if niveldeAgua<=100:
    print("Bajo nivel de agua")
elif niveldeAgua >100 and niveldeAgua<400:
    print("Operación optima")
elif niveldeAgua >= 400:
    print("Peligro...")
else:
    print("Nivel de agua no valido")

