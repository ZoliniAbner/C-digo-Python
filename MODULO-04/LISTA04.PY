
"""
Atividade 1

1) Escreva um programa para encontrar a soma S = 3 + 6 + 9 +…. + 333.

"""
soma = 0

for x in range(3, 333, 3):
    soma += x
    
print("soma :" , soma)

"""
Atividade 2

2) Escreva um programa que leia 10 notas e informe a média dos alunos.

"""

soma2 = 0

for i in range(10):


 nota = float(input("Informe a nota: "))

 soma2 += nota

media = soma2 / 10

print("Média é: ", media)


"""
Atividade 3

3) Escreva um programa de MENU contendo as opções de (1=Inclusão, 2=Exclusão, 3=Consulta, 4=Relatório e 9=Sair). 
O programa só deve ser finalizado quando o usuário digitar a opção 9=Sair

"""

while True:
    print("\n=== MENU ===")
    print("1 - Inclusão")
    print("2 - Exclusão")
    print("3 - Consulta")
    print("4 - Relatório")
    print("9 - Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        print("Escolheu opção - Inclusão")     
    elif opcao == '2':
        print("Escolheu opção - Exclusão") 
    elif opcao == '3':
        print("Escolheu opção - Exclusão")
    elif opcao == '4':
        print("Escolheu opção - Exclusão")
    elif opcao == '9':
        print("Programa encerrado.")
    break 


"""
Atividade 4 

4) Escreva um programa que leia um número de 1 a 10, e mostre a tabuada desse número, somente a multiplicação.

"""
    

