# Programa para encontrar los divisores de un número entre 2 a 50

contador : int = 1 # Se inicializa la variable contador con el valor de 1
numero = int(input("Ingrese un número de 2 a 50 y a continuación verá sus divisores: "))
# Se le indica al usuario que ingrese una número entero
while contador <= 50: # se propone un bucle while en donde entrará si el contador es menor o igual a 50
    if numero % contador == 0: # Ahora, se hace un condicional si la división entre el número y el contador es exacta, es decir si el contador es divisor del número
        print(contador) # se imprimirá el contador si es divisor
    contador = contador + 1 # Se le hace una asignación a la variable contador para que el ciclo while vuelva a evaluar el siguiente número