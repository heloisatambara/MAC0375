## Exercício Programa 1 ######################################################
#  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP,             #
#  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA.             #
#  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM              #
#  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES               #
#  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA             #
#  OU PLÁGIO.                                                                 #
#  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS                     #
#  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A                       #
#  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E                    #
#  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS                #
#  DIVULGADOS NA PÁGINA DA DISCIPLINA.                                        #
#  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,                     #
#  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.              #
#                                                                             #
#  Nome : Heloisa Tambara Paiva                                               #
#  NUSP : 12556819                                                            #
#  Turma: MAC0375                                                             #
#  Prof.:                                                                     #
###############################################################################

'''Referências aqui'''

'''
Exemplo de arquivo de entrada:

A,    !A&C
B,    !A&!B
C,    A&B

Exemplo de execução:

arquivo: exemplo.txt
atrator: ['000', '010'] tamanho da bacia: 5
atrator: ['001', '110'] tamanho da bacia: 3

'''
#seu código aqui
# importações
from itertools import product
#

'''
# input dos genes
askgenes = input('Nomes dos genes (separados por vírgula): ')
askgenes = askgenes.split(sep=',') # separa os nomes dos genes e coloca numa lista
for k in range(len(askgenes)):
    askgenes[k] = askgenes[k].replace(' ', '') # tira espaços
#
'''

# recieving functions and genes
getgenes = open('E:/usp/programacoes/mac/MAC0375/example.txt','r') 
genfunlist = getgenes.readlines() 

genes = []
func_list = []
for k in range(len(genfunlist)):
    genfunlist[k] = genfunlist[k].replace('\n', '').replace(' ','') # delete blank spaces and jump lines
    genfunlist[k] = genfunlist[k].split(',') 
    genes.append(genfunlist[k][0]) # get a list of the genes
    getfunc = genfunlist[k][1] 
    getfunc = getfunc.split(sep='|')
    func_list.append(getfunc) # get a list of the functions - each index is the function of a gene
    
for k in range(len(func_list)):
    for j in range(len(func_list[k])):
        func_list[k][j] = func_list[k][j].split(sep = '&') # split on each participation of the gene for each function of each gene
#

# lista de todos os estados possíveis
a = list(product('01', repeat=len(genes))) # lista dos estados possíveis dos genes (on/off) - tuplas com a situação de cada gene
state_list = []
for k in range(len(a)):
    state = ''
    for j in range(len(genes)):
        state = state + a[k][j]
    state_list.append(state) # lista dos estados possíveis dos genes
#

aux = []
# interpretação das funções
# func_list[g][i][k] - gene k participa da função de ativação f do gene g
for g in range(len(func_list)):
    activate = set() # zera o set de estados que ativam para cada gene
    for f in range(len(func_list[g])):
        
        # dicionário de relação ativa/desativa/não-participa dos genes para cada função
        func_dict = {} 
        for k in range(len(genes)):
            func_dict.update({genes[k]: ''}) # index de cada gene
        
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
    aux.append(acti_li)
    #

# create the state paths
for k in range(len(genes)):
    func_dict.update({genes[k]: ''})
    
attractors = []
allpaths = []
for k in range(len(state_list)):
    for i in range(len(allpaths)):
        if state_list[k] in allpaths[i]:
            a = 0
            break
        else: a = 1
    if a:
        path = []
        state = state_list[k]
        while state not in path: # stop when a state goes back to the path
            path.append(state)
            next_state = ''
            for j in range(len(genes)):
                if state in aux[j]: 
                    func_dict.update({genes[j]: 1})
                    next_state += '1'
                else: next_state += '0' # if the current state activates a gene, it recieves "1", else it recieves "0"
            state = next_state # the new state will be the current in the next loop
            if state in path:
                for k in range(len(path)): 
                    if path[k] == state:
                        if path[k:] not in attractors:
                            attractors.append(path[k:]) # predicts if the loop will stop, then add the chain of attraction to a list of attractors, if it's not already there
        allpaths.append(path) 
#

# create the attraction bays
bays = []
for j in range(len(attractors)):
    bayj =[]
    for k in range(len(allpaths)):
        for l in range(len(attractors[j])):
            if attractors[j][l] not in allpaths[k]:
                b = 0
                break
        else: b = 1
        if b:
            for i in range(len(allpaths[k])):
                if allpaths[k][i] not in bayj:
                    bayj.append(allpaths[k][i])
    bays.append(bayj)
    print(f'atrator: {attractors[j]} tamanho da bacia: {len(bays[j])}')
#

