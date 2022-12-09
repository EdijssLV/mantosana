import math
class Punkts:
  def __init__(self, x_cord, y_cord):
    self.x_cord = x_cord
    self.y_cord = y_cord
  def cordinates(self):
    vector = math.sqrt(self.x_cord**2+self.y_cord**2)
    return vector
  def output(self):
    return [self.x_cord, self.y_cord]

class PunktaKrasa(Punkts):
  def __init__(self, x_cord, y_cord, color):
    self.x_cord = x_cord
    self.y_cord = y_cord
    self.color = color
  def krasaoutpur(self):
    return self.color

x_cord = int(input("x cords: "))
y_cord = int(input("y cords: "))
color = input("ievadiet color plz: ")

dot = PunktaKrasa(x_cord, y_cord, color)
print("punkta cords ir",dot.output(), "vektors ir",dot.cordinates(),"krasa ir",dot.krasaoutpur())
