import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


def iterate_matrix(field, max = 500, step = 1):
  # Iteration (We assume that the iteration is convergence in maxIter = 500)
  
  for _ in range(0, max):
      for i in range(1, len(field)-1, step):
          for j in range(1, len(field[0])-1, step):
              field[i, j] = 0.25 * (field[i+1][j] + field[i-1][j] + field[i][j+1] + field[i][j-1])


def plot_heatmap(x,y,field):
    """Creates 3D plot with colored levels
    :param x: array from zero to field's max coordinate
    :param y: array from zero to field's max coordinate
    :param field: 2D matrix for the values of Z
    """
    # # Configure the contour
    plt.title("x(0) = 0; x(a)=arctan(y/a)")
    plt.xlabel("X");
    plt.ylabel("Y")
    plt.contourf(x,y,field, 100, cmap=plt.cm.jet)

    # # Set Colorbar
    plt.colorbar()

    # # Show
    plt.show()




def plot_3d_heatmap(x,y,field):
    """Creates 3D plot with colored levels
    :param x: array from zero to field's max coordinate
    :param y: array from zero to field's max coordinate
    :param field: 2D matrix for the values of Z
    """
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(x,y,field, cmap=plt.cm.jet, linewidth=0, antialiased=True)

    # Color bar
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()
