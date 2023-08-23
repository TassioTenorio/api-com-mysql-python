import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Dudinha10@123',
    database='bd_api_com_mysql',
)

cursor = conexao.cursor()

# CRUD

# create
# name = "Duda"
# email = "Duda@teste.com.br"
# senha = "duda12356"

# comando = f'INSERT INTO dados(name, email, senha) VALUES ("{name}", "{email}", "{senha}")'
# cursor.execute(comando)
# conexao.commit()

# --------------------------------------------------------------//-----------------------------------------------------

# Update
# name = "Duda"
# email = "Duda123@teste.com.br"
# senha = ""
# comando = f'UPDATE dados SET email = "{email}" WHERE name = "{name}"'
# cursor.execute(comando)
# conexao.commit()

# --------------------------------------------------------//------------------------------------------------------------

# #  DELETE
# name = "Duda"
# comando = f'DELETE FROM dados WHERE name = "{name}"'
# cursor.execute(comando)
# conexao.commit()

# ---------------------------------------------------------//-------------------------------------------------------------

# READ
comando = 'SELECT * FROM dados'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)

cursor.close()
conexao.close()
