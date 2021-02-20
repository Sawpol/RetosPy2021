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




x = 7
y = 8  






list_of_multiples(1,10)




def cuenta_regresiva(numero):
     numero -= 1
if numero > 0:
         print numero
         cuenta_regresiva(numero)
     else:
         print "Boooooooom!"
 print "Fin de la función", numero



def factorial(number):
    if number > 1:
        number = number * factorial (number-1)
    return number



factorial(5)