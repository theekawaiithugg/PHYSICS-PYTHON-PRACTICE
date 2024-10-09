import matplotlib.pyplot as plt
import numpy as np

#PLOT 1 Basic
x = [5, 6, 7, 8]
y = [10,8,9,7]
 
plt.plot(x,y)
plt.show()

#Title and Lables
#Plot 2 sine's on grids
#SImple sine(x) and sine(x^2) for x include [0,2pi]

x2 = np.linspace(0, 2*np.pi, 300) # x2 is a NumPy array
y2 = np.sin(x2) # Compute sin(x) for x2

y3 = np.sin(x2**2) # Compute sin(x^2) for x2

plt.figure() #Opens a figure that includes the plots specified in the cell
plt.plot(x2, y2, label=r'$\sin(x)$')    # Plot sin(x)
plt.plot(x2, y3, label=r'$\sin(x^2)$') # Plot sin(x^2)
plt.title('Some functions')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

plt.show()

#To controll lines and markers 

x4 = np.linspace(0, 2*np.pi,50)
y4 = np.sin(x4)
plt.plot(x4,y4,linewidth =8)
plt.show()

plt.plot(x4, y4, '-', markersize = 5, color = 'r')
plt.show()


#Other Plot Types Errorbars, Logarithmic axes, Histogram, 2D arrays, Simple 3d plotting

# example data
x5 = np.arange(0.1, 4, 0.5)
y5 = np.exp(-x5)

# example variable error bar values
yerr = 0.1 + 0.2*np.sqrt(x5)
xerr = 0.1 + yerr

#plt.errorbar(x, y, xerr=0.2, yerr=0.4)
plt.errorbar(x5, y5, xerr=xerr, yerr=yerr)
plt.title("Be certain about your uncertainties")
plt.show()

#Logarithmic
x6 = np.linspace(-5, 5)
y6 = np.exp(-x6**2)
#plt.plot(x,y);
plt.semilogy(x6, y6)
plt.show()

#histogram
mu, sigma = 100, 15
x7 = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x7, 50, density=1, facecolor='r', alpha=0.5)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
# This will put a text fragment at the position given:
plt.text(55, .027, r'$\mu=100,\ \sigma=15$', fontsize=14)
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()

#2D array
plt.imshow(np.random.rand(5,10), interpolation='nearest', cmap='Blues')
plt.show()

#simple 3d plotting
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.YlGnBu,
        linewidth=0, antialiased=False)
ax.set_zlim3d(-1.01, 1.01)
plt.show()