class Item: 
    def __init__(self, nome, valor): 
        self.nome = nome  
        self.valor = valor   
    
class Livro(Item): 
    def __init__(self, nome, valor):
        super().__init__(nome, valor) 
        self.desconto  = 0.03  
        self.tipo = "Livro"
class Brinquedo(Item): 
    def __init__(self, nome, valor):
        super().__init__(nome, valor) 
        self.desconto  = 0.05 
        self.tipo = " Brinquedo"
class Eletronico(Item): 
    def __init__(self, nome, valor):
        super().__init__(nome, valor) 
        self.desconto  = 0.08 
        self.tipo = "Eletronico"
   
 #recebe os itens    
class CestaCompras(Item):  
    def __init__(self):  
        self.itens = { }  

    def adicionar_item(self,item, qtde): 
        Item.__init__(self, item.nome , item.valor)
        self.itens[item] = qtde   
    
    def relatorio_final(self):  
        valor_total_d = valor_total_s = aux_valor_uni_d =  aux_valor_uni_s = 0
        for i in (self.itens): 
            #desconto    
            
            aux_valor_uni_d = self.itens[i]*(i.valor - (i.valor * i.desconto)) 
            valor_total_d  = valor_total_d  + aux_valor_uni_d    
            aux_valor_uni_s = self.itens[i]*i.valor  
            valor_total_s = valor_total_s + aux_valor_uni_s      
        print("{:.2f}".format(valor_total_d))  
        for i in (self.itens):  
            aux_desc =  i.valor - (i.valor * i.desconto )
            desc = self.itens[i] * aux_desc    
            s_desc = self.itens[i] * i.valor
            print(i.tipo, i.nome, self.itens[i]," {:.2f}, {:.2f}, {:.2f}".format(i.valor, s_desc , desc) ) 