import time

def f(b_0, b_1, x):
    return b_0 + (b_1*x)

def RSS(b0, b1, points):
    sum_squared_error = 0
    for i in range(len(points)):
        error = (f(b0,b1,points[i][0]) - points[i][1])**2
        sum_squared_error += error
    return sum_squared_error

def d_dx(points, b0,b1,h):
    db_0 = (RSS(b0+h,b1, points)-RSS(b0-h,b1, points))/(2*h)
    db_1 = (RSS(b0,b1+h, points)-RSS(b0,b1-h, points))/(2*h)
    return (db_0,db_1)

def step(points, steps, alpha, h, b0, b1):
    for _ in range(steps):
        delta = d_dx(points, b0,b1,h)
        B0 = b0 - alpha*delta[0]
        B1 = b1 - alpha*delta[1]
        b0 = B0
        b1 = B1
    return b0,b1


print("Python:")
times = 0
for _ in range(10):
    start = time.time()
    result = step([(0,0),(1,1),(2,4)], 2, 0.001, 0.1, 0,2)
    print("\t "+str(result))
    times += time.time()-start
print("\tTime: "+str(times/10))
