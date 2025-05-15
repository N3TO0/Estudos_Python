import pytz
from datetime import datetime, timezone

#usando de maneira correta com boa pratica o uso de data e horas, e colocando fuso horario, utilizando biblioteca pytz.
 
data = datetime.now(pytz.timezone("Europe/Oslo")).strftime("Data :%d %m %Y\nHora: %H:%M\n\n")
data2 = datetime.now(pytz.timezone("America/Sao_Paulo")).strftime("Data :%d %m %Y\nHora: %H:%M\n\n")

print(data)
print(data2)