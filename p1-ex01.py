import datetime

data_atual = datetime.date.today()

print("Data atual: ", data_atual)
print("Ano atual: ", data_atual.year)
print("Mês atual: ", data_atual.month)
print("Dia atual: ", data_atual.day)
print("Data atual formatada: ", data_atual.strftime("%d/%m/%Y"))
meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
         "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
print("Data atual formatada: ", data_atual.strftime("%d de %B de %Y").replace(data_atual.strftime("%B"), meses[data_atual.month - 1]))
