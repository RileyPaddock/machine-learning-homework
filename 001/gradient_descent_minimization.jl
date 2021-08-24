function f(x,y)
    1+2*(x*x)+3*(y*y)
end


a = 0.01
x_0 = 1
y_0 = 2


function d_dx(x,y, h)
    d_x = (f(x+h, y) - f(x-h,y))/(2*h)
    d_y = (f(x, y+h) - f(x,y-h))/(2*h)
    return (d_x, d_y)
end

function step(x_0,y_0, a, h, steps)
    for _ in 1:steps
        x_prime,y_prime = d_dx(x_0, y_0, h)
        x_1 = x_0 - a*x_prime
        y_1 = y_0 - a*y_prime
        x_0 = x_1
        y_0 = y_1
    end

    return x_0,y_0
end

a = 0.001
x_0 = 1
y_0 = 2
global times = 0
print("Julia: ")
for _ in 1:10
    start = time_ns()
    print("\n\t2 step result: ")
    print(step(1, 2, 0.001, 0.1, 1000))
    global times += time_ns()-start
end
print("\n\tTime: ")
print(times/10000000000)