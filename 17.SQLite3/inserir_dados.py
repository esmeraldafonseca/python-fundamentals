import sqlite3

conexao = sqlite3.connect("meu_banco.db")

cursor = conexao.cursor()

nome= input("Digite o seu nome: ")
email = input("Digite o seu email: ")
print()

comandos_sql = """
INSERT INTO user(
nome, email)
VALUES (?,?)
"""
try:
    cursor.execute(comandos_sql, (nome, email))
    print(f"Usuario {nome} inserido com sucesso.")
    conexao.commit()
except  sqlite3.IntegrityError:
    print("Error: email. ja cadastrado")

except Exception as e:
    print(f"Ocorreu o erro{e}")


conexao.close()