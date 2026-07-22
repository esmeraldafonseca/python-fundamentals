import sqlite3

#1. Cria um novo banco de dados ou coneta com o banco de dados existente
conexao = sqlite3.connect("meu_banco.db")

#2. Cria um cursoro(mensageiro que envia os comandos para o nosso banco de dados)
cursor = conexao.cursor()

#3. Escreve comandos sql para criar tabelas
comando_sql ="""
CREATE TABLE  IF NOT EXISTS user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(20) NOT NULL,
    email TEXT NOT NULL UNIQUE
)
"""

#4. Executa comandos sql 
cursor.execute(comando_sql)

#5.Salva as alteraçoes no banco de dados
conexao.commit()

#6. Fecha conexao com o banco de dados
conexao.close()
print("Banco de dados e tabela criados com sucesso")