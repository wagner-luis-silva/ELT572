# Respostas das perguntas

## 1. Qual o valor da variável `resultado` após a execução do código? Explique sua resposta.

No código de `Activity 1.py`:

```python
tupla = (3, 5, 7, 9)
resultado = tupla[1] + tupla[-1]
```

- `tupla[1]` acessa o segundo elemento da tupla, que é `5`.
- `tupla[-1]` acessa o último elemento da tupla, que é `9`.
- O valor de `resultado` é a soma desses dois valores: `5 + 9 = 14`.

Portanto, `resultado` vale `14`.

## 2. Dado o código a seguir: Qual será o conteúdo da lista após a execução do código? Descreva as alterações feitas em cada passo.

No código de `Activity 2.py`:

```python
lista = [2, 4, 6, 8, 10]
lista.append(12)
lista.insert(2, 5)
del lista[4]
```

Passo a passo:

1. Inicialmente, a lista é `[2, 4, 6, 8, 10]`.
2. `lista.append(12)` adiciona o valor `12` ao final da lista. Agora a lista passa a ser `[2, 4, 6, 8, 10, 12]`.
3. `lista.insert(2, 5)` insere o valor `5` na posição de índice `2` (terceira posição), deslocando os elementos seguintes para a direita. Depois dessa operação, a lista fica `[2, 4, 5, 6, 8, 10, 12]`.
4. `del lista[4]` remove o elemento que está no índice `4`, que é o número `8` na lista atual. Após a remoção, a lista final é `[2, 4, 5, 6, 10, 12]`.

Portanto, o conteúdo final da lista é `[2, 4, 5, 6, 10, 12]`.

## 3. Qual será o estado final do dicionário após a execução do código? Explique como os valores foram alterados ou adicionados.

No código de `Activity 3.py`:

```python
dicionario = {'a': 1, 'b': 2, 'c': 3}
dicionario['b'] = dicionario['c'] + 2
dicionario['d'] = 4
```

Passo a passo:

1. O dicionário começa como `{'a': 1, 'b': 2, 'c': 3}`.
2. A linha `dicionario['b'] = dicionario['c'] + 2` altera o valor da chave `'b'`. Ela usa o valor de `dicionario['c']`, que é `3`, e soma `2`, resultando em `5`. Então `'b'` passa a ter valor `5`.
3. A linha `dicionario['d'] = 4` adiciona uma nova chave `'d'` com o valor `4`.

O dicionário final é:

```python
{'a': 1, 'b': 5, 'c': 3, 'd': 4}
```

## 4. Qual será o conteúdo da lista `resultado` após a execução do loop, e qual será o valor da variável `resultado_final`? Explique como o código funciona.

No código de `Activity 4.py`:

```python
numeros = [1, 2, 3, 4, 5, 6]
resultado = []

for i in range(len(numeros)):
    if i % 2 == 0:
        resultado.append(numeros[i] ** 2)
    else:
        resultado.append(numeros[i] * 2)

print(resultado)

resultado_final = sum(resultado)
print(resultado_final)
```

Como o loop funciona:

- Ele percorre os índices de `numeros` com `i` de `0` a `5`.
- Quando o índice `i` é par (`i % 2 == 0`), ele eleva ao quadrado o elemento `numeros[i]` e adiciona ao `resultado`.
- Quando o índice `i` é ímpar, ele multiplica por `2` o elemento `numeros[i]` e adiciona ao `resultado`.

Cálculo passo a passo:

- `i = 0` (par): `numeros[0] = 1` → `1 ** 2 = 1`
- `i = 1` (ímpar): `numeros[1] = 2` → `2 * 2 = 4`
- `i = 2` (par): `numeros[2] = 3` → `3 ** 2 = 9`
- `i = 3` (ímpar): `numeros[3] = 4` → `4 * 2 = 8`
- `i = 4` (par): `numeros[4] = 5` → `5 ** 2 = 25`
- `i = 5` (ímpar): `numeros[5] = 6` → `6 * 2 = 12`

Assim, a lista `resultado` fica:

```python
[1, 4, 9, 8, 25, 12]
```

E `resultado_final` é a soma desses valores:

```python
1 + 4 + 9 + 8 + 25 + 12 = 59
```

Portanto, `resultado_final` vale `59`.
