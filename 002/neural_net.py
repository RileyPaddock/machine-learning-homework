import matplotlib.pyplot as plt
import numpy
import time


class Neuron:
  def __init__(self, index, activation_function, activation_derivative):
    self.index = index
    self.activation_function = activation_function
    self.activation_derivative = activation_derivative
    self.parents = []
    self.children = []


class Network:
  def __init__(self,edges, points, weights, activation_function, activation_derivative):
    self.edges = edges
    self.neurons = []
    self.activation_function = activation_function
    self.activation_derivative = activation_derivative
    self.setup_network()
    self.weights = weights
    self.output = max([edge[1] for edge in edges])
    self.points = points
    
  
  def setup_network(self):
    seen_indices = []
    for edge in self.edges:
      if edge[0] not in seen_indices:
        seen_indices.append(Neuron(edge[0], self.activation_function, self.activation_derivative))
      if edge[1] not in seen_indices:
        seen_indices.append(Neuron(edge[1], self.activation_function, self.activation_derivative))

    seen_indices = sorted(seen_indices, key=lambda neuron: neuron.index)
    self.neurons = seen_indices

    for edge in self.edges:
      seen_indices[edge[0]].parents.append(seen_indices[edge[1]])
      seen_indices[edge[1]].children.append(seen_indices[edge[0]])

  def f(self, i, point, derivative = False):
    if i in [j for j in range(len(point))]:

      if derivative:
        return self.neurons[i].activation_derivative(point[i])
      else:
        return self.neurons[i].activation_function(point[i])

    #elif i == len(point):
    elif False:

      if derivative:
        return self.neurons[i].activation_derivative(1)
      else:
        return self.neurons[i].activation_function(1)

    else:
      result = 0
      for edge in self.weights:
        if edge[1] == i:
          result += (self.f(edge[0], point)*self.weights[edge])

      if derivative:
        return self.neurons[i].activation_derivative(result)
      else:
        return self.neurons[i].activation_function(result)

  def dE_dw(self, weight, point, neuron_gradients):
    return neuron_gradients[weight[1]]*self.dn_dw(weight[1], weight, point)

  def dE_dn(self,node, point, neuron_gradients):
    if node == self.output:
      return self.activation_derivative(self.f(self.output, point, False))
    else:
      succesors = [key[1] for key in self.weights if key[0] == node]
      result = 0
      for succesor in succesors:
        if succesor in neuron_gradients:
          result += neuron_gradients[succesor]*self.dn_dn(succesor, node, point)
        else:
          result += self.dE_dn(succesor, point)*self.dn_dn(succesor, node, point)
      return result

  def dn_dn(self,node_1, node_2, point):
    return self.f(node_1, point, True)*self.weights[(node_2, node_1)]
  
  def dn_dw(self, node, weight, point):
    return self.f(node, point, True)*self.f(weight[0], point)

  def update_weights(self):
    new_weights = {key:0 for key in self.weights}
    relevant_points = []
    
    for point in self.points:
      #DO NOT FORGET THIS COMMENT!!!!!!
      #if (self.f(self.output, point['point'], False) < 0 and point['class'] == '+') or (self.f(self.output, point['point'], False) > 0 and point['class'] == '-'):
        relevant_points.append(point['point'])


    for edge in self.weights:
      weight_sum = 0
      for point in relevant_points:
        neuron_gradients = {}
        for i in range(self.output, -1, -1):
          neuron_gradients[i] = self.dE_dn(i,point, neuron_gradients)
        weight_sum += self.dE_dw(edge, point, neuron_gradients)
      new_weights[edge] = self.weights[edge] - 0.01*weight_sum

    self.weights = new_weights


# def boundry(weights, x):
#   return -((x*weights[(0,2)]*weights[(2,4)]) + (x*weights[(0,3)]*weights[(3,4)]))/((weights[(1,2)]*weights[(2,4)]) + (weights[(1,3)]*weights[(3,4)]))

points = [{'point':(1,2), 'class':'-'}]


def func(x): return numpy.arctan(x)

def de_func(x): return 1/(1+(x**2))

def generate_network_edges(layers):
  nodes = (layers*2)+1
  edges = []
  #first node in each layer goes is i*2
  for i in range(layers-1):
    edges.append((i*2,(i+1)*2))
    edges.append((i*2+1,(i+1)*2))
    edges.append((i*2,((i+1)*2)+1))
    edges.append((i*2+1,((i+1)*2)+1))
  edges.append(((layers-1)*2,layers*2))
  edges.append(((layers-1)*2+1,layers*2))
  return edges

times = []
for x in range(1,6):
  edges = generate_network_edges(x)
  weights = {edge:1 for edge in edges}
  start = time.time()
  nn = Network(edges,points,weights, func, de_func)
  for _ in range(1000):
    nn.update_weights()
  print("Iteration "+str(x)+" complete")
  times.append(time.time()-start)

print([x for x in range(1,6)], times)

plt.plot([x for x in range(1,6)], times)
plt.savefig('net_times.png')





   

       
