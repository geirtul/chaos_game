import numpy as np
import matplotlib.pyplot as plt
import sys

def get_corners(n):
    """
    Return the corners of an n-gon
    :param n: The number of corners to generate
    """
    # We don't want the origin point twice
    stop = 2*np.pi*(1 - 1/n)
    circlepoints = np.linspace(0, stop, n)

    # Convert to cartesian coordinates
    x = np.cos(circlepoints)
    y = np.sin(circlepoints)
    cartesian = np.c_[x,y]
    return cartesian

def pick_starting_point(corners):
    """
    Draw n points and generate a starting point
    for the chaos game algorithm.
    """

    # Number of corners defines the amount of random numbers we use
    n = corners.shape[0]
    # Pick random points and scale them so sum(points) = 1
    points = np.random.random((n, 1))
    points /= np.sum(points)
    # Generate the starting point
    start = np.sum(points*corners, axis=0)
    return start

n_sides = 3
corners = get_corners(n_sides)
starting_points = [pick_starting_point(corners) for i in range(1000)]

# %%
plt.scatter(*zip(*corners), c='b')
plt.scatter(*zip(*starting_points), c='r')
plt.axis("equal")
plt.show()
