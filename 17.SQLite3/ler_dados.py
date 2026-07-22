import sqlite3

conexao = sqlite3.connect("meu_banco.db")

cursor = conexao.cursor()

comandos_sql="""
SELECT * FROM user
"""
cursor.execute(comandos_sql)
usuarios = cursor.fetchall()

conexao.close()

print("Lista dos usuarios: ")
for usuario in usuarios:
    print(f'ID: {usuario[0]} | Nome: {usuario[1]} | Email: {usuario[2]}')



