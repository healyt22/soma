import Boltzmann as boltz
import numpy as np

distances = np.array([[0, 10, 20, 5, 18],
                      [10, 0, 15, 32, 10],
                      [20, 15, 0, 25, 16],
                      [5, 32, 25, 0, 35],
                      [18, 10, 16, 35, 0]])
cities = ['A', 'B', 'C', 'D', 'E']

x = boltz.Boltzmann(cities, distances)
x.train(50)