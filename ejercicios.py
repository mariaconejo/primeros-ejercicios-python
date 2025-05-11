#ejercicio 1

#Funcion que maneja la bienvenida del usuario
def bienvenida():
    nombre = input("Ingrese su nombre: ")
    print(f"¡Bienvenido/a, {nombre}!")
    return nombre #Me retorna el nombre para usarlo en la funcion mostrar_resultado

#Funcion que maneja la operacion matematica para calcular el promedio
def calcular_promedio(nota1, nota2):
    promedio = (nota1 + nota2) / 2 # se suman las dos notas y se dividen por 2
    return promedio #Me retorna el promedio

#Funcion principal que llama a las otras funciones y pide los numeros al usuario
def mostrar_resultado():
    nombre = bienvenida()  # Llamamos a la función de bienvenida y obtenemos el nombre
    nota1 = float(input("Ingrese la primera nota: "))# Pide los numeros al usuario
    nota2 = float(input("Ingrese la segunda nota: "))
    promedio = calcular_promedio(nota1, nota2)  # Llamamos a la función de calcular_promedio y obtenemos el nombre
    print(f"{nombre}, tu promedio es: {promedio}")

# Llamamos a la función principal para iniciar el programa
mostrar_resultado()

#ejercicio  2

# Función para clasificar si es niño
def es_nino(edad):
    return edad < 13

# Función para clasificar si es adolescente
def es_adolescente(edad):
    return 13 <= edad < 18

# Función para clasificar si es adulto
def es_adulto(edad):
    return 18 <= edad < 60

# Función para clasificar si es adulto mayor
def es_adulto_mayor(edad):
    return edad >= 60

# Función principal para obtener y mostrar el resultado
def clasificar_edad():
    edad = int(input("Ingrese la edad: "))
    
    if es_nino(edad):
        print("La persona es un niño.")
    elif es_adolescente(edad):
        print("La persona es un adolescente.")
    elif es_adulto(edad):
        print("La persona es un adulto.")
    elif es_adulto_mayor(edad):
        print("La persona es un adulto mayor.")
    else:
        print("Edad no válida.")

# Llamar a la función principal
clasificar_edad()

# ejercicio 3

# Funcion que solicita los numeros al usuario
def solicitar_numeros():
    # Solicitar al usuario que ingrese una lista de números separados por comas
    numeros = input("Ingrese una lista de números separados por comas: ")
    # Convertir la entrada en una lista de enteros
    """
    input: el usuario ingresa los numeros pero se ven de esta manera ["1,2,3,"] una sola cadena por lo tanto usamos
    .split: separa los numeros y los coloca como numero separado ["1","2","3"]
    int: los  convierte en numeros enteros 
    map: hace que cada elemento de la lista se vuelva entero
    list: lo convierte en una lista int("1") int("2") int("3") => [1,2,3]
    https://www.reddit.com/r/learnpython/comments/it9pi2/what_does_listmapintinputsplit_do_in_python/?rdt=47379
    """
    return list(map(int, numeros.split(',')))   

def clasificar_numeros(lista_numeros):
    # Inicializar listas y contadores
    pares = [] # Las listas estan vacias al comienzo
    impares = []
    # Usar enumerate para iterar y clasificar números
    for i, numero in enumerate(lista_numeros):
        if numero % 2 == 0: # Si al dividir un número entre 2 el resto es cero, el número es par.
            pares.append(numero) # Usar append para agregar elementos a la lista
            print(f"Número: {numero} (Par)")
        else:
            impares.append(numero)
            print(f"Número: {numero} (Impar)")
    return pares, impares

def mostrar_resultados(pares, impares):
    # Mostrar los resultados
    print(f"Números pares: {pares} - Total: {len(pares)}")
    print(f"Números impares: {impares} - Total: {len(impares)}")

def contar_pares_impares():
    lista_numeros = solicitar_numeros()
    pares, impares = clasificar_numeros(lista_numeros)
    mostrar_resultados(pares, impares)

# Llamar a la función
contar_pares_impares()

#Ejercicio 4

def contar_vocales():
    # Pedir al usuario que ingrese una frase
    frase = input("Ingrese una frase: ").lower()
    
    # Definir las vocales incluyendo las acentuadas
    vocales = "aeiouáéíóú"
    
    # Inicializar un contador
    contador_vocales = 0
    
    # Recorrer la frase y contar las vocales
    for letra in frase:
        if letra in vocales:
            contador_vocales += 1
    
    # Mostrar el resultado
    print(f"La cantidad de vocales en la frase es: {contador_vocales}")

# Llamar a la función
contar_vocales()

# Ejercicios extra

#Ejercicio 1

import random

def pedir_intento():
    # Solicitar el intento al usuario y devolver el número ingresado
    return int(input("Adivina un número entre 1 y 100: "))

def inicializar_juego():
    # Generar el número secreto y dar la bienvenida
    numero_secreto = random.randint(1, 100)
    print("¡Bienvenido al juego de adivinar el número!")
    return numero_secreto

def jugar(numero_secreto):
    # Inicializar el contador de intentos
    intentos = 0

    # Pedir el primer intento al usuario
    intento = pedir_intento()
    intentos += 1  # Incrementar el contador

    # Usar un bucle while para continuar hasta adivinar
    while intento != numero_secreto:
        if intento < numero_secreto:
            print("Demasiado bajo. ¡Inténtalo de nuevo!")
        elif intento > numero_secreto:
            print("Demasiado alto. ¡Inténtalo de nuevo!")
        
        # Pedir otro intento al usuario usando la función
        intento = pedir_intento()
        intentos += 1  # Incrementar el contador
    
    return intentos, numero_secreto

