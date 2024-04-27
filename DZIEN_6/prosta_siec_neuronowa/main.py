import numpy as np
from simplenn import SimpleNeuralNetwork

network = SimpleNeuralNetwork()
print(network.weights)

train_inputs = np.array([[1,1,0],[1,1,1],[1,1,0],[1,0,0],[0,1,1],[0,1,0],])
train_output = np.array([[0,1,0,0,1,0]]).T
train_iters = 50000

network.train(train_inputs,train_output,train_iters)
print(network.weights)

print("testowanie - progrnoza siecie neuronowej")
test_data = np.array([[1,1,1],[1,0,0],[0,1,1],[0,1,0],[0,0,1],[0,0,0],])

for data in test_data:
    print(f"wynik dla {data} -> {network.propagation(data)}")
