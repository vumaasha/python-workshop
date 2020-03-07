def fibonacci_iterative(n):
    previous = 0
    current = 1
    print(previous)
    print(current)
    for i in range(n - 1):
        current_old = current
        current = previous + current
        previous = current_old
        print(current)
    return current
