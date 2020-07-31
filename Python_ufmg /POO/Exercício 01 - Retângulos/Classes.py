class Ponto2D:
    def __init__(self, x= 0.0 , y= 0.0 ): 
        self.x = x  
        self.y = y 
class Retangulo(Ponto2D): 
    def __init__(self, esq_sup , dir_inf ): 
        self.__esq_sup = esq_sup 
        self.__dir_inf = dir_inf   
    @property 
    def esq_sup(self): 
        return self.__esq_sup 
    @property 
    def dir_inf(self): 
        return self.__dir_inf 

    @property 
    def width(self): 
        return abs(self.__dir_inf.x - self.__esq_sup.x) 
    @property 
    def height(self): 
        return abs(self.__esq_sup.y - self.__dir_inf.y)
         
    def calcularArea(self):  
        area = self.width * self.height 
        return area  

    def calcularIntersecao(self, Retangulo):  
        limites_x = sorted([Retangulo.esq_sup.x, Retangulo.dir_inf.x, self.esq_sup.x , self.dir_inf.x]) 
        limites_y = sorted([Retangulo.esq_sup.y, Retangulo.dir_inf.y, self.esq_sup.y , self.dir_inf.y]) 
        n_retangulo_x , n_retangulo_y = limites_x[1:3] , limites_y[1:3]  
        width, height = abs(n_retangulo_x[1] - n_retangulo_x[0]), abs(n_retangulo_y[1] - n_retangulo_y[0]) 
        PC = [n_retangulo_x[0]+width/2. , n_retangulo_y[0]+ height/2.] 
        lim_ret = [sorted([Retangulo.esq_sup.x ,Retangulo.dir_inf.x]),sorted([Retangulo.esq_sup.y ,Retangulo.dir_inf.y])] 
        lim_self = [sorted([self.esq_sup.x , self.dir_inf.x]),sorted([Retangulo.esq_sup.y ,Retangulo.dir_inf.y])]          
        if lim_ret[0][0] < PC[0] and PC[0]< lim_ret[0][1]: 
            if lim_ret[1][0]<PC[1] and PC[1]<lim_ret[1][1]: 
                if lim_self[0][0]<PC[0] and PC[0]<lim_self[0][1]: 
                    if lim_self[1][0]<PC[1] and PC[1]<lim_self[1][1]: 
                        return width*height 
        
        return None 
              



