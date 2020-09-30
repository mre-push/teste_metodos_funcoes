# Escreva uma função que calcula o volume de uma esfera dado seu raio.
def vol(num):

    return  4 * 3.14 * num**2 /  3
# RESPOSTA:
#     vol(3)
#     37.68

# Escreva uma função que verifica se um número está em um determinado intervalo (inclusive o máximo e mínimo)
1 in range(0,10)
# RESPOSTA:
# True
def ran_check(num, low, high):
    if num in list(range(low, high)):
        print("True")            
    else:
        print("False")
# RESPOSTA :
# ran_check(5,1,10)
# True
# ran_check(13,1,10)
# False

# Escreva uma função Python que aceita uma string e calcule o número de maiúsculas e minúsculas.
# Exemplo de Cadeia: 'Olá Sr. Rogers, como você está bem, terça-feira?'      Saída esperada:      Número de caracteres maiúsculas: 4      Número de caracteres minúsculos: 33
# Se você se sentir ambicioso, explore o módulo de Coleções para resolver esse problema!

string = 'O'
string.isupper()
# RESPOSTA:
# True

string = 'O'
string.islower()
# RESPOSTA:
# False

def up_low(s):
    up = 0
    low = 0
    
    for i in s:
        if i.isupper():
            up += 1
        elif i.islower():
            low+=1
        else:
            continue
    print('Numero de caracteres maiúsculas: ', up)
    print('Numero de caracteres minúsculas: ', low)

# RESPOSTA :
# up_low('Olá Sr. Rogers, como você está bem, terça-feira?')
# Numero de caracteres maiúsculas:  3
# Numero de caracteres minúsculas:  33

# Escreva uma função Python que recebe uma lista e retorna uma nova lista com elementos exclusivos da primeira lista.

#  Lista de Amostras: [1,1,1,1,2,2,3,3,3,3,4,5]                    Lista única: [1, 2, 3, 4, 5]

l = [1,1,1,1,2,2,3,3,3,3,4,5]

def unique_list(l):
    return list(set(l)) 
# RESPOSTA :
#  unique_list(l)
#  [1, 2, 3, 4, 5]

# Escreva uma função Python para multiplicar todos os números em uma lista.

#  Lista de exemplos: [1, 2, 3, -4]      Saída esperada: -24
# def multiply(numbers):
# pass

def multiply(l):
    p = 1
    for num in l:
        p *= num
        print(p)
# RESPOSTA :
# e = [1,2,3,-4]
# 1
# 2
# 6
# -24

# Escreva uma função Python que verifica se uma string passada é palindrome ou não.
# Nota: Um palíndromo é palavra, frase ou seqüência que lê o mesmo para trás.
# def palindrome(s): pass
# def palindrome(s): for palavra in palavras: palavra.reverse() == palavra print(True) else: print(False) TENTEI USANDO O REVERSE, mas pesquisando achei forma mais fácil e rápida.

def palin(l):
    if l == l[::-1]:
        print("True")
    else:
        print("False")

palin('ese')
# RESPOSTA:
# True

# DIFÍCIL: Escreva uma funçaõ que verifica se na string há um pangrama, ou seja, uma palavra contendo cada uma das letras do alfabeto pelo uma vez.

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    num = len(alphabet)
    count = 0
    
    for i in alphabet:
        if i in str1:
            count+=1
            
    return count == num

ispangram("The quick brown fox jumps over the lazy dog")

# RESPOSTA:
# ispangram("The")
# False

