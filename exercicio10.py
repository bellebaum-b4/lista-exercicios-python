matriculas = []
nomes = []
notas1 = []
notas2 = []
notas3 = []

while True:
    print("\n--- SISTEMA DE ANÁLISE DE ALUNOS ---")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Consultar aluno")
    print("4 - Estatísticas da turma")
    print("5 - Alunos aprovados")
    print("6 - Alunos reprovados")
    print("7 - Aluno com maior média")
    print("0 - Encerrar")

    opcao = input("Digite uma opção: ")

    # CADASTRAR ALUNO
    if opcao == "1":
        matricula = input("Digite a matrícula: ")

        if matricula in matriculas:
            print("Essa matrícula já está cadastrada.")
        else:
            nome = input("Digite o nome do aluno: ")

            nota1 = float(input("Digite a primeira nota: "))
            while nota1 < 0 or nota1 > 10:
                print("Nota inválida! Digite uma nota entre 0 e 10.")
                nota1 = float(input("Digite a primeira nota: "))

            nota2 = float(input("Digite a segunda nota: "))
            while nota2 < 0 or nota2 > 10:
                print("Nota inválida! Digite uma nota entre 0 e 10.")
                nota2 = float(input("Digite a segunda nota: "))

            nota3 = float(input("Digite a terceira nota: "))
            while nota3 < 0 or nota3 > 10:
                print("Nota inválida! Digite uma nota entre 0 e 10.")
                nota3 = float(input("Digite a terceira nota: "))

            matriculas.append(matricula)
            nomes.append(nome)
            notas1.append(nota1)
            notas2.append(nota2)
            notas3.append(nota3)

            print("Aluno cadastrado com sucesso!")

    # LISTAR ALUNOS
    elif opcao == "2":
        if len(matriculas) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            print("\n--- ALUNOS CADASTRADOS ---")

            for i in range(len(matriculas)):
                media = (notas1[i] + notas2[i] + notas3[i]) / 3

                if media >= 7:
                    situacao = "Aprovado"
                elif media >= 5:
                    situacao = "Recuperação"
                else:
                    situacao = "Reprovado"

                print("\nMatrícula:", matriculas[i])
                print("Nome:", nomes[i])
                print("Média:", round(media, 2))
                print("Situação:", situacao)

    # CONSULTAR ALUNO
    elif opcao == "3":
        if len(matriculas) == 0:
            print("Não há alunos cadastrados.")
        else:
            matricula = input("Digite a matrícula para consultar: ")

            if matricula in matriculas:
                posicao = matriculas.index(matricula)

                media = (
                    notas1[posicao]
                    + notas2[posicao]
                    + notas3[posicao]
                ) / 3

                print("\n--- ALUNO ENCONTRADO ---")
                print("Matrícula:", matriculas[posicao])
                print("Nome:", nomes[posicao])
                print("Nota 1:", notas1[posicao])
                print("Nota 2:", notas2[posicao])
                print("Nota 3:", notas3[posicao])
                print("Média:", round(media, 2))
            else:
                print("Aluno não encontrado.")

    # ESTATÍSTICAS
    elif opcao == "4":
        if len(matriculas) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            medias = []

            for i in range(len(matriculas)):
                media = (
                    notas1[i]
                    + notas2[i]
                    + notas3[i]
                ) / 3

                medias.append(media)

            aprovados = 0
            recuperacao = 0
            reprovados = 0

            for media in medias:
                if media >= 7:
                    aprovados += 1
                elif media >= 5:
                    recuperacao += 1
                else:
                    reprovados += 1

            media_geral = sum(medias) / len(medias)

            print("\n--- ESTATÍSTICAS DA TURMA ---")
            print("Quantidade de alunos:", len(matriculas))
            print("Média geral:", round(media_geral, 2))
            print("Maior média:", round(max(medias), 2))
            print("Menor média:", round(min(medias), 2))
            print("Quantidade de aprovados:", aprovados)
            print("Quantidade em recuperação:", recuperacao)
            print("Quantidade de reprovados:", reprovados)

    # ALUNOS APROVADOS
    elif opcao == "5":
        if len(matriculas) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            encontrou = False

            print("\n--- ALUNOS APROVADOS ---")

            for i in range(len(matriculas)):
                media = (
                    notas1[i]
                    + notas2[i]
                    + notas3[i]
                ) / 3

                if media >= 7:
                    encontrou = True
                    print("\nMatrícula:", matriculas[i])
                    print("Nome:", nomes[i])
                    print("Média:", round(media, 2))

            if not encontrou:
                print("Nenhum aluno aprovado.")

    # ALUNOS REPROVADOS
    elif opcao == "6":
        if len(matriculas) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            encontrou = False

            print("\n--- ALUNOS REPROVADOS ---")

            for i in range(len(matriculas)):
                media = (
                    notas1[i]
                    + notas2[i]
                    + notas3[i]
                ) / 3

                if media < 5:
                    encontrou = True
                    print("\nMatrícula:", matriculas[i])
                    print("Nome:", nomes[i])
                    print("Média:", round(media, 2))

            if not encontrou:
                print("Nenhum aluno reprovado.")

    # MAIOR MÉDIA
    elif opcao == "7":
        if len(matriculas) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            medias = []

            for i in range(len(matriculas)):
                media = (
                    notas1[i]
                    + notas2[i]
                    + notas3[i]
                ) / 3

                medias.append(media)

            maior_media = max(medias)

            print("\n--- ALUNO(S) COM MAIOR MÉDIA ---")

            for i in range(len(matriculas)):
                if medias[i] == maior_media:
                    print("\nMatrícula:", matriculas[i])
                    print("Nome:", nomes[i])
                    print("Nota 1:", notas1[i])
                    print("Nota 2:", notas2[i])
                    print("Nota 3:", notas3[i])
                    print("Média:", round(medias[i], 2))

    # ENCERRAR
    elif opcao == "0":
        print("Programa encerrado.")
        break

    # OPÇÃO INVÁLIDA
    else:
        print("Opção inválida.")