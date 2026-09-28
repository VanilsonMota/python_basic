n1 = input("Digite um numero:")
n2 = input("Digite outro numero:")

operacao = input("Digite a operação desejada (+, -, *, /): ")

if operacao == "+":
    print(f"O resultado da soma é: {float(n1) + float(n2)}")

elif operacao == "-":
    print(f"O resultado da subtração é: {float(n1) - float(n2)}")

elif operacao == "*":
    print(f"O resultado da multiplicação é: {float(n1) * float(n2)}")

elif operacao == "/":
    if float(n2) == 0:
        print("Erro: Divisão por zero não é permitida.")
    else:
        print(f"O resultado da divisão é: {float(n1) / float(n2)}")

else:
    print("Operação inválida. Por favor, escolha entre +, -, * ou /.")

