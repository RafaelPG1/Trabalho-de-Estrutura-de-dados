from desafio_1 import desafio_1
from desafio_2 import desafio_2


def eh_pos_fixa(expressao):
    tokens = expressao.replace(",", " ").split()
    return len(tokens) >= 2 and tokens[0].isdigit() and tokens[1].isdigit()


def main():
    expressao = input("Digite a expressão: ")

    if eh_pos_fixa(expressao):
        print("Expressão pós-fixa: desafio_1")
        tokens = expressao.replace(",", " ").split()
        expressao_normalizada = ",".join(tokens)
        resultado = desafio_1(expressao_normalizada)
    else:
        print("Expressão infixa: desafio_2")
        resultado = desafio_2(expressao)

    print("Resultado:", resultado)


if __name__ == "__main__":
    main()