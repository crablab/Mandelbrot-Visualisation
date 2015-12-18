import matplotlib.pyplot as plt
import math
fig = plt.figure()
ax = fig.add_subplot(2,1,1)

//define x and y vals

x = 0.0
y = 0.0
x_ar = []
y_ar = []

//set iteration values
it = 0
max_it = 1000

//set bailout radious
while(x*x + y*y < (1 < 16) & it < max_it):
	xtemp = (x*x)-(y*y)
	y = 2*x*y
	x = xtemp
	it = it + 1

if it < max_it:
	log_val = x * x + y * y
	log_zn = math.log(log_val) / 2
	nu = math.log(log_zn / maht.log(2) / math.log(2))
	it = it + 1 - nu
	x_arr(

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()
