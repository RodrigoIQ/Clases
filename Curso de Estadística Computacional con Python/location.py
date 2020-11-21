class Location:
    def __init__(self,x,y,):
        self.x = x
        self.y = y 
    
    def movement(self, delta_x, delta_y):
        return Location(self.x + delta_x, self.y + delta_y)

    def distance(self, otra_cordenada):
        delta_x = self.x - otra_cordenada.x
        delta_y = self.y - otra_cordenada.y

        return(delta_x**2 + delta_y**2)**0.5
