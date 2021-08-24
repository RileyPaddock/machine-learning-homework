sums = []
for _ in 1:10
    start = time_ns()
    total = 0
    for i in 1:1000000
        total += i
    end
    stop = time_ns()
    append!(sums, (stop - start)/1000000000)
end
print(sum(sums)/length(sums))