# Nome: Rafael Peixoto Gonçalves  Matrícula: 2025010288
# Nome: Antonio Everardo Liveira LIma Filho  Matrícula: 2025010334
# Nome: Cid Xavier Pacheco Araujo  Matrícula: 2025010285

from desafio1 import Pilha

PRIORIDADE = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
DIREITA = {"^"}  # operadores resolvidos da direita para a esquerda


def tokenizar(expressao):
    tokens = []
    inicio = 0
    tamanho = len(expressao)

    while inicio < tamanho:
        caractere = expressao[inicio]

        # espaço: ignora
        if caractere.isspace():
            inicio += 1

        # número: pode ter vários dígitos (12, 2.5)
        elif caractere.isdigit() or caractere == ".":
            fim = inicio
            while fim < tamanho and (expressao[fim].isdigit() or expressao[fim] == "."):
                fim += 1

            numero = expressao[inicio:fim]
            try:
                float(numero)  # recusa "1.2.3" e "."
            except ValueError:
                return None, "erro: caractere invalido"

            tokens.append(numero)
            inicio = fim

        # operador ou parêntese
        elif caractere in "+-*/^()":
            tokens.append(caractere)
            inicio += 1

        else:
            return None, "erro: caractere invalido"

    return tokens, None


def converter(expressao):
    # recebe a string e devolve: trace, posfixa (string), erro
    tokens, erro = tokenizar(expressao)
    if erro:
        return [], None, erro

    operadores = Pilha()
    saida = []
    trace = []

    for token in tokens:

        # abre parêntese: só empilha
        if token == "(":
            operadores.empilhar(token)

        # fecha parêntese: despeja operadores até achar o "("
        elif token == ")":
            while not operadores.vazia() and operadores.topo() != "(":
                saida.append(operadores.desempilhar())

            if operadores.vazia():
                return trace, None, "erro: parentese fechado sem abertura"

            operadores.desempilhar()  # descarta o "("

        # operador: tira da pilha quem deve sair antes
        elif token in PRIORIDADE:
            while not operadores.vazia() and operadores.topo() != "(":
                operador_topo = operadores.topo()

                if token in DIREITA:
                    # ^ : o topo só sai se for estritamente mais forte
                    if PRIORIDADE[operador_topo] > PRIORIDADE[token]:
                        saida.append(operadores.desempilhar())
                    else:
                        break
                else:
                    # outros: o topo sai se for mais forte ou igual
                    if PRIORIDADE[operador_topo] >= PRIORIDADE[token]:
                        saida.append(operadores.desempilhar())
                    else:
                        break

            operadores.empilhar(token)

        # número: vai direto para a saída
        else:
            saida.append(token)

        # foto do momento (list(saida) é uma cópia)
        trace.append((token, operadores.visualizar(), list(saida)))

    # fim: despeja o que sobrou na pilha
    while not operadores.vazia():
        if operadores.topo() == "(":
            return trace, None, "erro: parentese aberto sem fechamento"
        saida.append(operadores.desempilhar())

    trace.append(("(fim)", operadores.visualizar(), list(saida)))

    return trace, " ".join(saida), None