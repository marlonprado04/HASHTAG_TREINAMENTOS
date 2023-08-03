# Python Impressionador

Esse curso tem foco em desenvolver diversas habilidades em Python, desde automação, criação de jogos até análise de dados.

## Índice

- [Python Impressionador](#python-impressionador)
  - [Índice](#índice)
  - [Módulo 06: If - Condições em Python](#módulo-06-if---condições-em-python)
    - [Aula 03: Elif](#aula-03-elif)
    - [Aula 04: Comparadores](#aula-04-comparadores)
    - [Aula 05: And e Or](#aula-05-and-e-or)
    - [Aula 06: Exercícios If](#aula-06-exercícios-if)
    - [Aula 07: Comparações Contraintuitivas](#aula-07-comparações-contraintuitivas)
    - [Aula 08: Exercícios If - Parte 2](#aula-08-exercícios-if---parte-2)
    - [Aula 09: Exercícios Extras (Opcional) - Estruturas de Decisão](#aula-09-exercícios-extras-opcional---estruturas-de-decisão)
  - [Módulo 07: Strings - Textos e a importância no Python](#módulo-07-strings---textos-e-a-importância-no-python)
    - [Aula 01: Por que aprender Strings e a importância pro Python](#aula-01-por-que-aprender-strings-e-a-importância-pro-python)
    - [Aula 02: Índice e Tamanho de String](#aula-02-índice-e-tamanho-de-string)
    - [Aula 03: Índice Negativo e Pedaço de String](#aula-03-índice-negativo-e-pedaço-de-string)
    - [Aula 04: Operações com String](#aula-04-operações-com-string)
    - [Aula 05: Métodos de String - Apresentação](#aula-05-métodos-de-string---apresentação)
    - [Aula 06: Exercícios String - Parte 1](#aula-06-exercícios-string---parte-1)
    - [Aula 07: Formatação de números](#aula-07-formatação-de-números)

## Módulo 06: If - Condições em Python

Aulas de como realizar operações com _if_ no Python.

Exemplo de código:

```python
meta = 0.05
taxa = 0
rendimento = 0.10

if rendimento > meta:
    if rendimento > 0.20:
        taxa = 0.04
        print(f"A taxa foi de {taxa*100}%")
    else:
        taxa = 0.2
        print(f"A taxa foi de {taxa*100}%")
else:
    taxa = 0
    print(f"A taxa foi de {taxa*100}%")
```

### Aula 03: Elif

A estrutura do elif é a mesma do _if_, porém ele substitui um _else_ e coloca um comparador no lugar.

Abaixo um exemplo de código:

```python
if condição:
    o que fazer se a condição 1 for verdadeira
elif condição_2:
    o que fazer se a condição 1 for falsa e a condição 2 for verdadeira
else:
    o que fazer se a condição 1 e a condição 2 forem falsas
```

### Aula 04: Comparadores

O Python suporta diversos comparadores de informação, sendo eles:

- `==`    igual
- `!=`    diferente
- `>`     maior que (>= maior ou igual)
- `<`     menor que (<= menor ou igual)
- `in`    texto existe dentro de outro texto
- `not`   verifica o contrário da comparação

Obs: Se em alguma condi��o voc� n�o quiser fazer nada, voc� pode simplesmente escrever:
pass

### Aula 05: And e Or

Os operadores __or__ e __end__ servem para complementar comparações lógicas.

Exemplo de uso:

```python
meta_funcionario = 10000
meta_loja = 25000
vendas_funcionario = 5000
vendas_loja = 20000

if vendas_funcionario > meta_funcionario and vendas_loja > meta_loja:
    bonus = vendas_funcionario * 0.03
    print("Bônus do funcionário foi de {}".format(bonus))
else:
    print("Funcionário não ganhou bônus")
```

### Aula 06: Exercícios If

Nesta aula terão diversos exercícios para testar os conhecimentos em Python.

### Aula 07: Comparações Contraintuitivas

Nessa aula serão trabalhadas comparações contraintuitivas.

O código abaixo apresenta um erro que o impede de executar corretamente no caso do usuário deixar de preencher uma informação:

```python
faturamento = input('Qual foi o faturamento da loja nesse mês?')
custo = input('Qual foi o custo da loja nesse mês?')

lucro = int(faturamento) - int(custo)

print("O lucro da loja foi de {} reais".format(lucro))
```

Para solucionar isso, podemos usar um __if__ para verificar se os valores foram preenchidos corretamente, como no exemplo abaixo:

```python
faturamento = input('Qual foi o faturamento da loja nesse mês?')
custo = input('Qual foi o custo da loja nesse mês?')

if faturamento and custo:
    lucro = int(faturamento) - int(custo)
    print("O lucro da loja foi de {} reais".format(lucro))
else:
    print("Preencha o faturamento e lucro corretamente!")
```

No código acima estamos verificando se a variável __faturamento__ e __lucro__ estão preenchidas (não vazias). Caso positivo, continuamos o código, caso negativo, pedimos que o usuário preencha.

### Aula 08: Exercícios If - Parte 2

Mais exercícios de IF.

### Aula 09: Exercícios Extras (Opcional) - Estruturas de Decisão

Aula opcional de exercícios extras.

Fiz os 3 primeiros, é muito básico e são +20.

## Módulo 07: Strings - Textos e a importância no Python

### Aula 01: Por que aprender Strings e a importância pro Python

É essencial que uma das primeiras aulas sejam de __Strings__ em Python, pois no Python as string são vistas como listas de caracteres.

Dessa forma, adiantamos os aprendizados de listas além de aprender a trabalhar com um dos principais tipos de variáveis utilizados.

### Aula 02: Índice e Tamanho de String

Um conhecimento básico sobre strings em python é que elas são uma __lista de caracteres__, ou seja, cada posição da lista pode ser acessada individualmente.

Para imprimir o tamanho da lista usamos o comando __len__ e para acessar determinado caracter dentro da lista usamos o __[indice]__ onde o _indice_ é a posição desejada.

Abaixo um exemplo:

```python

email = 'lira@gmail.com'
nome = 'João Lira'

print(len(email)) # retorna o tamanho do texto
print(nome[1]) # retorna "o" que é o caractere na 3ª posição do texto

```

### Aula 03: Índice Negativo e Pedaço de String

Da mesma forma que podemos pegar o índice dos elementos de uma lista contando a __partir do zero__, para frente, podemos pegar o elemento final com o índice __negativo__.

Ou seja, se quisermos acessar o elemento final da lista podemos usar o índice `-1`.

Abaixo um exemplo:

```markdown
Texto: lira@gmail.com

-14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
  l   i   r   a   @  g  m  a  i  l  .  c  o  m
  0   1   2   3   4  5  6  7  8  9 10 11 12 13
  
Para pegar um texto de trás para frente: texto[índice] -> onde índice é negativo
Para pegar o pedaço de um texto use : (dois pontos). texto[:indice] ou texto[indice:] ou ainda texto[indice:indice]
```

Podemos também trabalhar com pedaços de strings passando ":" como parâmetro dentro dos colchetes, conforme abaixo:

```python
email = 'lira@gmail.com'
nome = 'João Paulo Lira'

# Printando um caractere final
print(email[-3]) # retorna "c" do ".com"

# Printando um pedaço do texto
print(email[:-1]) # retorna "lira@gmail.co", o texto todo menos o índice -1 
```

> Importante detalhe: ao colocar o ":" antes de um índice, ele não inclui o índice informado.
> Se colocarmos um índice e depois um ":", ele inclui o índice.

Abaixo um exemplo para fixação:

```python
email = 'lira@gmail.com'
print('Tamanho do e-mail ' + str(len(email)) + ' caracteres')
print('Primeiro Caractere ' + email[0])
print('Último Caractere ' + email[-1])
print('Servidor do email ' + email[5:-4])
```

### Aula 04: Operações com String

A __String__ em Python traz algumas funcionalidades consigo e nesta aula vamos aprender algumas delas.

Abaixo alguns exemplos de funcionalidades e após alguns exemplos de uso:

str -> transforma número em string
in -> verifica se um texto está contido dentro do outro
operador + -> concatenar string
format e {} -> substitui valores
%s -> substitui textos
%d -> substitui números decimais

Usando __format__ para formatar strings:

```python
faturamento = 1000
custo = 500
lucro = faturamento - custo

print('O faturamento foi de: {}. O custo foi de: {}. O lucro foi de: {}'.format(faturamento, custo, lucro))

print('O faturamento foi de: {0}. O custo foi de: {1}. O lucro foi de: {2}. Lembrando que o faturamento foi de: {0}'.format(faturamento, custo, lucro))
```

Usando __%__ para concatenar strings:

```python
faturamento = 1000
custo = 500
lucro = faturamento - custo

print ('O faturamento foi de %d, o custo foi de %d e o lucro de %d' % (faturamento, custo, lucro))

```

Usando o __in__ para localizar valor dentro de string:

```python
print('@' in 'lira@gmail.com') # retorna true
print('@' in 'lira.gmail.com') # retorna false
```

### Aula 05: Métodos de String - Apresentação

Métodos são fórmulas / ações que podemos realizar com, por exemplo, as Strings.

Alguns métodos de Strings no Python são:

- __capitalize()__: Coloca a primeira letra em maiúsculo;
- __casefold()__: Coloca todas letras do texto em minúsculo;
- __count(<texto_procurado>)__: Conta o número de vezes que determinado texto aparece em outro;
- __ednswith(<texto_procurado>)__: Verifica se o texto termina com o texto procurado;
- __find(<texto_procurado>)__: Localiza um texto dentro de outro e __retorna a posição dele__;
- __format(<texto_formatado>)__: Permite formatar os valores dentro do texto de acordo com o que for passado;
- __isalnum()__: Verifica se todos os caracteres dentro do texto são alfanuméricos e retorna __true__ caso positivo;
- __isalpha()__: Verifica se todos os caracteres dentro do texto são apenas letras e retorna __true__ caso positivo;
- __isnumeric()__: Verifica se todos os caracteres dentro do texto são apenas numéricos e retorna __true__ caso positovo;
- __replace(<texto_a_ser_substituido>, <texto_a_ser_colocado_no_lugar>)__: Substitui um texto pelo outro;
- __split(<texto_delimitador>)__: Separa o texto em vários textos diferentes de acordo com um delimitador passado;
- __splitlines()__: Separa um texto em vários textos de acordo com os "enters" do texto;
- __startswith(<texto_procurado>)__: Verifica se um texto começa com outro procurado;
- __strip()__: Retira caracteres indesejados no início e no fim do texto;
- __title()__: Coloca a primeira letra de cada palavra em maiúsculo;
- __upper()__: Coloca todas as letras do texto em maiúsculo.

Todos estes métodos são usados passando seguindo a lógica deste exemplo:

```python
texto = "olá mundo"
print(texto.capitalize()) # Retorna o texto com primeira letra em maiúsculo
```

### Aula 06: Exercícios String - Parte 1

Aula apenas para explicar resolução dos exercícios de __String__.

- [x] Realizar exercícios sozinho

### Aula 07: Formatação de números
