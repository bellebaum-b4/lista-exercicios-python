votos = []

while True:
    voto = int(input("Digite seu voto (1 - A, 2 - B, 3 - C, 9 - Encerrar): "))

    if voto == 9:
        break

    votos.append(voto)

votos_a = 0
votos_b = 0
votos_c = 0
votos_invalidos = 0

for voto in votos:
    if voto == 1:
        votos_a += 1
    elif voto == 2:
        votos_b += 1
    elif voto == 3:
        votos_c += 1
    else:
        votos_invalidos += 1

total_votos = len(votos)

if total_votos > 0:
    porcentagem_a = (votos_a / total_votos) * 100
    porcentagem_b = (votos_b / total_votos) * 100
    porcentagem_c = (votos_c / total_votos) * 100
else:
    porcentagem_a = 0
    porcentagem_b = 0
    porcentagem_c = 0

if votos_a >= votos_b and votos_a >= votos_c:
    mais_votado = "Candidato A"
elif votos_b >= votos_a and votos_b >= votos_c:
    mais_votado = "Candidato B"
else:
    mais_votado = "Candidato C"

print("\n--- RESULTADO DA VOTAÇÃO ---")
print("Total de votos:", total_votos)
print("Votos do candidato A:", votos_a)
print("Votos do candidato B:", votos_b)
print("Votos do candidato C:", votos_c)
print("Votos inválidos:", votos_invalidos)
print("Porcentagem A:", round(porcentagem_a, 2), "%")
print("Porcentagem B:", round(porcentagem_b, 2), "%")
print("Porcentagem C:", round(porcentagem_c, 2), "%")
print("Mais votado:", mais_votado)