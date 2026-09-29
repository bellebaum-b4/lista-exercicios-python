idades = []

while True:
    idade = int(input("Digite uma idade (0 para encerrar): "))

    if idade == 0:
        break

    if idade < 0:
        print("Idade inválida! Digite uma idade maior ou igual a 0.")
    else:
        idades.append(idade)

if len(idades) > 0:
    total = len(idades)
    maior = max(idades)
    menor = min(idades)
    media = sum(idades) / total

    menores_18 = 0
    maiores_ou_iguais_18 = 0
    maiores_50 = 0

    criancas = 0
    adolescentes = 0
    adultos = 0
    idosos = 0

    for idade in idades:

        if idade < 18:
            menores_18 += 1
        else:
            maiores_ou_iguais_18 += 1

        if idade > 50:
            maiores_50 += 1

        if idade <= 12:
            criancas += 1
        elif idade <= 17:
            adolescentes += 1
        elif idade <= 59:
            adultos += 1
        else:
            idosos += 1

    print("\n--- RESULTADO ---")
    print("Total de idades:", total)
    print("Maior idade:", maior)
    print("Menor idade:", menor)
    print("Média das idades:", round(media, 2))
    print("Menores de 18 anos:", menores_18)
    print("Maiores ou iguais a 18 anos:", maiores_ou_iguais_18)
    print("Maiores de 50 anos:", maiores_50)

    print("\n--- CLASSIFICAÇÃO ---")
    print("Crianças:", criancas)
    print("Adolescentes:", adolescentes)
    print("Adultos:", adultos)
    print("Idosos:", idosos)

else:
    print("Nenhuma idade foi cadastrada.")