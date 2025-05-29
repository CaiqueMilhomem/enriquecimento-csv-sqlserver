🛠️ Enriquecimento de Dados CSV com SQL Server
Este projeto automatiza o processo de integração, enriquecimento e exportação de dados a partir de arquivos CSV, utilizando Python e SQL Server. O objetivo é facilitar o tratamento de bases externas por meio de uma tabela temporária no banco de dados, onde os dados podem ser manipulados com flexibilidade usando SQL.

🚀 Funcionalidades
📥 Leitura automática de arquivos .csv a partir de uma pasta local.

🧩 Criação dinâmica de uma tabela temporária no SQL Server baseada nas colunas do CSV.

🛠️ Inserção de dados do arquivo na tabela temporária.

🧠 Execução de query SQL personalizada para tratar ou enriquecer os dados.

📤 Exportação do resultado em um novo arquivo .csv, separado por ;.

🧹 Limpeza automática da tabela temporária após o processo.

📚 Pré-requisitos
Python 3.8+

SQL Server (com acesso válido)

Pacotes Python:

pandas

pyodbc

getpass

Instale os pacotes necessários com:

bash
Copiar
Editar
pip install pandas pyodbc
🧪 Exemplo de uso
Configure os seguintes valores no script:

SERVER

DATABASE

UID (usuário)

idArquivo (identificador da pasta/arquivo)

Caminho da pasta de entrada/saída dos arquivos.

Execute o script:

bash
Copiar
Editar
python enriquecimento_csv_sql.py
O script:

Solicitará a senha de acesso ao banco.

Lerá o primeiro arquivo .csv na pasta indicada.

Criará e preencherá uma tabela temporária.

Executará a query que você configurar.

Gerará um arquivo IDXXXX_enriquecido.csv com os dados tratados.

🔐 Segurança
A senha do banco é solicitada via getpass, sem exibição no terminal.

O script escapa caracteres especiais para evitar quebras na inserção SQL.

⚠️ Observações
A query SQL usada para enriquecer os dados deve ser personalizada de acordo com seu contexto (o exemplo fornecido é genérico).

O script assume que todos os arquivos CSV têm cabeçalho e que as colunas devem ser convertidas para NVARCHAR(255).

🧼 Boas práticas aplicadas
Uso de tabela temporária para não interferir em estruturas permanentes do banco.

Conversão de colunas com dtype=str para evitar problemas com dados mistos.

Escape de apóstrofos simples ' para prevenir erros na inserção SQL.

🧑‍💻 Autor
Caique Milhomem – Engenheiro de Dados Júnior
🔗 GitHub: @CaiqueMilhomem