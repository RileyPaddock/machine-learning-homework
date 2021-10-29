from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from synthetic_data import get_synthetic_data
import matplotlib.pyplot as plt
colors = ['blue','red']

data = get_synthetic_data()
for dataset in data:
    for datapoint in dataset:
        plt.plot(datapoint['point'][0], datapoint['point'][1], color = colors[datapoint['class']], marker = 'o', alpha = 1)


def transform_format(data):
    X = []
    Y = []
    for dataset in data:
        for data_point in dataset:
            X.append([data_point['point'][0],data_point['point'][1]])
            Y.append(data_point['class'])
    return (X,Y)

train_x, train_y = transform_format(data)

clf = RandomForestClassifier(n_estimators = 100)
clf.fit(train_x, train_y)


for x in range(0,40):
    for y in range(0,40):
        plt.plot(x/10, y/10, color = colors[clf.predict([[x/10,y/10]])[0]],marker = 'o', alpha = 0.5)
plt.savefig('pngs/random_forest_viz.png')
