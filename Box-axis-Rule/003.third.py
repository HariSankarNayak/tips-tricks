n = int(input("Enter base number: "))


for i in range(0, n+1):
    for j in range(0, n+1):
        if i+j == n or i == j:
            print(' * ', end='')
        else:
            print('   ', end='')
    print()

print('========================================================')

for i in range(0, n+1):
    for j in range(0, n+1):
        if i+j >= n:
            print(' * ', end='')
        else:
            print('   ', end='')
    print()

print('========================================================')
for i in range(0, n+1):
    for j in range(0, n+1):
        if i+j <= n:
            print(' * ', end='')
        else:
            print('   ', end='')
    print()
