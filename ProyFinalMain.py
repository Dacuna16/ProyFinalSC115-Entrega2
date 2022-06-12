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

# Utilizamos una constante para determinar el peso máximo que recibimos, puede cambiar en el futuro
PESOMAX = 45
#Constante utilizada para hacer le número de orden más parecido a una real
NUMORDEN = 1000

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
print("\nMenú principal:")
print("1. Módulo de envío")
print("2. Módulo de facturación")
print("3. Módulo de informes")
print("4. Salir")
opcion = int(input("Ingrese la acción que desea ejecutar: (1, 2, 3, 4): "))

# Dependiendo de el input del cliente, hacemos llamada al módulo específico 
if opcion == 1:
    # Módulo de envío
    print("\n\n=====================================")
    print("=====================================")
    print("          Módulo de envío")
    print("=====================================")
    print("=====================================")
    # Convierto a float el input pues el sistema debe de ser capaz de trabajar con paquetes que no son de un peso entero
    peso = float(input("\n\nIngrese el peso (en Kg) del paquete a enviar: "))
    if peso <=0 or peso > PESOMAX:
        print("\nOpción inválida. Debe de ingresar un valor mayor a 0 o igual o menor a", PESOMAX,"\n")
        exit()

    print("\n\nTenemos tres tipos de envío:")
    print("1. BAJO COSTO (100 colones por cada kg adicional)")
    print("2. EXPRESS (200 colones por cada kg adicional)")
    print("3. INTERNACIONAL (300 colones por cada kg adicional)")

    tipoEnvio = int(input("\nIndique el tipo de envío que va a realizar (1, 2, o 3): "))

    if tipoEnvio==1:
        envio = "Bajo Costo"
        costoKg = 100
        #envio="Express"
        #costoKg = 200
    elif tipoEnvio==2:
        envio="Express"
        costoKg = 200
        #envio = "Bajo Costo"
        #costoKg = 100
    elif tipoEnvio==3:
        envio = "Internacional"
        costoKg = 300
    else:
        print("Ha ingresado una opción incorrecta")
        exit()

    # Calculo de costo
    costoMin=1000
    if peso>0 and peso<=1:
        costo = costoMin
    elif peso <= PESOMAX:
        # Utilizamos la funcion math.ceil para redondear hacia arriba pues no cobramos en fracciones
        # sino que cobramos por kg completos
        # Tomado de https://www.w3schools.com/python/ref_math_ceil.asp
        costo = math.ceil((peso-1)) * costoKg + costoMin
    else:
        print("Ingresó un valor incorrecto. Debe de ser mayor a 0 pero menor a",PESOMAX)

    # Resumen de lo ingresado
    # En un future release, este reporte se mostrara cuando el cliente indique que ya ha agregado todos los paquetes necesarios
    # Utilizamos l.just para alinear los resultados y hacerlo mas atractivo visualmente para el usuario
    # Tomado de https://www.w3schools.com/python/ref_string_ljust.asp
    print("\nEligió un paquete de:".ljust(50,"_"),peso,"kg")
    print("Eligió un tipo de envío:".ljust(50,"_") + " " + envio)
    print("El costo total a pagar por su paquete es de:".ljust(50,"_"),costo,"colones")
    print("Su número de orden es:".ljust(50,"_"),NUMORDEN+1,"\n\n")#mas adelante el +1 se cambiaria por una variable contador

elif opcion == 2:
    #Módulo de facturación
    print("\n\n=====================================")
    print("=====================================")
    print("       Módulo de facturación")
    print("=====================================")
    print("=====================================")
    print("\nCódigo en construcción, disculpe las molestias, trabajamos en mejorar nuestros productos!\n")
    exit()
elif opcion == 3:
    #Módulo de informes
    print("\n\n=====================================")
    print("=====================================")
    print("         Módulo de informes")
    print("=====================================")
    print("=====================================")
    print("\nCódigo en construcción, disculpe las molestias, trabajamos en mejorar nuestros productos!\n")
    exit()
elif opcion == 4:
    #Salir
    print("\nHa seleccionado la opción para salir del programa.")
    print("Gracias por usar nuestros servicios, le esperamos pronto!\n")
else:
    print("\nOpción inválida\n")
    exit()

