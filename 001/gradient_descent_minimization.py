import time

def f(x,y):
    return 1+2*(x*x)+3*(y*y)


a = 0.01
x_0 = 1
y_0 = 2


def d_dx(x,y, h = 0.1):
    d_x = (f(x+h, y) - f(x-h,y))/(2*h)
    d_y = (f(x, y+h) - f(x,y-h))/(2*h)
    return (d_x, d_y)

def step(x_0,y_0, a, steps = 1000):
    for _ in range(steps):
        x_prime,y_prime = d_dx(x_0, y_0)
        x_1 = x_0 - a*x_prime
        y_1 = y_0 - a*y_prime
        x_0 = x_1
        y_0 = y_1
    return x_0,y_0
times = 0
print("\nPython: ")
for _ in range(10):
    start = time.time()
    print("\t2 step result: "+str(step(1, 2, 0.001)))
    times += time.time()-start
print("\tTime: "+str(times/10))