def mostrar_resultados(intentos, numero_secreto):
    # Mostrar el mensaje al adivinar correctamente
    print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")

def juego_adivinar():
    numero_secreto = inicializar_juego()  # Iniciar el juego y generar el número secreto
    intentos, numero_secreto = jugar(numero_secreto)  # Ejecutar el juego
    mostrar_resultados(intentos, numero_secreto)  # Mostrar los resultados

# Llamar a la función para iniciar el juego
juego_adivinar()

#Ejercicio 2 
def mostrar_menu():
    # Mostrar el menú de opciones
    print("¡Bienvenido al conversor de unidades!")
    print("Opciones de conversión:")
    print("1. Metros a kilómetros")
    print("2. Gramos a kilogramos")
    print("3. Centígrados a Fahrenheit")
    print("4. Salir")

def convertir_metros_a_kilometros():
    # Conversión de metros a kilómetros
    metros = float(input("Introduce el valor en metros: "))
    kilometros = metros / 1000
    print(f"{metros} metros son {kilometros} kilómetros.")

def convertir_gramos_a_kilogramos():
    # Conversión de gramos a kilogramos
    gramos = float(input("Introduce el valor en gramos: "))
    kilogramos = gramos / 1000
    print(f"{gramos} gramos son {kilogramos} kilogramos.")

def convertir_centigrados_a_fahrenheit():
    # Conversión de centígrados a Fahrenheit
    centigrados = float(input("Introduce la temperatura en °C: "))
    fahrenheit = (centigrados * 9/5) + 32
    print(f"{centigrados} °C son {fahrenheit} °F.")

def conversor_unidades():
    # Inicializar la variable opcion
    opcion = 0

    # Iniciar un bucle que continuará hasta que el usuario elija salir
    while opcion != 4:
        mostrar_menu()  # Mostrar el menú
        opcion = int(input("Elige una opción (1-4): "))

        # Condiciones para cada opción
        if opcion == 1:
            convertir_metros_a_kilometros()
        elif opcion == 2:
            convertir_gramos_a_kilogramos()
        elif opcion == 3:
            convertir_centigrados_a_fahrenheit()
        elif opcion == 4:
            print("Gracias por usar el conversor de unidades. ¡Hasta luego!")
        else:
            print("Opción inválida. Por favor elige entre 1 y 4.")

        print()  # Imprimir una línea en blanco para separar las conversiones

# Llamar a la función para iniciar el programa
conversor_unidades()

#Ejercicio 3

# Función para mostrar el inventario actual
def ver_inventario(inventario):
    if inventario:
        print("\nInventario actual:")
        for nombre, datos in inventario.items():
            print(f"Producto: {nombre}, Cantidad: {datos['cantidad']}, Precio: ${datos['precio']:.2f}")
    else:
        print("\nEl inventario está vacío.")

# Función para agregar nuevos productos al inventario
def agregar_producto(inventario):
    nombre = input("Introduce el nombre del producto: ")
    cantidad = int(input("Introduce la cantidad: "))
    precio = float(input("Introduce el precio por unidad: $"))
    inventario[nombre] = {"cantidad": cantidad, "precio": precio}
    print(f"Producto '{nombre}' agregado correctamente.")

# Función para modificar un producto existente
def modificar_producto(inventario):
    nombre = input("Introduce el nombre del producto a modificar: ")
    if nombre in inventario:
        print(f"Producto actual: {nombre}, Cantidad: {inventario[nombre]['cantidad']}, Precio: ${inventario[nombre]['precio']}")
        nueva_cantidad = int(input("Introduce la nueva cantidad: "))
        nuevo_precio = float(input("Introduce el nuevo precio por unidad: $"))
        inventario[nombre]["cantidad"] = nueva_cantidad
        inventario[nombre]["precio"] = nuevo_precio
        print(f"Producto '{nombre}' actualizado correctamente.")
    else:
        print(f"El producto '{nombre}' no existe en el inventario.")

# Función para eliminar productos del inventario
def eliminar_producto(inventario):
    nombre = input("Introduce el nombre del producto a eliminar: ")
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado correctamente.")
    else:
        print(f"El producto '{nombre}' no existe en el inventario.")

# Función principal que gestiona el menú y las operaciones
def gestion_inventario():
    inventario = {}
    opcion = 0

    print("¡Bienvenido al sistema de gestión de inventario!")

    while opcion != 5:
        print("\nMenú de opciones:")
        print("1. Ver el inventario actual")
        print("2. Agregar nuevos productos")
        print("3. Modificar la cantidad o precio de un producto existente")
        print("4. Eliminar productos")
        print("5. Salir")
        # https://www.w3schools.com/python/python_try_except.asp Use esto para poder seleccionar las opciones del menu, podria haber usado match case
        try:
            opcion = int(input("Elige una opción (1-5): "))
            if opcion == 1:
                ver_inventario(inventario)
            elif opcion == 2:
                agregar_producto(inventario)
            elif opcion == 3:
                modificar_producto(inventario)
            elif opcion == 4:
                eliminar_producto(inventario)
            elif opcion == 5:
                print("Gracias por usar el sistema de gestión de inventario. ¡Hasta luego!")
            else:
                print("Opción inválida. Por favor elige entre 1 y 5.")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número válido.")

# Llamar a la función principal para iniciar el programa
gestion_inventario()

