import math  
class circ : 
    def area(self,r):  
        
        area = math.pi*r*r 
        return area   

circle = circ() 
radio = float(input(" Radio: ")) 
a = circle.area(radio)
print(a) 
