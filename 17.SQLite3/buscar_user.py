import sqlite3

conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()

id_busca = input("Digite o ID do usuario: ")

comandos_sql ="""
SELECT nome, email FROM user
WHERE id = ?
"""
cursor.execute(comandos_sql, (id_busca,))
usuario = cursor.fetchone()
conexao.close()

if usuario:
    print(F'Usuario encontrado: {usuario[0]} | {usuario[1]}')
else:
    print("Usuario não encontrado.")