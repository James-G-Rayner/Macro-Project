Rate=input ('Interest Rate:')
Num_Rate =  int(Rate)
if Num_Rate<2 and Num_Rate>0:
    print ('Below Target Range')
elif Num_Rate<3 and Num_Rate>2:
    print ('In Target Range')
elif 3<Num_Rate<25:
    print ('above target range')
elif Num_Rate>25 or Num_Rate<0:
    print ('Interest Rate Outside of Realistic Bounds-')
