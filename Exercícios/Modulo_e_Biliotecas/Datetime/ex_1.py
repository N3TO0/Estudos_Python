from datetime import date,datetime

d = date(2025,6,14)
print("1",d)

#retorna data atual que esta no computador
print("2",date.today())

d2 = datetime(2025,6,14, 14, )
print("3",d2)

#retorna data e hora atual que esta no computador
print("4",datetime.today())