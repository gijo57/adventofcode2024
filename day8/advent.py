from collections import defaultdict
import numpy as np

with open('example.txt') as f:
    antenna_map = np.array([list(line.strip()) for line in f.readlines()])
