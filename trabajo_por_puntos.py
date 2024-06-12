asientos = [
    [" \n"],
    ["01","02","03"," ", " ","04","05","06\n"],
    ["07","08","09"," ", " ","10","11","12\n"],
    ["13","14","15"," ", " ","16","17","18\n"],
    ["19","20","21"," ", " ","22","23","24\n"],
    ["25","26","27"," ", " ","28","29","30\n"],
    ["31","32","33"," ", " ","34","35","36\n"],
    ["37","38","39"," ", " ","40","41","42\n"]
]

datos_pasajeros = []

def tomar_pasaje(datos_pasajeros,asiento_ocupado):
    nombre_completo = input("Ingrese su nombre completo porfavor: ")
    try:
        rut_pasajero = int(input("Ingrese su rut sin puntos ni guion: "))
    except ValueError:
        print("Ingrese un rut valido")
    


while True:
    print("\n1. Ver asiento disponible")
    print("2. Comprar asiento")
    print("3. Anular vuelo")
    print("4. Modificar datos de pasajero")
    print("5. Salir")
    try:
        opc = int(input("Ingrese una opcion: "))
        if opc == 1:
            for fila in asientos:
                for elemento in fila:
                    print(elemento,end=" ")
        elif opc == 2:
            print("rellenar")
        elif opc == 3:
            print("rellenar")
        elif opc == 4:
            print("rellenar")
        elif opc == 5:
            print("rellenar") 
        else:
            print("Ingrese una opcion valida\n")      
    except ValueError:
        print("Error: Ingrese una opcion valida\n")
        