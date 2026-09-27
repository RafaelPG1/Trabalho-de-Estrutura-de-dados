from desafio1 import fmt, avaliar
from desafio2 import tokenizar, converter


def formatar_lista(lista, formatador=str):
    if not lista:
        return "-"
    return " ".join(formatador(v) for v in lista)


def imprimir_trace_desafio1(trace):
    for token, pilha in trace:
        print(f"{token:<5}| {formatar_lista(pilha, fmt)}")


def imprimir_trace_desafio2(trace):
    for token, pilha, saida in trace:
        print(f"{token:<5}| {formatar_lista(pilha):<11}| {formatar_lista(saida)}")


def processar_pos_fixa(tokens):
    trace, resultado, erro = avaliar(tokens)
    imprimir_trace_desafio1(trace)

    if erro:
        print(erro)
    else:
        print("resultado:", fmt(resultado))


def main():
    expressao = input("Digite a expressão: ")

    tokens, erro = tokenizar(expressao)
    if erro:
        print(erro)
        return

    trace, posfixa, erro = converter(tokens)
    imprimir_trace_desafio2(trace)

    if erro:
        print(erro)
        return

    print("posfixa:", " ".join(posfixa))
    processar_pos_fixa(posfixa)


if __name__ == "__main__":
    main()