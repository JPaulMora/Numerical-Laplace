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
colorinterpolation = 100
colourMap = plt.cm.jet


n = 1
a = 50
b = 50

X, Y = np.meshgrid(np.arange(0, b), np.arange(0, a))

# Set initial values to zero in all cells
T = np.empty((a, b))
T.fill(0)

# Set Boundary condition

# Y = b
T[(b-1):, :] = 0
# Y = 0
T[:1, :] = 0

# X = a
# T[:, (a-1):] = 0
# X = 0
# T[:, :1] = 0

for i in range(a):
  T[:, (a-1):][i] = np.arctan(i/a)

nx = 41
ny = 41

x = np.linspace(0,1,nx)
y = np.linspace(0,1,ny)

p_an = p_analytical(x,y)

plot_3D(a,b,p_an)

# iterateMatrix(T, n)

# # Configure the contour
# plt.title("x(0) = 0; x(a)=arctan(y/a)")
# plt.xlabel("X");
# plt.ylabel("Y")
# plt.contourf(X, Y, T, colorinterpolation, cmap=colourMap)

# # Set Colorbar
# plt.colorbar()

# # Show
# plt.show()
