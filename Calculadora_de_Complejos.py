#Calculadora de Numeros complejos
#Estudiante: Diego Fernando Macana Naranjo

import math
     
def suma(A,B):
    #print ("(",A[0],"+",A[1],"i) + (",B[0],"+",B[1],"i)  = ","(",A[0],"+",B[0],") + (",A[1],"+",B[1],")i")    
    r=A[0]+B[0]
    c=A[1]+B[1]
    #if r==0:
    #   print("=",c,"i")
    #else:
    #   print ("=",r," + ",c,"i")
    f=(r,c)
    return (f)
def resta(A,B):
    #print ("(",A[0],"+",A[1],"i) - (",B[0],"+",B[1],"i)  = ","(",A[0],"-",B[0],") + (",A[1],"-",B[1],")i")    
    r=A[0]-B[0]
    c=A[1]-B[1]
    #if r==0:
    #    print("=",c,"i")
    #else:
    #    print ("=",r," + ",c,"i")
    f=(r,c)
    return(f)
        
def multiplicar(A,B):
    x=(A[0]*B[0])
    y=(A[1]*B[1])
    ff=x-y
    w=(A[0]*B[1])
    z=(A[1]*B[0])
    gg=w+z
    #print("=",ff,"+",gg,"i")
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
    #print(sum2,sumat,"i")
    a=(B[0]*B[0])
    f=-(B[1]*conjugado)
    sum1=a+f
    #print(sum2,sumat,"i / ",sum1)
    #print(sum1)
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
    
def prettyPrinting(X):# no probar
    print("(",X[0],"+",X[1],"i)")
    
def carteciana(X):
    return(X)
    
def polar(X):
    a=modulo(X)
    b=math.atan(X[1]/X[0])*(180/math.pi)
    print("(",a,",",b,"°)")


def main():
    
    
    A=(-64,0)
    B=(0,2)
    print(multiplicar(A,B))
    """
    suma(A,B)
    resta(A,B)
    multiplicar(A,B)
    dividir(A,B)
    modulo(A)
    prettyPrinting(A)
    polar(A)
    carteciana(A)
    print(suma(A,B))
    """
main()
