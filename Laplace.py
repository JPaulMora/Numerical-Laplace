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
n = 0

X, Y = np.meshgrid(np.arange(0, square), np.arange(0, square))
x = np.linspace(0,1,square)
y = np.linspace(0,1,square)

# Set initial values to zero in all cells
T = np.zeros((square,square))

# Set Boundary condition
T[-1,:] = np.arctan(y/y[-1])

iterate_matrix(T, n)

# plot_heatmap(X,Y,T)
plot_3d_heatmap(X,Y,T)
