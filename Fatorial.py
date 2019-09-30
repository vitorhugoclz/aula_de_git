def fatorial(n:int)->int:
    #comentario, teste para conflito de branch
    if n < 0:
        print("valor inválido")
        return
    elif n == 0:
        return 1
    return n * fatorial(n - 1)
