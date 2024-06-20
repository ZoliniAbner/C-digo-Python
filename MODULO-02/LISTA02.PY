""" 
1) Faça um programa em Python que receba três números e calcule a soma 
deles 
"""


n1 = int(input("Informe um número: "))
n2 = int(input("Informe um número: "))
n3 = int(input("Informe um número: "))

soma = n1 + n2 + n3

print("Soma dos números é: ", soma)


"""
2) Faça um programa em Python que leia dois números inteiros e imprima a 
média aritmética entre esses dois valores. 

"""


n1 = int(input("Informe um número: "))
n2 = int(input("Informe um número: "))

media = (n1 + n2)/2

print("Média dos números é: ", media)



"""
3) Faça um programa em Python que calcule a área do triângulo e apresente o 
resultado.

"""

base = int(input("Informe à base do triângulo: "))
altura = int(input("Informe à altura do triângulo: "))

area = (base * altura)/2

print("Área do triângulo é igual: ", area)


"""

4) Faça um programa em Python que receba o valor de uma conta e um 
percentual de desconto. Calcule o novo valor da conta ao ser aplicado, o 
percentual de desconto e escreva o resultado obtido. 

"""

saldo = int(input("Informe o  valor da conta: "))
desconto = int(input("Informe o valor do desconto: "))

valorDesconto = ( saldo * (desconto/100))

valorFinal1 = saldo - valorDesconto

print("Valor atual ", valorFinal1 )

"""

5) Faça um programa em Python que receba o valor de um salário e um 
percentual de reajuste. Calcule o valor do novo salário reajustado. 

"""

salario = int(input("Informe o  valor do salario: "))
reajuste = int(input("Informe o valor do reajuste: "))

valorReajuste = ( salario * (reajuste/100))

valorFinal2 = salario + valorReajuste

print("Valor atual do salário é", valorFinal2)

"""

6) Faça um programa em Python que leia o número de eleitores de um 
município, o número de votos em branco, nulos e válidos. Calcular e 
escrever o percentual que cada um representa em relação ao total de 
eleitores, isto é, o percentual de votos brancos, percentual de votos nulos e o 
percentual de votos válidos. 

"""

eleitor = int(input("Informe número de voltos dos eleitores"))
votosBranco = int(input("Informe número de voltos brancos "))
votosNulos = int(input("Informe número de voltos nulos "))
votosValidos = int(input("Informe número de voltos válidos "))

percentualVotosBrancos = (votosBranco * 100)/eleitor

percentualVotosNulos = (votosNulos * 100)/eleitor

percentualVotosValidos = (votosValidos * 100)/eleitor

print("Porcentual de votos brancos é: " , percentualVotosBrancos , " %")

print("Porcentual de votos nulos é: " , percentualVotosNulos , " %")

print("Porcentual de votos válidos é: " , percentualVotosValidos , " %")