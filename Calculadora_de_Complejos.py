#Calculadora de Numeros complejos
#Estudiante: Diego Fernando Macana Naranjo
import math
def suma(A,B):     
    r=A[0]+B[0]
    c=A[1]+B[1]
    f=(r,c)
    return (f)
def resta(A,B):
    r=A[0]-B[0]
    c=A[1]-B[1]
    f=(r,c)
    return(f)
def multiplicar(A,B):
    x=(A[0]*B[0])
    y=(A[1]*B[1])
    ff=x-y
    w=(A[0]*B[1])
    z=(A[1]*B[0])
    gg=w+z
    f=(ff,gg)
    return (f)
def dividir(A,B):
    conjugado=B[1]*-1
    q=(A[0]*B[0])
    w=(A[0]*conjugado)
    e=(A[1]*B[0])
    r=-(A[1]*conjugado)
    sum2=q+r
    sumat=w+e
    a=(B[0]*B[0])
    f=-(B[1]*conjugado)
    sum1=a+f
    qq=sum2/sum1
    ww=sumat/sum1
    ff=(qq,ww)
    return(ff)
def modulo(X):
    mod=math.sqrt((X[0]*X[0])+(X[1]*X[1]))
    return (mod)
def conjugado(X):
    ff=(X[0],(-X[1]))
    return(ff)
def prettyPrinting(X):
    return("(",X[0],"+",X[1],"i)")
def carteciana(X):
    return(X)  
def polar(X):
    a=modulo(X)
    if X[1]>=0 and X[0]<0:
        b=math.atan2(X[1]/X[0])+math.pi
    elif X[1]<0 and X[0]<0:
        b=math.atan2(X[1]/X[0])-math.pi
    y=(a,b)
    return(y)
def inversa(A):
    suma_de_cuadrados=(A[1]*A[1])+(A[0]*A[0])
    rta=(A[0]/suma_de_cuadrados,-A[1]/suma_de_cuadrados)
    return rta
