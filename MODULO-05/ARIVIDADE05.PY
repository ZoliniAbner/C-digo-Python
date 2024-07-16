"""
Atividade 1

1. Considere a string A = "Um elefante incomoda muita gente" Que fatia da
variável A em python corresponde a "elefante incomoda"?

"""

A = "Um elefante incomoda muita gente"

# Encontrar a substring "elefante incomoda"
substring = A[3:21]  # Começa na posição 3 e vai até a posição 21 (exclusivo)

print(substring)


"""
Atividade 2

2. Escreva um programa que solicite uma frase ao usuário e escreva a frase toda em
maiúscula e sem espaços em branco.


"""

frase = input("Digite uma frase: ")

frase_sem_espacos = frase.upper().replace(" ", "")

print("Frase em maiúsculas e sem espaços em branco:")
print(frase_sem_espacos)


"""
Atividade 3

3. Faça um programa que leia um nome e imprima somente as 4 primeiras letras do
nome. Em seguida, imprima as 4 últimas letras do nome.


"""
nome = input("Digite um nome: ")

primeiras_letras = nome[:4]
print("As 4 primeiras letras do nome:", primeiras_letras)

ultimas_letras = nome[-4:]
print("As 4 últimas letras do nome:", ultimas_letras)

"""
Atividade 4

4. Faça um programa que leia um nome, calcule e imprima a quantidade letras que
tem esse nome.

"""

nome = input("Digite um nome: ")

quantidade_letras = len(nome)

print(f"O nome '{nome}' possui {quantidade_letras} letras.")


"""
Atividade 5

5. Faça um programa que receba uma palavra e a imprima de trás-para-frente

"""

palavra = input("Digite uma palavra: ")

palavra_invertida = palavra[::-1]

print("Palavra de trás para frente:", palavra_invertida)

"""

Atividade 6

6. Faça a um programa que receba do usuário um nome e imprima este mesmo nome
sem as suas vogais.

"""
nome = input("Digite um nome: ")

vogais = "aeiouAEIOU"

nome_sem_vogais = ""

for letra in nome:
    if letra not in vogais:
        nome_sem_vogais += letra

print("Nome sem vogais:", nome_sem_vogais)


"""

Atividade 7

7. Faça um programa que leia um nome e converta todos os caracteres para maiúscula
e, em seguida, converta todos os caracteres para minúscula.

"""

nome = input("Digite um nome: ")

nome_maiusculo = nome.upper()

nome_minusculo = nome.lower()

print(f"Nome em maiúsculas: {nome_maiusculo}")
print(f"Nome em minúsculas: {nome_minusculo}")

"""

Atividade 8

8. Faça um programa que leia um endereço de e-mail informado pelo usuário. Caso o e-
mail informado esteja no padrão correto, ou seja, tenha no mínimo @.com o seu
programa deverá imprimir a mensagem “e-mail informado está correto” e finalizar o
programa, caso contrário deverá imprimir “e-mail inválido” e solicitar que o usuário
informe um novo e-mail válido.

"""
while True:
    email = input("Digite um endereço de e-mail: ")

    if "@" in email and ".com" in email:
        print("E-mail informado está correto.")
        break  # Finaliza o loop, pois o e-mail é válido
    else:
        print("E-mail inválido. O e-mail deve conter pelo menos '@' e '.com'. Tente novamente.")    