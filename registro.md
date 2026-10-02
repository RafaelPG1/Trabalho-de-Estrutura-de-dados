# Trabalho 02 - Processamento de Expressões Matemáticas

Disciplina: Estruturas de Dados, Sistemas de Informação
Professor: Raul de Araújo Lima
Linguagem: Python 3 (apenas biblioteca padrão)
Entrega: 02/10/2026 | Apresentação: 05/10/2026

## Integrantes

| Nome | Matrícula |
|---|---|
| Rafael Peixoto Gonçalves | 2025010288 |
| Antonio Everardo Liveira Lima Filho | 2025010334 |
| Cid Xavier Pacheco Araujo | 2025010285 |

---

## 1. Introdução

O trabalho trata do cálculo de expressões aritméticas escritas na notação usual, como `3 + 4 * (2 - 1)`. O programa converte a expressão para a notação pós-fixa e, em seguida, calcula o resultado. As duas etapas utilizam uma pilha encadeada implementada pela equipe, sem recorrer a `list` como estrutura da pilha.

A solução foi dividida em dois desafios independentes, cada um com a sua própria pilha:

| Desafio | Entrada | Saída | Conteúdo da pilha |
|---|---|---|---|
| 1. Avaliar expressão pós-fixa | `3 4 2 * +` | `11` | Números (operandos) que aguardam um operador |
| 2. Converter para pós-fixa | `3 + 4 * 2` | `3 4 2 * +` | Operadores e parênteses que ainda não puderam ser aplicados |

O programa principal (`main.py`) encadeia as duas etapas: a saída do desafio 2 é a entrada do desafio 1.

### 1.1 Justificativa para o uso de pilha

Ao ler `3 + 4 * 2` da esquerda para a direita, o operador `+` não pode ser aplicado no momento em que aparece, porque o `*` que vem depois precisa ser resolvido antes. O operador deve, portanto, ser guardado e retomado mais tarde, começando sempre pelo mais recente entre os que estão pendentes. Esse é o comportamento LIFO (último a entrar, primeiro a sair) de uma pilha, o que torna a estrutura adequada ao problema.

---

## 2. Organização dos arquivos

| Arquivo | Conteúdo |
|---|---|
| `desafio1.py` | Classes `No` e `Pilha`, funções `fmt`, `tokenizar` (pós-fixa) e `avaliar` |
| `desafio2.py` | Funções `tokenizar` (notação usual) e `converter` (infixa para pós-fixa) |
| `main.py` | Programa principal: lê a expressão, converte, avalia e imprime os rastreamentos |
| `registro.md` | Este documento |

As funções `tokenizar`, `converter` e `avaliar` não imprimem nada. Toda a saída em tela é feita pela `main.py`.

---

## 3. Estruturas de dados

### 3.1 Classe `No`

Cada elemento da pilha é um nó que guarda um valor e uma referência ao nó imediatamente abaixo dele.

```python
class No:
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo = proximo
```

### 3.2 Classe `Pilha`

A pilha mantém uma referência ao nó do topo (`topo_no`) e um contador de elementos (`contador`). Os demais nós são alcançados pela cadeia de referências `proximo`.

| Método | Descrição |
|---|---|
| `empilhar(novo_valor)` | Cria um nó cujo `proximo` é o topo anterior e o define como novo topo |
| `desempilhar()` | Remove o nó do topo e devolve o seu valor |
| `topo()` | Devolve o valor do topo sem removê-lo |
| `vazia()` | Retorna `True` quando não há nenhum nó |
| `tamanho()` | Retorna a quantidade de elementos, a partir do contador |
| `visualizar()` | Percorre os nós do topo até a base, copia os valores para uma lista e a inverte, de modo que o resultado fica da base para o topo. A pilha não é alterada |

Os métodos `empilhar`, `desempilhar`, `topo`, `vazia` e `tamanho` têm custo constante, O(1), pois só acessam o topo ou o contador. O método `visualizar` tem custo O(n).

### 3.3 Finalidade do método `visualizar`

O enunciado exige que o rastreamento mostre o conteúdo da pilha a cada passo, sem destruí-la. Como a pilha é formada por nós encadeados, não é possível imprimi-la diretamente. O método percorre os nós com uma variável auxiliar (`atual`), de modo que `topo_no` permanece intacto, e devolve uma cópia em forma de lista. Alterações nessa cópia não afetam a pilha original.

---

## 4. Desafio 1: avaliação de expressão pós-fixa

### 4.1 Função `tokenizar(expressao)`

Na notação pós-fixa os tokens já são fornecidos separados por espaço, então `expressao.split()` é suficiente.

### 4.2 Função `avaliar(tokens)`

