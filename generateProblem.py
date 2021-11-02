import numpy as np

def generate_cities(n_cities):
    coordinates = []
    for i in range(n_cities):
        coordinates.append((np.random.randint(0,100), np.random.randint(0,100)))

    x = [coordinate[0] for coordinate in coordinates]
    y = [coordinate[1] for coordinate in coordinates]
    
    return coordinates, x, y