from desafio1 import Pilha

PRECEDENCIA = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
ASSOC_DIREITA = {"^"}


def tokenizar(expressao):
    tokens = []
    i = 0
    n = len(expressao)

    while i < n:
        c = expressao[i]

        if c.isspace():
            i += 1
        elif c.isdigit() or c == ".":
            j = i
            while j < n and (expressao[j].isdigit() or expressao[j] == "."):
                j += 1
            tokens.append(expressao[i:j])
            i = j
        elif c in "+-*/^()":
            tokens.append(c)
            i += 1
        else:
            return tokens, "erro: caractere invalido"

    return tokens, None


def converter(tokens):
    operadores = Pilha()
    saida = []
    trace = []

    for token in tokens:
        if token == "(":
            operadores.empilhar(token)
        elif token == ")":
            while not operadores.vazia() and operadores.topo() != "(":
                saida.append(operadores.desempilhar())

            if operadores.vazia():
                return trace, None, "erro: parentese fechado sem abertura"

            operadores.desempilhar()
        elif token in PRECEDENCIA:
            while not operadores.vazia() and operadores.topo() != "(":
                topo = operadores.topo()

                if token in ASSOC_DIREITA:
                    if PRECEDENCIA[topo] > PRECEDENCIA[token]:
                        saida.append(operadores.desempilhar())
                    else:
                        break
                else:
                    if PRECEDENCIA[topo] >= PRECEDENCIA[token]:
                        saida.append(operadores.desempilhar())
                    else:
                        break

            operadores.empilhar(token)
        else:
            saida.append(token)

        trace.append((token, operadores.para_lista(), list(saida)))

    while not operadores.vazia():
        if operadores.topo() == "(":
            return trace, None, "erro: parentese aberto sem fechamento"
        saida.append(operadores.desempilhar())

    trace.append(("(fim)", operadores.para_lista(), list(saida)))

    return trace, saida, None