A função devolve a tupla `(trace, resultado, erro)`. Para cada token, o algoritmo procede da seguinte forma:

1. Se o token é um número, converte-o com `float` e o empilha.
2. Se é um operador (`+`, `-`, `*`, `/`, `^`), verifica se a pilha tem ao menos dois elementos. Em caso negativo, retorna erro. Caso contrário, desempilha `b` e depois `a`, calcula `a operador b` e empilha o resultado. A ordem é relevante para `-`, `/` e `^`: em `5 2 -`, o resultado esperado é `5 - 2`.
3. Ao final de cada token, registra no `trace` o token e uma cópia da pilha.

Terminados os tokens, deve restar exatamente um elemento na pilha, que é o resultado.

### 4.3 Tratamento de erros

| Situação | Mensagem |
|---|---|
| Operador sem operandos suficientes (`3 + * 4`) | `erro: operandos insuficientes` |
| Operandos sobrando (`3 4 5 +`) | `erro: expressao malformada` |
| Divisão por zero (`8 0 /`) | `erro: divisao por zero` |
| Token que não é número nem operador | `erro: caractere invalido` |
| Potência que estoura o limite ou resulta em número complexo (`10 1000 ^`, `-8 0.5 ^`) | `erro: resultado invalido` |

Em todos os casos de erro, o `trace` acumulado até aquele ponto também é devolvido, para que a `main.py` exiba o rastreamento antes da mensagem.

### 4.4 Função `fmt(v)`

Utiliza o formato `:g` do Python para imprimir `8` no lugar de `8.0`, mantendo `2.5` inalterado. Serve apenas para exibição e não participa dos cálculos.

---

## 5. Desafio 2: conversão para pós-fixa

### 5.1 Função `tokenizar(expressao)`

A entrada pode vir sem espaços (`3+42*(7-1)`), situação em que `split()` não separa os símbolos. A função lê a expressão caractere a caractere, controlada por um índice (`inicio`), e trata quatro casos:

- espaço: é ignorado;
- dígito ou ponto: um segundo índice (`fim`) avança enquanto o caractere continuar fazendo parte do número, e o trecho `expressao[inicio:fim]` é recortado como um único token (`42`, `12.5`). O trecho é validado com `float`, de modo que `1.2.3` e `.` são recusados;
- `+`, `-`, `*`, `/`, `^`, `(` e `)`: cada símbolo forma um token;
- qualquer outro caractere: retorna `erro: caractere invalido`.

Para a entrada `3+42*(7-1)`, o resultado é `['3', '+', '42', '*', '(', '7', '-', '1', ')']`.

### 5.2 Tabelas de regras

```python
PRIORIDADE = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
DIREITA = {"^"}
```

`PRIORIDADE` indica a precedência de cada operador, sendo maior o número do operador mais forte. `DIREITA` reúne os operadores associativos à direita, que no caso é apenas `^`.

### 5.3 Função `converter(expressao)`

A função recebe a expressão como string, chama `tokenizar` e devolve a tupla `(trace, posfixa, erro)`, na qual `posfixa` é uma string (por exemplo, `"3 4 2 * +"`). Ela usa uma pilha de operadores e uma lista `saida`. Para cada token:

| Token | Ação |
|---|---|
| Número | Vai diretamente para a `saida` |
| `(` | É empilhado e funciona como delimitador de grupo |
| `)` | Os operadores são transferidos da pilha para a `saida` até se encontrar o `(`, que então é descartado. Se a pilha esvaziar antes disso, há erro |
| Operador | Enquanto o topo da pilha (exceto `(`) precisar sair antes, ele é transferido para a `saida`. Depois, o operador atual é empilhado |

O critério para o topo sair depende da associatividade do operador atual:

- operadores associativos à esquerda (`+`, `-`, `*`, `/`): o topo sai se tiver precedência maior ou igual;
- operador associativo à direita (`^`): o topo sai apenas se tiver precedência estritamente maior.

Com isso, `10 - 3 - 2` torna-se `10 3 - 2 -` (resultado 5) e `2 ^ 3 ^ 2` torna-se `2 3 2 ^ ^` (resultado 512).

Terminados os tokens, os operadores que restam na pilha são transferidos para a `saida`. Se um `(` aparecer nesse momento, ele nunca foi fechado.

Após cada token, o `converter` registra no `trace` o token, o conteúdo da pilha de operadores e uma cópia da saída (`list(saida)`). A cópia é necessária porque, sem ela, todas as linhas do rastreamento apontariam para a mesma lista e exibiriam o resultado final. A última linha do rastreamento usa o token literal `(fim)`.

### 5.4 Tratamento de erros

