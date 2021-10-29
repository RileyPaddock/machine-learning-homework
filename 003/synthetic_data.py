import random
import math
import matplotlib.pyplot as plt
random.seed(1)
def get_synthetic_data():
  num_centers = 4
  centers = [(1,1), (3,3), (1,3), (3,1)]
  classes = [1,1,0,0]
  # centers = [(random.uniform(0,4), random.uniform(0,4)) for _ in range(num_centers)]
  # classes = [random.choice([0,1]) for _ in range(num_centers)]
  cluster_count = [0 for _ in range(num_centers)]
  data_points = [[] for _ in range(num_centers)]
  data_point = {'point':(1,1), 'class':1}

  def distance(point, center):
    return ((center[0]-point[0])**2 + (center[1]-point[1])**2)**0.5

  while cluster_count != [50 for _ in range(num_centers)]:
    point = (random.uniform(0,4),random.uniform(0,4))
    distances = [distance(point, center) for center in centers]
    min_1 = min(distances)
    min_2 = min([x for x in distances if x != min_1])
    if (min_2 - min_1) < 0.5:
      class_ = random.choice([0,1]) 
      if class_ == 1: 
        if cluster_count[distances.index(min_2)] == 50: continue
        cluster_count[distances.index(min_2)]+=1
        data_points[distances.index(min_2)].append({'point':point, 'class':class_})

      else: 
        if cluster_count[distances.index(min_1)] == 50: continue
        cluster_count[distances.index(min_1)]+=1
        data_points[distances.index(min_1)].append({'point':point, 'class':class_})


    else:
      if cluster_count[distances.index(min_1)] == 50: continue
      cluster_count[distances.index(min_1)]+=1
      class_ = classes[distances.index(min_1)]
      data_points[distances.index(min_1)].append({'point':point, 'class':class_})
  return data_points


# colors = ['bo', 'r+']
# for data in data_points:
#   plt.plot(data['point'][0],data['point'][1], colors[data['class']])
# for center in centers:
#   plt.plot(center[0],center[1], 'go')
# plt.savefig('synthetic_data.png')