rates = [4, 4.3, 3.85, 3.1, 4.6]
x=0
y=0
z=0
max=0
total=0
closest=0
closest_diff=10
while x<5:
    if max<rates[x]:
        max=rates[x]
    else:
        max=max
    x=x+1
while y<5:
    total = total + rates[y]
    y=y+1
average=total/5
while z<5:
    if (abs(rates[z]-average)<closest_diff):
        closest=rates[z]
        closest_diff=abs(closest-average)
    else:
        closest=closest
    z=z+1
print (max)
print (average)
print (closest)
