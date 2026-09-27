from desafio_1 import desafio_1


def desafio_2(expressao):

    operadores = []

    saida = []

    expressao = expressao.replace("(", " ( ").replace(")", " ) ")
    tokens = expressao.split()

    for token in tokens:

        if token.isdigit():

            saida.append(token)

        elif token == "(":

            operadores.append(token)

        elif token == ")":

            while operadores and operadores[-1] != "(":
                saida.append(operadores.pop())

            if operadores:
                operadores.pop()

        elif token in ["+", "-", "*", "/", "^"]:

            while operadores and operadores[-1] != "(":

                topo = operadores[-1]

                if topo in ["+", "-"]:
                    prioridade_topo = 1

                elif topo in ["*", "/"]:
                    prioridade_topo = 2

                elif topo == "^":
                    prioridade_topo = 3

                if token in ["+", "-"]:
                    prioridade_atual = 1

                elif token in ["*", "/"]:
                    prioridade_atual = 2

                elif token == "^":
                    prioridade_atual = 3

                if token == "^":

                    if prioridade_topo > prioridade_atual:
                        saida.append(operadores.pop())
                    else:
                        break

                else:

                    if prioridade_topo >= prioridade_atual:
                        saida.append(operadores.pop())
                    else:
                        break

            operadores.append(token)

    while operadores:
        saida.append(operadores.pop())

    pos_fixa = " ".join(saida)
    pos_fixa_virgula = pos_fixa.replace(" ", ",")

    return desafio_1(pos_fixa_virgula)