from pymysql.connections import Connection

import check_email
import pymysql

def trocar_senha():
    email = input("Digite o e-mail do usuário que deseja trocar a senha: ")
    email = email.lower()
    check_email.check_email(email)
    print("O email está sendo procurado...")
    conexao = pymysql.connect(db='novo_hu', user='root', passwd='')
    cursor = conexao.cursor()
    query = "select count(1) from system_users where user_email = %s"
    cursor.execute(query, email)
    resultado = cursor.fetchall()
    print(resultado)
    if resultado == "((0,),)":
        print("Email encontrado: ", email)
    else:
        print("Email não encontrado")
    conexao.close()

def adicionar_usuario():
    email = input("Digite o email do novo executivo:")
    check_email.check_email(email)
    nome = input("Digite o nome e o sobrenome do executivo:")
    conexao = pymysql.connect(db='novo_hu', user='root', passwd='')
    cursor = conexao.cursor()
    query = "INSERT INTO system_users(username,password,roles,user_email,user_type,status,status_email) VALUES(%s," \
            "'null','ROLE_ADMIN',%s,2,1,1); "
    cursor.execute(query,(nome,email))
    print(nome, "está sendo adicionado...")
    conexao.commit()
    print(nome, "foi adicionadx")
    conexao.close()
