vel={'x':1,'y':2,'speed':'slow'}
print("Old velocity is : " + str(vel['x']))

if vel['speed']=='fast':
    x_increament=1
elif vel['speed']=='slow':
    x_increament=3
else:
    x_increament=15

vel=vel['x']+x_increament
print("new velocity is : "+str(vel))
