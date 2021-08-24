points = [[0,0],[1,1],[2,4],[3,9]]
times = []
for _ in 1:10
    start = time_ns()
    X = [0 1; 1 1; 2 1; 3 1]
    Y = [0; 1; 4; 9]
    psuedoinverse = inv(transpose(X) * X) * (transpose(X) * Y)
    append!(times, time_ns()-start/1000000000)
end

print(sum(times)/10)
print("\n")