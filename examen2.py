dineroJuan=[]
dineroCamila=[]
dineroRicardo=[]


dineroJuan=int(input("¿Qué cantidad de dinero tiene Juan?: "))

dineroCamila=dineroJuan / 2
dineroRicardo=(dineroJuan + dineroCamila) / 2
dineroTotal= dineroJuan + dineroCamila + dineroRicardo


print("La cantidad de dinero de Camila es: ")
print(dineroCamila)

print("La cantidad de dinero de Ricardo es: ")
print(dineroRicardo)

print("La cantidad de dinero de los tres es: ")
print(dineroTotal)

