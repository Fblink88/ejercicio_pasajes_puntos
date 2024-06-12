asientos = [
    [" \n"],
    ["01","02","03"," ", " ","04","05","06","\n"],
    ["07","08","09"," ", " ","10","11","12","\n"],
    ["13","14","15"," ", " ","16","17","18","\n"],
    ["19","20","21"," ", " ","22","23","24","\n"],
    ["25","26","27"," ", " ","28","29","30","\n"],
    ["31","32","33"," ", " ","34","35","36","\n"],
    ["37","38","39"," ", " ","40","41","42","\n"]
]

datos_pasajeros = []
precio_norm = 78900
precio_vip = 240000

def mostrar_asiento():
    for fila in asientos:
        for elemento in fila:
            print(elemento,end=" ")
        
    

def tomar_pasaje():
    nombre_pasajero = input("Ingrese su nombre completo porfavor: ")
    try:
        while True:
            rut_pasajero = int(input("Ingrese su rut sin puntos ni guion, si termina en k remplazala por un 0: "))
            if rut_pasajero < 1000000:
                print("Ingresa un valor de rut valido porfavor")
            else:
                print("RUT registrado con exito")
                break
    except ValueError:
        print("Error: Ingrese un rut valido")
    try:
        while True:
            telefono_pasajero = int(input("Ingrese el numero de telefono del pasajero: "))
            telefono_pasajero_str = str(telefono_pasajero)
            if telefono_pasajero < 900000000 and telefono_pasajero > 999999999:
                print("Ingrese un formato de telefono valido porfavor")
            else:
                if telefono_pasajero_str.startswith("9"):
                    print("Numero de telefono valido.")
                    break
                else:
                    print("Ingrese un numero de telefono no valido")
    except ValueError:
            print("Error: Ingrese un formato de telefono valido")
    banco_pasajero = input("Ingrese el banco con el que va a pagar: ").upper()
    try:
        while True:
            mostrar_asiento()
            asiento_pasajero = input("Ingrese el asiento que de sea comprar: ")
            asiento_encontrado = False
            for fila in asientos:
                if asiento_pasajero in fila:
                    asiento_encontrado = True
                    fila[fila.index(asiento_pasajero)] = 'x'
                    break
            if asiento_encontrado:
                if int(asiento_pasajero) <= 30:
                    vip = False
                else:
                    vip = True
                print("Asiento disponible, ha quedado reservado para ti")
                break
            else:
                print("Asiento no encontrado, seleccione otro")     
    except ValueError:
        print("Error:Asiento invalido porfavor ingrese un asiento valido")
        
    def revertir_asiento():
        for fila in asientos:
            if 'x' in fila:
                fila[fila.index('x')] = asiento_pasajero

    if vip == True:
        pasajero_vip = "Si"
    else:
        pasajero_vip = "No"


            
    while True:
        opc3 = input("Desea confirmar el monto (Si/No)? ").upper()
        if opc3 == "SI":
            print("Gracias por su compra, vuelva pronto!")
            dict_datos_pasajero = {
                "Nombre":nombre_pasajero,
                "RUT":rut_pasajero,
                "Telefono":telefono_pasajero,
                "Banco":banco_pasajero,
                "Asiento":asiento_pasajero,
                "VIP":pasajero_vip
            }
            datos_pasajeros.append(dict_datos_pasajero)
            break
        elif opc3 == "NO":
            print("Compra cancelada volviendo al menu principal...")
            revertir_asiento()
            break
        else: 
            print("Error: Ingrese una opcion valida")
    
    return datos_pasajeros

# def eliminar_pasajero():
#     try:
#         rut_pasajero = int(input("Ingrese el rut del pasajero que desea eliminar(Sin puntos ni guion, si termina en k remplazala por un 0): "))
#         for diccionario in datos_pasajeros:
#             if rut_pasajero in diccionario:
                
        
            


while True:
    print("\n1. Ver asiento disponible")
    print("2. Comprar asiento")
    print("3. Anular vuelo")
    print("4. Modificar datos de pasajero")
    print("5. Salir")
    try:
        opc = int(input("Ingrese una opcion: "))
        if opc == 1:
            mostrar_asiento()
        elif opc == 2:
            tomar_pasaje()
            
            
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
        
        
