a = 0 #Nathan, 8
for i in range(1, 6, 2):
     print(' '.join(str(a := a + 1) for _ in range(i)))
    
