def desafio_1(expressao):
    numero = []
    exp = expressao.split(",")
    for token in exp:
        if token.isdigit():
            numero.append(float(token))
        else:

            # Definir a e b
            b = numero.pop()
            a = numero.pop()

            # calculadora
            if token == "+":
                resultado = a + b
            elif token == "-":
                resultado = a - b
            elif token == "*":
                resultado = a * b
            elif token == "/":
                resultado = a / b
            elif token == "^":
                resultado = a ** b

            numero.append(resultado)

    resultado_final = numero.pop()
    return resultado_final