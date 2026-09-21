expressao = input("Digite uma expressão matemática: ")
exp = expressao.split(" ")



numero = []
for i in range(len(exp)):
    if exp[i].isdigit():
        numero.append(exp[i]) 
    else:
        print(f"O elemento na posição {exp[i]} não é um número.")


print(numero)