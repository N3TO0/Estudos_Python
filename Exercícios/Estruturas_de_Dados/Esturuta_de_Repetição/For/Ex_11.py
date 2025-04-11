def desempacotamento(*args):
    for linha in args:
        for elemento in linha:
            print(elemento, end=' ')

L1=[[1,2,3,4],[5,6,7,],[8,9,10]]

desempacotamento(*L1)
