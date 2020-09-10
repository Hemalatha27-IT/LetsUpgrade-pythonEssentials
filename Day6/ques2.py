from math import pi
class cone:
    def __init__(self,radius,height,slat_height):
        self.radius=radius
        self.height=height
        self.slat_height=slat_height
 # Function to calculate Volume of Cone 
    def volume(r, h): 
         return (1 / 3) * pi * r * r * h 
  
 # Function To Calculate Surface Area of Cone 
    def surfacearea(r, s): 
         return pi * r * s + pi * r * r 
  
s=cone(float(13),float(15),float(3))
s.volume(float(13),float(15))
s.surfacearea((float(13),float(15),float(3)))
