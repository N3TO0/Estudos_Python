def fun1(msg,nome):
    return f'{msg},{nome}!'

def fun2(fun1,*args):
    return fun1(*args)

print(fun2(fun1,'Olá',' Neto'))

print(fun2(fun1,'Bom dia',' Iderval'))