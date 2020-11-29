
#this section allows user to define the number of points
n = int(input("Please insert here the desired number of Polygon points: "))

x = []
y = []

print()

#section: demands the user's inputs point's coordinates
print("Please insert here coordinates for Polygon points: ")
print()

for i in range(n):
	a = float (input(f'X {i + 1}: '))
	b = float (input(f'Y {i + 1}: '))

	x.append(a)
	y.append(b)

print()


#section: points and coordinates organized on a table

print("It follows point's coordinates by X and Y:")
print()
print(f'{"Point":15} {"x":15} {"y":15}')
print('.' * 40)

for i in range(n):
	print(f'{i + 1} {x[i]:15} {y[i]:15}')

#section: for Geometric calculations 
print()
print("It follows the polygon's geometric characteristics:")
print()

s1 = 0
for i in range(n):
	a = x[i] + x[i-1]
	b = y[i] - y[i-1]
	m = a * b
	s1 = s1 + m

print()
Ax = 0.5 * (s1)
print (f'{"Ax:":6} {Ax:10.2f}')

s2 = 0
for i in range(n):
	 a = x[i] - x[i-1]
	 b = y[i]**2 + y[i] *y[i-1] + y[i-1]**2
	 m = a * b
	 s2 = s2 + m

Sx = -(1/6) * s2
print (f'{"Sx:":6} {Sx:10.2f}')

s3 = 0 
for i in range(n):
	a = y[i] - y[i-1]
	b = x[i]**2 + x[i] * x[i-1] + x[i-1]**2
	m = a * b
	s3 = s3 + m

Sy = 1/6 * s3
print (f'{"Sy:":6} {Sy:10.2f}')

s4 = 0
for i in range(n):
	a = x[i] - x[i-1]
	b = y[i]**3 + (y[i]**2) * y[i-1] + y[i] * (y[i-1]**2) + y[i-1]**3
	m = a * b
	s4 = s4 + m 

Ix = -(1/12) * s4
print (f'{"Ix:":6} {Ix:10.2f}')

s5 = 0
for i in range(n):
    a = y[i] - y[i-1]
    b = x[i]**3 + (x[i]**2) * x[i-1] + x[i] * (x[i-1]**2) + x[i-1]**3
    m = a * b
    s5 = s5 + m

Iy = (1/12) * s5
print(f'{"Iy:":6} {Iy:10.2f}')

s6 = 0
for i in range(n):
    a = y[i] - y[i-1]
    b = (y[i] * (3 * x[i]**2 + 2 * x[i] * x[i-1] + x[i-1]**2)) + y[i-1] * (3 * x[i-1]**2 + 2 * x[i] * x[i-1] + x[i]**2)
    m = a * b
    s6 = s6 + m

Ixy = -(1/24) * s6
print(f'{"Ixy:":6} {Ixy:10.2f}')

xt = Sy / Ax
print(f'{"xt:":6} {xt:10.2f}')

yt = Sx / Ax
print(f'{"yt:":6} {yt:10.2f}')

Ixt = Ix - (yt**2) * Ax
print(f'{"Ixt:":6} {Ixt:10.2f}')

Iyt = Iy - (xt**2) * Ax
print(f'{"Iyt:":6} {Iyt:10.2f}')

Ixyt = Ixy + xt * yt * Ax
print(f'{"Ixyt:":6} {Ixyt:10.2f}')