#TPC3

import random 
lista=[]
continuar= True

def criaLista(N):
    lista = []
    i=0
    while i<N:
        lista.append(random.randint(1,100))
        i=i+1
    return lista

def lerLista(N):
    lista = []
    for i in range(N):
        num=int(input(f"Introduza um número: {i+1} /{N} "))
        lista.append(num)
    return lista

def somaLista(lista):
    soma=0
    for elem in lista:
        soma=soma+elem
    return soma

def mediaLista(lista):
    soma=somaLista(lista)
    return soma/len(lista)

def maiorLista(lista):
    maior=lista[0]
    for elem in lista[1:]:
        if elem>maior:
            maior=elem
    return maior

def menorLista(lista):
    menor=lista[0]
    for elem in lista[1:]:
        if elem<menor:
            menor=elem
    return menor

def ordenacrescente(lista):
    anterior = lista[0]
    for atual in lista[1:]:
        if atual < anterior:   
            print("NÃO, a lista não está ordenada por ordem crescente!")
            return
        anterior = atual      
    print("SIM, a lista está ordenada por ordem crescente!")

def ordenadecrescente(lista):
    anterior = lista[0]
    for atual in lista[1:]:
        if atual > anterior:   
            print("NÃO, a lista não está ordenada por ordem decrescente!")
            return
        anterior = atual      
    print("SIM, a lista está ordenada por ordem decrescente!")

def procurarelem(lista,elem):
    if elem in lista:
        return lista.index(elem)
    else:
        return -1


while continuar==True:
    print("""Menu:
    (1) Criar Lista 
    (2) Ler Lista
    (3) Soma
    (4) Média
    (5) Maior
    (6) Menor
    (7) estaOrdenada por ordem crescente
    (8) estaOrdenada por ordem decrescente
    (9) Procura um elemento
    (0) Sair
                """)
    menu=int(input("O que deseja fazer? "))
    if menu not in range(0,10):
        menu=int(input("Por favor insira um número de 0 a 9!"))
        continue
    if menu==1:
        N=int(input("Quantos elementos quer adicionar à lista? "))
        lista=criaLista(N)
        print("Lista criada:", lista)
    elif menu==2:
        N=int(input("Quantos elementos quer adicionar à lista? "))
        lista=lerLista(N)
        print("Lista criada:", lista)
    elif menu==3:
        print("A soma dos elementos da lista é ", somaLista(lista))
    elif menu==4:
        print("Média=",mediaLista(lista))
    elif menu==5:
        if len(lista)>0:
            print("O maior elemento da lista é:", maiorLista(lista))
        else:
            print("A lista está vazia, crie uma lista primeiro!")
    elif menu==6:
        if len(lista)>0:
            print("O menor elemento da lista é:",menorLista(lista))
        else:
            print("A lista está vazia, crie uma lista primeiro!")
    elif menu==7:
        if len(lista)>0:
            ordenacrescente(lista)
        else:
            print("A lista está vazia, crie uma lista primeiro!")
    elif menu==8:
        if len(lista)>0:
            ordenadecrescente(lista)
        else:
            print("A lista está vazia, crie uma lista primeiro!")
    elif menu==9:
        elemento=int(input("Que elemento da lista quer procurar? "))
        posição=procurarelem(lista, elemento)
        if posição==-1:
            print("Elemento não encontrado.")
        else:
            print(f"Elemento encontrado na posição {posição}.")
    else:
        print("Programa terminado. Lista final:", lista)
        continuar=False


