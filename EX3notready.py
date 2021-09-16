'''
Faça um programa que receba uma lista de genes e uma função de regulação para cada gene 
com operadores not, and e or ('!', '&', ' | ') e imprima uma lista dos estados em que 
cada gene estará ativado. A ordem dos genes deverá ser a ordem dada na lista. 
Repare que o operador or está entre espaços que equivale a separar com parênteses. 
Por exemplo, '!A&C | B&C | !C' que equivale a (!A&C) | (B&C) | (!C). 
Não haverá parênteses nas expressões.
Para simplificar, consideraremos que as funções serão sempre nesse formato, 
sem encadeamentos sobrepostos difíceis de identificar. 

Em outras palavras: dá para fazer um split primeiro com ' | ' para separar os pedaços 
e depois use o que foi feito no exercício anterior para '&'. 
Repita para todos os genes. 
Se quiser usar outra implementação muito mais simples, utilize-a.

Exemplo de execução:

Nomes dos genes (separados por vírgula): A,B,C
Função para A: !A&C | B&C | !C
Função para B: !A&!B | C
Função para C: A&B
Estados que ativarão A: ['000', '001', '010', '011', '100', '110', '111']
Estados que ativarão B: ['000', '001', '011', '101', '111']
Estados que ativarão C: ['110', '111']

'''
from itertools import product


askgenes = input('Nomes dos genes (separados por vírgula): ')
askgenes = askgenes.split(sep=',') # separa os nomes dos genes e coloca numa lista
for k in range(len(askgenes)):
    askgenes[k] = askgenes[k].replace(' ', '') # tira espaços que possam atrapalhar na leitura eventualmente


# Cria lista das funções
func_list = [] # cria uma lista para as funções dos genes
for k in range(len(askgenes)):
    askfunc = input('Função para {0}: '.format(askgenes[k])).strip('\n') # pergunta as funções
    askfunc = askfunc.split(sep=' | ') # separa nos "or"
    func_list.append(askfunc) # adiciona as funções numa lista - cada indexação para um gene
    
for k in range(len(func_list)):
    for j in range(len(func_list[k])):
        func_list[k][j] = func_list[k][j].split(sep = '&') # divide os genes citados

for k in range(len(func_list)): 
    for j in range(len(func_list[k])):
        for i in range(len(func_list[k][j])):
            func_list[k][j][i] = func_list[k][j][i].replace(' ', '') # tira espaços que possam atrapalhar na leitura eventualmente


# Cria dicionários para dar significado às funções
fundic = {}
gen_dict = {} 
for k in range(len(askgenes)):
    gen_dict.update({askgenes[k]: ''}) # cria um dicionário de relação entre os genes
for k in range(len(askgenes)):
    fundic.update({askgenes[k]: gen_dict})
genes = list(fundic.keys()) # lista dos index do dicionário, para poder percorrer os valores

for k in range(len(func_list)): # aqui, os genes recebem valores de relação
    for j in range(len(fundic[genes[k]])):
        for i in range(len(func_list[k][j])):
            if func_list[k][j][i][0] == '!':
                func_list[k][j][i] = func_list[k][j][i].replace('!','')
                fundic[k][j][i].update({func_list[k][j][i]: 0}) # se o gene aparece na função com ! na frente, recebe o valor 0 no dicionario
            else:
                fundic[k][j][i].update({func_list[k][j][i]: 1})  # se o gene aparece na função, recebe o valor 1 no dicionário
# se o gene não aparece, seu valor é uma string vazia

print(fundic)

a = list(product('01', repeat=len(askgenes))) # lista dos estados possíveis dos genes (on/off) - tuplas com a situação de cada gene
state_list = []
for k in range(len(a)):
    state = ''
    for j in range(len(askgenes)):
        state = state + a[k][j]
    state_list.append(state) # lista dos estados possíveis dos genes - strings representando a situação dos genes respectivamente




activate = [] # lista de estados que ativam
for k in range(len(state_list)): # para cada estado,
    for j in range(len(genes)): 
        if fundic[genes[j]] != '': # se houver algum gene na função
            if str(fundic[genes[j]]) != state_list[k][j]: # cujo valor não corresponde à sua posição nesse estado
                break # ele não será adicionado na lista de ativação
    else:
        activate.append(state_list[k])
        
print(activate)
