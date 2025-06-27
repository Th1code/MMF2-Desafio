import pandas as pd

# Caminho do arquivo CSV
caminho_arquivo = '2025.CSV'  # Ajuste o caminho conforme necessário

# Lendo o arquivo com separador ";" e codificação ISO-8859-1
df = pd.read_csv(caminho_arquivo, sep=';', encoding='ISO-8859-1')

# Convertendo vírgulas para pontos e transformando colunas numéricas
for col in df.columns:
    df[col] = df[col].astype(str).str.replace(',', '.', regex=False)
    try:
        df[col] = pd.to_numeric(df[col], errors='ignore')
    except:
        pass

# Criando lista para armazenar os resultados
tabela_resultados = []

# Montando os dados
for coluna in df.columns:
    dados_disponiveis = df[coluna].notna().sum()
    if pd.api.types.is_numeric_dtype(df[coluna]):
        media = round(df[coluna].mean(), 2)
    else:
        media = "N/A"
    tabela_resultados.append([coluna, dados_disponiveis, media])

# Criando DataFrame com os resultados
tabela = pd.DataFrame(tabela_resultados, columns=['Coluna', 'Dados Disponíveis', 'Média'])

# Exibindo a tabela final
print(tabela)
