# ================================
# Grupo 9 SC-115
# Programación básica
# Versión/Entrega 2.0
# ================================

# En versión 1.0 utilizabamos exit() cada vez que un usuario ingresaba un dato inválido.
# En esta segunda versión, pasamos a utilizar ciclos por lo que desplegamos la pregunta de nuevo
# en caso de que se ingrese un dato inválido.

# Se importa time para poder utilizar la funcion sleep y mejorar la experiencia de usuario
# Tomado de https://www.pythoncentral.io/pythons-time-sleep-pause-wait-sleep-stop-your-code/
import time

# Se importa el modulo sys para poder terminar la ejecucion con la funcion exit
import sys

# Se ipmporta el módulo math para poder redondear los kilos y tener cálculos de costos correctos
import math
from pickle import FALSE, TRUE

# Se utiliza una constante para determinar el peso máximo que se recibe, puede cambiar en el futuro
PESOMAX = 45

#Constante utilizada para hacer le número de orden más parecido a una real
NUMORDEN = 1000

# Variable utilizada para entrar por lo menos una vez al menú principal
menuPrinc = TRUE



# |===========================================================================================================================|
#                                                Función para módulo de envío
# |===========================================================================================================================|

def modEnvio():
    global NUMORDEN # Se declara la constante global para poder referenciarla dentro de la función
    indice = 0 # Indice para todos los arreglos, al final se agrega un contador
    otroPaq = 1 # variable para controlar el ciclo que maneja si se desea ingresar otro paquete a la orden

    # Inicializo 4 listas donde voy a guardar los valores de acuerdo a la cantidad de productos a ser enviados en una orden
    # Las declaro con un scope específico para poder referenciarlas luego en una función diferente
    # Se maneja una lista por cada tipo de dato, en una futura entrega se podría cambiar a que cada lista contenga
    # información de una orden específica
    modEnvio.peso = []
    modEnvio.envio = []
    modEnvio.costoKg = []
    modEnvio.costo = []
    modEnvio.numFactura = []

    while otroPaq == 1:
        # Módulo de envío
        print("\n\n=====================================")
        print("=====================================")
        print("          Módulo de envío")
        print("=====================================")
        print("=====================================")

        # variable pesoValido para controlar el ciclo que maneja si el peso de un producto es válido o no
        pesoVal = 0

        while pesoVal == 0:
            # Se convierte a float el input pues el sistema debe de ser capaz de trabajar con paquetes que no son de un peso entero
            # No se almacena el input directamente en la lista para primero validar si el número es válido
            pesoEntrada = (float(input("\n\nIngrese el peso (en Kg) del paquete a enviar: ")))
            if pesoEntrada <=0 or pesoEntrada > PESOMAX:
                print("\nOpción inválida. Debe de ingresar un valor mayor a 0 o igual o menor a", PESOMAX,"\n")
                pesoVal=0
            else:
                # Si el número es válido, ahora sí se almacena en la lista
                modEnvio.peso.append(pesoEntrada)
                pesoVal=1

        print("\n\nTenemos tres tipos de envío:")
        print("1. BAJO COSTO (100 colones por cada kg adicional)")
        print("2. EXPRESS (200 colones por cada kg adicional)")
        print("3. INTERNACIONAL (300 colones por cada kg adicional)")

        tipoEnvio = int(input("\nIndique el tipo de envío que va a realizar (1, 2, o 3): "))

        if tipoEnvio==1:
            modEnvio.envio.append("Bajo Costo") 
            modEnvio.costoKg.append(100)
        elif tipoEnvio==2:
            modEnvio.envio.append("Express")
            modEnvio.costoKg.append(200)
        elif tipoEnvio==3:
            modEnvio.envio.append("Internacional") 
            modEnvio.costoKg.append(300)
        else:
            print("Ha ingresado una opción incorrecta")
            sys.exit()

        # Calculo de costo
        costoMin=1000

        
        if modEnvio.peso[indice]>0 and modEnvio.peso[indice]<=1: # Si el peso es mayor a 0 pero menor o igual a 1kg, el costo es el mínimo
            modEnvio.costo[indice] = costoMin
        elif modEnvio.peso[indice] <= PESOMAX: # Si el peso es menor a PESOMAX, calculo el costo total
            # Utilizamos la funcion math.ceil para redondear hacia arriba pues no cobramos en fracciones
            # sino que cobramos por kg completos
            # Tomado de https://www.w3schools.com/python/ref_math_ceil.asp
            # Para calcular, multiplico la diferencia de kilos por el tipo de envío, y sumo el costoMin del primer kilo:
            modEnvio.costo.append(math.ceil((modEnvio.peso[indice]-1)) * modEnvio.costoKg[indice] + costoMin)
        else:
            # En teoría, aquí no debería de llegar un peso inválido debido a una validación anterior
            print("Ingresó un valor incorrecto. Debe de ser mayor a 0 pero menor a",PESOMAX)

        # Pregunto al usuario si desea ingresar otro paquete
        # En caso de digitar un valor invalido, despliego error y vuelvo a preguntar

        otroPaqErr = 1
        while otroPaqErr == 1:
            otroPaq = int(input("Desea ingresar otro paquete? (1 para si, 0 para no): "))
            if otroPaq == 1:
                indice+=1 # si otro paquete, contador del indice
                otroPaqErr = 0
            elif otroPaq == 0:
                otroPaqErr = 0
                ind = 0
                # Resumen de lo ingresado
                # Utilizamos l.just para alinear los resultados y hacerlo mas atractivo visualmente para el usuario
                # Tomado de https://www.w3schools.com/python/ref_string_ljust.asp
                print("\nResumen del envio:\n")
                for x in range(len(modEnvio.peso)):
                    print("\nPAQUETE #",ind+1)
                    print("Eligió un paquete de:".ljust(50,"_"),modEnvio.peso[ind],"kg")
                    print("Eligió un tipo de envío:".ljust(50,"_") + " " + modEnvio.envio[ind] )
                    print("El costo total a pagar por su paquete es de:".ljust(50,"_"),modEnvio.costo[ind] ,"colones")
                    ind+=1

                costoFinal=0
                for x in range(len(modEnvio.costo)):
                    costoFinal=costoFinal+modEnvio.costo[x]

                print("\nEl costo final a pagar es: ",costoFinal,"colones.")
                modEnvio.numFactura.append(NUMORDEN+1)
                NUMORDEN+=1
                print("Su número de orden es:".ljust(50,"_"),modEnvio.numFactura[0],"\n\n")#mas adelante el +1 se cambiaria por una variable contador
                print("\nEstá siendo redirigido al menún principal, donde podra tener la oportunidad de facturar esta orden.")
                time.sleep(2)
            else:
                print("Ingreso un valor invalido, las opciones validas son 1 o 0")
                otroPaqErr = 1

    # Vuelvo a 0 estos valores en caso de que el usuario quiera volver a ingresar los valores
    # Antes de volverlos a 0, creo una copia que puedo utilizar en la función de facturación
    modEnvio.peso2 = modEnvio.peso
    modEnvio.peso = []
    modEnvio.envio2 = modEnvio.envio
    modEnvio.envio = []
    modEnvio.costoKg2 = modEnvio.costoKg
    modEnvio.costoKg = []
    modEnvio.costo2 = modEnvio.costo
    modEnvio.costo = []
    indice = 0

