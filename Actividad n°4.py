# Programa para imprimir el factorial de un número natural dado

contador : int = 1 #se inciialiaza un contador con el valor de 1
factorial : int = 1 # se inciialiaza la variable llamada factorial con el valor de 1
numero = int(input("Ingrese un número natural, el programa le dará el factorial de su número: "))
# se le indica al usuario que digite un valor
while contador <= numero: # se propone un bucle while, el cual entrará al programa si el contador es menor o igual al número ingresado
    factorial = factorial * contador # Se usa la variable factorial, el cual nos ayudará a llevar la cuenta de la multiplicación de todos los números anteriores al digitado por el usuario
    contador = contador + 1 # Se actualiza el contador para que el while evalué el siguiente número

print("El factorial del número "+str(numero)+ " es "+str(factorial)) # Finalmente, se imprimen los resultados