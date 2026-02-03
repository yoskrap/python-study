n = int(input())

for i in range(n - 1):
    for _ in range(n - 1 - i):
        print(' ' , end = '')

    
    for _ in range(2 * i + 1):
        print('*', end = '')

    # for _ in range(n - 2 - i):
    #     print(' ' , end = '')
    print('')

for i in range(2 * n - 1):
    print('*' , end = '')
print('')

for i in range(n - 1):
    for _ in range(i + 1):
        print(' ' , end = '')

    
    for _ in range(2*n - 1 - 2 * i - 2):
        print('*', end = '')

    # for _ in range(i + 1):
    #     print(' ' , end = '')
    print('')

