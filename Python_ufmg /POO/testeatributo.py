class Testeatributo: 
    atributo_class = 0  

    def __init__(self): 
        self.atributo_instancia = 1   

obj_1  = Testeatributo() 
print(Testeatributo.atributo_class)  
obj_1.atributo_instancia += 2 
print(obj_1.atributo_instancia)

obj_2 = Testeatributo() 
print(Testeatributo.atributo_class)  
print(obj_2.atributo_instancia)
