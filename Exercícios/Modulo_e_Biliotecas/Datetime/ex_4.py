from datetime import datetime, timedelta

#usar utc.now() é boas praticas


# Data/hora em UTC
agora_utc = datetime.utcnow()

# Suponha que o usuário está no fuso horário UTC-3 (ex: Brasil)
horario_local = agora_utc - timedelta(hours=3)

print("\n\nNUTC:", agora_utc)
print("\n\nHorário local estimado:", horario_local)
print("\n\n")