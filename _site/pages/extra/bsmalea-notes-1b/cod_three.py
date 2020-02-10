from mpl_toolkits import mplot3d
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.colors import LinearSegmentedColormap
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from scipy.constants import golden
from matplotlib.animation import FuncAnimation
from celluloid import Camera

plt.rcParams.update({'figure.max_open_warning': 0})

mpl.rc("text", usetex=True)
mpl.rc("font", family="serif")


X = np.array([
    [0.33, 0.88, 0.11],
    [0.74, 0.54, 0.62],
    [0.79, 0.07, 0.31],
    [0.83, 0.24, 0.47],
    [0.05, 0.42, 0.47],
    [0.82, 0.70, 0.10],
    [0.51, 0.76, 0.51],
    [0.71, 0.92, 0.59],
    [0.78, 0.19, 0.05],
    [0.43, 0.53, 0.53]
])
t = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])




for angle in range(0,720):
    angle = angle/2
    fig = plt.figure(figsize=(6,6))

    ax = fig.add_subplot(111, projection="3d")

    ax.scatter3D(X[:5,0], X[:5,1], X[:5,2],
        edgecolor = "magenta",
        facecolor=(0,0,0,0),
        s = 17.5,
        marker = "o",
        label = "Class 0"
    )
    ax.scatter3D(X[5:,0], X[5:,1], X[5:,2],
        edgecolor = "turquoise",
        facecolor=(0,0,0,0),
        s = 17.5,
        marker = "o",
        label = "Class 1"
    )

    ### FIRST POINT
    ax.add_collection3d(Poly3DCollection(
        [
            [[0.2,0.8,0], [0.4,0.8,0], [0.4,1.0,0], [0.2,1.0,0]],
            [[0.2,0.8,0], [0.4,0.8,0], [0.4,0.8,0.2], [0.2,0.8,0.2]],
            [[0.2,0.8,0], [0.2,1.0,0], [0.2,1.0,0.2], [0.2,0.8,0.2]],
            [[0.4,1.0,0.2], [0.2,1.0,0.2], [0.2,0.8,0.2], [0.4,0.8,0.2]],
            [[0.4,1.0,0.2], [0.2,1.0,0.2], [0.2,1.0,0], [0.4,1.0,0]],
            [[0.4,1.0,0.2], [0.4,0.8,0.2], [0.4,0.8,0], [0.4,1.0,0]]
        ],
        facecolors="magenta",
        linewidths=0.5,
        edgecolors="k",
        alpha=0.2)
    )
    ### SECOND POINT
    ax.add_collection3d(Poly3DCollection(
        [
            [[0.6,0.4,0.6], [0.8,0.4,0.6], [0.8,0.6,0.6], [0.6,0.6,0.6]],
            [[0.6,0.4,0.6], [0.8,0.4,0.6], [0.8,0.4,0.8], [0.6,0.4,0.8]],
            [[0.6,0.4,0.6], [0.6,0.6,0.6], [0.6,0.6,0.8], [0.6,0.4,0.8]],
            [[0.8,0.6,0.8], [0.6,0.6,0.8], [0.6,0.4,0.8], [0.8,0.4,0.8]],
            [[0.8,0.6,0.8], [0.6,0.6,0.8], [0.6,0.6,0.6], [0.8,0.6,0.6]],
            [[0.8,0.6,0.8], [0.8,0.4,0.8], [0.8,0.4,0.6], [0.8,0.6,0.6]]
        ],
        facecolors="magenta",
        linewidths=0.5,
        edgecolors="k",
        alpha=0.2)
    )
    ### THIRD POINT
    ax.add_collection3d(Poly3DCollection(
        [
            [[0.6,0.0,0.2], [0.8,0.0,0.2], [0.8,0.2,0.2], [0.6,0.2,0.2]],
            [[0.6,0.0,0.2], [0.8,0.0,0.2], [0.8,0.0,0.4], [0.6,0.0,0.4]],
            [[0.6,0.0,0.2], [0.6,0.2,0.2], [0.6,0.2,0.4], [0.6,0.0,0.4]],
            [[0.8,0.2,0.4], [0.6,0.2,0.4], [0.6,0.0,0.4], [0.8,0.0,0.4]],
            [[0.8,0.2,0.4], [0.6,0.2,0.4], [0.6,0.2,0.2], [0.8,0.2,0.2]],
            [[0.8,0.2,0.4], [0.8,0.0,0.4], [0.8,0.0,0.2], [0.8,0.2,0.2]]
        ],
        facecolors="magenta",
        linewidths=0.5,
        edgecolors="k",
        alpha=0.2)
    )
    ### FOURTH POINT
    ax.add_collection3d(Poly3DCollection(
        [
            [[0.8,0.2,0.4], [1.0,0.2,0.4], [1.0,0.4,0.4], [0.8,0.4,0.4]],
            [[0.8,0.2,0.4], [1.0,0.2,0.4], [1.0,0.2,0.6], [0.8,0.2,0.6]],
            [[0.8,0.2,0.4], [0.8,0.4,0.4], [0.8,0.4,0.6], [0.8,0.2,0.6]],
            [[1.0,0.4,0.6], [0.8,0.4,0.6], [0.8,0.2,0.6], [1.0,0.2,0.6]],
            [[1.0,0.4,0.6], [0.8,0.4,0.6], [0.8,0.4,0.4], [1.0,0.4,0.4]],
            [[1.0,0.4,0.6], [1.0,0.2,0.6], [1.0,0.2,0.4], [1.0,0.4,0.4]]
        ],
        facecolors="magenta",
        linewidths=0.5,
        edgecolors="k",
        alpha=0.2)
    )
    ### FIFTH POINT
    ax.add_collection3d(Poly3DCollection(
        [
            [[0.0,0.4,0.4], [0.2,0.4,0.4], [0.2,0.6,0.4], [0.0,0.6,0.4]],
            [[0.0,0.4,0.4], [0.2,0.4,0.4], [0.2,0.4,0.6], [0.0,0.4,0.6]],
            [[0.0,0.4,0.4], [0.0,0.6,0.4], [0.0,0.6,0.6], [0.0,0.4,0.6]],
            [[0.2,0.6,0.6], [0.0,0.6,0.6], [0.0,0.4,0.6], [0.2,0.4,0.6]],
            [[0.2,0.6,0.6], [0.0,0.6,0.6], [0.0,0.6,0.4], [0.2,0.6,0.4]],
            [[0.2,0.6,0.6], [0.2,0.4,0.6], [0.2,0.4,0.4], [0.2,0.6,0.4]]
        ],
        facecolors="magenta",
        linewidths=0.5,
        edgecolors="k",
        alpha=0.2)
    )
    ### SIXTH POINT
    ax.add_collection3d(Poly3DCollection(
        [
            [[0.8,0.6,0.0], [1.0,0.6,0.0], [1.0,0.8,0.0], [0.8,0.8,0.0]],
            [[0.8,0.6,0.0], [1.0,0.6,0.0], [1.0,0.6,0.2], [0.8,0.6,0.2]],
            [[0.8,0.6,0.0], [0.8,0.8,0.0], [0.8,0.8,0.2], [0.8,0.6,0.2]],
            [[1.0,0.8,0.2], [0.8,0.8,0.2], [0.8,0.6,0.2], [1.0,0.6,0.2]],
            [[1.0,0.8,0.2], [0.8,0.8,0.2], [0.8,0.8,0.0], [1.0,0.8,0.0]],
            [[1.0,0.8,0.2], [1.0,0.6,0.2], [1.0,0.6,0.0], [1.0,0.8,0.0]]
        ],
        facecolors="turquoise",
        linewidths=0.5,
        edgecolors="k",
        alpha=0.2)
    )
    ### SEVENTH POINT
    ax.add_collection3d(Poly3DCollection(
        [
            [[0.4,0.6,0.4], [0.6,0.6,0.4], [0.6,0.8,0.4], [0.4,0.8,0.4]],
            [[0.4,0.6,0.4], [0.6,0.6,0.4], [0.6,0.6,0.6], [0.4,0.6,0.6]],
            [[0.4,0.6,0.4], [0.4,0.8,0.4], [0.4,0.8,0.6], [0.4,0.6,0.6]],
            [[0.6,0.8,0.6], [0.4,0.8,0.6], [0.4,0.6,0.6], [0.6,0.6,0.6]],
            [[0.6,0.8,0.6], [0.4,0.8,0.6], [0.4,0.8,0.4], [0.6,0.8,0.4]],
            [[0.6,0.8,0.6], [0.6,0.6,0.6], [0.6,0.6,0.4], [0.6,0.8,0.4]]
        ],
        facecolors="turquoise",
        linewidths=0.5,
        edgecolors="k",
        alpha=0.2)
    )
    ### EIGTH POINT
    ax.add_collection3d(Poly3DCollection(
        [
            [[0.6,0.8,0.4], [0.8,0.8,0.4], [0.8,1.0,0.4], [0.6,1.0,0.4]],
            [[0.6,0.8,0.4], [0.8,0.8,0.4], [0.8,0.8,0.6], [0.6,0.8,0.6]],
            [[0.6,0.8,0.4], [0.6,1.0,0.4], [0.6,1.0,0.6], [0.6,0.8,0.6]],
            [[0.8,1.0,0.6], [0.6,1.0,0.6], [0.6,0.8,0.6], [0.8,0.8,0.6]],
            [[0.8,1.0,0.6], [0.6,1.0,0.6], [0.6,1.0,0.4], [0.8,1.0,0.4]],
            [[0.8,1.0,0.6], [0.8,0.8,0.6], [0.8,0.8,0.4], [0.8,1.0,0.4]]
        ],
        facecolors="turquoise",
        linewidths=0.5,
        edgecolors="k",
        alpha=0.2)
    )
    ### NINETH POINT
    ax.add_collection3d(Poly3DCollection(
        [
            [[0.6,0.0,0.0], [0.8,0.0,0.0], [0.8,0.2,0.0], [0.6,0.2,0.0]],
            [[0.6,0.0,0.0], [0.8,0.0,0.0], [0.8,0.0,0.2], [0.6,0.0,0.2]],
            [[0.6,0.0,0.0], [0.6,0.2,0.0], [0.6,0.2,0.2], [0.6,0.0,0.2]],
            [[0.8,0.2,0.2], [0.6,0.2,0.2], [0.6,0.0,0.2], [0.8,0.0,0.2]],
            [[0.8,0.2,0.2], [0.6,0.2,0.2], [0.6,0.2,0.0], [0.8,0.2,0.0]],
            [[0.8,0.2,0.2], [0.8,0.0,0.2], [0.8,0.0,0.0], [0.8,0.2,0.0]]
        ],
        facecolors="turquoise",
        linewidths=0.5,
        edgecolors="k",
        alpha=0.2)
    )
    ### TENTH POINT
    ax.add_collection3d(Poly3DCollection(
        [
            [[0.4,0.4,0.4], [0.6,0.4,0.4], [0.6,0.6,0.4], [0.4,0.6,0.4]],
            [[0.4,0.4,0.4], [0.6,0.4,0.4], [0.6,0.4,0.6], [0.4,0.4,0.6]],
            [[0.4,0.4,0.4], [0.4,0.6,0.4], [0.4,0.6,0.6], [0.4,0.4,0.6]],
            [[0.6,0.6,0.6], [0.4,0.6,0.6], [0.4,0.4,0.6], [0.6,0.4,0.6]],
            [[0.6,0.6,0.6], [0.4,0.6,0.6], [0.4,0.6,0.4], [0.6,0.6,0.4]],
            [[0.6,0.6,0.6], [0.6,0.4,0.6], [0.6,0.4,0.4], [0.6,0.6,0.4]]
        ],
        facecolors="turquoise",
        linewidths=0.5,
        edgecolors="k",
        alpha=0.2)
    )


    # for i in range(1,5):
    #     ax = fig.add_subplot(2,2,i, projection="3d")

    #     ax.scatter3D(X[:5,0], X[:5,1], X[:5,2],
    #         edgecolor = "magenta",
    #         facecolor=(0,0,0,0),
    #         s = 12.5,
    #         marker = "o",
    #         label = "Class 0"
    #     )
    #     ax.scatter3D(X[5:,0], X[5:,1], X[5:,2],
    #         edgecolor = "turquoise",
    #         facecolor=(0,0,0,0),
    #         s = 12.5,
    #         marker = "o",
    #         label = "Class 1"
    #     )


    #     def h(x, y):
    #         return 0.015 + 0.005*x + y
    #     x_dec, y_dec = np.meshgrid(
    #         np.linspace(-0.01,1.01,num=1000),
    #         np.linspace(-0.01,1.01,num=1000)
    #     )
    #     z_dec = h(x_dec, y_dec)
    #     ax.plot_surface(x_dec,y_dec,z_dec,
    #         color="black",
    #         alpha=0.25
    #     )

    #     ax.set_xlim(-0.01,1.01)
    #     ax.set_ylim(-0.01,1.01)
    #     ax.set_zlim(-0.01,1.01)
    #     ax.set_xticks([0.1,0.3,0.5,0.7,0.9])
    #     ax.set_yticks([0.1,0.3,0.5,0.7,0.9])
    #     ax.set_zticks([0.1,0.3,0.5,0.7,0.9])
    #     # ax.set_xlabel('X Label')
    #     # ax.set_ylabel('Y Label')
    #     # ax.set_zlabel('Z Label')

    #     if i == 1:
    #         ax.legend(frameon=False,loc="upper left")
    #         ax.view_init(42.5, 37.5)
    #     elif i == 2:
    #         ax.view_init(40, 40)
    #     elif i == 3:
    #         ax.view_init(37.5, 42.5)
    #     else:
    #         ax.view_init(35, 46)

    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    ax.set_zlim(0,1)
    # ax.set_xlabel('x')
    # ax.set_ylabel('y')
    # ax.set_zlabel('z')

    plt.tight_layout()

    ax.view_init(30,angle)

    angle = int(angle*2)
    if angle < 10:
        angle_str = "00" + str(angle)
    elif angle < 100:
        angle_str = "0" + str(angle)
    else:
        angle_str = str(angle)
    filename="cod_3d_ani/step"+angle_str+".svg"
    plt.savefig(filename)
    plt.gca()

# animation = camera.animate()
# animation.save('animation.mp4')
#plt.savefig("three_dim_cod.svg")
#plt.show()
