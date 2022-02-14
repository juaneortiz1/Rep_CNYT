import math
def suma_cplx(a, b):
    real = a[0] + b[0]
    img = a[1] + b[1]
    return (real, img)
def product_cplx(a,b):
    real = (a[0] * b[0]) - (a[1] * b[1])
    img = (a[0] * b[1]) + (a[1] * b[0])
    return (real, img)
def resta_cplx(a,b):
    real = a[0] - b[0]
    img = a[1] - b[1]
    return (real, img)
def div_cplx(a,b):
    real = (a[0] * b[0] + a[1] * b[1]) / (b[0]**2 +b[1]**2)
    img = (a[1] * b[0 - a[0] * b[1]]) / (b[0]**2 +b[1]**2)
    return (real, img)
def mod_cplx(a):
    result = (a[0]**2 + a[1]**2)**(1/2)
    return result
def conjugate_cplx(a):
    real = a[0]
    img = -a[1]
    return (real, img)
def pol_cart_cplx(a):
    r = mod_cplx(a)
    ang = a * math.tan(a[0] / a[1])
    z = str(r) + "*" + "e^" + str(ang) + "i"
    return z
def cart_pol_cplx(p,ang):
    r = mod_cplx(p)
    real = r * math.cos(ang)
    img = r * math.sin(ang)
    return (real,img)
def fase_cplx(a):
    ang = a * math.tan(a[0] / a[1])
    return ang











