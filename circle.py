from figures.figurecolor import *
import math

class Circle():
 
 def _init_(self,radius=5,color=FigureColor()):
  self._radius = radius
  self._color = color
  self._area = math.pi*radius*radius

 def _reper_(self):
  return f"Круг площадью {self._area}, цвет: {str(self._color)}"
