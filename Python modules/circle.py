# in this simple module we calculate some properties of a circle given its radius.
import math 

# here we have functions to calculate diameter, perimeter, area, arc lenghth and sector area:
def circle_diameter(radius):
    return 2 * radius 

def circle_perimeter(radius):
    return 2 * math.pi * radius

def circle_area(radius):
    return math.pi * radius ** 2 

def circle_arc_lenghth(radius, angle_in_degrees):
    return (angle_in_degrees / 360) * circle_perimeter(radius)

def circle_sector_area(radius, angle_in_degrees):
    return (angle_in_degrees / 360) * circle_area(radius)

# and last but not leasr, a function that returns all the info in a dictionary:
def circle_info(radius):
    return {
        "radius": radius,
        "diameter": circle_diameter(radius),
        "perimeter": circle_perimeter(radius),
        "area": circle_area(radius),
        "arc length": circle_arc_lenghth(radius, 90),
        "sector area": circle_sector_area(radius, 90)
    }

# i hope you will enjoy this module! Consider that I'm 13 years old and this is one of my first serious programs. Thanks for viewing!
#IMPORTANT NOTE: remember to put the file where you import this module 