rates = [
    {'country name':'australia', 'Central bank name': 'RBA'},
    {'country name':'USA', 'Central bank name':'FED'},
]

Country = input ('Country:')
if Country=='australia':
    num_country=0
if Country=='USA':
    num_country=1

if Country =='australia' or Country =='USA':
    print (rates[num_country]['Central bank name'])
else:
    print ('sorry your country is not in the database')