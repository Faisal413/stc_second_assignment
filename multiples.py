# sort inputs
n1 = int(input('Enter a positive integer: '))
n2 = int(input('Enter another positive integer: '))

if n1 > n2:
    n1, n2 = n2,n1
elif n2 > n1:
    n1, n2 = n1,n2

print("n1",n1)
print("n2",n2)
    
ls = [x for x in range(n2+1) if x % n1 == 0 and x != 0]
print(f'All the number between {n1} and {n2} divisable by {n1} are {ls}')