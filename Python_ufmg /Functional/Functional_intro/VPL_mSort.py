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

def size(L):
    if not L:
        return 0
    else : 
        return 1 + size(tail(L)) 

def sorted(L):
    if not L : 
        return True
    elif not tail(L): 
        return True  
    else: 
        C1 = head(L) <= head(tail(L)) 
        return C1 and sorted(tail(L))  

def sum(L):   
    if not L : 
        return None  
    H0 = head(L) 
    T0 = tail(L) 
    if not T0: 
        count = H0
        return count  
    else :   
        count = H0     
        return count + sum(tail(L))



def split(L):
    if not L : 
        return (None , None) ; 
    elif not tail(L): 
        return (L, None)  
    else : 
        H0 = head(L) 
        H1 = head(tail(L)) 
        (T0,T1)= split(tail(tail(L))) 
        return ((H0,T0), (H1,T1))  


def merge(L0, L1):
    if not L0: 
        return L1 
    elif not L1: 
        return L0   
    else : 
        H0 = head(L0) 
        H1 = head(L1) 
        T0 = tail(L0) 
        T1 = tail(L1) 
        if H0 < H1 : 
            return (H0, merge(T0,L1)) 
        else : 
            return (H1, merge(L0, T1)) 

    
    

def mSort(L):
    if not L : 
        return None  
    elif not tail(L): 
        return L  
    else : 
        (L0 , L1) = split(L) 
        return merge(mSort(L0), mSort(L1)) 

def max(L): 
    py2ll(L)  
    L = mSort(L)  
    H0 = head(L) 
    T0 = tail(L)
    if not T0 : 
        return H0
    else : 
        return max(T0)  
    

def get(L, N): 
    
    if not N:
        return head(L)
    else:
        return get(tail(L),N-1) 
    
