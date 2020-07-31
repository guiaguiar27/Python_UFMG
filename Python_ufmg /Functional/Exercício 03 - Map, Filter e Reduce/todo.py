import operator 
from collections import Counter 
def py2llInvert(L):
    if not L:
         return None
    else:
        return (L[-1], py2llInvert(L[0:-1])) 
def reduce(L, f, inic):
    if not L:
        return inic
    else: 
        return f(head(L),reduce(tail(L), f, inic))
def size(L): 
    if not L:
        return 0
    else : 
        return 1 + size(tail(L)) 
def head(L):
    return L[0]
 
def tail(L):
    return L[1]

def py2ll(L):   
    if not L : 
        return None 
    else : 
        #retorna elemento recursivo  
        return (L[0], py2ll(L[1:])) 

def ll2py(L): 
    if not L:
        return []
    else:
        return [head(L)] + ll2py(tail(L))
def mapL(L, f):
     if not L:
         return None
     else:
         return (f(head(L)), mapL(tail(L), f))
def filterL(L, f):
    if not L:
        return None
    else:
         T = filterL(tail(L), f)
         H = head(L)
         return (H, T) if f(H) else T
def most_common(lst):
    return max(set(lst), key=lst.count) 

def firstChars(L): 
    # return a list map 
    """ Maps strings in L to a list with the first character of each string.
    For instance:
    firstChars(['python', 'is', 'pythy']) == ['p', 'i', 'p']
    """  
    return ll2py(mapL(py2ll(L), lambda x: x[0]))

def sum(L): 
    #return a value reduce 
    """ Sums the elements in L """
    return reduce(py2ll(L),lambda acc, b : acc + b, 0)

def avg(L):
    def Len(L):
        if not L: return 0
        else: return 1 + Len(tail(L))
    return sum(L) / Len(py2ll(L))        


def maxString(L): 
    #return a value use reduce 
    """ Retorna a maior string dentre as strings em L.
    Por exemplo: maxString(['python', 'is', 'pythy']) == 'python'
    Se houver empate, retorna a primeira string encontrada.
    """ 
    return reduce(py2llInvert(L),lambda x, y: y if len(y)>len(x) else x, '' )

def add2Dict(D, N, S):
    """ Insere a string S na lista associada ao inteiro N dentro
    do dicionario D.
    Por exemplo, se D = {1: ['b'], 2: ['xd'], 3: ['abc']}, entao,
    add2Dict(D, 2, 'ww') produz o novo dicionario:
    {1: ['b'], 2: ['xd', 'ww'], 3: ['abc']}
    Voce pode usar essa funcao para completar buildLenFreq
    """
    D[N] = D[N] + [S] if N in D else [S]
    return D

def buildLenFreq(L):
    """ Esta funcao constroi um dicionario que associa inteiros a listas com
    palavras daquele tamanho. Por exemplo:
    ins(['abc', 'xd', 'b', 'xxx']) = {1: ['b'], 2: ['xd'], 3: ['abc', 'xxx']}
    """
    D = { }  

    return reduce(py2llInvert(L), lambda b, acc : add2Dict(acc, len(b), b), {})

def incValue(D, N): 
    #return a dictionary 
    """Esta funcao incrementa o valor associado a chave N dentro do dicionario
    D. Por exemplo, se D = {1: 2, 2: 4, 3: 11}, entao
    Voce pode usar essa funcao para completar countFirsts
    """ 
    D[N] = D[N] + 1 if N in D else 1
    return D


def countFirsts(L): 
    #return a dictionary  
    """ Conta o numero de ocorrencias do primeiro caracter de cada string em L.
    Por exemplo, countFirsts(['python', 'is', 'pythy']) === {'i': 1, 'p': 2}
    Note que essa funcao retorna um dicionario com cada caracter associada ao
    numero de strings que comecam com aquele caracter.
    """ 
    if not L: 
        return None 
    #primeiras letras 
    else : 
        
        return reduce(py2llInvert(L), lambda b, acc : incValue(acc, b[0]), {})



def mostCommonFirstChar(L):
    #return a value use reduce 
    """ Retorna a letra mais comum entre as primeiras letras de strings em L.
    Por exemplo:
    mostCommonFirstChar(['python', 'is', 'pythy']) === 'p' 
    L_aux = ['p','i','p'] 

    """ 
    dic = countFirsts(L)
    return reduce(mapL(py2ll(L), lambda x: x[0]) ,lambda x, y : x[0] if dic[x[0]]>=dic[y[0]] else y[0],  L[0])
    #return functools.reduce(lambda acc ,b : acc if acc in b else b ,map(op, D)) 
