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

    if vip == True:
        print(f"El precio final de su pasaje con asiento VIP es de ${precio_vip}")
    else:
        print(f"El precio final de su pasaje con asiento normal es de ${precio_norm}")
        
    if banco_pasajero == "BANCO DUOC":
        print("Se a detectado un descuento del 15% por ser socio del banco DUOC")
        if vip == True:
            descuento = precio_vip * 0.15
            precio_vip_desc = precio_vip - descuento
            print(f"El precio final de su pasaje con el descuento aplicado es de ${precio_vip_desc}")
        else:
            descuento = precio_norm * 0.15
            precio_norm_desc = precio_norm - descuento
            print(f"El precio final de su pasaje con el descuento aplicado es de ${precio_norm_desc}")
    else:
        print("No se detecto ningun descuento")
        
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


def anular_vuelo():
    try:
        rut_pasajero = int(input("Ingrese el rut del pasajero del vuelo que desea cancelar: "))
        asiento_pasajero = input("Ingrese el asiento correspondiente a su rut: ")
        vuelo_encontrado = False
        
        for diccionario in datos_pasajeros:
            if diccionario["RUT"] == rut_pasajero and diccionario["Asiento"] == asiento_pasajero:
                datos_pasajeros.remove(diccionario)
                vuelo_encontrado = True
                for fila in asientos:
                    if 'x' in fila:
                        fila[fila.index('x')] = asiento_pasajero
                print("Vuelo anulado con exito")
                break
        if not vuelo_encontrado:
            print("Rut y asiento no coinciden")
            
                    
    except ValueError:
        print("Error: formato de rut invalido")
                
        
            


while True:
    print("\n1. Ver asiento disponible")
    print("2. Comprar asiento")
    print("3. Anular vuelo")
    print("4. Modificar datos de pasajero")
    print("5. Mostrar lista de pasajeros")
    print("5. Salir")
    try:
        opc = int(input("Ingrese una opcion: "))
        if opc == 1:
            mostrar_asiento()
        elif opc == 2:
            tomar_pasaje()
        elif opc == 3:
            anular_vuelo()
        elif opc == 4:
            print("rellenar")
        elif opc == 5:
            print(datos_pasajeros)
        else:
            print("Ingrese una opcion valida\n")      
    except ValueError:
        print("Error: Ingrese una opcion valida\n")
        
        
