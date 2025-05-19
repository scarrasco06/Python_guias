#1. Recorrido y búsqueda en secuencias
# ejercicio 1.1
# def pertenece(s: [int], e: int ) -> bool:



def pertenece_2(s: [int], e: int) -> bool:
    return e in x

#print(pertenece_2([0, 1, 2, 3, 4], 5))

def pertenece_1(s, e):
    for x in s:
        if x == e:
            return True
    return False
#print(pertenece_1([0, 1, 2, 3, 4], 3))


def pertenece_3(s: [int], e: int) -> bool:
    i = 0
    res = False
    while i < len(s):
        res = s[i] == e 
        if res:
            break
        i += 1
    return res
    
print(pertenece_3([0, 1, 2, 3, 4], 9))

#ejercicio 1.2
def divide_a_todos(s: [int], e: int) -> bool:
    i: int
    i = 0
    while i < len(s):
        res = s[i] % e == 0
        print (res)
        i += 1
print(divide_a_todos([2, 4, 5, 7], 2))

#ejercicio 1.3
def suma_total(s:[int]) -> int:
    res =  
        
           

