idade = int(input("Digite sua idade: "))

autorizacao = input("Possui autorização ou é admin? (sim/admin/não): ")

if idade >= 18 and autorizacao == "sim" or autorizacao == "admin":

    print("Entra aí fi")

elif idade < 18 and autorizacao == "sim":

    print("Entra aí fi, mas com autorização")

elif idade >= 18 and autorizacao == "não":

    print("Entra aí fi, mas sem autorização")

elif idade < 18 and autorizacao == "não":

    print("Vai embora fi, sem autorização e menor de idade")

else:

    print("Opção inválida")