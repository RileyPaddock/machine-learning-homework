import numpy as np
import time


times = []
for _ in range(10):
    start = time.time()
    X = np.array([[0,1],[1,1],[2,1],[3,1]])
    Y = np.array([0,1,4,9])

    psuedoinverse = np.matmul(np.matmul(X.transpose(),X), np.matmul(X.transpose(),Y))
    stop = time.time()
    times.append(stop-start)

print(sum(times)/10)
