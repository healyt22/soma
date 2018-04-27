

# Soma

This repository holds the code for neural networks I've implemented for my Neural Networks course at JHU. `FFBP.py` and `Boltzmann.py` are objects used to implement
Feed Forward Back Propagation Networks and Boltzmann Machines, respectively.

#### Feed Forward Back Propagation (FFBP) Multilayer Perceptron Network

A FFBP perceptron network can be created and trained like so:

```python
from soma import FFBP
# Input data and initial parameters
inputs = [1, 2]
desired_output = 0.7
structure = [2, 1]
# Length of list = numbers of layers
# Items in list = number of perceptrons in each layer
weights = [[[0.3, 0.3], [0.3, 0.3]], [[0.8, 0.8]]]
bias = 0

# Initialize network
x = Network(structure, weights, bias)
# Train with input data for 15 iterations
x.trainer(inputs, desired_output, 15, 1)
```
This example trains the network on one input - output pair for 15 iterations. More input - output pairs can be presented to train the network.

The built-in trainer utilizes a batch method. An online training method can be used if the user sets up a loop that alternates presentation of inputs to the network.


#### Boltzmann Machine with Simulated Annealing for the Traveling Salesman Problem

A Boltzmann Machine can be created and trained as follows. It takes a distance matrix as its only argument. The row and column indices in the matrix represents
cities, and thus, each entry represents the distance between cities. For example, entry (0,1), represents the distance between city A and B, which is 10. This matrix is symmetric, since the distance from A to B is the same as the distance from B to A, or (0,1) = (1,0).

```python
from soma import Boltzmann as bolt
import numpy as np

# Distance matrix for Programming Assignment
distances = np.array([[0, 10, 20, 5, 18],
                      [10, 0, 15, 32, 10],
                      [20, 15, 0, 25, 16],
                      [5, 32, 25, 0, 35],
                      [18, 10, 16, 35, 0]])

# Initialize Boltzmann Machine
x = bolt.Boltzmann(distances)
# Iterate and anneal for 50 iterations
x.train(50)
```

With output:
```shell
Optimized Route: C -> D -> A -> B -> E -> C
Distance: 66
```
![](examples/Boltzmann_example.png)

This example is captured in the `examples/Boltzmann_example.py` script
