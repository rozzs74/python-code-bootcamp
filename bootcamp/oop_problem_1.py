# Description: Program that returns slope and distance of line using class by passing x and y coordinates
# Author: John Royce Punay
# Date created: March 10, 2018 6:03 PM
# Hints:
# Slope formula = m = (y2 - y1 / x2 - x1)
# Distnace formula = sqrt(squared(x2-x1) + square(y2-y1))

class Line():

    slope = None
    distance = None

    def __init__(self, coordinates1, coordinates2):
        self.coordinates1 = coordinates1
        self.coordinates2 = coordinates2

    def get_distance(self):
        Line.distance = ((self.x_coordinates_difference()**2) + (self.y_coordinates_difference()**2))**0.5
        return Line.distance

    def get_slope(self):
        Line.slope = (self.y_coordinates_difference() / self.x_coordinates_difference())
        return Line.slope

    def x_coordinates_difference(self):
        x1 = self.coordinates1[0] 
        x2 = self.coordinates2[0] 
        return (x2 - x1)

    def y_coordinates_difference(self):
        y1 = self.coordinates1[1] 
        y2 = self.coordinates2[1] 
        return (y2 - y1)
    
coordinate1 = (3, 2)
coordinate2 = (8, 10)
myline = Line(coordinate1, coordinate2)

print(f"Slope: {myline.get_slope()}")
print(f"Distance: {myline.get_distance()}")