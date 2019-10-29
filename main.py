# coding=utf-8
# variáveis globais
usuario = "tripulante"
chamada_1 = "Essa mãozada é para trocar a senha do usuário do reservas!"
chamada_2 = "Essa mãozada é para cadastrar um novo executivo na extranet!"
chamada_menu = "Digite o número da mãozada que você precisa: "
menu = {'1': 'Trocar a senha do usuário da Extranet', '2': 'Cadastrar Executivo na Extranet'}


print("Olá, " + usuario)
print(chamada_menu)

for chave in menu:
    print(" " + chave + " : " + menu[chave])

escolha = input()
print(escolha)

if escolha == "1":
    print(chamada_1)
    q_usuario = input("Digite o e-mail do usuário que deseja a troca: ")
    q_usuario = q_usuario.lower()
    busca_arroba = q_usuario.find("@")
    if busca_arroba == -1:
        print("Email inválido")
    else:
        print(q_usuario, "está sendo procurado...")
else:
    print(chamada_2)
    q_email = input("Digite o email do novo executivo:")
    q_nome_exec = input("Digite o nome e o sobrenome do executivo:")
    print(q_nome_exec, "está sendo adicionado...")
