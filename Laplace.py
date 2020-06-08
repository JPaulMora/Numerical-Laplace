import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from modulos import *
from scipy import ndimage

# Coordenadas Rectangulares

# Una tuber ́ıa rectangular recta se extiende infinitamente a lo largo del eje z.
# Sus paredes se encuentran en los planos x=0,y=0,x=a y y=b. 
# Los planos y = 0 y y = b se encuentran aterrizados, mientras que los planos
# x = 0 y x = a se encuentran a potenciales g(y) y h(y) respectivamente.

# Matplotlib configurations
square = 70

X, Y = np.meshgrid(np.arange(0, square), np.arange(0, square))
x = np.linspace(0,1,square)
y = np.linspace(0,1,square)

# Set initial values to zero in all cells
# T = np.zeros((square,square))
T = np.empty((square,square))
T.fill(0)

# Set Boundary condition ":" means all items, -1 means last item
# T[:,-1] translates to "all items on last row"

# plano Y = b es 0 
# T[-1,:] = 0
# plano Y = 0 es 0
# T[0,:] = 0
# plano X = b es 0 
T[:,-1] = np.arctan(y/y[-1])


# T[:,-1] = 2*y**3+5
# T[:,0] = 2*y**3+5

name = "arctan"
title = "h(y) = arctan(y/a)"

for n in [0,2,5,10,20]:
  out = iterate_matrix(T, n)
  plot_3d_heatmap(X,Y,out, name, n, title)

  if n is 20:
    plot_electric_field(x,y,out, name)
    lap = -10* ndimage.laplace(out)
    title = "densidad de carga " + title
    plot_heatmap(X,Y,lap,name,title)
    # plot_3d_heatmap(X,Y,lap, name+"-density", 0, title)

