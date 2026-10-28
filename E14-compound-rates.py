def func(r, x, y):
    z=0
    while z<=y:
        r=r*(1+x)
        z=z+1
    return r
deposit=input('Deposit: ')
rate=input('Monthly Rate: ')
term=input('Term (Months): ')
numdeposit=int(deposit)
numrate = float(rate)
numterm = int(term)
value = func(numdeposit, numrate, numterm)
print (value)