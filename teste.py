# -*- coding = utf8 -*-
usuario = "tripulante"
chamada = "Essa mãozinha é para trocar a senha do usuário do reservas!"
# todas as perguntas começarão com q

print("Olá, "+usuario)
print(chamada)
q_usuario = input("Digite o e-mail do usuário que deseja a troca: ")
q_usuario = q_usuario.lower()
busca_arroba = q_usuario.find("@")

if busca_arroba == -1:
    print("Email inválido")
else:
    print(q_usuario, "está sendo procurado...")