import numpy as np

class Universe:

    def __init__(self):
        self.galaxies_count = np.random.randint(low = 1e8, high = np.inf)
        self.galaxis_names = []

