n = int(input("Enter base number: "))
# n = 10

for i in range(0, n+1):
    for j in range(0, n+1):
        if j-i >= n/2:
            print(' * ', end='')
        else:
            print('   ', end='')
    print()

print('\n==========================j-i >= n/2==============================\n')

for i in range(0, n+1):
    for j in range(0, n+1):
        if j-i <= n/2:
            print(' * ', end='')
        else:
            print('   ', end='')
    print()

print('\n===========================j-i <= n/2=============================\n')

for i in range(0, n+1):
    for j in range(0, n+1):
        if i-j <= n/2:
            print(' * ', end='')
        else:
            print('   ', end='')
    print()

print('\n===========================i-j <= n/2=============================\n')

for i in range(0, n+1):
    for j in range(0, n+1):
        if i-j >= n/2:
            print(' * ', end='')
        else:
            print('   ', end='')
    print()

print('\n========================== i-j >= n/2==============================\n')

for i in range(0, n+1):
    for j in range(0, n+1):
        if i+j >= n/2:
            print(' * ', end='')
        else:
            print('   ', end='')
    print()

print('\n===========================i+j >= n/2=============================\n')

for i in range(0, n+1):
    for j in range(0, n+1):
        if i+j <= n/2:
            print(' * ', end='')
        else:
            print('   ', end='')
    print()


print('\n===========================i+j <= n/2=============================\n')


for i in range(0, n+1):
    for j in range(0, n+1):
        if i+j >= n+n/2:
            print(' * ', end='')
        else:
            print('   ', end='')
    print()


print('\n==========================i+j >= n+n/2==============================\n')


for i in range(0, n+1):
    for j in range(0, n+1):
        if i+j <= n+n/2:
            print(' * ', end='')
        else:
            print('   ', end='')
    print()

print('\n==========================i+j <= n+n/2==============================\n')


for i in range(0, n+1):
    for j in range(0, n+1):
        if j-i >= n/2 or i+j >= n+n/2 or i+j <= n/2 or i-j >= n/2:
            print(' * ', end='')
        else:
            print('   ', end='')
    print()
print('\n========================== j-i >= n/2 or i+j >= n+n/2 or i+j <= n/2 or i-j >= n/2==============================\n')


#
for i in range(0, n+1):
    for j in range(0, n+1):
        if j-i <= n/2 and i+j <= n+n/2 and i+j >= n/2 and i-j <= n/2:
            print(' * ', end='')
        else:
            print('   ', end='')
    print()
print('\n==========================j-i <= n/2 and i+j <= n+n/2 and i+j >= n/2 and i-j <= n/2:==============================\n')
