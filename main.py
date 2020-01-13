# coding=utf-8
import usuarioreservas
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
#print(escolha)

if escolha == "1":
    usuarioreservas.trocar_senha()
else:
    usuarioreservas.adicionar_usuario()
