import os
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 120)

CSV_PATHS = [
    'data/vendas_brasil.csv',
]

csv_path = next((p for p in CSV_PATHS if os.path.exists(p)), None)as
if csv_path is None:
    raise FileNotFoundError(
        'Não encontrei o arquivo vendas_brasil.csv. '
        'Envie o arquivo para o Colab (menu Arquivos → Fazer upload) '
        'ou coloque-o na pasta data/ e rode novamente.'
    )


# Carregar dados
df = pd.read_csv(csv_path)
df.head()
print(f"Linhas e Colunas: {df.shape}")
print(f"Nomes das Colunas: {df.columns.tolist()}")
df.info()
