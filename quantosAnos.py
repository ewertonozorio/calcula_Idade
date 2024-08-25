#What is your name and your age?

anoAtual = 2024
nome = str(input("Informe sue nome completo: "))
anoIdade = int(input("Informe o ano em que você nasceu com quatro digitos: "))

while ((anoIdade < 1922) or (anoIdade > 2023)):
    anoIdade = int(input("Informe o ano em que você nasceu com quatro digitos: "))
    break

idade = anoAtual-anoIdade

print (f"Seu nome completo é: {nome} e você tem {idade} anos de vida")


