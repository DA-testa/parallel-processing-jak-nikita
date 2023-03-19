def parallel_processing(n, data):
    output = []
    # create the output pairs
    # m output pairs: 0-based index of the thread for the i-th job
    # + time in seconds when it'll start processing 
    
    # using min-heap priority queue
    # it is possible to get the smallest indexed thread
    # the idea is to use both the smallest thread index
    # and more importantly the smallest time available
     
    # initialize the priority queue
    threads = []
    for a in range(0, n):
        print(a)
        threads.append([0, a])
    
    # here's where the scheduling happens
    for job in data:
        time, thread = pop_heap(threads)
        output.append((thread, time))
        time += job
        threads.append((time, thread))
        build_heap(threads, n)

    return output

# from task 3
# modified to deal with tuples
def build_heap(data, n):
    start = n // 2 - 1

    for i in range(start, -1, -1):
        smol = i

        while True:
            l = 2 * i + 1
            r = 2 * i + 2

            if l < n and data[l][0] < data[smol][0]:
                smol = l
            elif l < n and data[l][0] == data[smol][0] and data[l][1] < data[smol][1]:
                smol = l

            if r < n and data[r][0] < data[smol][0]:
                smol = r
            elif r < n and data[r][0] == data[smol][0] and data[r][1] < data[smol][1]:
                smol = r

            if smol != i:
                data[i], data[smol] = data[smol], data[i]
                i = smol

            else:
                break
    
    return data

# i need a function that pops the highest-priority element from the min-heap
def pop_heap(data):
    popped = data[0]
    data[0] = data[-1]
    data.pop()
    return popped

def main():
    # n - thread count 
    # m - job count
    n = None
    m = None
    data = None

    try:
        n, m = list(map(int, input("Enter n and m: ").split()))
        # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
        data = list(map(int, input("Enter m integers t(i): ").split()))
        assert len(data) == m
    except ValueError:
        print("Invalid input")

    result = parallel_processing(n, data)
    
    for i, j in result:
        print(i, j)

if __name__ == "__main__":
    main()
