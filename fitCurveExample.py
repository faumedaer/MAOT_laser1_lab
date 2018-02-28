from pylab import *
from scipy.optimize import curve_fit

x = np.array([1,2,3,4,5,6])
y = np.array([0.03663127777746836,
0.0006709252558050237,
1.228842470665642e-05,
2.2507034943851823e-07,
4.122307244877116e-09,
7.550269088558195e-11])

def func(x, a, c):
    return a*np.exp(-c*x)

popt, pcov = curve_fit(func, x, y, p0=(1, 1e-6))
print(popt)

