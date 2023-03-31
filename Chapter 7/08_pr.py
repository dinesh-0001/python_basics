for i in range(5):
    print('*' * (i+1))


n = 5
for k in range(5):
    print(' '*(n-k), end='')
    print('*'*(2*k+1), end='')
    print(' '*(n-k))
