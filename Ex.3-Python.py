# Comentários:
#      O arquivo "Ex.3 - ResultadoLicenca.xlsx" mostra o resultado antes de se agrupar
# por data, usuário e tempo de uso. O exercício pede o ID do usário
# e o tipo de licença, porém, todos os tipos de licença de cada entrada
# do usuário é diferente, então coloquei esse arquivo "Ex.3 - ResultadoLicenca.xlsx" 
# com os tipos de licenças e IDs de sessão e o arquivo "Ex.3 - ResultadoAgrupadoData.xlsx"
# sem os tipos de licenças ou IDs de sessão, porém agrupado pelo tempo total de uso por dia

import pandas as pd
import time
 
start = time.time()
dataframe = pd.read_excel("Input_Teste_Python_exercicio 3.xlsx")
dataframe['Day'] = pd.to_datetime(dataframe['Start Time']).dt.date
dataframe['Start Time'] = pd.to_datetime(dataframe['Start Time'])
dataframe['End Time'] = pd.to_datetime(dataframe['End Time'])

dataframe['Total Time'] = dataframe['End Time'] - dataframe['Start Time']
dataframe['Total Time'] = (pd.Timestamp('now').normalize() +  dataframe['Total Time']).dt.time

dataframe1 = pd.DataFrame()
dataframe1['Session ID'] = dataframe['Session ID']
dataframe1['User Name'] = dataframe['User Name']
dataframe1['License Type'] = dataframe['License Type']
dataframe1['Day'] = dataframe['Day']
dataframe1['Total Time'] = dataframe['Total Time']
dataframe1 = dataframe1.sort_values('User Name')
dataframe1.to_excel("Ex.3 - ResultadoLicenca.xlsx")

dataframe2 = pd.DataFrame()
dataframe2['Session ID'] = dataframe['Session ID']
dataframe2['User Name'] = dataframe['User Name']
dataframe2['License Type'] = dataframe['License Type']
dataframe2['Day'] = dataframe['Day']
dataframe2['Total Time'] = dataframe['Total Time']

sec = []
for d in dataframe2['Total Time']:
    [h,m,s] = str(d).split(':')
    sec.append(int(h)*3600 + int(m)*60 + int(s))

dataframe2['Total Time'] =  pd.to_numeric(pd.Series(sec))
dataframe2 = dataframe2.groupby(['User Name', 'Day']).agg({'Total Time' : 'sum'})
dataframe2['Total Time'] = pd.to_datetime(dataframe2['Total Time'], unit='s').dt.strftime("%H:%M:%S")
dataframe2.to_excel("Ex.3 - ResultadoAgrupadoData.xlsx") 

text_file = open("Ex.3 - Tempo Execucao.txt", "w")
text_file.write(str(time.time() - start) + " ms")
text_file.close()
