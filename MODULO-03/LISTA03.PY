"""
Atividade 1

"""


n = int(input("Informe o número: "))

z = n%2

if z == 0:
    print("Número é par")

else:
   print("Número é ímpar") 

  
"""
Atividade 2

"""

n1 = int(input("Informe o número: "))
n2 = int(input("Informe o número: "))
n3 = int(input("Informe o número: "))
n4 = int(input("Informe o número: "))

media = (n1+n2+n3+n4)/4

if 60 <= media:
    print("Aluno aprovado" , media)

else:
    print("Aluno Reprovado" , media)



"""
Atividade 3

"""
salario = int(input("Informe o  valor do salario: "))
reajuste = int(input("Informe o valor do reajuste: "))

valorReajuste = ( salario * (reajuste/100))

valorFinal2 = salario + valorReajuste

if valorFinal2 >= 2000:
    print("Novo salário é Acima da média nacional brasileira" , valorFinal2)

else:
    print("Novo salário é Abaixo da média nacional brasileira", valorFinal2)

"""
Atividade 4

"""

nome = str(input("Digite nome do produto"))
preço = int(input("Digite preço do produto"))


if preço <= 100:

    desconto1 = ( preço * (25/100))

    valor1 = preço - desconto1

    print("Desconto de 25%" , nome , valor1)

else:
    desconto2 = ( preço * (15/100))

    valor2 = preço - desconto2

    print("Desconto de 25%" , nome , valor2)
    
"""
Atividade 5

"""

positivos = 0
resposta = input("Telefonou para a vítima? (S ou N): ")
if resposta.upper() == "S":
    positivos += 1
resposta = input("Esteve no local do crime? (S ou N): ")
if resposta.upper() == "S":
    positivos += 1
resposta = input("Mora perto da vítima? (S ou N): ")
if resposta.upper() == "S":
    positivos += 1
resposta = input("Devia para a vítima? (S ou N): ")
if resposta.upper() == "S":
    positivos += 1
resposta = input("Já trabalhou com a vítima? (S ou N): ")
if resposta.upper() == "S":
    positivos += 1

if positivos < 2:
    print("Inocente")
elif positivos == 2:
    print("Suspeita")
elif positivos < 5:
    print("Cúmplice")
else:
    print("Assassino")