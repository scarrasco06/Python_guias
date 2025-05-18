#ejercicio 1.1
def imprimirHolaMundo():
    print("¡Hola mundo!")

#imprimirHolaMundo()

#ejercicio 1.2
def imprimirUnVerso():
    print("Once you know what my love's gonna feel like \n Nothing else will feel right \n You can feel like \n Moonbeam ice cream, taking off your blue jeans \n Dancing at the movies \n 'Cause it feels so")

#imprimirUnVerso()

#ejrcicio 1.3
def raizDe2():
    res = round(2 ** 0.5, 4)
    print(res)

#raizDe2()

#ejercicio 1.4
def factorial2(n: int) -> int:
    if n == 0 or n == 1:
        resultado = 1
    elif n > 1:
        resultado = 2 * factorial2(n - 1)
        print(resultado)
    return(resultado)

#factorial2(2)

#ejercicio 1.5 NI IDEAAAA

#-----------------------------------------------------------------
#ejercicio 2.1
def imprimirSaludo(name: str) -> None:
    print(f"Hola {name}")

#imprimirSaludo("Sarelia")


#ejercicio 2.2
def raizCuadradaDe(n:float) -> float:
    resultado: float
    resultado = n ** 0.5
    print(round(resultado, 3))

#raizCuadradaDe(6)


#ejercicio 2.3
def fahrenheit_a_celsius(t:float) -> float:
    resultado = float((t - 32) / 1.8) 
    return round(resultado, 3)

#fahrenheit_a_celsius(200)

#ejercicio 2.4 
def imprimirVerso():
    estribillo = "Once you know what my love's gonna feel like\nNothing else will feel right\nYou can feel like\nMoonbeam ice cream, taking off your blue jeans\nDancing at the movies\n'Cause it feels so\n"
    print(estribillo * 2)

#imprimirVerso()

#ejercicio 2.5
def esMultiploDe(n: int, m:int) -> bool:
    if m == 0 :
        return False
    return n % m == 0 
   
#print(esMultiploDe(36, 4))

#ejercicio 2.6
def es_par(numero:int) -> bool:
    res = esMultiploDe(numero, 2)
    return res
    

#print(es_par(9)) 

#ejercicio 2.7
import math

def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> int:
    total_porciones = comensales * min_cant_de_porciones
    return math.ceil(total_porciones / 8)

#print(cantidad_de_pizzas(23, 6))  

#-----------------------------------------------------------------

#ejercicio 3.1
def alguno_es_0(numero1: float, numero2: float) -> bool:
    res: bool
    res = numero1 == 0 or numero2 == 0
    return res 
#print(alguno_es_0(0.5, 4))

#ejercicio 3.2
def ambos_son_0(numero1: float, numero2:float) -> bool:
    res: bool
    res = numero1 == 0 and numero2 == 0
    return res
# print(ambos_son_0(0, 0))

#ejercicio 3.3 
def es_nombre_largo(name:str) -> bool:
    res:bool
    res = len(name) >= 3 and len(name) <= 8
    return res 

#print(es_nombre_largo("lu"))

#ejercicio 3.4 
def esMultiploDe(n: int, m:int) -> bool:
    if m == 0 :
        return False
    return n % m == 0 

def es_bisiesto(n:int) -> bool:
    res: bool
    res = esMultiploDe(n, 4) and not esMultiploDe(n, 100)
    return res

#print(es_bisiesto(2012))

#-----------------------------------------------------------------

#ejercicio 4
def peso_pino(altura_en_cm:int) -> int:
    peso_del_pino: int
    if altura_en_cm <= 300:
        peso_del_pino = altura_en_cm * 3
    else:
        peso_del_pino = 900 + ((altura_en_cm - 300) * 2)
    return peso_del_pino
#print(peso_pino(300))

def es_peso_util(peso_pino_en_kg: int):
    if peso_pino_en_kg >=400 and peso_pino_en_kg <= 1000:
        return "Este peso de pino sirve"
    else:
        return "Este peso de pino no sirve"

#print(es_peso_util(600))

def sirve_pino(altura_pino_en_cm: int) -> bool:
    res = peso_pino(altura_pino_en_cm)  
    return es_peso_util(res)
     
#print(sirve_pino(300))

#--------------------------------------------------------------

#ejercicio 5.1
def devolver_el_doble_si_es_par(numero:int) -> int:
    if numero % 2 == 0:
        res =  numero * 2
        return res
    else:
        return numero

#print(devolver_el_doble_si_es_par(10))

#ejecicio 5.2
#Primera forma:
def devolver_valor_si_es_par_si_no_el_que_sigue (numero: int): 
    if numero % 2 == 0:
        return numero  
    else: 
        return numero + 1

