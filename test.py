import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import binary_fill_holes
from opensimplex import OpenSimplex
import random

# Generate random landmass outline using OpenSimplex noise
def generate_outline(width, height):
    scale = 100.0
    print(random.randint(0,4))
    simplex = OpenSimplex(seed=44)  # You can change the seed value for different patterns
    world = np.zeros((width, height))
    for i in range(width):
        for j in range(height):
            world[i][j] = simplex.noise2(i / scale, j / scale)
    threshold = 0
    outline = binary_fill_holes(world > threshold)
    return outline

# Divide the landmass into x pieces
def divide_landmass(outline, num_pieces):
    # Split the outline into equal parts
    pieces = np.array_split(outline, num_pieces)
    return pieces

# Render the map
def render_map(outline, pieces):
    plt.imshow(outline, cmap='Greens', interpolation='nearest')
    for i, piece in enumerate(pieces):
        plt.contour(piece, colors=[f'C{i}'], linewidths=2)
    plt.axis('off')
    plt.show()

# Parameters
width, height = 200, 200
num_pieces = 5

# Generate landmass outline using OpenSimplex noise
outline = generate_outline(width, height)

# Divide landmass into pieces
pieces = divide_landmass(outline, num_pieces)

# Render the map
render_map(outline, pieces)
