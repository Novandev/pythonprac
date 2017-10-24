# quadratic.py
# A program that computes the real roots of a quadratic equation.
# Illustrates use of the math library.
# Note: this program crashes if the equation has no real roots.
import math # Makes the math library available.
print ("This program finds the real solutions to a quadratic")

a, b, c = input("Please enter the coefficients (a, b, c): ").split(",")

discRoot = math.sqrt(b * b - 4 * a * c)
root1 = (-b + discRoot) / (2 * a)
root2 = (-b - discRoot) / (2 * a)
print ("The solutions are:", root1, root2)
