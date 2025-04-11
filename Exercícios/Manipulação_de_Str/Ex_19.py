#CODIO QUE IDENTIFICA QUANTAS LETRAS TEM E A POSSIÇÃO DA PRIMA E ULTIMA LETRA.

a=str(input("\nDigite uma frase: ")).strip().upper()
b=str(input("\nDigite uma letra para saber se contem essa letra na frase que escreveu e qual a possição dela: ")).strip().upper()
print("\nA letra que vc escreveu contem na frase?: ", b in a)
print("\nContem quantas letras {}, da frase: {}".format(b, a.count(b)))
print("\nQual a possição da primeira letra {}?: {}".format(b,a.find(b)+1))
print("\nQual a possição da ultima letra {}?: {}\n".format(b,a.rfind(b)+1))
N