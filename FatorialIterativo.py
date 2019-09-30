def fatorialIterativo(n:int)->int:
    resultado = 1
    while(n > 0):
        resultado = resultado * n
        n = n - 1
    return resultado
