def validar_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    return True


import re

def validar_email(email):
    
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(regex, email):
        return True
    return False


usuarios = []


while True:
    print("\nMENU:")
    print("1=Incluir usuário")
    print("2=Excluir usuário")
    print("3=Consultar usuário")
    print("4=Alterar usuário")
    print("5=Listar todos os usuários cadastrados")
    print("9=Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        
        print("\nIncluir usuário:")

        nome = input("Nome completo: ")
        cpf = input("CPF (apenas números): ")
        telefone = input("Telefone: ")
        email = input("E-mail: ")
        data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")

        
        if not validar_cpf(cpf):
            print("CPF inválido. Deve conter exatamente 11 dígitos numéricos.")
            continue
        
        if not validar_email(email):
            print("E-mail inválido. Verifique o formato.")
            continue

        
        usuario = {
            'Nome': nome,
            'CPF': cpf,
            'Telefone': telefone,
            'Email': email,
            'Data de Nascimento': data_nascimento
        }

        
        usuarios.append(usuario)
        print("Usuário incluído com sucesso.")

    elif opcao == '2':
       
        print("\nExcluir usuário:")
        cpf_excluir = input("Digite o CPF do usuário a ser excluído: ")

      
        encontrado = False
        for usuario in usuarios:
            if usuario['CPF'] == cpf_excluir:
                usuarios.remove(usuario)
                encontrado = True
                print(f"Usuário com CPF {cpf_excluir} excluído.")
                break
        
        if not encontrado:
            print(f"Usuário com CPF {cpf_excluir} não encontrado.")

    elif opcao == '3':
       
        print("\nConsultar usuário:")
        cpf_consultar = input("Digite o CPF do usuário a ser consultado: ")

        
        encontrado = False
        for usuario in usuarios:
            if usuario['CPF'] == cpf_consultar:
                print(f"\nDados do usuário com CPF {cpf_consultar}:")
                for chave, valor in usuario.items():
                    print(f"{chave}: {valor}")
                encontrado = True
                break
        
        if not encontrado:
            print(f"Usuário com CPF {cpf_consultar} não encontrado.")

    elif opcao == '4':
        
        print("\nAlterar usuário:")
        cpf_alterar = input("Digite o CPF do usuário a ser alterado: ")

       
        encontrado = False
        for usuario in usuarios:
            if usuario['CPF'] == cpf_alterar:
                print("Digite os novos dados do usuário:")
                usuario['Nome'] = input("Novo nome completo: ")
                usuario['Telefone'] = input("Novo telefone: ")
                usuario['Email'] = input("Novo e-mail: ")
                usuario['Data de Nascimento'] = input("Nova data de nascimento (dd/mm/aaaa): ")

                
                if not validar_email(usuario['Email']):
                    print("E-mail inválido. Verifique o formato.")
                    continue

                print(f"Dados do usuário com CPF {cpf_alterar} alterados com sucesso.")
                encontrado = True
                break
        
        if not encontrado:
            print(f"Usuário com CPF {cpf_alterar} não encontrado.")

    elif opcao == '5':
       
        print("\nLista de todos os usuários cadastrados:")
        if len(usuarios) == 0:
            print("Nenhum usuário cadastrado.")
        else:
            for i, usuario in enumerate(usuarios, start=1):
                print(f"\nUsuário {i}:")
                for chave, valor in usuario.items():
                    print(f"{chave}: {valor}")

    elif opcao == '9':
        
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida. Por favor, digite uma opção válida.")

print("Programa encerrado.")