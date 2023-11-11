#UTILIZAR O DATETIME: manipular datas e horas em Python.
import datetime
from datetime import datetimedelta 

data_e_hora = datetime.datetime.now()
print(data_e_hora = datetime.datetime.now())

#DIRETIVAS: formata datas e horas: 
# As diretivas da função `strftime` em Python são usadas para formatar objetos `datetime` em strings de acordo com um padrão específico. Aqui estão algumas das diretivas mais comuns que você pode usar com `strftime`:

# %Y: Ano com quatro dígitos (por exemplo, 2023).
# %y: Ano com dois dígitos (por exemplo, 23 para 2023).
# %m: Mês com zero à esquerda (por exemplo, 01 para janeiro).
# %B: Nome completo do mês (por exemplo, "January").
# %b ou %h: Nome abreviado do mês (por exemplo, "Jan").
# %d: Dia do mês com zero à esquerda (por exemplo, 05 para o dia 5).
# %H: Hora (00-23) com zero à esquerda.
# %I: Hora (01-12) com zero à esquerda.
# %M: Minuto com zero à esquerda.
# %S: Segundo com zero à esquerda.
# %p: AM ou PM (dependendo do horário).
# %A: Nome completo do dia da semana (por exemplo, "Sunday").
# %a: Nome abreviado do dia da semana (por exemplo, "Sun").
# %j: Dia do ano como um número decimal (001 a 366).
# %U: Número da semana no ano (00 a 53, onde a semana começa no domingo).
# %W: Número da semana no ano (00 a 53, onde a semana começa na segunda-feira).
# %w: Dia da semana como um número decimal (0 para domingo, 6 para sábado).
# %Z: Nome do fuso horário.
# %z: Offset do fuso horário (por exemplo, "+0200").

from datetime import datetime

dt = datetime(2023, 9, 27, 14, 30, 0)
data_nascimento = input("Digite sua data de nascimento (ano-mes-dia):")
nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d")
idade = datetime.now() - nascimento

# Extrair apenas a parte dos anos da diferença de datas
anos = idade.days // 365

print(anos)

# Formatando a data e hora
formatted_datetime = dt.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_datetime)  # Saída: "2023-09-27 14:30:00"

# datetime.datetimedelta: retorna datas e horarios
hoje = datetime.now() 
anteontem = datetime.datetimedelta(day - 2) #mostra a data e hora de 2 dias atrás

# EXERCÍCIO01 - Peça ao usuário que insira seu ano de nascimento e calcule sua idade.

from datetime import datetime

dt = datetime(2023, 9, 27, 14, 30, 0)
data_nascimento = input("Digite sua data de nascimento (ano-mes-dia):")
nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d")
idade = datetime.now() - nascimento


# EXERCÍCIO02 - Calcule e exiba a data e hora exatas daqui a 7 dias a partir de agora.
import datetime
from datetime import timedelta, datetime
atual = datetime.now()
proxima_semana = atual + timedelta(days=7)
print(proxima_semana)


# EXERCÍCIO03 - Peça ao usuário para inserir um ano e, em seguida, exiba o ano atual.

year = int(input("Digite um ano"))
ano_atual = datetime.now().year     
print(ano_atual)

# EXERCÍCIO04 - Calcule e exiba a data e hora atuais em um formato personalizado(utilize diretivas).
today = datetime.now()
print(today.strftime(("%y/%B/%d")))

