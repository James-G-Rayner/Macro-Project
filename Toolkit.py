values=[3,0,21,4,18]
def mean(a):
    sum=0
    x=0
    for values in range (0,5):
        sum=sum+a[x]
        x=x+1
    mean=sum/x
    return (mean)
def var(a,b):
    sum=0
    x=0
    for values in range (0,5):
        sum=sum+(a[x]-float(b))**2
        x=x+1
    var=sum/x
    return (var)
def sd(a):
    sd=a**0.5
    return (sd)
ansmean=mean(values)
ansvar=var(values, ansmean)
anssd=sd(ansvar)
print (ansmean)
print (ansvar)
print (anssd)