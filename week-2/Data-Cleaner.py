data = ['3.2', '4.5', 'na', '1.3', 'na']
fdata = [float(i) for i in data if i != 'na']
number = data.count('na')

print (fdata)