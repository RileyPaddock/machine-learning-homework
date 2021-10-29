from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from synthetic_data import get_synthetic_data
import matplotlib.pyplot as plt

data = get_synthetic_data()

test = [dataset[:len(dataset)//2] for dataset in data]
train = [dataset[len(dataset)//2:] for dataset in data]

colors = ['bo', 'r+']
for dataset in test:
    for datapoint in dataset:
        plt.plot(datapoint['point'][0],datapoint['point'][1], 'bo')
for dataset in train:
    for datapoint in dataset:
        plt.plot(datapoint['point'][0],datapoint['point'][1], 'r+')
plt.savefig('test_train.png')

plt.clf()

def transform_format(data):
    X = []
    Y = []
    for dataset in data:
        for data_point in dataset:
            X.append([data_point['point'][0],data_point['point'][1]])
            Y.append(data_point['class'])
    return (X,Y)
accuaracies = []
train_x, train_y = transform_format(train)
test_x, test_y = transform_format(test)
for k in range(1,50):
    knn = KNeighborsClassifier(n_neighbors=k*2)
    knn.fit(train_x,train_y)
    correct = 0
    for i in range(len(test_x)):
        if knn.predict([[test_x[i][0],test_x[i][1]]]) == [test_y[i]]:
            correct += 1
    accuaracies.append(correct/len(test_y))
    plt.plot(k*2,correct/len(test_y), 'bo')

plt.savefig('knn_plot.png')
print(accuaracies)

plt.clf()
accuaracies = []

for mss in range(2,50):
    clf = DecisionTreeClassifier(min_samples_split = mss)
    clf.fit(train_x, train_y)
    correct = 0
    for i in range(len(test_x)):
        if clf.predict([[test_x[i][0],test_x[i][1]]]) == [test_y[i]]:
            correct += 1
    accuaracies.append(correct/len(test_y))
    plt.plot(mss,correct/len(test_y), 'rd')

plt.savefig('decision_tree.png')
plt.clf()
print(accuaracies)
print("here")
accuaracies = []
for num_trees in range(1,100):
    clf = RandomForestClassifier(n_estimators = num_trees)
    clf.fit(train_x, train_y)
    correct = 0
    for i in range(len(test_x)):
        if clf.predict([[test_x[i][0],test_x[i][1]]]) == [test_y[i]]:
            correct += 1
    accuaracies.append(correct/len(test_y))
    plt.plot(num_trees,correct/len(test_y), 'gd')
plt.savefig('random_forest.png')
print(accuaracies)