# Captura os 11 dígitos do CPF
cpf = input("Digite os 11 dígitos do CPF: ")

# Verifica se tem 11 dígitos e se são todos números
if len(cpf) != 11 or not cpf.isdigit():
    print("CPF inválido! O CPF deve conter exatamente 11 dígitos numéricos.")
else:
    # Converte cada dígito para inteiro e armazena em uma lista
    digitos = [int(digito) for digito in cpf]

    # Cálculo do primeiro dígito verificador
    soma = 0
    peso = 10
    for digito in digitos[:9]:  # Usa apenas os 9 primeiros dígitos
        soma += digito * peso
        peso -= 1

    resto = (soma * 10) % 11
    primeiro_digito = 0 if resto > 9 else resto

    # Cálculo do segundo dígito verificador
    soma = 0
    peso = 11
    for digito in digitos[:10]:  # Usa os 9 primeiros dígitos + o primeiro dígito verificador
        soma += digito * peso
        peso -= 1

    resto = (soma * 10) % 11
    segundo_digito = 0 if resto > 9 else resto

    # Verifica se os dígitos verificadores calculados são iguais aos informados
    if primeiro_digito == digitos[9] and segundo_digito == digitos[10]:
        print("CPF válido!")
    else:
        print("CPF inválido!")