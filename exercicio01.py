matricula = input("Digite sua matrícula: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
if media < 4:
    situacao = "Reprovado"
elif media < 6:
    situacao = "Recuperação"
elif media < 8:
    situacao = "Aprovado"
else:
    situacao = "Aprovado com excelente desempenho"
ultimo_digito = int(matricula[-1])
if ultimo_digito % 2 == 0:
    perfil = "Perfil A"
else:
    perfil = "Perfil B"

print("\n--- RESULTADO ---")
print("Matrícula:", matricula)
print("Nota 1:", nota1)
print("Nota 2:", nota2)
print("Nota 3:", nota3)
print("Média:", round(media, 2))
print("Situação:", situacao)
print("Perfil:", perfil)