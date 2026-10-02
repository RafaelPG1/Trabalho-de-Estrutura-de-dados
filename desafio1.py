# Nome: Rafael Peixoto Gonçalves  Matrícula: 2025010288
# Nome: Antonio Everardo Liveira LIma Filho  Matrícula: 2025010334
# Nome: Cid Xavier Pacheco Araujo  Matrícula: 2025010285


class No:
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo


class Pilha:
    def __init__(self):
        self.topo_no = None
        self.contador = 0

    def empilhar(self, novo_valor):
        self.topo_no = No(novo_valor, self.topo_no)
        self.contador += 1

    def desempilhar(self):
        valor_removido = self.topo_no.valor
        self.topo_no = self.topo_no.proximo
        self.contador -= 1
        return valor_removido

    def topo(self):
        return self.topo_no.valor

    def vazia(self):
        return self.topo_no is None

    def tamanho(self):
        return self.contador

    def visualizar(self):
        # copia os valores da base até o topo, sem mexer na pilha
        itens = []
        atual = self.topo_no
        while atual is not None:
            itens.append(atual.valor)
            atual = atual.proximo
        itens.reverse()
        return itens


def fmt(v):
    """Imprime 8 em vez de 8.0, mas mantém 2.5 como 2.5."""
    return f"{v:g}"


def tokenizar(expressao):
    return expressao.split()


def avaliar(tokens):
    pilha = Pilha()
    trace = []

    for token in tokens:
        if token in ("+", "-", "*", "/", "^"):
            if pilha.tamanho() < 2:
                return trace, None, "erro: operandos insuficientes"

            # b sai primeiro, depois a
            b = pilha.desempilhar()
            a = pilha.desempilhar()

            if token == "+":
                resultado = a + b
            elif token == "-":
                resultado = a - b
            elif token == "*":
                resultado = a * b
            elif token == "/":
                if b == 0:
                    return trace, None, "erro: divisao por zero"
                resultado = a / b
            elif token == "^":
                try:
                    resultado = a ** b
                except (OverflowError, ZeroDivisionError):
                    return trace, None, "erro: resultado invalido"
                if isinstance(resultado, complex):
                    return trace, None, "erro: resultado invalido"

            pilha.empilhar(resultado)
        else:
            try:
                pilha.empilhar(float(token))
            except ValueError:
                return trace, None, "erro: caractere invalido"

        trace.append((token, pilha.visualizar()))

    if pilha.tamanho() != 1:
        return trace, None, "erro: expressao malformada"

    return trace, pilha.topo(), None