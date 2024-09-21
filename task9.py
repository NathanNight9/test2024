a = 1 #Nathan, 8
for i in range(1, 5):
    print(" ".join(map(str, range(a + i - 1, a - 1, -1))))
    a += i

