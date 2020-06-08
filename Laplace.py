import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from modulos import *

# Coordenadas Rectangulares

# Una tuber ́ıa rectangular recta se extiende infinitamente a lo largo del eje z.
# Sus paredes se encuentran en los planos x=0,y=0,x=a y y=b. 
# Los planos y = 0 y y = b se encuentran aterrizados, mientras que los planos
# x = 0 y x = a se encuentran a potenciales g(y) y h(y) respectivamente.

# Matplotlib configurations
square = 35

X, Y = np.meshgrid(np.arange(0, square), np.arange(0, square))
x = np.linspace(0,1,square)
y = np.linspace(0,1,square)

# Set initial values to zero in all cells
T = np.zeros((square,square))

# Set Boundary condition ":" means all items, -1 means last item
# T[:,-1] translates to "all items on last row"
T[:,-1] = np.arctan(y/y[-1])

for n in [0,2,5,10,20]:
  out = iterate_matrix(T, n)
  plot_3d_heatmap(X,Y,out)

