
#encontra o indice do ultimo termode uma string ou lista conforme 

def cap(str): 
    return str[0].capitalize() + "."+ " "
def get(match): 
    value = match[0]  
    modified = cap(value) + match[-1] 
    return modified 

def lastNames(L):
    """Mapeia uma lista de nomes para o ultimo nome de cada item.
    Por exemplo, seja:
    L = [['Antonio', 'Franco'], ['Caius', 'Vitelus'], ['Cristovao', 'Buarque']]
    Entao lastNames(L) == ['Franco', 'Vitelus', 'Buarque']
    """ 
    if not L : return None  
    else :    
        acc = []
        for row in L : acc +=  filter(lambda x: x == row[-1],row) 
        return acc

def citations(L):
    """Mapeia uma lista de nomes para a primeira letra mais sobrenome.
    Por exemplo, seja:
    L = [['Antonio', 'Franco'], ['Caius', 'Vitelus'], ['Cristovao', 'Buarque']]
    entao citations(L) = ['A. Franco', 'C. Vitelus', 'C. Buarque']
    Note que a primeira letra precisa estar capitalizada.
    """
    if not L : 
        return None  
    else :  
        return map(get, L)


def fullCitations(L):
    """Mapeia uma lista de nomes para as iniciais mais o ultimo nome.
    Por exemplo, seja:
    L = [
        ['Antonio', 'Franco', 'Molina'],
        ['Caius', 'vitelus', 'Aquarius'],
        ['cristovao', 'buarque', 'Holanda']]
    entao fullCitations(L) = ['A. F. Molina', 'C. V. Aquarius', 'C. B. Holanda']
    Note que as iniciais precisam estar capitalizada.
    """ 
    if not L : 
        return None  
    else :   
        acc = []
        for row in L :  
            acc += map(lambda x:cap(x) if x!= row[-1] else x, row)
        return acc 
        
