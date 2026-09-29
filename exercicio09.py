saldo = float(input("Digite o saldo inicial da conta: "))

extrato = []

while True:
    print("\n--- CAIXA ELETRÔNICO ---")
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Extrato")
    print("0 - Sair")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        print("\nSaldo atual: R$", round(saldo, 2))

    elif opcao == "2":
        valor = float(input("Digite o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f}")
            print("Depósito realizado com sucesso.")
        else:
            print("O valor do depósito deve ser maior que zero.")

    elif opcao == "3":
        valor = float(input("Digite o valor do saque: R$ "))

        if valor <= 0:
            print("O valor do saque deve ser maior que zero.")
        elif valor > saldo:
            print("Saldo insuficiente.")
        else:
            saldo -= valor
            extrato.append(f"Saque: R$ {valor:.2f}")
            print("Saque realizado com sucesso.")

    elif opcao == "4":
        print("\n--- EXTRATO ---")

        if len(extrato) == 0:
            print("Nenhuma operação realizada.")
        else:
            for operacao in extrato:
                print(operacao)

        quantidade_depositos = 0
        quantidade_saques = 0
        total_depositado = 0
        total_sacado = 0

        for operacao in extrato:
            if operacao.startswith("Depósito"):
                quantidade_depositos += 1
                valor = float(operacao.split("R$ ")[1].replace(",", "."))
                total_depositado += valor

            elif operacao.startswith("Saque"):
                quantidade_saques += 1
                valor = float(operacao.split("R$ ")[1].replace(",", "."))
                total_sacado += valor

        print("\n--- ESTATÍSTICAS ---")
        print("Quantidade de depósitos:", quantidade_depositos)
        print("Quantidade de saques:", quantidade_saques)
        print("Total depositado: R$", round(total_depositado, 2))
        print("Total sacado: R$", round(total_sacado, 2))
        print("Saldo atual: R$", round(saldo, 2))

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")