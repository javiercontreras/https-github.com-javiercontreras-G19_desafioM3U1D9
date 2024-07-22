print("RespoonDA las siguientes pregunta con SI o NO para entregar los primeros auxilios apropiados")

a1 = str(input("Responde a estimulos? SI/NO :"))
if(a1 == "SI"):
    print("Valorar la necesidad de llevarlo al hospital mas cercano")
elif(a1 == "NO"):
    print("Abrir la via Aerea")
    a2 = str(input("Respira? SI/NO :"))
    if(a2 == "SI"):
        print("Permitirle posicion suficiente de respiracion")
    elif(a2 == "NO"):
        print("Administrar 5 Ventilaciones y llamar ambulancia")
        a4 = "NO"
        while a4 == "NO":
            a3 = str(input("Signos de vida? SI/NO :"))
            if(a3 == "SI"):
                print("Reevaluar a la espera de la ambulacia")
            elif(a3 == "NO"):
                print("Administrar Compresiones Toracicas")
            a4 = str(input("Llego la ambulancia? SI/NO :"))
else:
    print("Por favor solo responda con SI o NO")

print("FIN")
