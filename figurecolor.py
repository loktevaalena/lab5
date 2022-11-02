class FigureColor:

 def _init_(self,r=1,g=0,b=0):
  self._R = r
  self._G = g
  self._B = b
 
 def get_color(self):
  return (self._R,self._G,self._B)

 def set_color(self,r,g,b):
  self._R = r
  self._G = g
  self._B = b
 def _reper_(self):
  return f"R:{self._R},G:{self._G},B:{self._B}"
