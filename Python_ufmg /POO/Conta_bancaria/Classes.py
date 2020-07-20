class Conta: 

    def __init__(self, numero):  
        self.numero = numero
        self.saldo  = 0  

    def depositar(self, valor): 
        self.saldo = self.saldo + valor  
         

    def sacar(self, valor): 
        self.saldo = self.saldo -  valor  
        return self.saldo  
   
class ContaCorrente(Conta): 
   
    def __init__(self,conta,  taxa = 1.5): 
        self.taxa = taxa     
        Conta.__init__(self, conta)   
    def cobrar_taxa(self): 
        self.sacar(self.taxa)

class ContaPoupanca(Conta): 
    def __init__(self,conta , juros= 0.05): 
        self.juros = juros 
        Conta.__init__(self, conta)
    def aplicar_juros(self):  
        aux_value = self.saldo*self.juros  
        self.depositar(aux_value) 