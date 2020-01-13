def check_email(email):
    busca_arroba = email.find("@")
    while busca_arroba == -1:
        print("Email inválido")
        break

