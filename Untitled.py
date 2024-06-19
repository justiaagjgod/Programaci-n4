
bateria = int(input("Ingrese el valor de bateria:"))
if bateria <20:
    print ("recargar")
elif bateria >80:
    print("full")
elif bateria >50:
    print("optimo")
else:
    print ("normal")
