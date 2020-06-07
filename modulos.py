from matplotlib import pyplot
from matplotlib import cm
import numpy as np


def iterateMatrix(field, max = 500, step = 1):
  # Iteration (We assume that the iteration is convergence in maxIter = 500)
  
  for _ in range(0, max):
      for i in range(1, len(field)-1, step):
          for j in range(1, len(field[0])-1, step):
              field[i, j] = 0.25 * (field[i+1][j] + field[i-1][j] + field[i][j+1] + field[i][j-1])

def p_analytical(x, y):
    X, Y = np.meshgrid(x,y)

    p_an = np.sinh(1.5*np.pi*Y / x[-1]) /\
    (np.sinh(1.5*np.pi*y[-1]/x[-1]))*np.sin(1.5*np.pi*X/x[-1])

    return p_an

def plot_3D(x, y, p):
    '''Creates 3D plot with appropriate limits and viewing angle

    Parameters:
    ----------
    x: array of float
        nodal coordinates in x
    y: array of float
        nodal coordinates in y
    p: 2D array of float
        calculated potential field

    '''
    fig = pyplot.figure(dpi=100)
    ax = fig.gca(projection='3d')
    X,Y = np.meshgrid(x,y)
    surf = ax.plot_surface(X,Y,p[:], rstride=1, cstride=1, cmap=cm.viridis,
            linewidth=0, antialiased=False)

    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_zlabel('$z$')
    ax.view_init(30,45)
