lista = []

while True:
    print("\n--- MENU ---")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Consultar item")
    print("4 - Alterar item")
    print("5 - Listar itens")
    print("0 - Encerrar")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        if len(lista) >= 12:
            print("A lista já possui 12 itens.")
        else:
            item = input("Digite o item: ").strip().lower()

            if item == "":
                print("O item não pode ser vazio.")
            elif item in lista:
                print("Esse item já está na lista.")
            else:
                lista.append(item)
                print("Item adicionado com sucesso.")

    elif opcao == "2":
        item = input("Digite o item que deseja remover: ").strip().lower()

        if item in lista:
            lista.remove(item)
            print("Item removido com sucesso.")
        else:
            print("Item não encontrado.")

    elif opcao == "3":
        item = input("Digite o item que deseja consultar: ").strip().lower()

        if item in lista:
            print("O item está na lista.")
        else:
            print("O item não está na lista.")

    elif opcao == "4":
        item = input("Digite o item que deseja alterar: ").strip().lower()

        if item in lista:
            novo_item = input("Digite o novo item: ").strip().lower()

            if novo_item == "":
                print("O novo item não pode ser vazio.")
            elif novo_item in lista:
                print("Esse item já existe na lista.")
            else:
                posicao = lista.index(item)
                lista[posicao] = novo_item
                print("Item alterado com sucesso.")
        else:
            print("Item não encontrado.")

    elif opcao == "5":
        if len(lista) == 0:
            print("A lista está vazia.")
        else:
            print("\n--- LISTA DE COMPRAS ---")

            for item in lista:
                print("-", item)

    elif opcao == "0":
        break

    else:
        print("Opção inválida.")

print("\n--- FINAL ---")
print("Quantidade de itens:", len(lista))

if len(lista) > 0:
    print("Lista final:")

    for item in lista:
        print("-", item)
else:
    print("A lista está vazia.")