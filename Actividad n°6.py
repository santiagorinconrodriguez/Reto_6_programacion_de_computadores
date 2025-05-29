# Programa para determinar los números primos del 1 al 100

def es_primo(n):  # Función que verifica si n es un número primo
    if n < 2:  # Si n es menor que 2, no es primo
        return False  # Retorna False en ese caso
    i : int = 2  # Inicia el divisor en 2
    while i * i <= n:  # Mientras i no supere la raíz cuadrada de n
        if n % i == 0:  # Si n es divisible por i
            return False  # n no es primo, retorna False
        i = i + 1  # Incrementa i para probar el siguiente divisor
    return True  # Si no encontró divisores, n es primo, retorna True

if __name__ == "__main__":  # Punto de entrada principal del programa
    num = 1  # Inicializa la variable num en 1
    print("Números primos del 1 al 100:")  # Imprime el encabezado

    while num <= 100:  # Se pronone un bucle while que recorre los números del 1 al 100
        if es_primo(num):  # Si num es primo
            print(num)  # Imprime num
        num = num + 1  # Incrementa num en 1 con una asignación

