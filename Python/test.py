import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# Initialize the Simulation

dim = 1000
a = np.matrix(np.zeros((dim, dim)))
pos = np.matrix([[dim // 2], [dim // 2]])  # current position of ant
direction = np.matrix([[1], [0]])  # direction ant is currently moving

# Rotation Matrices
clock = np.matrix([[0, 1], [-1, 0]])
counter = np.matrix([[0, -1], [1, 0]])

def takestep(a, pos, direction):
    pos[:] = pos + direction
    if a[pos[0, 0], pos[1, 0]] == 0:  # landed on white
        a[pos[0, 0], pos[1, 0]] = 1
        direction[:] = clock * direction
    else:
        a[pos[0, 0], pos[1, 0]] = 0
        direction[:] = counter * direction

fig = plt.figure()
im = plt.imshow(a, interpolation='none', vmin=0, vmax=1)

def animate(i):
    takestep(a, pos, direction)
    im.set_data(a)
    return [im]


anim = animation.FuncAnimation(fig, animate,
                               frames=20000, interval=0, blit=True,
                               repeat=False)
plt.show()