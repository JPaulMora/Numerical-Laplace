import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import copy

IMG_PATH='Informe/images/'

def iterate_matrix(T, max = 20, step = 1):
    field = copy.deepcopy(T)
    for _ in range(0, max):
        for i in range(1, len(field)-1, step):
            for j in range(1, len(field[0])-1, step):
                field[i, j] = 0.25 * (field[i+1][j] + field[i-1][j] + field[i][j+1] + field[i][j-1])

    return field

def iterate_matrix_3d(T, max = 20, step = 1):
    field = copy.deepcopy(T)
    for _ in range(0, max):
        for i in range(1, len(field)-1, step):
            for j in range(1, len(field[0])-1, step):
                for k in range(1, len(field[0][0]) -1, step):
                    field[i, j, k] = 1/6 * (field[i+1][j][k] + field[i-1][j][k] + field[i][j+1][k] + field[i][j-1][k] + field[i][j][k+1] + field[i][j][k-1])

    return field

def plot_heatmap(x,y,field, name,title=""):
    """Creates 3D plot with colored levels
    :param x: array from zero to field's max coordinate
    :param y: array from zero to field's max coordinate
    :param field: 2D matrix for the values of Z
    """
    plt.title("x(0) = 0; x(a)=arctan(y/a)")
    plt.xlabel("X");
    plt.ylabel("Y")
    plt.contourf(x,y,field, 100, cmap=plt.cm.jet)
    plt.contour(x,y,field,100, colors='black');
    plt.title = title+" n=20"

    # # Set Colorbar
    plt.colorbar()
    plt.savefig(IMG_PATH + name + "-density", dpi=200)

def plot_3d_heatmap(x,y,field,name,n,title=""):
    """Creates 3D plot with colored levels
    :param x: array from zero to field's max coordinate
    :param y: array from zero to field's max coordinate
    :param field: 2D matrix for the values of Z
    :param name: Filename base
    :n: iteration number
    """
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.view_init(elev=40, azim=-130)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set(title=title+" n="+str(n))
    surf = ax.plot_surface(x,y,field, cmap=plt.cm.jet, linewidth=0, antialiased=True)

    # Color bar
    fig.colorbar(surf, shrink=0.5, aspect=5)
    fig.savefig(IMG_PATH + name + "-n" + str(n), dpi=200)

def plot_4d_heatmap(x,y,field,name,n,title=""):
    """Creates 3D plot with colored levels
    :param x: array from zero to field's max coordinate
    :param y: array from zero to field's max coordinate
    :param field: 2D matrix for the values of Z
    :param name: Filename base
    :n: iteration number
    """
    planes = 5
    planes_offset = int(len(field)/planes)

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.view_init(elev=40, azim=-40)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set(title=title+" n="+str(n))

    for z in range(0,len(field), planes_offset):
        ax.plot_surface(x,y,field[z]+z, cmap=plt.cm.jet, linewidth=0, antialiased=False, alpha=0.3)

    # Color bar
    # fig.colorbar(surf, shrink=0.5, aspect=5)
    fig.savefig(IMG_PATH + name + "-n" + str(n), dpi=200)


def plot_electric_field(x,y,field,name):
    """Creates gradient fields from a vector matrix
    :param x: array from zero to field's max coordinate
    :param y: array from zero to field's max coordinate
    :param field: (2D,2D) matrix for the vector's position and distance
    :param name: Filename base
    """
    dy, dx = np.gradient(field)
    fig, ax = plt.subplots()
    ax.quiver(x, y, -dx, -dy, field)
    ax.set(aspect=1, title="Campo eléctrico en n=20")
    fig.savefig(IMG_PATH + name + "-field", dpi=400)

