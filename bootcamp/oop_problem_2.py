# Description: Program that returns Cylinder's volume and surface area
# Author: John Royce Punay
# Date created: March 10, 2018 7:21 PM
# Hints:
# Cylinder volume formula = pi * squared(radius) * height
# Surface area formula = ((2 * pi * radius * h) + (2 * pi * square(radius)))

class Cylinder():

    pi = 3.14

    def __init__(self, height, radius):
        self.height = height
        self.radius = radius        
    
    def get_volume(self):
        return (self.get_pi_radius_squared() * self.height)

    def get_surface_area(self):
        return ((2 * Cylinder.pi * self.radius * self.height) + (2 * self.get_pi_radius_squared()))
    
    def get_pi_radius_squared(self):
        return Cylinder.pi * ((self.radius)**2)


c = Cylinder(2, 3)
print(f"Cylinder Volume: {c.get_volume()}")
print(f"Cylinder Surface area: {c.get_surface_area()}")