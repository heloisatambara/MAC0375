'''
Faça um programa que receba uma lista de genes e uma única função de regulação simples, 
que não contém o operador or (' | ') e imprima uma lista dos estados estados que podem ativar o suposto gene.

Exemplo de execução:

Nomes dos genes (separados por vírgula): A,B,C
Função: !A&B
['010', '011']

'''
# seu código aqui
# importações
from itertools import product
#


# input dos genes
askgenes = input('Nomes dos genes (separados por vírgula): ')
askgenes = askgenes.split(sep=',') # separa os nomes dos genes e coloca numa lista
for k in range(len(askgenes)):
    askgenes[k] = askgenes[k].replace(' ', '') # tira espaços
#


# input das funções
func_list = []
for k in range(len(askgenes)):
    askfunc = input('Função para {0}: '.format(askgenes[k])).strip('\n') # pergunta as funções
    askfunc = askfunc.split(sep=' | ') # separa nos "or"
    func_list.append(askfunc) # adiciona as funções numa lista - cada indexação para um gene
    
for k in range(len(func_list)):
    for j in range(len(func_list[k])):
        func_list[k][j] = func_list[k][j].split(sep = '&') # divide os genes

for k in range(len(func_list)): 
    for j in range(len(func_list[k])):
        for i in range(len(func_list[k][j])):
            func_list[k][j][i] = func_list[k][j][i].replace(' ', '') # tira espaços 
#


# lista de todos os estados possíveis
a = list(product('01', repeat=len(askgenes))) # lista dos estados possíveis dos genes (on/off) - tuplas com a situação de cada gene
state_list = []
for k in range(len(a)):
    state = ''
    for j in range(len(askgenes)):
        state = state + a[k][j]
    state_list.append(state) # lista dos estados possíveis dos genes
#


# interpretação das funções
# func_list[g][i][k] - gene k participa da função de ativação f do gene g
for g in range(len(func_list)):
    activate = set() # zera o set de estados que ativam para cada gene
    for f in range(len(func_list[g])):
        
        # dicionário de relação ativa/desativa/não-participa dos genes para cada função
        func_dict = {} 
        for k in range(len(askgenes)):
            func_dict.update({askgenes[k]: ''}) # index de cada gene
        genes = list(func_dict.keys()) # lista dos index do dicionário para poder percorrer os valores    
        
        for k in range(len(func_list[g][f])): # gene g recebe valor de relação com gene k
            if func_list[g][f][k][0] == '!':
                func_list[g][f][k] = func_list[g][f][k].replace('!','')
                func_dict.update({func_list[g][f][k]: 0}) # !gene k, recebe o valor 0
            else:
                func_dict.update({func_list[g][f][k]: 1})  # gene k, recebe o valor 1
        # se o gene não aparece, seu valor é uma string vazia
        #
     
  
        # set de estados que ativam
        for k in range(len(state_list)): # para cada estado,
            for j in range(len(genes)): 
                if func_dict[genes[j]] != '': # se houver algum gene na função
                    if str(func_dict[genes[j]]) != state_list[k][j]: # cujo valor não corresponde à sua posição nesse estado
                        break # ele não será adicionado no set de ativação
            else:
                activate.add(state_list[k])
        #
    
    # arruma o activate para imprimir igual o do enunciado
    acti_li = []
    for k in range(len(state_list)):
        if state_list[k] in activate:
            acti_li.append(state_list[k])
    print(f'Estados que ativarão {genes[g]}: {acti_li}') # printa a lista activate para cada gene
    #
#
