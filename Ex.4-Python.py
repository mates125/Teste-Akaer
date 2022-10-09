import pandas as pd
import time

start = time.time()
dataframe = pd.read_excel("Input_Teste_Python_Dados Exercicio 4 I.xlsx")
start_day1 = []
end_day1 = []
start_time1 = []
end_time1 = []

for d in dataframe['Start Time']:
    [data, hora] = str(d).split(' ')
    start_time1.append(hora)
    start_day1.append(data)
for d in dataframe['End Time']:
    [data, hora] = str(d).split(' ')
    end_time1.append(hora)
    end_day1.append(data)

dataframe1 = pd.DataFrame()
dataframe1['User Name'] = dataframe['User Name']
dataframe1['Start Time'] = pd.Series(start_time1)
dataframe1['Start Day'] = pd.Series(start_day1)
dataframe1['End Time'] = pd.Series(end_time1)
dataframe1['End Day'] = pd.Series(end_day1)

print(dataframe1)

for d in dataframe1['Start Time']:
    start_time1.append(d)
for d in dataframe1['Start Day']:
    start_day1.append(d)
for d in dataframe1['End Time']:
    end_time1.append(d)
for d in dataframe1['End Day']:
    end_day1.append(d)

dataframe2 = pd.read_excel("Input_Teste_Python_Dados Exercício 4 II.xlsx")
dataframe2 = dataframe2.drop(columns={'Unnamed: 0'})
dataframe2['Data Inicio'] = pd.to_datetime(dataframe2['Data Inicio']).dt.strftime('%d/%m/%Y')
print(dataframe2)

usuario2 = []
start_time2 = []
start_day2 = []
end_time2 = []
end_day2 = []

for d in dataframe2['Usuario']:
    usuario2.append(d)
for d in dataframe2['Hora Inicio']:
    start_time2.append(d)
for d in dataframe2['Data Inicio']:
    start_day2.append(d)
for d in dataframe2['Hora Termino']:
    end_time2.append(d)
for d in dataframe2['Data Termino']:
    end_day2.append(d)

notfinduser = []
notfinddate = []
notfindtime = []

usuario = []
start_day = []
start_time = []
end_day = []
end_time = []

for i in range(0, len(usuario2)):
    if (end_day1[i] == end_day2[i] and end_time1[i] == end_time2[i] and start_day2[i] == start_day1[i] and 
    start_time2[i] == start_time1[i]):
        usuario.append(usuario2[i])
        start_day.append(start_day2[i])
        start_time.append(start_time2[i])
        end_day.append(end_day2[i])
        end_time.append(end_time2[i])
    else: 
        if (end_day1[i] != end_day2[i] and end_time1[i] != end_time2[i] and start_day1[i] == start_day2[i] and 
    start_time2[i] == start_time1[i]):
          notfinduser.append(usuario2[i])
          notfinddate.append(start_day2[i])
          notfindtime.append(start_time2[i])

dataframe_nao_encontrados = pd.DataFrame()
dataframe_nao_encontrados['Username'] = pd.Series(notfinduser)
dataframe_nao_encontrados['Start Day'] = pd.Series(start_day2)
dataframe_nao_encontrados['Start Time'] = pd.Series(start_time2)

data_inicio = []
data_termino = []

for i in range(0, len(start_day)):
    data_inicio.append(str(start_day[i]) + ' ' + str(start_time[i]))
    data_termino.append(str(end_day[i]) + ' ' + str(end_time[i]))

dataframe_encontrados = pd.DataFrame()
dataframe_encontrados['Username'] = pd.Series(usuario)
dataframe_encontrados['Hora Inicial'] = pd.Series(data_inicio)
dataframe_encontrados['Hora Final'] = pd.Series(data_termino)

dataframe_encontrados.to_excel("Ex.4 - Usuários Encontrados.xlsx")
dataframe_nao_encontrados.to_excel("Ex.4 - Usuários Não Encontrados.xlsx")

text_file = open("Ex.4 - Tempo de Execucao.txt", "w")
text_file.write(str(time.time() - start) + " ms")
text_file.close()