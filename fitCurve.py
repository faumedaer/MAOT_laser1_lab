#############################
### approx series of points to exp fct
#############################

from pylab import *
from scipy.optimize import curve_fit

Ofile1 = open("lifetimeLab2DataX.txt", "r")
Ofile2 = open("lifetimeLab2DataY.txt", "r")


listDataX = []
listDataY = []

for line in Ofile1:
	temp = line.replace("\n","")
	listDataX.append(float(temp))

Ofile1.close()

for line in Ofile2:
	temp = line.replace("\n","")
	listDataY.append(float(temp))

Ofile2.close()

x = np.array(listDataX)
y = np.array(listDataY)

def func(x, a, c, d):
    return a*np.exp(-c*x)+d

popt, pcov = curve_fit(func, x, y, p0=(0.011, 1e-6, 0.0008))
print(popt)

CONST_A = popt[0]
CONST_B = popt[1]
CONST_C = popt[2]

file1 = open("lifetimeLab2DataX.txt", "r")
file2 = open("lifetimeLab2FitCurveData.txt", "w")

def funcExp(x,a,b,c): 
	return str(a*math.exp(-b*x)+c)

for line in file1:
	file2.write(funcExp(float(line),CONST_A, CONST_B, CONST_C)+"\n")

