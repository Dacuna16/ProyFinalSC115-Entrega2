# ================================
# Grupo 9 SC-115
# Programacion basica
#
# ================================

# Hago uso de exit() cuando el usuario ingresa un dato inválido para parar la ejecución (en if statements)
# Tomado de https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/
# Esto va a cambiar una vez que comenzemos a usar loops en el código

# Utilizamos una constante para determinar el peso máximo que recibimos, puede cambiar en el futuro
PESOMAX = 45

# Despliegue de menú
# En esta primera entrega no estamos utilizando módulos o funciones, por lo tanto 
# se da un error cuando intentan ir una opción que todavía no está desarrollada
# De momento, solo el módulo de Envío está parcialmente funcional, recibiendo un máx de un paquete por envío
# Más adelante haremos un llamado a las funciones desde la estructura de decision if, de momento
# estamos incluyendo todo el bloque de código dentro de la estructura

print("Bienvenidos a nuestro sistema de envíos 'Fidélitas Express'")
print("Menú principal:")
print("1. Módulo de envío")
print("2. Módulo de facturación")
print("3. Módulo de informes")
print("4. Salir")
opcion = int(input("Ingrese su opción requerida: (1, 2, 3, 4)"))

# Usamos estructuras de desición 
if opcion == 1:
    # Módulo de envío
    print("Módulo de envío")
    peso = int(input("Ingrese el peso en Kg del paquete a enviar"))
    if peso <=0 or peso > PESOMAX:
        print("El peso máximo que aceptamos es", PESOMAX," y el mínimo es 0")
        exit()

    print("Tenemos tres tipos de envio:")
    print("1. Express")
    print("2. Bajo Costo")
    print("3. Internacional")

    tipoEnvio = int(input("Indique el tipo de envio que va a realizar (1, 2, o 3)"))

    if tipoEnvio==1:
        envio="Express"
        costoKg = 200
        #print(envio)
    elif tipoEnvio==2:
        envio = "Bajo Costo"
        costoKg = 100
        #print(envio)
    elif tipoEnvio==3:
        envio = "Internacional"
        costoKg = 300
        #print(envio)
    else:
        print("Ha ingresado una opcion incorrecta")
        exit()

    # Resumen de lo ingresado
    print("eligio un paquete de",peso,"kg.")
    print("eligio un tipo de envio" + envio)

    # Calculo de costo
    costoMin=1000
    if peso<=1 and peso>0:
        costo = costoMin
    elif peso <= PESOMAX:
        costo = (peso-1) * costoKg + costoMin
    else:
        print("Ingresó un valor incorrecto. Debe de ser mayor a 0 pero menor a",PESOMAX)

    print("El costo total a pagar por su paquete es de ",costo)
elif opcion == 2:
    print("Código en construcción")
    exit()
elif opcion == 3:
    print("Código en construcción")
    exit()
elif opcion == 4:
    print("Gracias por usar nuestros servicios, le esperamos pronto!")
else:
    print("Opción inválida")
    exit()

