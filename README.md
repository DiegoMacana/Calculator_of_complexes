# Calculator_of_complexes
Este proyecto fue diseñado por DIEGO FERNANDO MACANA NARANJO en el lenguaje Python. Para la materia CNYT (Ciencias Naturales Y Tecnología). Es una libreria que opera numeros complejos. 
![mi primera captura](https://user-images.githubusercontent.com/59974540/75062476-def81900-54b0-11ea-91fe-57dbe6627f9f.PNG)


Este proyecto consta de 10 funciones 
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
8.carteciana: devuelve la misma tupla, debido a que si se grafica (a,b) siendo a el valor en x y b el valor en y. da la representacion del vector. 
9.polar: dado una dupla, la transformamos en magnitud y direccion, para la magnitud reciclamos la funcion modulo, y para la direccion, usamos la funcion de math.atan (tan^-1) para sacar el angulo, luego lo convierto en grados, para entenderlo mejor. 
10. inversa: la inversa sera una fraccion donde el dividendo sera la diferencia de la parte real e imaginaria (a,b) entonces a-b, y el divisor sera la suma de los cudrados de la parte real e imaginaria.

