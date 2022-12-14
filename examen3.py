opcion=100

print("SUPERMERCADO LAS REBAJAS")
print("*****************")

print("1. Registrar nombre del producto")
print("2. Mostrar todos los productos agregados")
print("3. Agregar un nuevo producto a la lista de productos")
print("4. Eliminar un producto de la lista")
print("0. SALIR ")

productos=[]
while opcion !=0:
    opcion= int(input("DIGITA UNA OPCIÓN: "))
    if opcion==1:
        producto=input("Digite el nombre del producto a registrar: ")
        productos.append(producto)

    elif opcion==2:
        for producto in productos:
            print(f'Los productos agregados son: {producto}')
    
    elif opcion==3:
        producto=input("Agregue el nuevo producto: ")
        productos.append(producto)

    elif opcion==4:
        productos.pop()
        print(producto)

    elif opcion==0:
        break

    else:
        print("La opción seleccionada no es valida")



       
        




    
