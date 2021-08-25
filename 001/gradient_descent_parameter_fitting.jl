function f(b_0, b_1, x)
    return b_0 + (b_1*x)
end

function RSS(b0, b1, points)
    sum_squared_error = 0
    for i in 1:3
        error = (f(b0,b1,points[i,1]) - points[i,2])^2
        sum_squared_error += error
    end
    return sum_squared_error
end

function d_dx(points, b0,b1,h)
    db_0 = (RSS(b0+h,b1, points)-RSS(b0-h,b1, points))/2*h
    db_1 = (RSS(b0,b1+h, points)-RSS(b0,b1-h, points))/2*h
    return (db_0,db_1)
end

function step(points, steps, alpha, h, b0, b1)
    for _ in 1:steps
        delta = d_dx(points, b0,b1,h)
        B0 = b0 - alpha*delta[1]
        B1 = b1 - alpha*delta[2]
        b0 = B0
        b1 = B1
    end
    return b0,b1
end


print("Julia:")
global times = 0
for _ in 1:10
    start = time_ns()
    result = step([ 0 0; 1 1; 2 4], 2, 0.001, 0.1, 1,2)
    print("\n\t ")
    print(result)
    global times += time_ns()-start
end
print("\n\tTime: ")
print(times/10000000000)