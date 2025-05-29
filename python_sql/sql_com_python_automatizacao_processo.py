import pandas as pd
import pyodbc
import getpass
import os
import glob

password = getpass.getpass("Digite a senha do usuário do SSMS:")

#conexão com o SQL Server
conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=SEU SERVER;"
    "DATABASE=SEU DB;"
    "UID=SEU USER;"
    f"PWD={password};"
)

cursor = conn.cursor()

idArquivo = '00006'
caminho_saida = f"caminho até o idArquivo/ID {idArquivo}/"
pasta = f"caminho até o idArquivo/ID {idArquivo}/"

arquivos = glob.glob(os.path.join(pasta, "*.csv"))  # Lista arquivos .xlsx
if not arquivos:
    raise FileNotFoundError(f"Nenhum arquivo Excel encontrado na pasta: {pasta}")

csv_file = arquivos[0]

print(f"📂 Arquivo de entrada selecionado: {csv_file}")

# Criar nome do arquivo de saída
nome_arquivo = f"ID{idArquivo}_enriquecido.csv"
arquivo_pronto = os.path.join(caminho_saida, nome_arquivo)

df = pd.read_csv(csv_file, dtype=str)  # Ler os dados como string para evitar erros

# Verificar o tamanho máximo de cada coluna no DataFrame
# for coluna in df.columns:
#     max_length = df[coluna].astype(str).apply(len).max()
#     if max_length > 255:
#         print(f"⚠️ Alerta: A coluna '{coluna}' contém um valor com {max_length} caracteres (maior que 255).")

tabela_temp = "#Temp_Tabela"

# 2️ Criar tabela temporária com colunas do CSV
colunas = ", ".join([f"[{col}] NVARCHAR(255)" for col in df.columns])
create_table_sql = f"CREATE TABLE {tabela_temp} ({colunas})"

cursor.execute(create_table_sql)
conn.commit()

# 3️ Inserir os dados na tabela temporária
for _, row in df.iterrows():
    valores_escapados = [str(v).replace("'", "''") for v in row.fillna("").tolist()]
    valores = "', '".join(valores_escapados)
    insert_sql = f"INSERT INTO {tabela_temp} VALUES ('{valores}')"
    cursor.execute(insert_sql)

conn.commit()

# 5️ Executar a query para unir os dados
query = f"""
SUA QUERY PARA TRATAR OS DADOS, A QUE EU USEI É CONFIDENCIAL SEGUE UM EXEMPLO DE QUERY: 

SELECT 
    NOME,
    IDADE, 
    EMAIL
FROM {tabela_temp}
ORDER BY IDADE DESC

"""


df_result = pd.read_sql(query, conn)

# 6️ Exportar resultado para CSV separado por ponto e vírgula
df_result.to_csv(arquivo_pronto, sep=';', index=False, encoding='utf-8')


# 7️ Excluir a tabela temporária
drop_table_sql = f"DROP TABLE {tabela_temp}"
cursor.execute(drop_table_sql)
conn.commit()

# Fechar conexão
cursor.close()
conn.close()

print(f"Processo finalizado e resultado salvo em {nome_arquivo}")