#print(devolver_valor_si_es_par_si_no_el_que_sigue(9))

#ejercicio 5.3
def esMultiploDe(n: int, m:int) -> bool:
    if m == 0 :
        return False
    return n % m == 0

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero: int): 
    if numero % 9 == 0:
        return numero * 3
    elif numero % 3 == 0:
        return numero * 2
    else:
        return numero

#print(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(3))

#ejercicio 5.4
def lindo_nombre(name: str) -> str:
    if len(name) >= 5 :
        return "Tu nombre tiene muchas letras!"
    else:
        return "Tu nombre tiene menos de 5 caracteres"
    
#print(lindo_nombre("Sare"))

#ejercicio 5.5
def elRango(numero:int) -> str:
    if numero < 5:
        return "Menor a 5"
    elif numero > 10 and numero < 20:
        return "Entre 10 y 20"
    else:
        return "Mayor a 20"
        
#print(elRango(5))


#ESPECIFICACIÓN!!!!!
# problema vacaciones_o_trabajar(sexo: String, edad: Entero) -> String:
#       requiere: {}
#       asegura: {res debe ser igual a un texto, que dependiendo la edad y sexo, te devolvera "Andá de vacaciones" o "Te toca trabajar"}
#

#ejercicio 5.6
def vacaciones_o_trabajar(sexo: str, edad: int) -> str:
    if sexo == "F" and (edad >= 60 or edad < 18):
        return "Anda de vacaciones"
    elif sexo == "M" and (edad >= 60 or edad < 18):
        return "Anda de vacaciones"
    else:
        return "Te toca trabajar"
    
#print(vacaciones_o_trabajar("M", 88))

#ejercicio 6.1
def imprimir_num_del_1_al_10 ():
    number = 1
    while number <= 10:
        print(number)
        number += 1 
#print(imprimir_num_del_1_al_10())


#ejercicio 6.2
def num_pares_entre_10_y_40():
    i: int = 10
    while i <= 40:
        print(i)
        i += 2
#print(num_pares_entre_10_y_40())

#ejercicio 6.3
def imprimir_eco_10_veces():
    i: str = 1
    while i <= 10:
        print("Eco")
        i += 1
#print(imprimir_eco_10_veces())

#ejercicio 6.4
def cuenta_regresiva(numero: int):
    while numero > 0:
        print(numero)
        numero -= 1
    print("Despegue")
#print(cuenta_regresiva(10))
        
 
#ejercicio 6.5 ????!!!!
#def viaje_en_el_tiempo(año_de_partida: int, x_año_de_llegada: int) -> str:
    # requiere año_de_partida_ > x_año_de_llegada
    

#ejercicio 6.6  NI IDEA

#--------------------------------------------------------------------------

#ejercicio 7.1
def imprimir_num_del_1_al_10_con_for():
    for numero in range(1,11,1):
        print(numero)
#print(imprimir_num_del_1_al_10_con_for())

#ejercicio 7.2
def num_pares_entre_10_y_40_con_for():
    for par in range (10,41,2):
        print(par)

#print(num_pares_entre_10_y_40_con_for())

#ejercicio 7.3
def imprimir_eco_10_veces_con_for():
    for res in range(1, 11, 1):
        print("eco")
#print(imprimir_eco_10_veces_con_for())

#ejercicio 7.4
def cuenta_regresiva_con_for(comienza_en: int):
    for i in range (comienza_en, 0, -1 ):
        print(i)
    print("Despegue")
#print(cuenta_regresiva_con_for(5))

#ejercicio 7.5  ?????#

#----------------------------------------------------------

#ejercicio 8
# x = 5
# y = 7

# ejrcicio 8.1
# x = x + y
# x = 5 + 7

# x = 12
# y = 7

#ejercicio 8.2
# z = x + y
# y = z * 2

# z = 12
# y = 12 * 2
# y = 24

# x = 5
# y = 24
# z = 12

#ejercicio 8.3
# x = "hora"
# y = x * 2

# x = "hora"
# y = "horahora"

#ejercicio 8.4
# x = False
# res = not(x)

# x = False
# res = True

#ejercicio 8.5
# x = False
# x = not(x)

# x = True

#ejercicio 8.6
# x = True
# y = False

# res = x and y
# x = res and x

# res = False
# x = False

#--------------------------------------------------------

#ejercicio 9
def rt(x: int, g: int)-> int: 
    g = g + 1 
    return x + g 
    
g: int = 0 
def ro(x: int)-> int: 
    global g 
    g = g + 1 
    return x + g

# print(rt(1, 0)) #2
# print(rt(1, 0)) #2
# print(rt(1, 0)) #2

# print(ro(1)) #2
# print(ro(1)) #3
# print(ro(1)) #4



     





    

