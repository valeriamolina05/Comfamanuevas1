opcion=100

print("EMPANADAS EL MACHETICO")
print("***********************\n")

print("1. Registrar empanada")
print("2. Ver empanada")
print("0. SALIR ")


empanadas=[]
while opcion != 0:
    opcion=int(input("DIGITA UNA OPCION: "))
    if opcion==1:
        empanada=input("Digite el nombre de la empanada a registrar: ")
        empanadas.append(empanada)
    elif opcion==2:
        
        for empanada in empanadas:
            print(f'La empanada es: {empanada}')


    elif opcion==0:
        break

    else:
        print("apreciado usuario debe seleccionar una opcion valida...")
