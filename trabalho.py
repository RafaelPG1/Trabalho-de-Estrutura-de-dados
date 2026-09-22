expressao = input("Digite uma expressão matemática: ")
exp = expressao.split(" ")

numero = []
for i in range(len(exp)):
    if exp[i].isdigit():
        numero.append(exp[i]) 
    else:
        print(f"O elemento na posição {exp[i]} não é um número.")
        sinal = exp[i]
        a = float(exp[i-2])
        b = float(exp[i-1])
        if sinal == "+":
            resultado = a + b
        elif sinal == "-":
            resultado = a - b
        elif sinal == "*":
            resultado = a * b
        elif sinal == "/":
            resultado = a / b
        del numero[-2:]
        break



print(numero)
print(f"a: {a}, b: {b}, sinal: {sinal}, resultado: {resultado}")