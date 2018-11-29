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

def gen_fractal_points(starting_point, corners, n_points):
    """
    Generate the set of points to plot based on the chaos game algorithm
    """
    # Initialize ponts array and starting point
    points = np.zeros((n_points+5,corners.shape[1]))
    points[0] = starting_point

    # Pick random corners
    indices = np.random.randint(0, corners.shape[0], n_points+5)
    for i in range(1, len(points)-1):
        points[i] = (points[i-1] + corners[indices[i-1]]) / 2

    return points[5:,:]

n_sides = 3
corners = get_corners(n_sides)
starting_point = pick_starting_point(corners)
generated_points = gen_fractal_points(starting_point, corners, 10000)

# %%
plt.scatter(*zip(*corners))
plt.scatter(*zip(*generated_points), s=1.0)
plt.axis("equal")
plt.show()
