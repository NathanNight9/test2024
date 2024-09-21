(a, b) = int(input()), 1
for i in range(a, 0, -1):
    print(' '.join(str(b) for _ in range(i)))
    b += 1
    