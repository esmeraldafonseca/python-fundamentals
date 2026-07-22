import sqlite3

conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()


id_busca = input("Digite o ID do usuario:")
novo_email= input("Digite o novo email: ")

comandos_sql = """
UPDATE user SET email = ?
WHERE id  = ?

"""
cursor.execute(comandos_sql, (novo_email, id_busca))

conexao.commit()
conexao.close()

print("Email actualizado com sucesso!")