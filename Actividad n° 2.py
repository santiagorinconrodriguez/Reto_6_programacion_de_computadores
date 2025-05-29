# Programa para Imprimir un listado con los números impares desde 1 hasta 999
numero : int = 1 # Se inicializa y declara la variable numero con el valor de 1
while numero <= 999: # se propone un bucle, en donde entrará la variable numero si es menor o igual a 999
    if numero % 2 != 0: # Ahora, con el condicional, el programa evaluará si el número es impar gracias al módulo, el cual tendrá un valor diferente de 0 si el número es impar
        print (numero) # si la variable entró al condicional y la cumplió, ese número es impar y el programa lo imprimirá
    numero = numero + 1 # se hace una asignación para que el bucle evalue inmediatamente el siguiente número

# Programa para imprimir un listado con los números pares desde 2 hasta 1000
numero : int = 2 # Se inicializa y declara la variable numero con el valor de 2
while numero <= 1000:  # se propone un bucle, en donde entrará la variable numero si es menor o igual a 1000
    if numero % 2 == 0: # Ahora, con el condicional, el programa evaluará si el número es par gracias al módulo, el cual tendrá un valor igual a 0 si el número es par
        print (numero) # # si la variable entró al condicional y la cumplió, ese número es par y el programa lo imprimirá
    numero = numero + 1 # se hace una asignación para que el bucle evalue inmediatamente el siguiente número