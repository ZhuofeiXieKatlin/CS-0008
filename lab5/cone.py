import math
def volume(r,h):
    '''volume(r,h) computes the volume of a right-circular cone with radius r and height h'''
    vol=(math.pi*r**2*h)/3
    return vol
    
def surface_area(r,h):    
    '''surface_area(r,h) computes the surface area of a right-circular cone with radius r and height h'''
    surface=math.pi*r*math.sqrt(r**2+h**2)
    return surface

def printstates(r,h):
    '''printstates(r,h) displays a summary of a right-circular cone's volume and surface area'''
    vol=(math.pi*r**2*h)/3
    surface=math.pi*r*math.sqrt(r**2+h**2)
    print("volume= %.2f" % (vol))
    print("surface area = %.2f" % (surface))

