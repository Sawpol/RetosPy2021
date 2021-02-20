# RetosPy2021


Ejercicio 1 
Crear una función que reciba un número como argunmento y devuelva el largo de este número.


def number_length(number):
    contador=0
    if isinstance(number, str):
        return None,'El valor tiene que ser número'
    elif numero < 0:
        return None,'El valor tiene que ser positivo'
    else:
        for i in str(number):
            contador += 1
        return (f'El largo del numero es:{contador}')

number_length(-3)




## Ejercicio 2

​

Crear una funcion que reciba dos numeros como argumentos (numero, longitud), y devolver una lista con los multiplos del numero dada la longitud


**Ejemplos**


`list_of_multiples(7, 5) ➞ [7, 14, 21, 28, 35]`

`list_of_multiples(17, 6) ➞ [17, 34, 51, 68, 85, 102]`

**Notas**

Vean que la lista contiene el numero que le pasan como argumento

​

**Restricciones**

- Los argumentos no puede ser negativos

- Los argumentos deben ser enteros



def multiplos(numero,rango):
   list_Numbers = []
   result = numero
   for i in range(rango):
       result += numero*i
       list_Numbers.append(result)
   return list_Numbers     


multiplos(3,4)




def factorial(number):
    if number > 1:
        number = number * factorial (number-1)
    return number



factorial(5)



Ejercicio 4

Crear una funcion que formatee numeros 😄

Ejemplos

format_numer(1000) -> '1,000'

format_numer(43214124) -> '43,214,124'

Restricciones

    El argumento no puede ser negativo
    El argumento deben ser entero

Ejercicio 4.1

    Agregar el separador que el usuario indique

Ejemplo

format_numer(1000,'#') -> '1#000'

format_numer(43214124) -> '43#214#124'


def numeros_formateados(numero,caracter):
    if not isinstance(numero,int):
        return None,'No es entero'
    if not isinstance(caracter,str):
        return None,'No es válido'





i= 20

[i for i in range (100) if not i % 2 == 0 ]








