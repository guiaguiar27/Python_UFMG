# -*- coding: utf8

from bs4 import BeautifulSoup
from functools import reduce
from collections import Counter
import multiprocessing as mp
import tarfile 



def extract_and_process(member):
    # observe como cada processo abre o tar novamente
    # a extração é feita por processo
    # veja exemplos do HTML na pasta exemplo
    # Para pegar o nome de um artist use texto.strip().split('-')[-1].
    # O formato do texto no html é Música - Artista
    
    # TODO: implemente o resto
    tar = tarfile.open("dados.tar.gz", "r:gz")
    f = tar.extractfile(member)
    soup = BeautifulSoup(f, 'html.parser')  
    #nome da muscia   
    # cada processo vai realizar a leitura em um html diferente  
    count = 0  
    L = [] 
    for i in soup.findAll(class_ = "trackName"):  
        aux = i.string  
        name = aux.strip().split('-')[-1]   
        covered =  soup.findAll(class_ = "listEntry trackCompactEntry")[count].find(class_ = "trackInfo").find(class_ = "counts")  
        count_1= covered.string  
        count_aux =  count_1.split(' ')
        times = count_aux[1]
        time_aux = int(times) 
        count +=1  
        for j in range(time_aux): 
            L.append(name) 
    return Counter(L)


def merge_function(dict_1, dict_2):
    
    return Counter(dict_1 + dict_2)


def mapreduce(num_cpus=2):
    tar = tarfile.open('dados.tar.gz', 'r:gz')
    if num_cpus > 1:
        with mp.Pool(num_cpus) as pool:
            intermed = pool.imap_unordered(extract_and_process,
                                           tar.getmembers())
    else:
        intermed = map(extract_and_process, tar.getmembers())
    final = reduce(merge_function, intermed)
    return final