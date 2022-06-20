# ================================
# Grupo 9 SC-115
# Programacion basica
#
# ================================

# Hago uso de exit() cuando el usuario ingresa un dato inválido para parar la ejecución (en if statements)
# Tomado de https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/
# Esto va a cambiar una vez que comenzemos a usar loops en el código

# Importo el modulo math para poder redondear los kilos y tener calculos de costos correctos
import math
from pickle import FALSE, TRUE

# Utilizamos una constante para determinar el peso máximo que recibimos, puede cambiar en el futuro
PESOMAX = 45

#Constante utilizada para hacer le número de orden más parecido a una real
NUMORDEN = 1000

# Variable utilizada para entrar por lo menos una vez al menu principal
menuPrinc = TRUE

# Funcion para modulo de envio
def modEnvio():
    indice = 0 # Indice para todos los arreglos, al final agrego un contador
    otroPaq = 1
    while otroPaq == 1:
        # Módulo de envío
        print("\n\n=====================================")
        print("=====================================")
        print("          Módulo de envío")
        print("=====================================")
        print("=====================================")
        peso = {}
        envio = {}
        costoKg = {}
        costo = {}
        # Convierto a float el input pues el sistema debe de ser capaz de trabajar con paquetes que no son de un peso entero
        peso[indice] = float(input("\n\nIngrese el peso (en Kg) del paquete a enviar: "))
        if peso[indice] <=0 or peso[indice] > PESOMAX:
            print("\nOpción inválida. Debe de ingresar un valor mayor a 0 o igual o menor a", PESOMAX,"\n")
            exit()

        print("\n\nTenemos tres tipos de envío:")
        print("1. BAJO COSTO (100 colones por cada kg adicional)")
        print("2. EXPRESS (200 colones por cada kg adicional)")
        print("3. INTERNACIONAL (300 colones por cada kg adicional)")

        tipoEnvio = int(input("\nIndique el tipo de envío que va a realizar (1, 2, o 3): "))

        if tipoEnvio==1:
            envio[indice] = "Bajo Costo"
            costoKg[indice] = 100
        elif tipoEnvio==2:
            envio[indice] ="Express"
            costoKg[indice] = 200
        elif tipoEnvio==3:
            envio[indice] = "Internacional"
            costoKg[indice] = 300
        else:
            print("Ha ingresado una opción incorrecta")
            exit()

        # Calculo de costo
        costoMin=1000
        if peso[indice]>0 and peso[indice]<=1:
            costo[indice] = costoMin
        elif peso[indice] <= PESOMAX:
            # Utilizamos la funcion math.ceil para redondear hacia arriba pues no cobramos en fracciones
            # sino que cobramos por kg completos
            # Tomado de https://www.w3schools.com/python/ref_math_ceil.asp
            costo[indice] = math.ceil((peso[indice]-1)) * costoKg[indice] + costoMin
        else:
            print("Ingresó un valor incorrecto. Debe de ser mayor a 0 pero menor a",PESOMAX)

        # Resumen de lo ingresado
        # En un future release, este reporte se mostrara cuando el cliente indique que ya ha agregado todos los paquetes necesarios
        # Utilizamos l.just para alinear los resultados y hacerlo mas atractivo visualmente para el usuario
        # Tomado de https://www.w3schools.com/python/ref_string_ljust.asp
        print("\nEligió un paquete de:".ljust(50,"_"),peso[indice],"kg")
        print("Eligió un tipo de envío:".ljust(50,"_") + " " + envio[indice] )
        print("El costo total a pagar por su paquete es de:".ljust(50,"_"),costo[indice] ,"colones")
        print("Su número de orden es:".ljust(50,"_"),NUMORDEN+1,"\n\n")#mas adelante el +1 se cambiaria por una variable contador
        
        # Pregunto al usuario si desea ingresar otro paquete
        # En caso de digitar un valor invalido, despliego error y vuelvo a preguntar
        # De momento la informacion de cada paquete se sobreescribe
        # En el futuro, se usaran arrays para ir almacenando todos los valores
        otroPaqErr = 1
        while otroPaqErr == 1:
            otroPaq = int(input("Desea ingresar otro paquete? (1 para si, 0 para no): "))
            if otroPaq == 1:
                indice+=1 # si otro paquete, contador del indice
                otroPaqErr = 0
            elif otroPaq == 0:
                otroPaqErr = 0
            else:
                print("Ingreso un valor invalido, las opciones validas son 1 o 0")
                otroPaqErr = 1

# Funcion para modulo de facturacion
def modFacturacion():
    #Módulo de facturación
    print("\n\n=====================================")
    print("=====================================")
    print("       Módulo de facturación")
    print("=====================================")
    print("=====================================")
    nombre = input("Por favor ingrese su nombre: ")
    cedula = input("Por favor ingrese su numero de cedula: ")
    orden = int(input("Por favor ingrese su numero de orden: "))
    print("\nCódigo en construcción, disculpe las molestias, trabajamos en mejorar nuestros productos!\n")
    #exit()

# Funcion para modulo de Informes
def modInformes():
    #Módulo de informes
    print("\n\n=====================================")
    print("=====================================")
    print("         Módulo de informes")
    print("=====================================")
    print("=====================================")
    print("\nCódigo en construcción, disculpe las molestias, trabajamos en mejorar nuestros productos!\n")
    #exit()

# Modulo de Salir
def modSalir():
    #Salir
    # Declaro la variable global para poder modificarla desde la funcion
    global menuPrinc 

    salir = int(input("Esta seguro que desea salir? 1 para si, 0 para volver al menu principal"))
    if salir != 1 and salir != 0:
        print("Ingreso un valor invalido, las opciones validas son 1 o 0")
        menuPrinc = TRUE
        print(menuPrinc)
    elif salir == 1:
        menuPrinc = FALSE
        print(menuPrinc)
        print("\nHa seleccionado la opción para salir del programa.")
        print("Gracias por usar nuestros servicios, le esperamos pronto!\n")
    else:
        menuPrinc = TRUE

# Despliegue de menú
# En esta primera entrega no estamos utilizando módulos o funciones, por lo tanto 
# se da un error cuando intentan ir una opción que todavía no está desarrollada
# De momento, solo el módulo de Envío está parcialmente funcional, recibiendo un máx de un paquete por envío
# Más adelante haremos un llamado a las funciones desde la estructura de decision if, de momento
# estamos incluyendo todo el bloque de código dentro de la estructura

print("\n=================================================================")
print("=================================================================")
print("  Bienvenidos a nuestro sistema de envíos 'Fidélitas Express'")
print("=================================================================")
print("=================================================================")

while menuPrinc == TRUE:
    print("\nMenú principal:")
    print("1. Módulo de envío")
    print("2. Módulo de facturación")
    print("3. Módulo de informes")
    print("4. Salir")
    opcion = int(input("Ingrese la acción que desea ejecutar: (1, 2, 3, 4): "))

    # Dependiendo de el input del cliente, hacemos llamada al módulo específico 
    if opcion == 1:
        modEnvio()
    elif opcion == 2:
        modFacturacion()
    elif opcion == 3:
        modInformes()
    elif opcion == 4:
        modSalir()
    else:
        print("\nOpción inválida\n")
        exit()

