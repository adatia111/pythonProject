import math

import yo as yo

g = float(input("input the acceleration due to gravity:"))
yo = float(input("input the height of the barrel in meters:"))
x = float(input("input horizontal distance in meters:"))
deg = float(input("input angle of barrel in degrees:"))
theta = deg * math.pi / 180
vo = float(input("input initial velocity"))

answer = yo + x * math.tan(theta) - (g * x**2) / (2 * (vo * math.cos(theta)) ** 2)

print("the height of the projectile is",answer,"meters")
