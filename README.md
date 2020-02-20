# Calculator_of_complexes
Este proyecto consta de 11 funciones 
1. suma de complejos: esta funcion suma(A,B), tiene como parametro dos duplas, que seran la representacion 
de dos numeros comoplejos. para realizar la suma, es necesario agarrar ambas partes reales de las duplas y ambas partes imaginarias para sumarlas y crear la nueva dupla que sera la suma entre A y B.
2. Resta de complejos: tiene los mismos procedimientos que en la suma, la diferencia es denotada cuando restamos las partes reales e imaginarias para crear la dupla resultante. 
3. multiplicacion de complejos: se puede ver como la multiplicacion distributiva de A sobre B, donde los extremos(en el orden convencional) se sumaran y seran la parte real, y los del medio seran la parte imaginaria. es decir 
(1+4i)(5+i)=(1)(5)+(1)(i)+(4i)(5)+(4i)(i)
(1)(5)+(4i)(i) seran los reales como sabemos i*i=-1
y (1)(i)+(4i)(5) seran la parte imaginaria 

4. divicion: La división de dos números complejos es otro número complejo tal que:Su módulo es el cociente de los módulos.Su argumento es la diferencia de los argumentos.
5.modulo: es la raiz de la suma de los cuadrados de ambas partes (reales e imaginarias)
6. conjugado: tiene como parametro A, donde A es una tupla. A representa un numero imaginario, lo que hace la funcion es cambiar la parte imaginaria por su inverso aditivo. 
7. pretty printing: tiene como parametro A donde A es una dupla que representa un numero imaginario. lo que hace la funcion es escribir realmente la expresion imaginaria. Digamos A=(2,3) entonces pretty printing(A)=2+3i
