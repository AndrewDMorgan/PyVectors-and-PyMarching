import numpy as np
from PIL import Image as im
import math as Math  # importing the math library to add cos, sin, sqrt, ect...
import random, pygame


"""
To Do

    Add a way to remove files
"""


small_num = 0.00000000000000001  # an incredibly small number


def divide(value1, value2):  # divides and avoids divition by zero errors
    return (value1 + small_num) / (value2 + small_num)


def divideT(value1, value2):  # to divide using the try;except method
    try:
        return value1 / value2
    except ZeroDivisionError:
        return 0


class vec4:  # this class stores and operates an a tuple/list containing four items (class functions gone over in the Vec2 class)
    def __init__(self, x=None, y=None, z=None, w=None):
        try:
            if None in [x, y, z, w]:
                if y == None:
                    y = x
                    z = x
                    w = x
                elif z == None:
                    z = x
                    w = y
                else:
                    if x == None:
                        raise SyntaxError("Position is undefined, please put an x or an x and y or an x, y, z, and w")
                    else:
                        raise SyntaxError("Requires more information, please put an x or an x and y or an x, y, z, and w")
        except AttributeError:  # filling it in with the other vectors components
            try:
                length = len(x)
                if length == 2:
                    self.x = x.x
                    self.y = x.y
                    
                    try:
                        length = len(y)
                        if length == 2:
                            self.z = y.x
                            self.w = y.y
                        else:
                            raise TypeError("Vector Is To Long")
                    except TypeError:
                        self.z = y
                        self.w = z
                elif length == 3:
                    self.x = x.x
                    self.y = x.y
                    self.z = x.z
                    self.w = y
                else:
                    raise TypeError("Vector Is To Long")
            except TypeError:
                self.x = x
                try:
                    length = len(y)
                    if length == 2:
                        self.y = y.x
                        self.z = y.y
                        self.w = z
                    elif length == 3:
                        self.y = y.x
                        self.z = y.y
                        self.w = y.z
                    else:
                        raise TypeError("Vector Is To Long")
                except TypeError:
                    self.y = y
                    try:
                        length = len(z)
                        if length == 2:
                            self.z = z.x
                            self.w = z.y
                        else:
                            raise TypeError("Vector Is To Long")
                    except TypeError:
                        self.z = z
                        self.w = w
            x = self.x
            y = self.y
            z = self.z
            w = self.w

        self.x = x
        self.y = y
        self.z = z
        self.w = w
        
        self.xy = [x, y]
        self.xyz = [x, y, z]
        self.xyzw = [x, y, z, w]
        
        self.yz = [y, z]
        self.xy = [x, y]
        self.xz = [x, z]
        
        self.r = x
        self.g = y
        self.b = z
        self.a = w
        self.rgb = [x, y, z]
        self.rgba = [x, y, z, w]
    def __add__(self, other):
        return Vec4(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)
    def __sub__(self, other):
        return Vec4(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)
    def __mul__(self, other):
        return Vec4(self.x * other.x, self.y * other.y, self.z * other.z, self.w * other.w)
    def __truediv__(self, other):
        return Vec4(divide(self.x, other.x), divide(self.y, other.y), divide(self.z, other.z), divide(self.w, other.w))
    def __floordiv__(self, other):
        return Vec4(self.x//other.x, self.y//other.y, self.z//other.z, self.w//other.w)
    def __mod__(self, other):
        return Vec4(self.x%other.x, self.y%other.y, self.z%other.z, self.w%other.w)
    def __pow__(self, other):
        return Vec4(self.x**other.x, self.y**other.y, self.z**other.z, self.w**other.w)
    def __rshift__(self, other):
        return Vec4(self.x>>other.x, self.y>>other.y, self.z>>other.z, self.w>>other.w)
    def __lshift__(self, other):
        return Vec4(self.x<<other.x, self.y<<other.y, self.z<<other.z, self.w<<other.w)
    def __lt__(self, other):
        dot1 = (self.x * self.x) + (self.y * self.y) + (self.z * self.z) + (self.w * self.w)
        dot2 = (other.x * other.x) + (other.y * other.y) + (other.z * other.z) + (other.w * other.w)
        if dot1 < dot2:
            return True
        else:
            return False
    def __gt__(self, other):
        dot1 = (self.x * self.x) + (self.y * self.y) + (self.z * self.z) + (self.w * self.w)
        dot2 = (other.x * other.x) + (other.y * other.y) + (other.z * other.z) + (other.w * other.w)
        if dot1 > dot2:
            return True
        else:
            return False
    def __le__(self, other):
        dot1 = (self.x * self.x) + (self.y * self.y) + (self.z * self.z) + (self.w * self.w)
        dot2 = (other.x * other.x) + (other.y * other.y) + (other.z * other.z) + (other.w * other.w)
        if dot1 <= dot2:
            return True
        else:
            return False
    def __ge__(self, other):
        dot1 = (self.x * self.x) + (self.y * self.y) + (self.z * self.z) + (self.w * self.w)
        dot2 = (other.x * other.x) + (other.y * other.y) + (other.z * other.z) + (other.w * other.w)
        if dot1 >= dot2:
            return True
        else:
            return False
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z and self.w == other.w:
            return True
        else:
            return False
    def __ne__(self, other):
        if self.x != other.x and self.y != other.y and self.z != other.z and self.w != other.w:
            return True
        else:
            return False
    def __isub__(self, other):
        return Vec4(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)
    def __iadd__(self, other):
        return Vec4(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)
    def __imult__(self, other):
        return Vec4(self.x * other.x, self.y * other.y, self.z * other.z, self.w * other.w)
    def __idiv__(self, other):
        return Vec4(divide(self.x, other.x), divide(self.y, other.y), divide(self.z, other.z), divide(self.w, other.w))
    def __ifloordiv__(self, other):
        return Vec4(self.x//other.x, self.y//other.y, self.z//other.z, self.w//other.w)
    def __imod__(self, other):
        return Vec4(self.x%other.x, self.y%other.y, self.z%other.z, self.w%other.w)
    def __ipow__(self, other):
        return Vec4(self.x**other.x, self.y**other.y, self.z**other.z, self.w**other.w)
    def __irshift__(self, other):
        return Vec4(self.x >> other.x, self.y >> other.y, self.z >> other.z, self.w >> other.w)
    def __ilshift__(self, other):
        return Vec4(self.x << other.x, self.y << other.y, self.z << other.z, self.w << other.w)
    def __neg__(self):
        return Vec4(-self.x, -self.y, -self.z, -self.w)
    def __pos__(self, other):
        return Vec4(+self.x, +self.y, +self.z, +self.w)
    def __abs__(self):
        return Vec4(abs(self.x), abs(self.y), abs(self.z), abs(self.w))
    def __str__(self):
        return 'Vec4(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ', ' + str(self.w) + ')'
    def mix(self, other, percentage):
        return Vec4(math.mix(self.x, other.x, percentage), math.mix(self.y, other.y, percentage), math.mix(self.z, other.z, percentage), math.mix(self.w, other.w, percentage))
    def clamp(self, min_, max_):
        return Vec4(math.clamp(self.x, min_, max_), math.clamp(self.y, min_, max_), math.clamp(self.z, min_, max_), math.clamp(self.w, min_, max_))
    def sqrt(self):
        return Vec4(math.sqrt(self.x), math.sqrt(self.y), math.sqrt(self.z), math.sqrt(self.w))
    def tan(self):
        return Vec4(math.tan(self.x), math.tan(self.y), math.tan(self.z), math.tan(self.w))
    def sin(self):
        return Vec4(math.sin(self.x), math.sin(self.y), math.sin(self.z), math.sin(self.w))
    def cos(self):
        return Vec4(math.cos(self.x), math.cos(self.y), math.cos(self.z), math.cos(self.w))
    def length(self):
        return math.lengthOfList(self.xyzw)
    def floor(self):
        return Vec4(math.floor(self.x), math.floor(self.y), math.floor(self.z), math.floor(self.w))
    def fract(self):
        return Vec4(math.fract(self.x), math.fract(self.y), math.fract(self.z), math.fract(self.w))
    def __len__(self):
        return 4
    def __getitem__(self, key):
        return self.xyzw[key]
    def dot(self, other):
        return (self.x * other.x + self.y * other.y + self.z * other.z + self.w * other.w)
    def __round__(self):
        return Vec4(round(self.x), round(self.y), round(self.z), round(self.w))


class vec3:  # this class stores and operates an a tuple/list containing three items (class functions gone over in the Vec2 class except for .cross)
    def __init__(self, x=None, y=None, z=None):
        try:
            if None in [x, y, z]:
                if y == None:
                    y = x
                    z = x
                else:
                    if x == None:
                        raise SyntaxError("Position is undefined, please put an x or an x, y and z")
                    else:
                        SyntaxError("Requires more information, please put an x or an x, y and z")
        except AttributeError:
            try:
                length = len(x)
                if length == 2:
                    self.x = x.x
                    self.y = x.y
                    self.z = y
                else:
                    raise TypeError("Vectors Is To Long")
            except TypeError:
                self.x = x
                try:
                    length = len(y)
                    if length == 2:
                        self.y = y.x
                        self.z = y.y
                    else:
                        raise TypeError("Vectors Is To Long")
                except TypeError:
                    self.y = y
                    self.z = z
            x = self.x
            y = self.y
            z = self.z
        
        self.x = x
        self.y = y
        self.z = z
        self.w = 0
        self.xy = [x, y]
        self.xyz = [x, y, z]
        
        self.yz = [y, z]
        self.xy = [x, y]
        self.xz = [x, z]
        
        self.r = x
        self.g = y
        self.b = z
        self.rgb = [x, y, z]
    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, other):
        return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)
    def __truediv__(self, other):
        return Vec3(divide(self.x, other.x), divide(self.y, other.y), divide(self.z, other.z))
    def __floordiv__(self, other):
        return Vec3(self.x//other.x, self.y//other.y, self.z//other.z)
    def __mod__(self, other):
        return Vec3(self.x%other.x, self.y%other.y, self.z%other.z)
    def __pow__(self, other):
        return Vec3(self.x**other.x, self.y**other.y, self.z**other.z)
    def __rshift__(self, other):
        return Vec3(self.x>>other.x, self.y>>other.y, self.z>>other.z)
    def __lshift__(self, other):
        return Vec3(self.x<<other.x, self.y<<other.y, self.z<<other.z)
    def __lt__(self, other):
        dot1 = (self.x * self.x) + (self.y * self.y) + (self.z * self.z)
        dot2 = (other.x * other.x) + (other.y * other.y) + (other.z * other.z)
        if dot1 < dot2:
            return True
        else:
            return False
    def __gt__(self, other):
        dot1 = (self.x * self.x) + (self.y * self.y) + (self.z * self.z)
        dot2 = (other.x * other.x) + (other.y * other.y) + (other.z * other.z)
        if dot1 > dot2:
            return True
        else:
            return False
    def __le__(self, other):
        dot1 = (self.x * self.x) + (self.y * self.y) + (self.z * self.z)
        dot2 = (other.x * other.x) + (other.y * other.y) + (other.z * other.z)
        if dot1 <= dot2:
            return True
        else:
            return False
    def __ge__(self, other):
        dot1 = (self.x * self.x) + (self.y * self.y) + (self.z * self.z)
        dot2 = (other.x * other.x) + (other.y * other.y) + (other.z * other.z)
        if dot1 >= dot2:
            return True
        else:
            return False
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False
    def __ne__(self, other):
        if self.x != other.x and self.y != other.y and self.z != other.z:
            return True
        else:
            return False
    def __isub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
    def __iadd__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    def __imult__(self, other):
        return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)
    def __idiv__(self, other):
        return Vec3(divide(self.x, other.x), divide(self.y, other.y), divide(self.z, other.z))
    def __ifloordiv__(self, other):
        return Vec3(self.x//other.x, self.y//other.y, self.z//other.z)
    def __imod__(self, other):
        return Vec3(self.x%other.x, self.y%other.y, self.z%other.z)
    def __ipow__(self, other):
        return Vec3(self.x**other.x, self.y**other.y, self.z**other.z)
    def __irshift__(self, other):
        return Vec3(self.x >> other.x, self.y >> other.y, self.z >> other.z)
    def __ilshift__(self, other):
        return Vec3(self.x << other.x, self.y << other.y, self.z << other.z)
    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)
    def __pos__(self, other):
        return Vec3(+self.x, +self.y, +self.z)
    def __abs__(self):
        return Vec3(abs(self.x), abs(self.y), abs(self.z))
    def __str__(self):
        return 'Vec3(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'
    def mix(self, other, percentage):
        return Vec3(math.mix(self.x, other.x, percentage), math.mix(self.y, other.y, percentage), math.mix(self.z, other.z, percentage))
    def clamp(self, min_, max_):
        return Vec3(math.clamp(self.x, min_, max_), math.clamp(self.y, min_, max_), math.clamp(self.z, min_, max_))
    def sqrt(self):
        return Vec3(math.sqrt(self.x), math.sqrt(self.y), math.sqrt(self.z))
    def tan(self):
        return Vec3(math.tan(self.x), math.tan(self.y), math.tan(self.z))
    def cross(self, other):  # returns the cross product of two Vectors
        val1 = (self.y * other.z) - (self.z * other.y)
        val2 = (self.z * other.x) - (self.x * other.z)
        val3 = (self.x * other.y) - (self.y * other.x)
        return Vec3(val1, val2, val3)
    def sin(self):
        return Vec3(math.sin(self.x), math.sin(self.y), math.sin(self.z))
    def cos(self):
        return Vec3(math.cos(self.x), math.cos(self.y), math.cos(self.z))
    def length(self):
        return math.lengthOfList(self.xyz)
    def floor(self):
        return Vec3(math.floor(self.x), math.floor(self.y), math.floor(self.z))
    def fract(self):
        return Vec3(math.fract(self.x), math.fract(self.y), math.fract(self.z))
    def __len__(self):
        return 3
    def __getitem__(self, key):
        return self.xyz[key]
    def dot(self, other):
        return (self.x * other.x + self.y * other.y + self.z * other.z)
    def __round__(self):
        return Vec3(round(self.x), round(self.y), round(self.z))


