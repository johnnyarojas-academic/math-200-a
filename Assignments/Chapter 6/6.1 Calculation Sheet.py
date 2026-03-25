#!/usr/bin/env python3

from numpy import *

# Problem 1
print("Ans 1")
v1 = array([-1, 4 , 2])
v2 = array([3, -2, 1])
v3 = array([0, 2, -2])

print((1 * v1) + (-3 * v2) + (0 * v3))

# Problem 2
print("Ans 2")
c = array([4,2,0])

v1 = array([1,1,1])
v2 = array([0,-1,2])
v3 = array([1,0,1])
V = column_stack((v1, v2, v3))
image_c = V @ c

w1 = array([2, 0, -1])
w2 = array([-5, 2, -1])
w3 = array([1, 1, 0])
W = column_stack((w1, w2, w3))
image_image_c = W @ image_c

print(image_image_c)

# Problem 3
print("Ans 3")
v1, v2, v3 = array([1,1,1]), array([0,-1,2]), array([1,0,1])
w1, w2, w3 = array([2,0,-1]), array([-5,2,-1]), array([1,1,0])

target = array([4,2,0])
V = column_stack((v1, v2, v3))
coeff = linalg.solve(V, target)

W = column_stack((w1, w2, w3))
image = W @ coeff
print(image)

# Problem 4
print("Ans 4")
from sympy import *

# Augmented matrix [A | 0]
A = Matrix([[0,1,-2,2,0],
            [-1,4,5,0,0],
            [0,1,3,2,0]])

rref_matrix, pivots = A.rref()
print(rref_matrix)

# Solve the system
x1, x2, x3, x4 = symbols('x1 x2 x3 x4')
system = Matrix([[0,1,-2,2],[-1,4,5,0],[0,1,3,2]])
b = Matrix([0,0,0])

solution = linsolve((system, b), x1, x2, x3, x4)
print(solution)

# Problem 11
a, b = symbols('a b')

solution = solve([
    4*a - 3*b - 5,
    3*a + 4*b - 0
], [a, b])

print(solution)
