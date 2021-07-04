num = int(input('Please enter an integer: '))


# return all the nontrivial positive divisors of a given number
n = abs(num)
divisors = []
while n > 1:
    if num % n == 0:
        divisors.append(n)
    n -= 1

# check whether the input num is a prime number
boo = len(divisors) == 1

if boo:
    print(f'The inputted number {num} is a prime')
else:
    print(f'The inputted number {num} is NOT a prime, it has divisors {divisors}')