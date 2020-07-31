# -*- coding: utf8


from collections import Counter # RECOMENDADO!

def conta_um_arquivo(fpath):   
    aux = [ ]
    with open(fpath) as input_file:
        for line in input_file:
            line = line.lower().strip()
            if line:
                palavras = line.split() 
                aux += palavras   
        count = Counter(aux)
    return count 
                



def reduz(contagens_1, contagens_2):
          
    return Counter(contagens_1 + contagens_2)
    