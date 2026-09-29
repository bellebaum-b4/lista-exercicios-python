nome = input("Digite o nome do aluno: ")
matricula = input("Digite a matrícula: ")

notas = []

for i in range(5):
    nota = float(input(f"Digite a nota {i + 1}: "))

    while nota < 0 or nota > 10:
        print("Nota inválida! Digite uma nota entre 0 e 10.")
        nota = float(input(f"Digite a nota {i + 1}: "))

    notas.append(nota)

media = sum(notas) / 5

ultimo_digito = int(matricula[-1])

if ultimo_digito <= 3:
    bonus = 0.5
elif ultimo_digito <= 6:
    bonus = 1.0
else:
    bonus = 1.5

nota_final = media + bonus

if nota_final > 10:
    nota_final = 10

if nota_final < 5:
    classificacao = "Reprovado"
elif nota_final < 7:
    classificacao = "Recuperação"
elif nota_final <= 9:
    classificacao = "Aprovado"
else:
    classificacao = "Excelente"

maior_nota = max(notas)
menor_nota = min(notas)

acima_media = 0
abaixo_media = 0

for nota in notas:
    if nota > media:
        acima_media += 1
    elif nota < media:
        abaixo_media += 1

print("\n--- RESULTADO ---")
print("Nome:", nome)
print("Matrícula:", matricula)
print("Notas:", notas)
print("Média original:", round(media, 2))
print("Bônus:", bonus)
print("Nota final:", round(nota_final, 2))
print("Classificação:", classificacao)
print("Maior nota:", maior_nota)
print("Menor nota:", menor_nota)
print("Notas acima da média:", acima_media)
print("Notas abaixo da média:", abaixo_media)