import numpy as np
import pandas as pd

df = pd.read_csv("https://pycourse.s3.amazonaws.com/bike-sharing.csv")
print('Qual o tamanho desse dataset?')
print(df.info())

print('Qual a média da coluna windspeed?')
print(df['windspeed'].mean())

print('Qual a média da coluna temp?')
print(df['temp'].describe())


print('Quantos registros existem para o ano de 2011?')
print(df[df['year'] == 0])

print('Quantos registros existem para o ano de 2012?')
print(df[df['year'] == 1])

df = df.set_index('year')
ano2012 = df.loc[df.index == 1, ['total_count']].values
print(f'Total de locações em 2012: {np.sum(ano2012)}')

print('Qual estação do ano contém a maior média de locações de bicicletas?')
print('Qual estação do ano contém a menor média de locações de bicicletas?')
df.groupby(by='season')
print(df.groupby(by='season').mean())

print('Qual horário do dia contém a maior média de locações de bicicletas?')
print('Qual horário do dia contém a menor média de locações de bicicletas?')
df.groupby(by='hour')
print(df.groupby(by='hour').mean())

print('Que dia da semana contém a maior média de locações de bicicletas?')
print('Que dia da semana contém a menor média de locações de bicicletas?')
df.groupby(by='weekday')
print(df.groupby(by='weekday').mean())

print('Às quartas-feiras (weekday = 3), qual o horário do dia contém a maior média de locações de bicicletas?')
df = df.set_index('weekday')
hora = df.loc[df.index == 3, ['hour','total_count']]
hora.groupby(by='hour')
print(hora.groupby(by='hour').mean())
