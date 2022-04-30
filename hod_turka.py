d = int(input('x:'))
d2 = int(input('y'))
for i in range(8):
    print()
    for j in range(8):
        if d == i or d2 == j:
            print('❎', end='\t')
        else:
            print(0, end='\t')