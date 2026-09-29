matriculas = []
acertos = []

while True:
    matricula = input("Digite a matrícula (0 para encerrar): ")

    if matricula == "0":
        break

    quantidade = int(input("Digite a quantidade de acertos (0 a 10): "))

    if quantidade < 0 or quantidade > 10:
        print("Quantidade de acertos inválida. Digite um valor de 0 a 10.")
    else:
        matriculas.append(matricula)
        acertos.append(quantidade)

if len(matriculas) > 0:

    media = sum(acertos) / len(acertos)
    maior = max(acertos)
    menor = min(acertos)

    aprovados = 0
    recuperacao = 0
    reprovados = 0

    for acerto in acertos:
        if acerto >= 8:
            aprovados += 1
        elif acerto >= 6:
            recuperacao += 1
        else:
            reprovados += 1

    print("\n--- RESULTADO DA TURMA ---")
    print("Média de acertos:", round(media, 2))
    print("Maior quantidade de acertos:", maior)
    print("Menor quantidade de acertos:", menor)
    print("Alunos aprovados:", aprovados)
    print("Alunos em recuperação:", recuperacao)
    print("Alunos reprovados:", reprovados)

    print("\n--- ALUNOS COM MAIOR QUANTIDADE DE ACERTOS ---")

    for i in range(len(acertos)):
        if acertos[i] == maior:
            print("Matrícula:", matriculas[i])
            print("Acertos:", acertos[i])