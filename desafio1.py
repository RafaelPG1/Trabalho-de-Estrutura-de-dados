class No:
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo


class Pilha:
    def __init__(self):
        self.topo_no = None
        self.n = 0

    def empilhar(self, valor):
        self.topo_no = No(valor, self.topo_no)
        self.n += 1

    def desempilhar(self):
        valor = self.topo_no.valor
        self.topo_no = self.topo_no.proximo
        self.n -= 1
        return valor

    def topo(self):
        return self.topo_no.valor

    def vazia(self):
        return self.topo_no is None

    def tamanho(self):
        return self.n

    def para_lista(self):
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

            # Definir a e b
            b = pilha.desempilhar()
            a = pilha.desempilhar()

            # calculadora
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
                resultado = a ** b

            pilha.empilhar(resultado)
        else:
            try:
                pilha.empilhar(float(token))
            except ValueError:
                return trace, None, "erro: caractere invalido"

        trace.append((token, pilha.para_lista()))

    if pilha.tamanho() != 1:
        return trace, None, "erro: expressao malformada"

    return trace, pilha.topo(), None