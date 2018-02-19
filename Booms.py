from math import *
import numpy as np

#============List  with constants and properties==========#
#input parameters

c_a = 0.505     #m
l_a = 1.611     #m
x_1 = 0.125     #m
x_2 = 0.498     #m
x_3 = 1.494     #m
x_a = 0.245     #m
h_a = 0.161     #m
t_sk = 0.0011   #m
t_sp = 0.0024   #m
t_st = 0.0012   #m
h_st = 0.013    #m
w_st = 0.017    #m
n_st = 11       #-
d_1 = 0.0389    #m
d_3 = 0.1245    #m
theta = 30      #deg
P = 49200.      #N
q = 3860        #N/m

#material properties Alu 2024-T3
sigma_y = 345
sigma_u = 483
Emodulus = 73100
G = 28000
tau = 283
theta = atan(0.0805/0.4245)


#lists
boom_matrix = np.array([[-0.04,-0.04,0,0,0.25,0.25],[boom_position(-0.04,'up'),boom_position(-0.04,'down'),0.0805,-0.0805,boom_position(0.25,'up'),boom_position(0.25,'down')]])


#=============functions==================#
def boom_position(z,specifier):
    if -0.0805<=z<0:
        y = sqrt(0.0805**2-z**2)
        if specifier == 'up':
            return y
        elif specifier == 'down':
            return -y
    elif 0<z<=0.4245:
        y = tan(theta)*(0.4245-z)
        if specifier == 'up':
            return y
        elif specifier == 'down':
            return -y
    else:
        print "something went wrong"


def boom_stress():
    (t*b)/ *





####==========MAIN=============####