# |===========================================================================================================================|
#                                                 Función para módulo de facturación
# |===========================================================================================================================|

def modFacturacion():
    # En esta función se referencian variables de la función modEnvio, utilizando su definición completa
    # Se utilizan las copias de las listas creadas en la función modEnvio

    global NUMORDEN # Se declara la constante global para poder referenciarla dentro de la función

    print("\n\n=====================================")
    print("=====================================")
    print("       Módulo de facturación")
    print("=====================================")
    print("=====================================")
    nombre = input("Por favor ingrese su nombre: ")
    cedula = input("Por favor ingrese su número de cédula: ")
    orden = int(input("Por favor ingrese su número de orden: "))
    
    # Se evalúa si el número de orden existe. Si no existe, se da un error y se devuelve al menú principal
    if orden in modEnvio.numFactura:
        print("\nInformación de su factura\n")
        print("A nombre de:".ljust(50,"_"),nombre)
        print("Número de cédula:".ljust(50,"_"),cedula)
        print("Número de factura:".ljust(50,"_"),orden)
        print("\nInformación detallada de los productos a enviar:")
        
        for x in range(len(modEnvio.peso2)):
            print("\nPAQUETE #",x+1)
            print("Eligió un paquete de:".ljust(50,"_"),modEnvio.peso2[x],"kg")
            print("Eligió un tipo de envío:".ljust(50,"_") + " " + modEnvio.envio2[x] )
            print("El costo total a pagar por su paquete es de:".ljust(50,"_"),modEnvio.costo2[x] ,"colones")
            #ind+=1
                        
        costoFinal=0
        for x in range(len(modEnvio.costo2)):
            costoFinal=costoFinal+modEnvio.costo2[x]

        print("\nEl costo final a pagar es: ".ljust(50,"_"),costoFinal,"colones.")
        print("\nEstá siendo redirigido al menú principal")
        time.sleep(2)
    else:
        print("Número de orden inválido")                

# |===========================================================================================================================|
#                                                Función para módulo de informes
# |===========================================================================================================================|

def modInformes():
    print("\n\n=====================================")
    print("=====================================")
    print("         Módulo de informes")
    print("=====================================")
    print("=====================================")
    print("\nCódigo en construcción, disculpe las molestias, trabajamos en mejorar nuestros productos!\n")
    time.sleep(2)

# |===========================================================================================================================|
#                                                Función para módulo salir
# |===========================================================================================================================|

def modSalir():
    # Declaro la variable global para poder modificarla desde la funcion
    global menuPrinc 

    salir = int(input("Está seguro que desea salir? (1 para si, 0 para volver al menú principal)\n"))
    if salir != 1 and salir != 0:
        print("\nIngresó un valor inválido, las opciones válidas son 1 o 0")
        menuPrinc = TRUE
    elif salir == 1:
        menuPrinc = FALSE
        print("\nHa seleccionado la opción para salir del programa.")
        print("Gracias por usar nuestros servicios, le esperamos pronto!\n")
    else:
        menuPrinc = TRUE

# |===========================================================================================================================|
#                                                       Código "main"
# |===========================================================================================================================|

# Despliegue de menú principal
# En esta segunda entrega comenzamos a usar funciones
# Si el usuario ingresa a una funcion que todavia no esta desarrollada, la aplicacion
# los va a devolver al menu pruncipal

# Variable usada para controlar que el módulo envío sea utilizao por lo menos una vez antes de ir al módulo de facturación
numEnvios = 0

print("\n|=================================================================|")
print("|=================================================================|")
print("|  Bienvenidos a nuestro sistema de envíos 'Fidélitas Express'    |")
print("|=================================================================|")
print("|=================================================================|")

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
        numEnvios += 1
    elif opcion == 2:
        if numEnvios == 0:
            print("\nDebe de realizar por lo menos un envío antes de utilizar el módulo de facturación")
            time.sleep(1)
        else:
            modFacturacion()
    elif opcion == 3:
        modInformes()
    elif opcion == 4:
        modSalir()
    else:
        print("\nOpción inválida, esta siendo redirigido al menú principal ...")
        time.sleep(2)