class vec2:  # this class stores and operates on a tuple/list containing two items
    def __init__(self, x=None, y=None):  # initializing the tuple/list
        if None in [x, y]:  # filling in the empty places of the Vector (i like to call this smart fill so you can do things like vec2(0) == vec2(0, 0))
            if y == None:
                y = x
            else:
                raise SyntaxError("Position is undefined, please put an x or an x and y")
        
        # defining the values of the Vector
        self.x = x
        self.y = y
        self.z = 0
        self.w = 0
        self.xy = [x, y]
        
        self.r = x
        self.g = y
        self.rg = [x, y]
    def __add__(self, other):  # adding two list like Vector1 + Vector2
        return Vec2(self.x + other.x, self.y + other.y)
    def __sub__(self, other):  # subtracting two Vectors like Vector1 - Vector2
        return Vec2(self.x - other.x, self.y - other.y)
    def __mul__(self, other):  # multiplying two Vectors like Vector1 * Vector2
        return Vec2(self.x * other.x, self.y * other.y)
    def __truediv__(self, other):  # divides two Vectors like Vector1 / Vector2
        return Vec2(divide(self.x, other.x), divide(self.y, other.y))
    def __floordiv__(self, other):  # divides two Vectors and returns the int of the division like Vector1 // Vector2
        return Vec2(self.x//other.x, self.y//other.y)
    def __mod__(self, other):  # gets the mod of two Vectors like Vector1 % Vector2
        return Vec2(self.x%other.x, self.y%other.y)
    def __pow__(self, other):  # gets the power of two Vectors like Vector1 ** Vector2
        return Vec2(self.x**other.x, self.y**other.y)
    def __rshift__(self, other):  # bit shifts to the right like Vector1 >> Vector2
        return Vec2(self.x>>other.x, self.y>>other.y)
    def __lshift__(self, other):  # bit shifts to the left like Vector1 << Vector2
        return Vec2(self.x<<other.x, self.y<<other.y)
    def __lt__(self, other):  # compares two Vectors magnitudes/dot products like Vector1 < Vector2
        dot1 = (self.x * self.x) + (self.y * self.y)
        dot2 = (other.x * other.x) + (other.y * other.y)
        if dot1 < dot2:
            return True
        else:
            return False
    def __gt__(self, other):  # compares two Vectors magnitudes/dot products like Vector1 > Vector2
        dot1 = (self.x * self.x) + (self.y * self.y)
        dot2 = (other.x * other.x) + (other.y * other.y)
        if dot1 > dot2:
            return True
        else:
            return False
    def __le__(self, other):  # compares two Vectors magnitudes/dot products like Vector1 <= Vector2
        dot1 = (self.x * self.x) + (self.y * self.y)
        dot2 = (other.x * other.x) + (other.y * other.y)
        if dot1 <= dot2:
            return True
        else:
            return False
    def __ge__(self, other):  # compares two Vectors magnitudes/dot products like Vector1 >= Vector2
        dot1 = (self.x * self.x) + (self.y * self.y)
        dot2 = (other.x * other.x) + (other.y * other.y)
        if dot1 >= dot2:
            return True
        else:
            return False
    def __eq__(self, other):  # checks if two Vectors are equal like Vector1 == Vector2
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
    def __ne__(self, other):  # checks if the Vectors are not equal like Vector1 != Vector2
        if self.x != other.x and self.y != other.y:
            return True
        else:
            return False
    def __isub__(self, other):  # subtracts a Vector from another Vector by using Vector1 -= Vector2
        return Vec2(self.x - other.x, self.y - other.y)
    def __iadd__(self, other):  # adds two Vectors by using Vector1 += Vector2
        return Vec2(self.x + other.x, self.y + other.y)
    def __imult__(self, other):  # multiples the Vector by another Vector by putting Vector1 *= Vector2
        return Vec2(self.x * other.x, self.y * other.y)
    def __idiv__(self, other):  # returns the Vector divided by another Vector by puting Vector1 /= Vector2
        return Vec2(divide(self.x, other.x), divide(self.y, other.y))
    def __ifloordiv__(self, other):  # gets the int of the divided product by using Vector1 //= Vector2
        return Vec2(self.x//other.x, self.y//other.y)
    def __imod__(self, other):  # gets the mod of the Vector and another Vector using Vector1 %= Vector2
        return Vec2(self.x%other.x, self.y%other.y)
    def __ipow__(self, other):  # puts the Vector to the power of another Vector using Vector1 **= Vector2
        return Vec2(self.x**other.x, self.y**other.y)
    def __irshift__(self, other):  # bit shifts to the right by using >>=
        return Vec2(self.x >> other.x, self.y >> other.y)
    def __ilshift__(self, other):  # bit shifts to the left by using <<=
        return Vec2(self.x << other.x, self.y << other.y)
    def __neg__(self):  # makes the Vector negative when you use -Vector
        return Vec2(-self.x, -self.y)
    def __pos__(self, other):  # makes the Vector positive when you use +Vector
        return Vec2(+self.x, +self.y)
    def __abs__(self):  # returns the absolute value of the Vector when you use abs()
        return Vec2(abs(self.x), abs(self.y))
    def __str__(self):  # this function makes it return the position as a string when printing (using the print("text") in python) the Vector
        return 'Vec2(' + str(self.x) + ', ' + str(self.y) + ')'
    def mix(self, other, percentage):  # mixes the Vector with another Vector based on a percentage
        return Vec2(math.mix(self.x, other.x, percentage), math.mix(self.y, other.y, percentage))
    def clamp(self, min_, max_):  # clamps the Vector
        return Vec2(math.clamp(self.x, min_, max_), math.clamp(self.y, min_, max_))
    def sqrt(self):  # returns the square root of the Vector
        return Vec2(math.sqrt(self.x), math.sqrt(self.y))
    def tan(self):  # returns the tangent of the Vector
        return Vec2(math.tan(self.x), math.tan(self.y))
    def sin(self):  # returns the sign of the Vector
        return Vec2(math.sin(self.x), math.sin(self.y))
    def cos(self):  # returns the cosine of the Vector
        return Vec2(math.cos(self.x), math.cos(self.y))
    def length(self):  # gets the length of the Vector (length(Vector) also works)
        return math.lengthOfList(self.xy)
    def floor(self):  # gets the floor of the Vector
        return Vec2(math.floor(self.x), math.floor(self.y))
    def fract(self):  # gets the decimal value of the number
        return Vec2(math.fract(self.x), math.fract(self.y))
    def __len__(self):  # returns the length of the Vector when you use the len() function
        return 2
    def __getitem__(self, key):  # gets the item at an index
        return self.xy[key]
    def dot(self, other):  # returns the dot product of tow vectors
        return (self.x * other.x + self.y * other.y)
    def __round__(self):  # rounds the vector
        return Vec2(round(self.x), round(self.y))


class Vec4:  # this class dosent use the smart fill making it slightly faster (what i mean by slighty faster is a 0.00000000001% speed increase but when doing things like ray tracing this version of this class will cause a noticable speed up)
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.xy = [x, y]
        self.xyz = [x, y, z]
        self.xyzw = [x, y, z, w]
        
        self.yz = [y, z]
        self.xy = [x, y]
        self.xz = [x, z]
        
        self.xyw = [x, y, w]
        
        self.r = x
        self.g = y
        self.b = z
        self.a = w
        self.rgb = [x, y, z]
        self.rgba = [x, y, z, w]
    def __add__(self, other):
        return Vec4(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)
    def __sub__(self, other):
        return Vec4(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)
    def __mul__(self, other):
        return Vec4(self.x * other.x, self.y * other.y, self.z * other.z, self.w * other.w)
    def __truediv__(self, other):
        return Vec4(divide(self.x, other.x), divide(self.y, other.y), divide(self.z, other.z), divide(self.w, other.w))
    def __floordiv__(self, other):
        return Vec4(self.x//other.x, self.y//other.y, self.z//other.z, self.w//other.w)
    def __mod__(self, other):
        return Vec4(self.x%other.x, self.y%other.y, self.z%other.z, self.w%other.w)
    def __pow__(self, other):
        return Vec4(self.x**other.x, self.y**other.y, self.z**other.z, self.w**other.w)
    def __rshift__(self, other):
        return Vec4(self.x>>other.x, self.y>>other.y, self.z>>other.z, self.w>>other.w)
    def __lshift__(self, other):
        return Vec4(self.x<<other.x, self.y<<other.y, self.z<<other.z, self.w<<other.w)
    def __lt__(self, other):
        dot1 = (self.x * self.x) + (self.y * self.y) + (self.z * self.z) + (self.w * self.w)
        dot2 = (other.x * other.x) + (other.y * other.y) + (other.z * other.z) + (other.w * other.w)
        if dot1 < dot2:
            return True
        else:
            return False
    def __gt__(self, other):
        dot1 = (self.x * self.x) + (self.y * self.y) + (self.z * self.z) + (self.w * self.w)
        dot2 = (other.x * other.x) + (other.y * other.y) + (other.z * other.z) + (other.w * other.w)
        if dot1 > dot2:
            return True
        else:
            return False
    def __le__(self, other):
        dot1 = (self.x * self.x) + (self.y * self.y) + (self.z * self.z) + (self.w * self.w)
        dot2 = (other.x * other.x) + (other.y * other.y) + (other.z * other.z) + (other.w * other.w)
        if dot1 <= dot2:
            return True
        else:
            return False
    def __ge__(self, other):
        dot1 = (self.x * self.x) + (self.y * self.y) + (self.z * self.z) + (self.w * self.w)
        dot2 = (other.x * other.x) + (other.y * other.y) + (other.z * other.z) + (other.w * other.w)
        if dot1 >= dot2:
            return True
        else:
            return False
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z and self.w == other.w:
            return True
        else:
            return False
    def __ne__(self, other):
        if self.x != other.x and self.y != other.y and self.z != other.z and self.w != other.w:
            return True
        else:
            return False
    def __isub__(self, other):
        return Vec4(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)
    def __iadd__(self, other):
        return Vec4(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)
    def __imult__(self, other):
        return Vec4(self.x * other.x, self.y * other.y, self.z * other.z, self.w * other.w)
    def __idiv__(self, other):
        return Vec4(divide(self.x, other.x), divide(self.y, other.y), divide(self.z, other.z), divide(self.w, other.w))
    def __ifloordiv__(self, other):
        return Vec4(self.x//other.x, self.y//other.y, self.z//other.z, self.w//other.w)
    def __imod__(self, other):
        return Vec4(self.x%other.x, self.y%other.y, self.z%other.z, self.w%other.w)
    def __ipow__(self, other):
        return Vec4(self.x**other.x, self.y**other.y, self.z**other.z, self.w**other.w)
    def __irshift__(self, other):
        return Vec4(self.x >> other.x, self.y >> other.y, self.z >> other.z, self.w >> other.w)
    def __ilshift__(self, other):
        return Vec4(self.x << other.x, self.y << other.y, self.z << other.z, self.w << other.w)
    def __neg__(self):
        return Vec4(-self.x, -self.y, -self.z, -self.w)
    def __pos__(self, other):
        return Vec4(+self.x, +self.y, +self.z, +self.w)
    def __abs__(self):
        return Vec4(abs(self.x), abs(self.y), abs(self.z), abs(self.w))
    def __str__(self):
        return 'Vec4(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ', ' + str(self.w) + ')'
    def mix(self, other, percentage):
        return Vec4(math.mix(self.x, other.x, percentage), math.mix(self.y, other.y, percentage), math.mix(self.z, other.z, percentage), math.mix(self.w, other.w, percentage))
    def clamp(self, min_, max_):
        return Vec4(math.clamp(self.x, min_, max_), math.clamp(self.y, min_, max_), math.clamp(self.z, min_, max_), math.clamp(self.w, min_, max_))
    def sqrt(self):
        return Vec4(math.sqrt(self.x), math.sqrt(self.y), math.sqrt(self.z), math.sqrt(self.w))
    def tan(self):
        return Vec4(math.tan(self.x), math.tan(self.y), math.tan(self.z), math.tan(self.w))
    def sin(self):
        return Vec4(math.sin(self.x), math.sin(self.y), math.sin(self.z), math.sin(self.w))
    def cos(self):
        return Vec4(math.cos(self.x), math.cos(self.y), math.cos(self.z), math.cos(self.w))
    def length(self):
        return math.lengthOfList(self.xyzw)
    def floor(self):
        return Vec4(math.floor(self.x), math.floor(self.y), math.floor(self.z), math.floor(self.w))
    def fract(self):
        return Vec4(math.fract(self.x), math.fract(self.y), math.fract(self.z), math.fract(self.w))
    def __len__(self):
        return 4
    def __getitem__(self, key):
        return self.xyzw[key]
    def dot(self, other):
        return (self.x * other.x + self.y * other.y + self.z * other.z + self.w * other.w)
    def __round__(self):
        return Vec4(round(self.x), round(self.y), round(self.z), round(self.w))


class Vec3:  # this class dosent use the smart fill making it slightly faster (what i mean by slighty faster is a 0.00000000001% speed increase but when doing things like ray tracing this version of this class will cause a noticable speed up)
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.w = 0
        self.xy = [x, y]
        self.xyz = [x, y, z]
        
        self.yz = [y, z]
        self.xy = [x, y]
        self.xz = [x, z]
        
        self.r = x
        self.g = y
        self.b = z
        self.rgb = [x, y, z]
    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, other):
        return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)
    def __truediv__(self, other):
        return Vec3(divide(self.x, other.x), divide(self.y, other.y), divide(self.z, other.z))
    def __floordiv__(self, other):
        return Vec3(self.x//other.x, self.y//other.y, self.z//other.z)
    def __mod__(self, other):
        return Vec3(self.x%other.x, self.y%other.y, self.z%other.z)
    def __pow__(self, other):
        return Vec3(self.x**other.x, self.y**other.y, self.z**other.z)
    def __rshift__(self, other):
        return Vec3(self.x>>other.x, self.y>>other.y, self.z>>other.z)
    def __lshift__(self, other):
        return Vec3(self.x<<other.x, self.y<<other.y, self.z<<other.z)
    def __lt__(self, other):
        dot1 = (self.x * self.x) + (self.y * self.y) + (self.z * self.z)
        dot2 = (other.x * other.x) + (other.y * other.y) + (other.z * other.z)
        if dot1 < dot2:
            return True
        else:
            return False
    def __gt__(self, other):
        dot1 = (self.x * self.x) + (self.y * self.y) + (self.z * self.z)
        dot2 = (other.x * other.x) + (other.y * other.y) + (other.z * other.z)
        if dot1 > dot2:
            return True
        else:
            return False
    def __le__(self, other):
        dot1 = (self.x * self.x) + (self.y * self.y) + (self.z * self.z)
        dot2 = (other.x * other.x) + (other.y * other.y) + (other.z * other.z)
        if dot1 <= dot2:
            return True
        else:
            return False
    def __ge__(self, other):
        dot1 = (self.x * self.x) + (self.y * self.y) + (self.z * self.z)
        dot2 = (other.x * other.x) + (other.y * other.y) + (other.z * other.z)
        if dot1 >= dot2:
            return True
        else:
            return False
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False
    def __ne__(self, other):
        if self.x != other.x and self.y != other.y and self.z != other.z:
            return True
        else:
            return False
    def __isub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
    def __iadd__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    def __imult__(self, other):
        return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)
    def __idiv__(self, other):
        return Vec3(divide(self.x, other.x), divide(self.y, other.y), divide(self.z, other.z))
    def __ifloordiv__(self, other):
        return Vec3(self.x//other.x, self.y//other.y, self.z//other.z)
    def __imod__(self, other):
        return Vec3(self.x%other.x, self.y%other.y, self.z%other.z)
    def __ipow__(self, other):
        return Vec3(self.x**other.x, self.y**other.y, self.z**other.z)
    def __irshift__(self, other):
        return Vec3(self.x >> other.x, self.y >> other.y, self.z >> other.z)
    def __ilshift__(self, other):
        return Vec3(self.x << other.x, self.y << other.y, self.z << other.z)
    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)
    def __pos__(self, other):
        return Vec3(+self.x, +self.y, +self.z)
    def __abs__(self):
        return Vec3(abs(self.x), abs(self.y), abs(self.z))
    def __str__(self):
        return 'Vec3(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'
    def mix(self, other, percentage):
        return Vec3(math.mix(self.x, other.x, percentage), math.mix(self.y, other.y, percentage), math.mix(self.z, other.z, percentage))
    def clamp(self, min_, max_):
        return Vec3(math.clamp(self.x, min_, max_), math.clamp(self.y, min_, max_), math.clamp(self.z, min_, max_))
    def sqrt(self):
        return Vec3(math.sqrt(self.x), math.sqrt(self.y), math.sqrt(self.z))
    def tan(self):
        return Vec3(math.tan(self.x), math.tan(self.y), math.tan(self.z))
    def cross(self, other):  # returns the cross product of two Vectors
        val1 = (self.y * other.z) - (self.z * other.y)
        val2 = (self.z * other.x) - (self.x * other.z)
        val3 = (self.x * other.y) - (self.y * other.x)
        return Vec3(val1, val2, val3)
    def sin(self):
        return Vec3(math.sin(self.x), math.sin(self.y), math.sin(self.z))
    def cos(self):
        return Vec3(math.cos(self.x), math.cos(self.y), math.cos(self.z))
    def length(self):
        return math.lengthOfList(self.xyz)
    def floor(self):
        return Vec3(math.floor(self.x), math.floor(self.y), math.floor(self.z))
    def fract(self):
        return Vec3(math.fract(self.x), math.fract(self.y), math.fract(self.z))
    def __len__(self):
        return 3
    def __getitem__(self, key):
        return self.xyz[key]
    def dot(self, other):
        return (self.x * other.x + self.y * other.y + self.z * other.z)
    def __round__(self):
        return Vec3(round(self.x), round(self.y), round(self.z))


class Vec2:  # this class dosent use the smart fill making it slightly faster (what i mean by slighty faster is a 0.00000000001% speed increase but when doing things like ray tracing this version of this class will cause a noticable speed up)
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = 0
        self.w = 0
        self.xy = [x, y]
        
        self.r = x
        self.g = y
        self.rg = [x, y]
    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return Vec2(self.x * other.x, self.y * other.y)
    def __truediv__(self, other):
        return Vec2(divide(self.x, other.x), divide(self.y, other.y))
    def __floordiv__(self, other):
        return Vec2(self.x//other.x, self.y//other.y)
    def __mod__(self, other):
        return Vec2(self.x%other.x, self.y%other.y)
    def __pow__(self, other):
        return Vec2(self.x**other.x, self.y**other.y)
    def __rshift__(self, other):
        return Vec2(self.x>>other.x, self.y>>other.y)
    def __lshift__(self, other):
        return Vec2(self.x<<other.x, self.y<<other.y)
    def __lt__(self, other):
        dot1 = (self.x * self.x) + (self.y * self.y)
        dot2 = (other.x * other.x) + (other.y * other.y)
        if dot1 < dot2:
            return True
        else:
            return False
    def __gt__(self, other):
        dot1 = (self.x * self.x) + (self.y * self.y)
        dot2 = (other.x * other.x) + (other.y * other.y)
        if dot1 > dot2:
            return True
        else:
            return False
    def __le__(self, other):
        dot1 = (self.x * self.x) + (self.y * self.y)
        dot2 = (other.x * other.x) + (other.y * other.y)
        if dot1 <= dot2:
            return True
        else:
            return False
    def __ge__(self, other):
        dot1 = (self.x * self.x) + (self.y * self.y)
        dot2 = (other.x * other.x) + (other.y * other.y)
        if dot1 >= dot2:
            return True
        else:
            return False
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
    def __ne__(self, other):
        if self.x != other.x and self.y != other.y:
            return True
        else:
            return False
    def __isub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)
    def __iadd__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)
    def __imult__(self, other):
        return Vec2(self.x * other.x, self.y * other.y)
    def __idiv__(self, other):
        return Vec2(divide(self.x, other.x), divide(self.y, other.y))
    def __ifloordiv__(self, other):
        return Vec2(self.x//other.x, self.y//other.y)
    def __imod__(self, other):
        return Vec2(self.x%other.x, self.y%other.y)
    def __ipow__(self, other):
        return Vec2(self.x**other.x, self.y**other.y)
    def __irshift__(self, other):
        return Vec2(self.x >> other.x, self.y >> other.y)
    def __ilshift__(self, other):
        return Vec2(self.x << other.x, self.y << other.y)
    def __neg__(self):
        return Vec2(-self.x, -self.y)
    def __pos__(self, other):
        return Vec2(+self.x, +self.y)
    def __abs__(self):
        return Vec2(abs(self.x), abs(self.y))
    def __str__(self):
        return 'Vec2(' + str(self.x) + ', ' + str(self.y) + ')'
    def mix(self, other, percentage):
        return Vec2(math.mix(self.x, other.x, percentage), math.mix(self.y, other.y, percentage))
    def clamp(self, min_, max_):
        return Vec2(math.clamp(self.x, min_, max_), math.clamp(self.y, min_, max_))
    def sqrt(self):
        return Vec2(math.sqrt(self.x), math.sqrt(self.y))
    def tan(self):
        return Vec2(math.tan(self.x), math.tan(self.y))
    def sin(self):
        return Vec2(math.sin(self.x), math.sin(self.y))
    def cos(self):
        return Vec2(math.cos(self.x), math.cos(self.y))
    def length(self):
        return math.lengthOfList(self.xy)
    def floor(self):
        return Vec2(math.floor(self.x), math.floor(self.y))
    def fract(self):
        return Vec2(math.fract(self.x), math.fract(self.y))
    def __len__(self):
        return 2
    def __getitem__(self, key):
        return self.xy[key]
    def dot(self, other):
        return (self.x * other.x + self.y * other.y)
    def __round__(self):
        return Vec2(round(self.x), round(self.y))


def mix(vector1, vector2, percentage):  # mixes two vectors based on a percentage
    return vector1.mix(vector2, percentage)


def Int(Vector):  # gets the floor/int of a vector
    return floor(Vector)


def clamp(Vector, min_, max_):  # clamps a vector between two values
    return Vector.clamp(min_, max_)


def fract(Vector):  # gets the fract of a vector (vector - int(vector))
    return Vector.fract()


def sqrt(Vector):  # gets the square root of a vector
    return Vector.sqrt()


def floor(Vector):  # gets the floor of a vector
    return Vector.floor()


def cos(Vector):  # gets the cosine of a vector
    return Vector.cos()


def sin(Vector):  # gets the sin of a vector
    return Vector.sin()


def tan(Vector):  # gets the tangint of a vector
    return Vector.tan()


def dot(vector1, vector2):  # gets the dot product of two vectors
    return vector1.dot(vector2)


def cross(vector1, vector2):  # gets the cross product of two vectors
    return vector1.cross(vector2)


def normalize(Vector):  # normalizes a vector
    mag = length(Vector)
    return Vector / Vec4(mag, mag, mag, mag)


def length(Vector):  # gets the length of a Vector (using the pythagorean theorem)
    return Vector.length()


class math:
    def mix(value1, value2, percentage):  # mixes two numbers based on a number ranging from 1 - 0
        percentage = math.clamp(percentage, 0, 1)
        return (value1*(1 - percentage))+(value2*percentage)
    def tan(value):  # returns the tangent of a number
        return Math.tan(value)
    def sin(value):  # returns the sign of a number
        return Math.sin(value)
    def cos(value):  # returns the cosine of a number
        return Math.cos(value)
    def fract(value):  # returns the decimal of the value
        return value - math.floor(value)
    def floor(value):  # returns the floor of the value
        return Math.floor(value)
    def clamp(val, min_, max_):  # sets the max and min of a number
        return min(max(val, min_), max_)
    def sqrt(value):  # square root
        return Math.sqrt(value)
    def map1D(list, fromMin, fromMax, toMin = None, toMax = None):  # changes the range of a 1d array of data (while keeping the detail of the numbers)
        if None in [toMin, toMax]:
            if toMin == None and toMax == None:
                toMin = fromMin
                toMax = fromMax
                fromMin = math.min1D(list)
                fromMax = math.max1D(list)
            else:
                raise SyntaxError("Invalid Input")
        for x in range(len(list)):
            list[x] -= fromMin
        
        scaler = divideT((toMax - toMin), max(list))
        for x in range(len(list)):
            list[x] *= scaler
            list[x] += toMin
        
        return list
    def map2D(list, fromMin, fromMax, toMin = None, toMax = None):  # changes the range of a 2d array of data (while keeping the detail of the numbers)
        if None in [toMin, toMax]:
            if toMin == None and toMax == None:
                toMin = fromMin
                toMax = fromMax
                fromMin = math.min2D(list)
                fromMax = math.max2D(list)
            else:
                raise SyntaxError("Invalid Input")
        maxOfList = []
        for x in range(len(list)):
            for y in range(len(list[x])):
                list[x][y] -= fromMin
            maxOfList.append(max(list[x]))
        
        maxOfList = max(maxOfList)
        scaler = (toMax - toMin) / maxOfList
        for x in range(len(list)):
            for y in range(len(list[x])):
                list[x][y] *= scaler
                list[x][y] += toMin
        
        return list
    def map3D(list, fromMin, fromMax, toMin = None, toMax = None):  # changes the range of a 3d array of data (while keeping the detail of the numbers)
        if None in [toMin, toMax]:
            if toMin == None and toMax == None:
                toMin = fromMin
                toMax = fromMax
                fromMin = math.min3D(list)
                fromMax = math.max3D(list)
            else:
                raise SyntaxError("Invalid Input")
        maxOfList = []
        for x in range(len(list)):
            for y in range(len(list[x])):
                for z in range(len(list[x][y])):
                    list[x][y][z] -= fromMin
        
        maxOfList = []
        for x in list:
            layer = []
            for y in x:
                layer.append(max(y))
            maxOfList.append(max(layer))
        maxOfList = max(maxOfList)
        
        scaler = (toMax - toMin) / maxOfList
        for x in range(len(list)):
            for y in range(len(list[x])):
                for z in range(len(list[x][y])):
                    list[x][y][z] *= scaler
                    list[x][y][z] += toMin
        
        return list
    def map4D(list, fromMin, fromMax, toMin = None, toMax = None):  # changes the range of a 4d array of data (while keeping the detail of the numbers)
        if None in [toMin, toMax]:
            if toMin == None and toMax == None:
                toMin = fromMin
                toMax = fromMax
                fromMin = math.min4D(list)
                fromMax = math.max4D(list)
            else:
                raise SyntaxError("Invalid Input")
        maxOfList = []
        for x in range(len(list)):
            for y in range(len(list[x])):
                for z in range(len(list[x][y])):
                    for w in range(len(list[x][y][z])):
                        list[x][y][z][w] -= fromMin
        
        maxOfList = []
        for x in list:
            layer = []
            for y in x:
                layer2 = []
                for z in y:
                    layer2.append(max(z))
                layer.append(max(layer2))
            maxOfList.append(max(layer))
        maxOfList = max(maxOfList)
        
        scaler = (toMax - toMin) / maxOfList
        for x in range(len(list)):
            for y in range(len(list[x])):
                for z in range(len(list[x][y])):
                    for w in range(len(list[x][y][z])):
                        list[x][y][z][w] *= scaler
                        list[x][y][z][w] += toMin
        
        return list
    def smooth1D(heights, smoothing = 100):  # smooths a list of numbers making them more uniform/reducing spikes in numbers
        for s in range(smoothing):
            for i in range(len(heights)):
                if i not in [0, len(heights) - 1]:
                    height1 = heights[i - 1]
                    height3 = heights[i + 1]
                    heights[i] = (heights[i] * 0.1) + (height1 * 0.45) + (height3 * 0.45)
        return heights
    def interpalate2(h, x, points):  # interpolates linearly between 2 points (use the math.smooth function for further smoothing)
        return ((list[1].y - list[0].y) / h) * x
    def interpalate3(h, x, list):  # interpolates smoothly between 3 points (use the math.smooth function to fixs small glitches)
        index2 = int(x / h)
        index1 = index2 - 1
        index3 = index2 + 1
        
        height1 = list[index1]
        height2 = list[index2]
        height3 = list[index3]
        
        x1 = index1 * h
        x2 = index2 * h
        x3 = index3 * h
        
        a0 = height2
        a1 = (height3 - height1) / (h * 2)
        a2 = (height1 - 2 * height2 + height3) / ((h ** 2) * 2)
        
        height_out = a0 + a1 * (x - x2) + a2 * (x - x2) ** 2
        
        return height_out
    def interpalate5(h, x, list):  # interpolates smoothly between 5 points (use the math.smooth function to fix glitches)
        middle_index = int(x / h)  #int((x / (h * 5)) * 5)
        index1 = middle_index - 2
        index2 = middle_index - 1
        index3 = middle_index
        index4 = middle_index + 1
        index5 = middle_index + 2
        
        height1 = list[index1]
        height2 = list[index2]
        height3 = list[index3]
        height4 = list[index4]
        height5 = list[index5]
        
        x1 = index1 * h
        x2 = index2 * h
        x3 = index3 * h
        x4 = index4 * h
        x5 = index5 * h
        
        a0 = height3
        a1 = (height4 - height2) / (h * 2)
        a2 = (-height5 + 16 * height4 - 30 * height3 + 16 * height2 - height1) / (24 * (h ** 2))
        a3 = (height5 - 2 * height4 + 2 * height2 - height1) / (12 * (h ** 3))
        
        height = a0 + a1 * (x - x3) + a2 * (x - x3) ** 2 + a3 * (x - x3) ** 3
        
        return height
    def smoothstep(x, e0 = 1, e1 = 1, e2 = 0):  # a function to smoothly step between 0 and 1
        X = math.clamp((x - e0) / (e1 - e2), 0, 1)
        return X * X * (3 - 2 * X)
    def lengthOfList(poses):  # gets the distance of the imputed values (using the pythagorean theorem)
        dist = poses[0]
        for Vector in poses:
            dist = math.sqrt((dist * dist) + (Vector * Vector))
        return dist
    def normalizeList(values):  # normalizes a list of values (for this function you need to put in the .xyz value of the Vector, the functions above do this for you)
        mag = lengthOfList(values)  # gets the magnitude
        new_values = []
        for old_value in values:
            new_values.append(divide(old_value, mag))  # changes the values by the magnitude
        return new_values
    def spline1D(noise, x, h):  # smoothly interpolates at a point between other points on a 1D list
        nx = x / h
        p1 = math.floor(nx)
        p2 = p1 + 1
        p3 = p2 + 1
        p0 = p1 - 1
        
        t = nx - p1
        tt = t * t
        ttt = tt * t
        ttt3 = ttt * 3
        
        q1 = -ttt + 2*tt - t
        q2 = ttt3 - 5*tt + 2
        q3 = -ttt3 + 4*tt + t
        q4 = ttt - tt
        ty = 0.5 * (noise[p0] * q1 + noise[p1] * q2 + noise[p2] * q3 + noise[p3] * q4)
        return ty
    def spline2D(noise, x, y, h):  # smoothly interpolates at a point between other points on a 2D list
        nx = x / h
        i = math.floor(nx)
        ty1 = math.spline1D(noise[i - 1], y, h)
        ty2 = math.spline1D(noise[i    ], y, h)
        ty3 = math.spline1D(noise[i + 1], y, h)
        ty4 = math.spline1D(noise[i + 2], y, h)
        return math.spline1D([ty1, ty2, ty3, ty4], (nx - i) * h + h, h)
    def spline3D(noise, x, y, z, h):  # smoothly interpolates at a point between other points on a 3D list
        nx = x / h
        i = math.floor(nx)
        ty1 = math.spline2D(noise[i - 1], y, z, h)
        ty2 = math.spline2D(noise[i    ], y, z, h)
        ty3 = math.spline2D(noise[i + 1], y, z, h)
        ty4 = math.spline2D(noise[i + 2], y, z, h)
        return math.spline1D([ty1, ty2, ty3, ty4], (nx - i) * h + h, h)
    def spline4D(noise, x, y, z, w, h):  # this is untested but should work and smoothly interpolates at a point between other points on a 4D list
        nx = x / h
        i = math.floor(nx)
        ty1 = math.spline3D(noise[i - 1], y, z, w, h)
        ty2 = math.spline3D(noise[i    ], y, z, w, h)
        ty3 = math.spline3D(noise[i + 1], y, z, w, h)
        ty4 = math.spline3D(noise[i + 2], y, z, w, h)
        return math.spline1D([ty1, ty2, ty3, ty4], (nx - i) * h + h, h)
    def min1D(list):  # gets the min of a list thats dimetion is stated
        return min(list)
    def min2D(list):  # gets the min of a 2d array
        layers = []
        for x in list:
            layers.append(min(x))
        return min(layers)
    def min3D(list):  # gets the min of a 3d array
        layers = []
        for x in list:
            newLayer = []
            for y in x:
                newLayer.append(min(y))
            layers.append(min(newLayer))
        return min(layers)
    def min4D(list):  # gets the min of a 4d array
        layers = []
        for x in list:
            newLayer = []
            for y in x:
                layers2 = []
                for z in y:
                    layers2.append(min(z))
                newLayer.append(min(layers2))
            layers.append(min(newLayer))
        return min(layers)
    def max1D(list):  # gets the max of a list thats dimetion is stated
        return max(list)
    def max2D(list):  # gets the max of a 2d array
        layers = []
        for x in list:
            layers.append(max(x))
        return max(layers)
    def max3D(list):  # gets the max of a 3d array
        layers = []
        for x in list:
            newLayer = []
            for y in x:
                newLayer.append(max(y))
            layers.append(max(newLayer))
        return max(layers)
    def max4D(list):  # gets the max of a 4d array
        layers = []
        for x in list:
            newLayer = []
            for y in x:
                layers2 = []
                for z in y:
                    layers2.append(max(z))
                newLayer.append(max(layers2))
            layers.append(max(newLayer))
        return max(layers)
    def RGBtoKCMY(color):  # converts rgb to kcmy(paint color format)
        """
        R' = R/255
        G' = G/255
        B' = B/255
        The black key (K) color is calculated from the red (R'), green (G') and blue (B') colors:
        K = 1-max(R', G', B')
        The cyan color (C) is calculated from the red (R') and black (K) colors:
        C = (1-R'-K) / (1-K)
        The magenta color (M) is calculated from the green (G') and black (K) colors:
        M = (1-G'-K) / (1-K)
        The yellow color (Y) is calculated from the blue (B') and black (K) colors:
        Y = (1-B'-K) / (1-K)
        
        https://www.rapidtables.com/convert/color/rgb-to-cmyk.html
        """
        R = divideT(color.r, 255)
        G = divideT(color.g, 255)
        B = divideT(color.b, 255)
        
        k = 1 - max([R, G, B])
        c = divideT((1 - R - k), (1 - k))
        m = divideT((1 - G - k), (1 - k))
        y = divideT((1 - B - k), (1 - k))
        
        return Vec4(k, c, m, y)


class dists:  # multipl distance functions for different shapes
    def distToCircularPoint(pos, center, r):  # gets the distance to a sphere/circle/hypershpere from a point (negitive when in the circle)
        return length(pos - center) - r
    def distToPoint(pos, point_pos):  # gets the distance to a point from a point
        return length(pos - point_pos)


class gradient:  # a way to make gradients that specifies what they are being used for
    def color(maxGap = 50):
        return colorGradient(maxGap)
    def number(maxGap = 50):
        return numberGradient(maxGap)
    def vector(maxGap = 50):
        return colorGradient(maxGap)


class numberGradient:  # a gradient for numbers
    def __init__(self, maxGap = 50):
        self.points = {}
        self.maxGap = maxGap
    def add(self, point, number):
        self.points[str(point)] = number
    def grade(self, point):
        point = int(point)
        p = point
        for x in range(self.maxGap):
            try:
                color1 = self.points[str(p)]
                break
            except KeyError:
                p -= 1
        
        if abs(point - p) == self.maxGap - 1:
            raise SyntaxError("Invalid Postion")
        
        distBetweenPoints = abs(point - p)
        
        color2 = None
        p2 = point
        for x in range(self.maxGap):
            try:
                color2 = self.points[str(p2)]
                break
            except KeyError:
                p2 += 1
        
        if color2 == None:
            raise SyntaxError("Invalid Postion")
        
        distBetweenPoints += abs(point - p2)
        
        return math.mix(color1, color2, divideT((point - p), distBetweenPoints))


class colorGradient:  # you can add points (only works in 1D) and then sample at points to craete a smooth color transition with multiple colors each with different distances apart
    def __init__(self, maxGap = 50):
        self.points = {}
        self.maxGap = maxGap
    def add(self, point, color):
        self.points[str(point)] = color
    def grade(self, point):
        point = int(point)
        p = point
        for x in range(self.maxGap):
            try:
                color1 = self.points[str(p)]
                break
            except KeyError:
                p -= 1
        
        if abs(point - p) == self.maxGap - 1:
            raise SyntaxError("Invalid Postion")
        
        distBetweenPoints = abs(point - p)
        
        color2 = Vec3(None, None, None)
        p2 = point
        for x in range(self.maxGap):
            try:
                color2 = self.points[str(p2)]
                break
            except KeyError:
                p2 += 1
        
        if color2 == Vec3(None, None, None):
            raise SyntaxError("Invalid Postion")
        
        distBetweenPoints += abs(point - p2)
        
        return mix(color1, color2, divideT((point - p), distBetweenPoints))


class noise:  # contains perlin noise functions that take in a list of random numbers thats the same dimention as the function, than the x, y, z, and w (only put the one that belong there for the demention of the function) and finaly the distance between points
    def perlin1D(randNoise, h, x):  # perlin noise at the dimention stated
        return math.spline1D(randNoise, x, h)
    def perlin2D(randNoise, h, x, y):
        return math.spline2D(randNoise, x, y, h)
    def perlin3D(randNoise, h, x, y, z):
        return math.spline3D(randNoise, x, y, z, h)
    def perlin4D(randNoise, h, x, y, z, w):
        return math.spline4D(randNoise, x, y, z, w, h)
    def ridge1D(randNoise, h, x):  # ridge noise aka perlin noise with abrupt ridges
        noise = math.spline1D(randNoise, x, h)
        noise = abs(noise)
        noise *= -1
        return noise
    def ridge2D(randNoise, h, x, y):  #
        noise = math.spline2D(randNoise, x, y, h)
        noise = abs(noise)
        noise *= -1
        return noise
    def ridge3D(randNoise, h, x, y, z):
        noise = math.spline3D(randNoise, x, y, z, h)
        noise = abs(noise)
        noise *= -1
        return noise
    def ridge4D(randNoise, h, x, y, z, w):
        noise = math.spline4D(randNoise, x, y, z, w, h)
        noise = abs(noise)
        noise *= -1
        return noise


def array(size, type, number):  # atomticaly fills in and array with numbers, the types are as following with the next input in brackets: constant (number), random int ([min number, max number]), random float ([min number, max number]), perlin ([[min height, max height, distance between points, height alteration method, (this paramiter is only if using mix) percentage (0 - 1)], more octaves that are same as last])   the demention of the array is determind by the len of size which can be a list or vector type.
    dem = len(size)
    if dem == 1:
        if type == 'constant':
            list = []
            for x in range(size[0]):
                list.append(number)
            return list
        elif type == 'random int':
            list = []
            for x in range(size[0]):
                list.append(random.randint(number[0], number[1]))
            return list
        elif type == 'random float':
            list = []
            for x in range(size[0]):
                list.append(random.uniform(number[0], number[1]))
            return list
        elif type == 'perlin':
            list = array(size, 'constant', 0)
            for octave in number:  # [[min, max, h, octave alteration method, (if using mix) mix amount (0 - 1)], nextOctaveSameAsLast]
                rNoise = array(size, 'random float', [octave[0], octave[1]])
                if octave[3] == 'add':
                    for x in range(size[0]):
                        list[x] = noise.perlin1D(rNoise, octave[2], x) + list[x]
                if octave[3] == 'sub':
                    for x in range(size[0]):
                        list[x] = noise.perlin1D(rNoise, octave[2], x) - list[x]
                if octave[3] == 'mix':
                    for x in range(size[0]):
                        list[x] = math.mix(noise.perlin1D(rNoise, octave[2], x), list[x], octave[4])
            return list
        elif type == 'ridge':
            list = array(size, 'constant', 0)
            for octave in number:  # [[min, max, h, octave alteration method, (if using mix) mix amount (0 - 1)], nextOctaveSameAsLast]
                rNoise = array(size, 'random float', [octave[0], octave[1]])
                if octave[3] == 'add':
                    for x in range(size[0]):
                        list[x] = noise.ridge1D(rNoise, octave[2], x) + list[x]
                if octave[3] == 'sub':
                    for x in range(size[0]):
                        list[x] = noise.ridge1D(rNoise, octave[2], x) - list[x]
                if octave[3] == 'mix':
                    for x in range(size[0]):
                        list[x] = math.mix(noise.ridge1D(rNoise, octave[2], x), list[x], octave[4])
            return list
        else:
            raise TypeError("Invalid Fill Type. Please use \"constant\", \"random int\", \"random float\", \"perlin\" or \"ridge\"")
    elif dem == 2:
        if type == 'constant':
            list = []
            for x in range(size[0]):
                layer = []
                for y in range(size[1]):
                    layer.append(number)
                list.append(layer)
            return list
        elif type == 'random int':
            list = []
            for x in range(size[0]):
                layer = []
                for y in range(size[1]):
                    layer.append(random.randint(number[0], number[1]))
                list.append(layer)
            return list
        elif type == 'random float':
            list = []
            for x in range(size[0]):
                layer = []
                for y in range(size[1]):
                    layer.append(random.uniform(number[0], number[1]))
                list.append(layer)
            return list
        elif type == 'perlin':
            list = array(size, 'constant', 0)
            for octave in number:  # [[min, max, h, octave alteration method, (if using mix) mix amount (0 - 1)], nextOctaveSameAsLast]
                rNoise = array(size, 'random float', [octave[0], octave[1]])
                if octave[3] == 'add':
                    for x in range(size[0]):
                        for y in range(size[1]):
                            list[x][y] = noise.perlin2D(rNoise, octave[2], x, y) + list[x][y]
                if octave[3] == 'sub':
                    for x in range(size[0]):
                        for y in range(size[1]):
                            list[x][y] = noise.perlin2D(rNoise, octave[2], x, y) - list[x][y]
                if octave[3] == 'mix':
                    for x in range(size[0]):
                        for y in range(size[1]):
                            list[x][y] = math.mix(noise.perlin2D(rNoise, octave[2], x, y), list[x][y], octave[4])
            return list
        elif type == 'ridge':
            list = array(size, 'constant', 0)
            for octave in number:  # [[min, max, h, octave alteration method, (if using mix) mix amount (0 - 1)], nextOctaveSameAsLast]
                rNoise = array(size, 'random float', [octave[0], octave[1]])
                if octave[3] == 'add':
                    for x in range(size[0]):
                        for y in range(size[1]):
                            list[x][y] = noise.ridge2D(rNoise, octave[2], x, y) + list[x][y]
                if octave[3] == 'sub':
                    for x in range(size[0]):
                        for y in range(size[1]):
                            list[x][y] = noise.ridge2D(rNoise, octave[2], x, y) - list[x][y]
                if octave[3] == 'mix':
                    for x in range(size[0]):
                        for y in range(size[1]):
                            list[x][y] = math.mix(noise.ridge2D(rNoise, octave[2], x, y), list[x][y], octave[4])
            return list
        else:
            raise TypeError("Invalid Fill Type. Please use \"constant\", \"random int\", \"random float\", \"perlin\" or \"ridge\"")
    elif dem == 3:
        if type == 'constant':
            list = []
            for x in range(size[0]):
                layer = []
                for y in range(size[1]):
                    layer2 = []
                    for z in range(size[2]):
                        layer2.append(number)
                    layer.append(layer2)
                list.append(layer)
            return list
        elif type == 'random int':
            list = []
            for x in range(size[0]):
                layer = []
                for y in range(size[1]):
                    layer2 = []
                    for z in range(size[2]):
                        layer2.append(random.randint(number[0], number[1]))
                    layer.append(layer2)
                list.append(layer)
            return list
        elif type == 'random float':
            list = []
            for x in range(size[0]):
                layer = []
                for y in range(size[1]):
                    layer2 = []
                    for z in range(size[2]):
                        layer2.append(random.uniform(number[0], number[1]))
                    layer.append(layer2)
                list.append(layer)
            return list
        elif type == 'perlin':
            list = array(size, 'constant', 0)
            for octave in number:  # [[min, max, h, octave alteration method, (if using mix) mix amount (0 - 1)], nextOctaveSameAsLast]
                rNoise = array(size, 'random float', [octave[0], octave[1]])
                if octave[3] == 'add':
                    for x in range(size[0]):
                        for y in range(size[1]):
                            for z in range(size[2]):
                                list[x][y][z] = noise.perlin3D(rNoise, octave[2], x, y, z) + list[x][y][z]
                if octave[3] == 'sub':
                    for x in range(size[0]):
                        for y in range(size[1]):
                            for z in range(size[2]):
                                list[x][y][z] = noise.perlin3D(rNoise, octave[2], x, y, z) - list[x][y][z]
                if octave[3] == 'mix':
                    for x in range(size[0]):
                        for y in range(size[1]):
                            for z in range(size[2]):
                                list[x][y][z] = math.mix(noise.perlin3D(rNoise, octave[2], x, y, z), list[x][y][z], octave[4])
            return list
        elif type == 'ridge':
            list = array(size, 'constant', 0)
            for octave in number:  # [[min, max, h, octave alteration method, (if using mix) mix amount (0 - 1)], nextOctaveSameAsLast]
                rNoise = array(size, 'random float', [octave[0], octave[1]])
                if octave[3] == 'add':
                    for x in range(size[0]):
                        for y in range(size[1]):
                            for z in range(size[2]):
                                list[x][y][z] = noise.ridge3D(rNoise, octave[2], x, y, z) + list[x][y][z]
                if octave[3] == 'sub':
                    for x in range(size[0]):
                        for y in range(size[1]):
                            for z in range(size[2]):
                                list[x][y][z] = noise.ridge3D(rNoise, octave[2], x, y, z) - list[x][y][z]
                if octave[3] == 'mix':
                    for x in range(size[0]):
                        for y in range(size[1]):
                            for z in range(size[2]):
                                list[x][y][z] = math.mix(noise.ridge3D(rNoise, octave[2], x, y, z), list[x][y][z], octave[4])
            return list
        else:
            raise TypeError("Invalid Fill Type. Please use \"constant\", \"random int\", \"random float\", \"perlin\" or \"ridge\"")
    elif dem == 4:
        if type == 'constant':
            list = []
            for x in range(size[0]):
                layer = []
                for y in range(size[1]):
                    layer2 = []
                    for z in range(size[2]):
                        layer3 = []
                        for w in range(size[3]):
                            layer3.append(number)
                        layer2.append(layer3)
                    layer.append(layer2)
                list.append(layer)
            return list
        elif type == 'random int':
            list = []
            for x in range(size[0]):
                layer = []
                for y in range(size[1]):
                    layer2 = []
                    for z in range(size[2]):
                        layer3 = []
                        for w in range(size[3]):
                            layer3.append(random.randint(number[0], number[1]))
                        layer2.append(layer3)
                    layer.append(layer2)
                list.append(layer)
            return list
        elif type == 'random float':
            list = []
            for x in range(size[0]):
                layer = []
                for y in range(size[1]):
                    layer2 = []
                    for z in range(size[2]):
                        layer3 = []
                        for w in range(size[3]):
                            layer3.append(random.uniform(number[0], number[1]))
                        layer2.append(layer3)
                    layer.append(layer2)
                list.append(layer)
            return list
        elif type == 'perlin':
            list = array(size, 'constant', 0)
            for octave in number:  # [[min, max, h, octave alteration method, (if using mix) mix amount (0 - 1)], nextOctaveSameAsLast]
                rNoise = array(size, 'random float', [octave[0], octave[1]])
                if octave[3] == 'add':
                    for x in range(size[0]):
                        for y in range(size[1]):
                            for z in range(size[2]):
                                for w in range(size[3]):
                                    list[x][y][z][w] = noise.perlin4D(rNoise, octave[2], x, y, z, w) + list[x][y][z][w]
                if octave[3] == 'sub':
                    for x in range(size[0]):
                        for y in range(size[1]):
                            for z in range(size[2]):
                                for w in range(size[3]):
                                    list[x][y][z][w] = noise.perlin4D(rNoise, octave[2], x, y, z, w) - list[x][y][z][w]
                if octave[3] == 'mix':
                    for x in range(size[0]):
                        for y in range(size[1]):
                            for z in range(size[2]):
                                for w in range(size[3]):
                                    list[x][y][z][w] = math.mix(noise.perlin4D(rNoise, octave[2], x, y, z, w), list[x][y][z][w], octave[4])
            return list
        elif type == 'ridge':
            list = array(size, 'constant', 0)
            for octave in number:  # [[min, max, h, octave alteration method, (if using mix) mix amount (0 - 1)], nextOctaveSameAsLast]
                rNoise = array(size, 'random float', [octave[0], octave[1]])
                if octave[3] == 'add':
                    for x in range(size[0]):
                        for y in range(size[1]):
                            for z in range(size[2]):
                                for w in range(size[3]):
                                    list[x][y][z][w] = noise.ridge4D(rNoise, octave[2], x, y, z, w) + list[x][y][z][w]
                if octave[3] == 'sub':
                    for x in range(size[0]):
                        for y in range(size[1]):
                            for z in range(size[2]):
                                for w in range(size[3]):
                                    list[x][y][z][w] = noise.ridge4D(rNoise, octave[2], x, y, z, w) - list[x][y][z][w]
                if octave[3] == 'mix':
                    for x in range(size[0]):
                        for y in range(size[1]):
                            for z in range(size[2]):
                                for w in range(size[3]):
                                    list[x][y][z][w] = math.mix(noise.ridge4D(rNoise, octave[2], x, y, z, w), list[x][y][z][w], octave[4])
            return list
        else:
            raise TypeError("Invalid Fill Type. Please use \"constant\", \"random int\", \"random float\", \"perlin\" or \"ridge\"")


class png:  # a tool to create and read png images
    def fromArray(list, name):  # converts a 2d array of colors into a png image
        img_w, img_h = [len(list), len(list[0])]
        data = np.zeros((img_h, img_w, 3), dtype=np.uint8)
        data[100, 100] = [255, 0, 0]  # dont know if this line is needed
        
        try:
            list[0][0].rgb
            for x in range(img_w):
                for y in range(img_h):
                    data[y][x] = list[x][y].rgb
        except AttributeError:
            for x in range(img_w):
                for y in range(img_h):
                    data[y][x] = list[x][y]
        
        img = im.fromarray(data, 'RGB')
        img.save(name)
        
        return img
    def getArray(imageFile):  # creates a 2d array of the pixel colors of a png
        surf = pygame.Surface(Vec2(5000, 3000))
        image = surf.blit(pygame.image.load(imageFile), Vec2(0, 0))
        size = Vec2(image.size[0], image.size[1])
        newList = array(size, 'constant', None)
        for x in range(size.x):
            for y in range(size.y):
                newList[x][y] = surf.get_at((x, y))
                newList[x][y] = Vec4(newList[x][y][0], newList[x][y][1], newList[x][y][2], newList[x][y][3])
        return newList


def vector(list):  # converts a list/tuple into a vectors
    if len(list) == 2:
        return Vec2(vector[0], vector[1])
    elif len(list) == 3:
        return Vec3(vector[0], vector[1], vector[2])
    elif len(list) == 4:
        return Vec4(vector[0], vector[1], vector[2], vector[3])
    else:
        raise TypeError("List Is To Long")


def copy(vector):  # copys a vector (returns a new vector with the same data as the old/current vector)
    if len(vector) == 2:
        return Vec2(vector.x, vector.y)
    elif len(vector) == 3:
        return Vec3(vector.x, vector.y, vector.z)
    elif len(vector) == 4:
        return Vec4(vector.x, vector.y, vector.z, vector.w)


class txt:  # a text file ateration tool
    def read(file):  # returns a list of each line in a file
        return open(file).read().split('\n')
    def delete(file, line):  # deltes a line for a file
        text = open(file).read().split('\n')
        del text[line]
        newData = ''
        text2 = []

        for t in text:
            text2.append([t, '\n'])
        
        for i in range(len(text2) - 1):
            newData += text2[i][0] + text2[i][1]
        newData += text2[len(text2) - 1][0]

        with open(file, 'w') as out:
            out.write(newData)
    def write(file, line, Text):  # writes a new line onto a file
        text = open(file).read().split('\n')
        text.insert(line, Text)
        text2 = []
        newData = ''
        
        for t in text:
            text2.append([t, '\n'])
        
        for i in range(len(text2) - 1):
            newData += text2[i][0] + text2[i][1]
        newData += text2[len(text2) - 1][0]

        with open(file, 'w') as out:
            out.write(newData)

