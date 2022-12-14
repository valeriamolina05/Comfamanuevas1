numeros=[]
numeros=0

for multiplo in range (10):
    numeros=int(input("INGRESE UN NUMERO: "))
        
    if multiplo % 3==0:
        numeros=numeros+1

print("Los multiplos de 3 son: ", numeros)



