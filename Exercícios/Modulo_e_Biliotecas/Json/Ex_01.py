import json

pessoas = [
    {"name":"tobias","sobrenome":"junior"},
    {"name":"ronny","sobrenome":"silva"},
    {"name":"livia","sobrenome":"fiqueredo"},
    {"name":"iderval","sobrenome":"neto"}
]


with open('Ex_04.json','w')as arquivo:
    json.dump(pessoas, arquivo)