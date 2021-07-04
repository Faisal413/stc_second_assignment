# gather imputs 
divisor = int(input('Enter a positive integer as a divisor: '))
range_max = int(input('Enter another positive integer as a range max: '))
    
ls = [x for x in range(range_max+1) if x % divisor == 0 and x != 0]
print(f'All the number between 0 and {range_max} divisable by {divisor} are {ls}')
