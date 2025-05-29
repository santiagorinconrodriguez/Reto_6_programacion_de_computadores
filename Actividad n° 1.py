# Programa para crear un listado con los números del 1 al 100 cada uno con su respectivo cuadrado

numero : int = 1 # Se inicializa la variable numero
while numero <= 100: # Se asigna un ciclo for, el cual evalua la condicion de que número debe ser menor o igual a 100 antes de entrar
    cuadrado : int = numero**2 # Se declara e inicializa la variable cuadrado, la cual nos mostrará el cuadrado del número
    print (numero, cuadrado, sep = " , ") # se imprime el número, seguidamente del cuadrado del mismo
    numero = numero + 1 # se hace una asignación para que la variable numero tengo como valor al siguiente entero y se evalue ese nuevo valor, volviendo a entrar al ciclo while