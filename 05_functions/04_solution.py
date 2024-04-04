import math

def circle (rad):
    area = (math.pi) * (rad**2)
    circumference = 2 * (math.pi) * rad
    return area , circumference

radii = int(input("Enter a Radius of Circle:"))
a, c = circle(radii)
# print("Area:",a ," Circumference:",c)
print("Area:",round(a,2) ," Circumference:",round(c,2))