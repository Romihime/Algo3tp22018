import random

n = 5
print '{0:d}'.format(n) #n
puntos = []
for i in range(0,n): #veces
	x = random.randint(0, 5)
	y = random.randint(0, 5)
	while ((x,y) in puntos):
		x = random.randint(0,5)
		y = random.randint(0,5)
	puntos.append((x,y))
	print '{0:d} {1:d}'.format(x,y)
print '{0:d} {1:d}'.format(0,0)