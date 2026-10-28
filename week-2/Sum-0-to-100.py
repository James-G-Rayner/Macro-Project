def func(min, max, x):
    sum=0
    while x<=nummax:
        sum=x+sum
        x=x+1
    return sum

min=input('min: ')
max=input('max: ')
nummin = int(min)
nummax = int(max)
value = func(nummin, nummax, nummin)
print (value)