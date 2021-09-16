'''
Faça um programa que receba uma lista de genes e uma única função de regulação simples, 
que não contém o operador or (' | ') e imprima uma lista dos estados estados que podem ativar o suposto gene.

Exemplo de execução:

Nomes dos genes (separados por vírgula): A,B,C
Função: !A&B
['010', '011']

'''
# seu código aqui
from itertools import product


askgenes = input('Nomes dos genes (separados por vírgula): ')
askgenes = askgenes.split(sep=',') # separa os nomes dos genes e coloca numa lista
for k in range(len(askgenes)):
    askgenes[k] = askgenes[k].replace(' ', '') # tira espaços que possam atrapalhar na leitura eventualmente

askfun = input('Função: ')
func_list = askfun.split('&') # pede a função e divide os genes citados
for k in range(len(func_list)):
    func_list[k] = func_list[k].replace(' ', '') # tira espaços que possam atrapalhar na leitura eventualmente


func_dict = {} 
for k in range(len(askgenes)):
    func_dict.update({askgenes[k]: ''}) # cria um dicionário de relação entre os genes
    
    

for k in range(len(func_list)): # aqui, os genes recebem valores de relação
    if func_list[k][0] == '!':
        func_list[k] = func_list[k].replace('!','')
        func_dict.update({func_list[k]: 0}) # se o gene aparece na função com ! na frente, recebe o valor 0 no dicionario
    else:
        func_dict.update({func_list[k]: 1})  # se o gene aparece na função, recebe o valor 1 no dicionário
# se o gene não aparece, seu valor é uma string vazia



a = list(product('01', repeat=len(askgenes))) # lista dos estados possíveis dos genes (on/off) - tuplas com a situação de cada gene
state_list = []
for k in range(len(a)):
    state = ''
    for j in range(len(askgenes)):
        state = state + a[k][j]
    state_list.append(state) # lista dos estados possíveis dos genes - strings representando a situação dos genes respectivamente



genes = list(func_dict.keys()) # lista dos index do dicionário, para poder percorrer os valores
activate = [] # lista de estados que ativam
for k in range(len(state_list)): # para cada estado,
    for j in range(len(genes)): 
        if func_dict[genes[j]] != '': # se houver algum gene na função
            if str(func_dict[genes[j]]) != state_list[k][j]: # cujo valor não corresponde à sua posição nesse estado
                break # ele não será adicionado na lista de ativação
    else:
        activate.append(state_list[k])
        
print(activate)
    
