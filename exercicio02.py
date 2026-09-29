matricula = input("Digite sua matrícula: ")

if len(matricula) != 8:
    print("Matrícula inválida: deve possuir exatamente 8 dígitos.")
elif not matricula.isdigit():
    print("Matrícula inválida: deve conter somente números.")
elif matricula[0] == "0":
    print("Matrícula inválida: o primeiro dígito não pode ser zero.")
else:
    print("Matrícula válida!")

    primeiro_digito = matricula[0]
    ultimo_digito = matricula[-1]

    print("Primeiro dígito:", primeiro_digito)
    print("Último dígito:", ultimo_digito)

    soma = 0

    for digito in matricula:
        soma += int(digito)

    print("Soma dos dígitos:", soma)

    if soma < 20:
        categoria = "Categoria 1"
    elif soma < 40:
        categoria = "Categoria 2"
    else:
        categoria = "Categoria 3"

    print("Categoria:", categoria)