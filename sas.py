#ejerciocio 1
def saludos(nombre = "juan"):      #parametro
    print(F"hola, {nombre}")

saludos("Renato")         #Argumento


#ejerciocio 2
def sumar(a, b):
    print(a + b)

sumar(3, 4)

#ejerciocio 3
def multiplicacion(x, y):
    return x * y
resultado = multiplicacion(2,4)
print(resultado)
#ejerciocio 4
def mostrar():
    mensaje = "hola"
    print(mensaje)

mostrar()
#ejerciocio 5
def numero(num):
    if num % 2 == 0:
        print(f"el numero {num} es par")
    else:
        print(f"el numero {num} es impar")
numero(10)