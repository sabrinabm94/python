from datetime import datetime, timedelta, time, timezone
from time import strptime
import pytz

# datetime class from datetime module
date_and_hour = datetime(2024, 9, 21, 17, 20, 10)
print("A data de ontem com hora é: ", date_and_hour)

today_datetime = datetime.today()
print("A data de hoje com hora é: ", today_datetime)

# Operações com datas
# Adicionar uma semana a data atual
date_add_week = datetime.today() + timedelta(weeks=1)
print("\nAdicionando uma semana a data atual: ", date_add_week)

# fuso horario
date_now = datetime.now()
print("\nPegando a data atual com fuso horario: ", date_now)

# Adiciona alguns minutos no tempo atual
date_now_add_minutes = date_now + timedelta(minutes=45)
print("Adicionando 45 minutos na data atual: ", date_now_add_minutes)
print(
    "Mostrando somente a hora com adição dos 45 minutos: ", date_now_add_minutes.time()
)

# strftime
# Converte data em string
date_time_mask = "%d/%m/%Y %H:%M:%S"
date_string = date_now_add_minutes.strftime(date_time_mask)
print("\nConvertendo data em string: ", date_string)

# strptime
# Converte string em data
date_date = datetime.strptime(date_string, date_time_mask)
print("Convertendo data em string: ", date_date)

# Mostrando datas localizadas
date_time_from_oslo = datetime.now(pytz.timezone("Europe/Oslo"))
print("\nMostrando a hora de Oslo agora: ", date_time_from_oslo.time())

date_time_from_sao_paulo = datetime.now((timezone(timedelta(hours=-3))))
# UTC-3 hora de sp br
print("Mostrando a hora de São Paulo agora: ", date_time_from_sao_paulo.time())
