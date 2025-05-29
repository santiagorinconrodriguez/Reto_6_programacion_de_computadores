# Programa para imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

numero = int(input("Ingrese un número natural mayor a 2 para ver los números pares de forma descendente hasta 2: "))
# Se le indica al usuario que debe ingresar un número el cual será evaluado en el programa

while numero >= 2: # Se propone un bucle, el cual entrará con el número ingresado en la consola, si este es mayor a 2
    if numero % 2 == 0: # Se propone un condicional en donde se cumplirá si el residuo de la división del número ingresado entre 2 es 0 (el número es par)
        numero = numero - 2 # ahora el programa asignará un valor de forma descendente a la variable numero.
        print (numero) # Con la asignación anterior se imprime el número par anterior a a la variable, número y el programa volverá a evaluar las condiciones

    else: # si la condición no se cumple (el número es impar), se entrará al ese
        numero = numero - 1 # Se le hace una asignación al número restándole una unidad, haciéndo de esta manera la variable numero un número par
        print (numero) # como la asignación nos dio un número par, este se imprime y volverá al ciclo while