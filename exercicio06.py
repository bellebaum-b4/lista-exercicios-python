produtos = ["arroz", "feijão", "macarrão", "cafe", "acucar"]
quantidades = [15, 8, 20, 5, 12]

while True:
    print("\n--- CONTROLE DE ESTOQUE ---")
    print("1 - Listar produtos")
    print("2 - Consultar estoque")
    print("3 - Entrada de produtos")
    print("4 - Saída de produtos")
    print("5 - Produtos com estoque baixo")
    print("0 - Sair")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        print("\n--- PRODUTOS ---")

        for i in range(len(produtos)):
            print(produtos[i], "-", quantidades[i], "unidades")

    elif opcao == "2":
        produto = input("Digite o nome do produto: ").strip().lower()

        if produto in produtos:
            posicao = produtos.index(produto)
            print("Quantidade em estoque:", quantidades[posicao])
        else:
            print("Produto não encontrado.")

    elif opcao == "3":
        produto = input("Digite o nome do produto: ").strip().lower()
        quantidade = int(input("Digite a quantidade recebida: "))

        if quantidade < 0:
            print("A quantidade não pode ser negativa.")
        elif produto in produtos:
            posicao = produtos.index(produto)
            quantidades[posicao] += quantidade
            print("Entrada registrada com sucesso.")
        else:
            print("Produto não encontrado.")

    elif opcao == "4":
        produto = input("Digite o nome do produto: ").strip().lower()
        quantidade = int(input("Digite a quantidade retirada: "))

        if quantidade < 0:
            print("A quantidade não pode ser negativa.")
        elif produto in produtos:
            posicao = produtos.index(produto)

            if quantidade <= quantidades[posicao]:
                quantidades[posicao] -= quantidade
                print("Saída registrada com sucesso.")
            else:
                print("Quantidade insuficiente em estoque.")
        else:
            print("Produto não encontrado.")

    elif opcao == "5":
        print("\n--- ESTOQUE BAIXO ---")

        encontrou = False

        for i in range(len(produtos)):
            if quantidades[i] < 10:
                print(produtos[i], "-", quantidades[i], "unidades")
                encontrou = True

        if not encontrou:
            print("Nenhum produto possui estoque baixo.")

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")