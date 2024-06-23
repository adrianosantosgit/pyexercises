import time

# Obtendo o tempo atual em segundos desde a época
segundos_desde_epoca = time.time()

print(time.gmtime())

print(time.time())

# Adicionando o deslocamento de fuso horário (UTC-03:00)
deslocamento_fuso_horario = -3 * 3600  # 3 horas em segundos
tempo_local = segundos_desde_epoca + deslocamento_fuso_horario

objeto_tempo = time.gmtime(tempo_local)

print(objeto_tempo)

data_hora_formatada = time.strftime("%d/%m/%Y %H:%M:%S", objeto_tempo)

print(data_hora_formatada)