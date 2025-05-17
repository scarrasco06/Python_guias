def es_primo(n:int) -> bool:
    n = abs(n)
    if n == 0 or n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            #return False es lo mismo que todo lo de abajo
            res = False
            break
        
    return True 
        
print(es_primo(7))

def cuantos_primos_en_rango(n:int, m: int) -> int:
    minimo = min(n, m)
    maximo = max(n, m)
    
    res = 0
    for i in range (minimo, maximo + 1):
        if es_primo(i):
            res = res + 1
    return res

#hacer test de esros casos:
#n<m
#n=m
#n>m
#n<0 y m>0
#m<0 y n>0    
    


