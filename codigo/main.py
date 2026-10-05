# Nome: Rafael Peixoto Gonçalves  Matrícula: 2025010288
# Nome: Antonio Everardo Liveira LIma Filho  Matrícula: 2025010334
# Nome: Cid Xavier Pacheco Araujo  Matrícula: 2025010285

from desafio1 import fmt, avaliar, tokenizar as tokenizar_posfixa
from desafio2 import converter


def texto(lista):
    # lista vazia vira "-"
    if not lista:
        return "-"
    return " ".join(lista)


def imprimir_desafio2(trace):
    if not trace:
        return
    print(f"{'token':<5}| {'pilha':<11}| saida")
    for token, pilha, saida in trace:
        print(f"{token:<5}| {texto(pilha):<11}| {texto(saida)}")


def imprimir_desafio1(trace):
    if not trace:
        return
    print(f"{'token':<5}| pilha")
    for token, pilha in trace:
        numeros = " ".join(fmt(v) for v in pilha)
        print(f"{token:<5}| {numeros}")


def processar(expressao):
    # --- desafio 2: converter para pós-fixa ---
    trace2, posfixa, erro = converter(expressao)
    imprimir_desafio2(trace2)

    if erro:
        print(erro)
        return

    print("posfixa:", posfixa)

    # --- desafio 1: avaliar a pós-fixa ---
    tokens = tokenizar_posfixa(posfixa)
    trace1, resultado, erro = avaliar(tokens)
    imprimir_desafio1(trace1)

    if erro:
        print(erro)
    else:
        print("resultado:", fmt(resultado))


def main():
    while True:
        expressao = input("Digite a expressão (vazio para sair): ")

        if expressao.strip() == "":
            break

        processar(expressao)
        print()


main()