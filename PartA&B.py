"""
Eric Smith
Southern Methodist University
CSE3365
February 8th, 2017
"""
from math import sin, cos, pi

f_out = open('output.csv', 'w')
x = pi/4
h_array = [0.1, 0.05, 0.025, 0.0125]


# math functions
def f(x):
    return sin(x)


def f_prime(x):
    return cos(x)


def forward_difference(x, h):
    return (f(x + h) - f(x))/h


def center_difference(x, h):
    return (f(x + h) - f(x - h))/(2*h)


# do calculations, output to file
def build_table(approximation_type):
    for h in h_array:
        a = approximation_type(x, h)
        b = f_prime(x) - a

        f_out.write('{0:.6f}'.format(h) + ',')
        f_out.write('{0:.6f}'.format(a) + ',')

        for i in range(4):
            f_out.write('{0:.6f}'.format(b / (h ** i)) + ',')

        f_out.write('\n')
    f_out.write('\n\n')

build_table(forward_difference)
build_table(center_difference)

f_out.close()