import sqlite3

conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()

id_para_deletar = input("Digite o ID do user que deseja deletar: ")

comandos_sql ="""
    DELETE FROM user
    WHERE id = ?
    """

cursor.execute(comandos_sql, (id_para_deletar,))
conexao.commit()
conexao.close()

if cursor.rowcount > 0:
    print(f"Usuario ID: {id_para_deletar} deletado com sucesso")
else:
    print("Nenhum usuario encontrado com esse id")