| Situação | Mensagem |
|---|---|
| `3 + 4)` | `erro: parentese fechado sem abertura` |
| `(3 + 4` | `erro: parentese aberto sem fechamento` |
| `3 $ 4` | `erro: caractere invalido` |

---

## 6. Programa principal (`main.py`)

| Função | Descrição |
|---|---|
| `texto(lista)` | Converte uma lista em texto separado por espaços; lista vazia vira `-` |
| `imprimir_desafio2(trace)` | Imprime o rastreamento `token \| pilha \| saida`, com token em 5 colunas e pilha em 11 |
| `imprimir_desafio1(trace)` | Imprime o rastreamento `token \| pilha`, usando `fmt` nos valores |
| `processar(expressao)` | Converte a expressão, imprime o rastreamento, avalia a pós-fixa, imprime o novo rastreamento e exibe o resultado ou o erro |
| `main()` | Repete a leitura de expressões até que uma linha vazia seja digitada |

Os dois arquivos definem uma função chamada `tokenizar`. Para evitar conflito de nomes, a `main.py` importa a do desafio 1 com o apelido `tokenizar_posfixa`.

Quando ocorre um erro, o programa imprime o rastreamento até aquele ponto e depois a mensagem, no lugar da linha `resultado:`. Em seguida, passa para a próxima expressão sem encerrar a execução.

### Execução

```
python main.py
```

Digita-se uma expressão por vez, e uma linha vazia encerra o programa.

---

## 7. Testes realizados

| Entrada | Pós-fixa | Resultado |
|---|---|---|
| `3 + 4 * 2` | `3 4 2 * +` | 11 |
| `(3 + 4) * 2` | `3 4 + 2 *` | 14 |
| `1 + 2 * 3 - 4 / 2` | `1 2 3 * + 4 2 / -` | 5 |
| `3 + 4 * (2 - 1)` | `3 4 2 1 - * +` | 7 |
| `10 - 3 - 2` | `10 3 - 2 -` | 5 |
| `2 ^ 3 ^ 2` | `2 3 2 ^ ^` | 512 |
| `(2 ^ 3) ^ 2` | `2 3 ^ 2 ^` | 64 |
| `3+42*(7-1)` | `3 42 7 1 - * +` | 255 |
| `3 + 4)` | | `erro: parentese fechado sem abertura` |
| `(3 + 4` | | `erro: parentese aberto sem fechamento` |
| `3 $ 4` | | `erro: caractere invalido` |
| `8 / (4 - 4)` | `8 4 4 - /` | `erro: divisao por zero` |

Exemplo de saída para `3 + 4 * 2`:

```
token| pilha      | saida
3    | -          | 3
+    | +          | 3
4    | +          | 3 4
*    | + *        | 3 4
2    | + *        | 3 4 2
(fim)| -          | 3 4 2 * +
posfixa: 3 4 2 * +
token| pilha
3    | 3
4    | 3 4
2    | 3 4 2
*    | 3 8
+    | 11
resultado: 11
```

Os três últimos casos do enunciado (`10 - 3 - 2`, `2 ^ 3 ^ 2` e `(2 ^ 3) ^ 2`) verificam a associatividade. Se todos os operadores fossem associativos à esquerda, `2 ^ 3 ^ 2` resultaria em 64. Se todos fossem associativos à direita, `10 - 3 - 2` resultaria em 9. A implementação trata cada operador conforme a sua associatividade e produz os valores esperados nos três casos.

---

## 8. Decisões de implementação e limitações

- A pilha é encadeada e não usa lista interna. O contrato respeitado é `empilhar`, `desempilhar`, `topo`, `vazia` e `tamanho`, acrescido do método `visualizar`, necessário para o rastreamento.
- O contador `contador` permite que `tamanho()` seja O(1), sem percorrer os nós.
- Todos os números são convertidos para `float`, o que simplifica a divisão e o uso de decimais. A função `fmt` cuida apenas da exibição.
- A validação do número no `tokenizar` do desafio 2 impede que entradas como `1.2.3` cheguem à etapa de avaliação.
- Números negativos (por exemplo, `-3 + 4`) não são suportados, pois o `-` é tratado apenas como operador binário. O enunciado não exige esse caso.

---

## 9. Declaração de uso de ferramentas de IA

Foi utilizado o Claude como ferramenta de estudo com as seguintes finalidades:

- explicação de conceitos como classes, `self`, nós encadeados, pilha e o algoritmo de conversão de notação infixa para pós-fixa;
- sugestão de nomes de variáveis mais claros;
- revisão do código em relação ao enunciado, que levou a ajustes nos nomes do contrato da pilha, no rastreamento, no tratamento de exceções da potenciação e na validação de números;
- apoio na redação e na revisão de estilo deste registro.

O código foi reescrito e testado pela equipe. 