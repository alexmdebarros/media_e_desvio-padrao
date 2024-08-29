import pandas as pd
import numpy as np

df = pd.read_csv('traffic.csv', sep=';')

#removendo primeira e ultima coluna
df_cleaned = df.iloc[:, 1:-1]

#criando arrays para cada dia
data_14 = df_cleaned.iloc[:27].sum(axis=1).values
data_15 = df_cleaned.iloc[27:54].sum(axis=1).values
data_16 = df_cleaned.iloc[54:81].sum(axis=1).values
data_17 = df_cleaned.iloc[81:108].sum(axis=1).values
data_18 = df_cleaned.iloc[108:135].sum(axis=1).values

#convertendo para arrays
array_14 = np.array(data_14)
array_15 = np.array(data_15)
array_16 = np.array(data_16)
array_17 = np.array(data_17)
array_18 = np.array(data_18)

# Exibir os arrays
print(f"14: {array_14.tolist()}")
print(f"15: {array_15.tolist()}")
print(f"16: {array_16.tolist()}")
print(f"17: {array_17.tolist()}")
print(f"18: {array_18.tolist()}")

#calculando medias
media_14 = np.mean(array_14)
media_15 = np.mean(array_15)
media_16 = np.mean(array_16)
media_17 = np.mean(array_17)
media_18 = np.mean(array_18)

#exibindo medias
print(f"Média do dia 14: {media_14}")
print(f"Média do dia 15: {media_15}")
print(f"Média do dia 16: {media_16}")
print(f"Média do dia 17: {media_17}")
print(f"Média do dia 18: {media_18}")

#calculando desvio padrao
desvio_padrao_14 = np.std(array_14)
desvio_padrao_15 = np.std(array_15)
desvio_padrao_16 = np.std(array_16)
desvio_padrao_17 = np.std(array_17)
desvio_padrao_18 = np.std(array_18)

#exibindo desvio padrao
print(f"Desvio padrão do dia 14: {desvio_padrao_14}")
print(f"Desvio padrão do dia 15: {desvio_padrao_15}")
print(f"Desvio padrão do dia 16: {desvio_padrao_16}")
print(f"Desvio padrão do dia 17: {desvio_padrao_17}")
print(f"Desvio padrão do dia 18: {desvio_padrao_18}")

maior_media = max(media_14, media_15, media_16, media_17, media_18)

if maior_media == media_14:
    dia_maior_media = "14/12/09"
elif maior_media == media_15:
    dia_maior_media = "15/12/09"
elif maior_media == media_16:
    dia_maior_media = "16/12/09"
elif maior_media == media_17:
    dia_maior_media = "17/12/09"
else:
    dia_maior_media = "18/12/09"

print(f"O dia com a maior média de acidentes por meia hora é {dia_maior_media} com média de {maior_media:.2f}")

menor_variacao = min(desvio_padrao_14, desvio_padrao_15, desvio_padrao_16, desvio_padrao_17, desvio_padrao_18)

if menor_variacao == desvio_padrao_14:
    dia_menor_variacao = "14/12/09"
elif menor_variacao == desvio_padrao_15:
    dia_menor_variacao = "15/12/09"
elif menor_variacao == desvio_padrao_16:
    dia_menor_variacao = "16/12/09"
elif menor_variacao == desvio_padrao_17:
    dia_menor_variacao = "17/12/09"
else:
    dia_menor_variacao = "18/12/09"

print(f"O dia com a menor variação de acidentes por meia hora é {dia_menor_variacao} com desvio padrão de {menor_variacao:.2f}")
