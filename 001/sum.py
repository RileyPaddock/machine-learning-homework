import time
times = []
for _ in range(10):
    start = time.time()
    total = 0
    for i in range(1,1000001):
        total += i
    end = time.time()
    times.append(end-start)

print(sum(times)/len(times))