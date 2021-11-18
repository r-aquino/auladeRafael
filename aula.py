# 1- Estrutura de Dados: estratégia para busca, inserção e remoção de elementos:

# Fila: o primeiro dado que entra é o primeiro que sai. FIFO = First-In, First-Out

# Pilha: o primeiro que entra é o último que sai. LIFO = Last-In, First-Out

# Lista [] - conjunto de elementos em sequencia. 
# Podendo ser de tipos diferentes. Podemos ordenar, inverter, verificar duplicados, etc. 

# 2 - Entrada de dados:
# idade = int(input("Digite sua idade: "))
# print(idade)

# idade = float(input("Digite sua idade: "))
# print(idade)

# type()
# int / float
# range(1,20, 2) 

# 3 - Loops ou Estruturas de repetição: for / while / else 

# FOR

# O for é utilizado para percorrer ou iterar sobre uma sequência de dados
# (seja essa uma lista, uma tupla, uma string), 
# executando um conjunto de instruções em cada item.

# lista = [1, 2, 3, 4, 5]

# for item in lista:
#     print(item)

# tupla = (1, 2, 3, 4, 5)

# for item in tupla:
#     print(item)

# texto = "Aqui Educa"

# for item in texto:
#     print(item)

# lista = [1, 2, 3, 4, 5]
# for item in lista:
#     print(item)
#     qualquer = item*2
#     print(qualquer)
# else:
#     print("outra coisa")
#     print('Todos os items foram exibidos com sucesso')

# a = int(input("Digite sua idade: "))

# if 0<a and a<50:  
#     print("idade está entre 0 e 50")
# elif a >= 50 and a < 100:
#     print("idade esta entre 50 e 100")
# elif a > 100:
#     print("idade maior que 100")   
# else:
#     print("Nenhuma das opções definidas")

# computador = ['Processador', 'Teclado', 'Mouse']
# print(computador[2])

# computador = ['Processador', 'Teclado', 'Mouse']

# for item in computador:
#     print(item)

# lista = [0,1,2,3]
# for item in lista:
#     print(item)
# else:
#     print('Todos os items foram exibidos com sucesso')

#Dicionário
# notas = {
#     'Potuguês': 7, 
#     'Matemática': 9, 
#     'Lógica': 7, 
#     'Algoritmo': 7
# }

# for chave, valor in notas.items():
#     print(chave, valwor)
# else:
#     print('Todos os items foram exibidos com sucesso')


# Loops utilizando while
# O while é uma estrutura de repetição utilizada quando queremos que 
# determinado bloco de código seja executado ENQUANTO (do inglês while) determinada condição for satisfeita.
# Em outras palavras: só saia da estrutura de repetição quando a condição não for mais satisfeita.

# Sua sintaxe básica é:

# while <condição>:
#     Bloco aser executado

# Exemplo

# contador = 0

# while contador <= 10:
#     print(contador)
#     contador += 1
# else:
#     print("Fim do código")


# contador = 0
# while contador < 10:
#     print(contador)
#     contador += 1
# else:
#     print("Fim do while!")


# Desafio facil: Escrever um programa em Python para exibir
#  os números de 1 até 50 na tela.
# utilizando o for e a função range(1,51)
# utilizando while

# Desafio dificil: escreva um codigo que de um print sequencial 
# em todas as letras das palavras da lista abaixo: 
# lista = ["Bahia", "Vitoria", "Fortaleza", "Sao Paulo"]





# Resposta 1: 
# for numero in range(1,50):
#     print(numero)

# Resposta 2:
# lista = ["Bahia", "Vitoria", "Fortaleza", "Sao Paulo"]
# a = 0
# while a != len(lista):
#     lista2 = lista[a] 
#     for item in lista2:
#         print(item)
#     a = a+1


# else:
#     print("Fim")


# Auxiliadores
# Existem 3 comandos que nos auxiliam quando queremos 
# alterar o fluxo de uma estrutura de repetição.

# São eles: break, continue e pass.

# Break
# for num in range(5):
#     # Se o número for igual a = 3, devemos parar o loop
#     if num == 3:
#         # Break faz o loop finalizar
#         break
#     else:
#         print(num)

# Continue com For
# listaDeIdades = [-1,2,3,-5,6,8,9,-15,18,14,5,6]
# for idade in listaDeIdades:
#     if idade < 0:
#         continue
#     print(idade)

# Continue com While
# num = 0
# while num < 3:
#     num += 1

#     if num == 2:
#         continue
        
#     print(num)

# Pass
# for i in "rafael":
#     pass


