from math import pi


#ejercicio 1.1
def imprimir_hola_mundo():
    print("Hola Mundo")
    
#imprimir_hola_mundo()

#ejercicio 1.2
def perimetro() -> float:
    res: float
    res = 2 * pi
    return res

resultado: float
resultado = perimetro()
#print(perimetro())
    

#ejercicio 1.3
def es_multiplo_de(n: int, m:int) -> bool:
    if m == 0 :
        return False
    else:
        return n % m == 0
    
#print(es_multiplo_de(3, 7))   

 
def n_es_multiplo_de_m(n: int, m:int) -> bool:
    res:bool
    res = n % m == 0

#print(n_es_multiplo_de_m(21, 7))
    


#def londitud(lista: list) -> list:

#ejercicio 1.3
def es_nombre_largo(name: str) -> bool:
    resultado:bool #primero definir lo que devuelve la función
    resultado = len(str(name)) >= 3 and len(str(name)) <= 8
    return resultado
    
#print(es_nombre_largo("Lu"))


# ejercicio 5.1
#Especificacion
# problema devolver_el_doble_si_es_par(n:Z): Z {
#   requiere: {n pertence a los }
#   asegura: {Si res es par devolver el doble de ese numero}
#   asegura: {Si el numero es impar devolver el mismo numero}
#}
def devolver_doble_si_es_par(n:int)-> int:
    #if n_es_multiplo_de_m(n, 2):
    if (n % 2 == 0):
        res: int
        res = 2 * n
        return res
    else:
        return n

#print(devolver_doble_si_es_par(100))


def imprimir_los_pares_entre_10_y_40() -> None:
    i: int
    i = 10
    while i < 40:
        print(i)
        i += 2
  
#print(imprimir_los_pares_entre_10_y_40())  

#def imprimir_pares_entre_10_y_40() -> None:
#   for i in range(10, 41, 2):
#        print(i)


def cuenta_regresiva(desde: int) -> None:
    desde: int
    
    while desde > 0: 
        print(desde)
        desde -= 1
    print("Despegar")
    
#print(cuenta_regresiva(5))










