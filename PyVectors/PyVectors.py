import numpy as np  # importing numpy to allow creation of png's unsing PIL (png.fromArray)
from PIL import Image as im  # importing PIL to create png's (png.fromArray)
import math as Math  # importing the math library to add cos, sin, sqrt, ect... (math.mathType)
import random, pygame  # importing random for perlin noise (noise.perlin or noise.ridge) and more and importing pygame to get the colors of a png (png.getArray)


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
        except AttributeError:  # filling it in with the other vectors components (when the input contains a vector)
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
        return Vec4(math.divideT(self.x, other.x), math.divideT(self.y, other.y), math.divideT(self.z, other.z), math.divideT(self.w, other.w))
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
        return Vec4(math.divideT(self.x, other.x), math.divideT(self.y, other.y), math.divideT(self.z, other.z), math.divideT(self.w, other.w))
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
        return math.length(self.xyzw)
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
    def ceil(self):
        return Vec4(math.ceil(self.x), math.ceil(self.y), math.ceil(self.z), math.ceil(self.w))


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
        return Vec3(math.divideT(self.x, other.x), math.divideT(self.y, other.y), math.divideT(self.z, other.z))
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
        return Vec3(math.divideT(self.x, other.x), math.divideT(self.y, other.y), math.divideT(self.z, other.z))
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
        return math.length(self.xyz)
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
    def ceil(self):
        return Vec3(math.ceil(self.x), math.ceil(self.y), math.ceil(self.z))


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
        return Vec2(math.divideT(self.x, other.x), math.divideT(self.y, other.y))
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
        return Vec2(math.divideT(self.x, other.x), math.divideT(self.y, other.y))
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
        return math.length(self.xy)
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
    def ceil(self):  # gets the ceiling of a vector
        return Vec2(math.ceil(self.x), math.ceil(self.y))


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
        return Vec4(math.divideT(self.x, other.x), math.divideT(self.y, other.y), math.divideT(self.z, other.z), math.divideT(self.w, other.w))
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
        return Vec4(math.divideT(self.x, other.x), math.divideT(self.y, other.y), math.divideT(self.z, other.z), math.divideT(self.w, other.w))
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
        return math.length(self.xyzw)
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
    def ceil(self):
        return Vec4(math.ceil(self.x), math.ceil(self.y), math.ceil(self.z), math.ceil(self.w))


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
        return Vec3(math.divideT(self.x, other.x), math.divideT(self.y, other.y), math.divideT(self.z, other.z))
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
        return Vec3(math.divideT(self.x, other.x), math.divideT(self.y, other.y), math.divideT(self.z, other.z))
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
        return math.length(self.xyz)
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
    def ceil(self):
        return Vec3(math.ceil(self.x), math.ceil(self.y), math.ceil(self.z))


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
        return Vec2(math.divideT(self.x, other.x), math.divideT(self.y, other.y))
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
        return Vec2(math.divideT(self.x, other.x), math.divideT(self.y, other.y))
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
        return math.length(self.xy)
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
    def ceil(self):
        return Vec2(math.ceil(self.x), math.ceil(self.y))


def ceil(vector):  # gets the ceiling of a vector
    return vector.ceil()


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


def cross(vector1, vector2):  # gets the cross product of two vectors (only works a vec3 types)
    return vector1.cross(vector2)


def normalize(Vector):  # normalizes a vector
    mag = length(Vector)
    return Vector / Vec4(mag, mag, mag, mag)


def length(Vector):  # gets the length of a Vector (using the pythagorean theorem  a^2 + b^2 = c^2)
    return Vector.length()


class lists:  # a class do do math operations across an entire list at the same time
    def copy1D(list2: list) -> list:  # copys a list
        size = len(list2)
        list1 = array([size], 'constant', None)
        for x in range(len(list1)):
            list1[x] = list2[x]
        return list1
    def copy2D(list2: list) -> list:  # copys a list
        size = Vec2(len(list2), len(list2[0]))
        list1 = array(size, 'constant', None)
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] = list2[x][y]
        return list1
    def copy3D(list2: list) -> list:  # copys a list
        size = Vec3(len(list2), len(list2[0]), len(list2[0][0]))
        list1 = array(size, 'constant', None)
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] = list2[x][y][z]
        return list1
    def copy4D(list2: list) -> list:  # copys a list
        size = Vec4(len(list2), len(list2[0]), len(list2[0][0]), len(list2[0][0][0]))
        list1 = array(size, 'constant', None)
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] = list2[x][y][z][w]
        return list1
    def clamp1D(list1: list, nMin: float, nMax: float) -> list:  # clamps a list
        for x in range(len(list1)):
            list1[x] = math.clamp(list1[x], nMin, nMax)
        return list1
    def clamp2D(list1: list, nMin: float, nMax: float) -> list:  # clamps a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] = math.clamp(list1[x][y], nMin, nMax)
        return list1
    def clamp3D(list1: list, nMin: float, nMax: float) -> list:  # clamps a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] = math.clamp(list1[x][y][z], nMin, nMax)
        return list1
    def clamp4D(list1: list, nMin: float, nMax: float) -> list:  # clamps a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] = math.clamp(list1[x][y][z][w], nMin, nMax)
        return list1
    def min1D(list1: list, nMin: float) -> list:  # sets the min of a list
        for x in range(len(list1)):
            list1[x] = min(list1[x], nMin)
        return list1
    def min2D(list1: list, nMin: float) -> list:  # sets the min of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] = min(list1[x][y], nMin)
        return list1
    def min3D(list1: list, nMin: float) -> list:  # sets the min of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] = min(list1[x][y][z], nMin)
        return list1
    def min4D(list1: list, nMin: float) -> list:  # sets the min of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] = min(list1[x][y][z][w], nMin)
        return list1
    def max1D(list1: list, nMax: float) -> list:  # sets the max of a list
        for x in range(len(list1)):
            list1[x] = max(list1[x], nMax)
        return list1
    def max2D(list1: list, nMax: float) -> list:  # sets the max of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] = max(list1[x][y], nMax)
        return list1
    def max3D(list1: list, nMax: float) -> list:  # sets the max of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] = max(list1[x][y][z], nMax)
        return list1
    def max4D(list1: list, nMax: float) -> list:  # sets the max of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] = max(list1[x][y][z][w], nMax)
        return list1
    def mix1D(list1: list, list2: list, list3: list) -> list:  # mixes 3 lists together
        for x in range(len(list1)):
            list1[x] = math.mix(list1[x], list2[x], list3[x])
        return list1
    def mix2D(list1: list, list2: list, list3: list) -> list:  # mixes 3 lists together
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] = math.mix(list1[x][y], list2[x][y], list3[x][y])
        return list1
    def mix3D(list1: list, list2: list, list3: list) -> list:  # mixes 3 lists together
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] = math.mix(list1[x][y][z], list2[x][y][z], list3[x][y][z])
        return list1
    def mix4D(list1: list, list2: list, list3: list) -> list:  # mixes 3 lists together
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] = math.mix(list1[x][y][z][w], list2[x][y][z][w], list3[x][y][z][w])
        return list1
    def floor_div1D(list1: list, list2: list) -> list:  # floor divides two lists
        for x in range(len(list1)):
            list1[x] = list1[x] // list2[x]
        return list1
    def floor_div2D(list1: list, list2: list) -> list:  # floor divides two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] = list1[x][y] // list2[x][y]
        return list1
    def floor_div3D(list1: list, list2: list) -> list:  # floor divides two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] = list1[x][y][z] // list2[x][y][z]
        return list1
    def floor_div4D(list1: list, list2: list) -> list:  # floor divides two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] = list1[x][y][z][w] // list2[x][y][z][w]
        return list1
    def mod1D(list1: list, list2: list) -> list:  # mods two lists
        for x in range(len(list1)):
            list1[x] = list1[x] % list2[x]
        return list1
    def mod2D(list1: list, list2: list) -> list:  # mods two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] = list1[x][y] % list2[x][y]
        return list1
    def mod3D(list1: list, list2: list) -> list:  # mods two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] = list1[x][y][z] % list2[x][y][z]
        return list1
    def mod4D(list1: list, list2: list) -> list:  # mods two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] = list1[x][y][z][w] % list2[x][y][z][w]
        return list1
    def pow1D(list1: list, list2: list) -> list:  # gets the power of two lists
        for x in range(len(list1)):
            list1[x] = list1[x] ** list2[x]
        return list1
    def pow2D(list1: list, list2: list) -> list:  # gets the power of two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] = list1[x][y] ** list2[x][y]
        return list1
    def pow3D(list1: list, list2: list) -> list:  # gets the power of two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] = list1[x][y][z] ** list2[x][y][z]
        return list1
    def pow4D(list1: list, list2: list) -> list:  # gets the power of two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] = list1[x][y][z][w] ** list2[x][y][z][w]
        return list1
    def round1D(list1: list) -> list:  # rounds a list
        for x in range(len(list1)):
            list1[x] = round(list1[x])
        return list1
    def round2D(list1: list) -> list:  # rounds a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] = round(list1[x][y])
        return list1
    def round3D(list1: list) -> list:  # rounds a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] = round(list1[x][y][z])
        return list1
    def round4D(list1: list) -> list:  # rounds a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] = round(list1[x][y][z][w])
        return list1
    def str1D(list1: list) -> list:  # casts a list to a string type
        for x in range(len(list1)):
            list1[x] = str(list1[x])
        return list1
    def str2D(list1: list) -> list:  # casts a list to a string type
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] = str(list1[x][y])
        return list1
    def str3D(list1: list) -> list:  # casts a list to a string type
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] = str(list1[x][y][z])
        return list1
    def str4D(list1: list) -> list:  # casts a list to a string type
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] = str(list1[x][y][z][w])
        return list1
    def int1D(list1: list) -> list:  # casts a list to a int type
        for x in range(len(list1)):
            list1[x] = int(list1[x])
        return list1
    def int2D(list1: list) -> list:  # casts a list to a int type
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] = int(list1[x][y])
        return list1
    def int3D(list1: list) -> list:  # casts a list to a int type
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] = int(list1[x][y][z])
        return list1
    def int4D(list1: list) -> list:  # casts a list to a int type
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] = int(list1[x][y][z][w])
        return list1
    def fract1D(list1: list) -> list:  # gets the fract of a list
        for x in range(len(list1)):
            list1[x] = math.fract(list1[x])
        return list1
    def fract2D(list1: list) -> list:  # gets the fract of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] = math.floor(fract[x][y])
        return list1
    def fract3D(list1: list) -> list:  # gets the fract of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] = math.fract(list1[x][y][z])
        return list1
    def fract4D(list1: list) -> list:  # gets the fract of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] = math.fract(list1[x][y][z][w])
        return list1
    def ceil1D(list1: list) -> list:  # gets the ceil of a list
        for x in range(len(list1)):
            list1[x] = math.ceil(list1[x])
        return list1
    def ceil2D(list1: list) -> list:  # gets the ceil of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] = math.ceil(list1[x][y])
        return list1
    def ceil3D(list1: list) -> list:  # gets the ceil of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] = math.ceil(list1[x][y][z])
        return list1
    def ceil4D(list1: list) -> list:  # gets the ceil of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] = math.ceil(list1[x][y][z][w])
        return list1
    def floor1D(list1: list) -> list:  # gets the floor of a list
        for x in range(len(list1)):
            list1[x] = math.floor(list1[x])
        return list1
    def floor2D(list1: list) -> list:  # gets the floor of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] = math.floor(list1[x][y])
        return list1
    def floor3D(list1: list) -> list:  # gets the floor of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] = math.floor(list1[x][y][z])
        return list1
    def floor4D(list1: list) -> list:  # gets the floor of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] = math.floor(list1[x][y][z][w])
        return list1
    def abs1D(list1: list) -> list:  # gets the absulute value of a list
        for x in range(len(list1)):
            list1[x] = abs(list1[x])
        return list1
    def abs2D(list1: list) -> list:  # gets the absulute value of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] = abs(list1[x][y])
        return list1
    def abs3D(list1: list) -> list:  # gets the absulute value of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] = abs(list1[x][y][z])
        return list1
    def abs4D(list1: list) -> list:  # gets the absulute value of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] = abs(list1[x][y][z][w])
        return list1
    def mult1D(list1: list, list2: list) -> list:  # multiplies two list
        for x in range(len(list1)):
            list1[x] *= list2[x]
        return list1
    def mult2D(list1: list, list2: list) -> list:  # multiplies two list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] *= list2[x][y]
        return list1
    def mult3D(list1: list, list2: list) -> list:  # multiplies two list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] *= list2[x][y][z]
        return list1
    def mult4D(list1: list, list2: list) -> list:  # multiplies two list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] *= list2[x][y][z][w]
        return list1
    def div1D(list1: list, list2: list) -> list:  # divides two lists
        for x in range(len(list1)):
            list1[x] /= list2[x]
        return list1
    def div2D(list1: list, list2: list) -> list:  # divides two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] /= list2[x][y]
        return list1
    def div3D(list1: list, list2: list) -> list:  # divides two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] /= list2[x][y][z]
        return list1
    def div4D(list1: list, list2: list) -> list:  # divides two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] /= list2[x][y][z][w]
        return list1
    def sub1D(list1: list, list2: list) -> list:  # subtracts two lists
        for x in range(len(list1)):
            list1[x] -= list2[x]
        return list1
    def sub2D(list1: list, list2: list) -> list:  # subtracts two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] -= list2[x][y]
        return list1
    def sub3D(list1: list, list2: list) -> list:  # subtracts two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] -= list2[x][y][z]
        return list1
    def sub4D(list1: list, list2: list) -> list:  # subtracts two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] -= list2[x][y][z][w]
        return list1
    def add1D(list1: list, list2: list) -> list:  # adds two lists
        for x in range(len(list1)):
            list1[x] += list2[x]
        return list1
    def add2D(list1: list, list2: list) -> list:  # adds two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] += list2[x][y]
        return list1
    def add3D(list1: list, list2: list) -> list:  # adds two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] += list2[x][y][z]
        return list1
    def add4D(list1: list, list2: list) -> list:  # adds two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] += list2[x][y][z][w]
        return list1


class math:  # math operations for non vectors (includes some functions from the math library but also new ones like fract, mix, map 1D-4D, ect...)
    def worly(grid: list, scale, x, y) -> float:
        scale = Vec2(scale, scale)
        cellPos = (x / scale.x, y / scale.y)
        currentCell = (math.floor(cellPos[0]), math.floor(cellPos[1]))
        cells = Vec2(len(grid), len(grid[0]))
        dists = []
        for X in range(-1, 2):
            for Y in range(-1, 2):
                NX = X + currentCell[0]
                NY = Y + currentCell[1]
                if NX >= 0 and NX < cells.x + 1 and NY >= 0 and NY < cells.y + 1:
                    PointPos = grid[NX][NY]
                    nx = (X * scale.x) + PointPos[0] + currentCell[0] * scale.x
                    ny = (Y * scale.y) + PointPos[1] + currentCell[1] * scale.y
                    distX = (nx - x) ** 2
                    distY = (ny - y) ** 2
                    dists.append(distX + distY)
        return math.sqrt(min(dists))
    def crystal(grid: list, scale, x, y) -> float:
        scale = Vec2(scale, scale)
        cellPos = (x / scale.x, y / scale.y)
        currentCell = (math.floor(cellPos[0]), math.floor(cellPos[1]))
        cells = Vec2(len(grid), len(grid[0]))
        dists = []
        for X in range(-1, 2):
            for Y in range(-1, 2):
                NX = X + currentCell[0]
                NY = Y + currentCell[1]
                if NX >= 0 and NX < cells.x + 1 and NY >= 0 and NY < cells.y + 1:
                    PointPos = grid[NX][NY]
                    nx = (X * scale.x) + PointPos[0] + currentCell[0] * scale.x
                    ny = (Y * scale.y) + PointPos[1] + currentCell[1] * scale.y
                    distX = (nx - x) ** 2
                    distY = (ny - y) ** 2
                    dists.append(distX + distY)
        del dists[dists.index(min(dists))]
        return math.sqrt(min(dists))
    def divideT(value1, value2) -> float:  # divides and avoids divition by zero errors (when dividing by zero, returns numbers near infity)
        small_num = 0.00000000000000001
        return (value1 + small_num) / (value2 + small_num)
    def divide0(value1, value2) -> float:  # divides two numbers but on divtion by zero returns 0 (the divide0 function will return numbers near to infinity this one wont)
        try:
            return value1 / value2
        except ZeroDivisionError:
            return 0.0
    def ceil(value) -> int:  # returns the ceiling of a number
        return Math.ceil(value)
    def mix(value1, value2, percentage: float) -> float:  # mixes two numbers based on a number ranging from 1 - 0
        percentage = math.clamp(percentage, 0, 1)
        return value1 * (1 - percentage) + value2 * percentage
    def tan(value) -> float:  # returns the tangent of a number
        return Math.tan(value)
    def sin(value) -> float:  # returns the sign of a number
        return Math.sin(value)
    def cos(value) -> float:  # returns the cosine of a number
        return Math.cos(value)
    def fract(value) -> float:  # returns the decimal of the value
        return value - math.floor(value)
    def floor(value) -> int:  # returns the floor of the value
        return Math.floor(value)
    def clamp(val, min_, max_):  # sets the max and min of a number
        return min(max(val, min_), max_)
    def sqrt(value) -> float:  # square root
        return Math.sqrt(value)
    def map1D(list: list, fromMin, fromMax, toMin = None, toMax = None) -> float:  # changes the range of a 1d array of data (while keeping the detail of the numbers)
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
        
        scaler = math.divide0((toMax - toMin), max(list))
        for x in range(len(list)):
            list[x] *= scaler
            list[x] += toMin
        
        return list
    def map2D(list: list, fromMin, fromMax, toMin = None, toMax = None) -> float:  # changes the range of a 2d array of data (while keeping the detail of the numbers)
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
        scaler = math.divide0((toMax - toMin), maxOfList)
        for x in range(len(list)):
            for y in range(len(list[x])):
                list[x][y] *= scaler
                list[x][y] += toMin
        
        return list
    def map3D(list: list, fromMin, fromMax, toMin = None, toMax = None) -> float:  # changes the range of a 3d array of data (while keeping the detail of the numbers)
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
        
        scaler = scaler = math.divide0((toMax - toMin), maxOfList)
        for x in range(len(list)):
            for y in range(len(list[x])):
                for z in range(len(list[x][y])):
                    list[x][y][z] *= scaler
                    list[x][y][z] += toMin
        
        return list
    def map4D(list: list, fromMin, fromMax, toMin = None, toMax = None) -> float:  # changes the range of a 4d array of data (while keeping the detail of the numbers)
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
        
        scaler = math.divide0((toMax - toMin), maxOfList)
        for x in range(len(list)):
            for y in range(len(list[x])):
                for z in range(len(list[x][y])):
                    for w in range(len(list[x][y][z])):
                        list[x][y][z][w] *= scaler
                        list[x][y][z][w] += toMin
        
        return list
    def map(val, cMin, cMax, nMin, nMax) -> float:
        nVal = val - cMin
        nVal *= math.divide0((nMax - nMin), (cMax - cMin))
        nVal += nMin
        return nVal
    def smooth1D(heights: list, smoothing = 100) -> list:  # smooths a list of numbers making them more uniform/reducing spikes in numbers
        for s in range(smoothing):
            for i in range(len(heights)):
                if i not in [0, len(heights) - 1]:
                    height1 = heights[i - 1]
                    height3 = heights[i + 1]
                    heights[i] = (heights[i] * 0.1) + (height1 * 0.45) + (height3 * 0.45)
        return heights
    def interpalate2(h, x, points: list):  # interpolates linearly between 2 points (use the math.smooth function for further smoothing)
        return ((points[1].y - points[0].y) / h) * x
    def interpalate3(h, x, list: list):  # interpolates smoothly between 3 points (use the math.smooth function to fixs small glitches)
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
    def interpalate5(h, x, list: list):  # interpolates smoothly between 5 points (use the math.smooth function to fix glitches)
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
    def smoothstep(x: float) -> float:  # a function to smoothly step between 0 and 1
        k = math.clamp(x, 0, 1)
        return k ** 2 * (3 - 2 * k)
    def length(poses: list) -> float:  # gets the distance of the imputed values (using the pythagorean theorem)
        squared = 0
        for point in poses:
            squared += point * point
        return math.sqrt(squared)
    def normalize(values: list) -> list:  # normalizes a list of values (for this function you need to put in the .xyz value of the Vector, the functions above do this for you)
        mag = math.length(values)  # gets the magnitude
        new_values = []
        for old_value in values:
            new_values.append(math.divideT(old_value, mag))  # changes the values by the magnitude
        return new_values
    def spline1D(noise: list, x, h) -> float:  # smoothly interpolates at a point between other points on a 1D list
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
    def spline2D(noise: list, x, y, h) -> float:  # smoothly interpolates at a point between other points on a 2D list
        nx = x / h
        i = math.floor(nx)
        ty1 = math.spline1D(noise[i - 1], y, h)
        ty2 = math.spline1D(noise[i    ], y, h)
        ty3 = math.spline1D(noise[i + 1], y, h)
        ty4 = math.spline1D(noise[i + 2], y, h)
        return math.spline1D([ty1, ty2, ty3, ty4], (nx - i) * h + h, h)
    def spline3D(noise: list, x, y, z, h) -> float:  # smoothly interpolates at a point between other points on a 3D list
        nx = x / h
        i = math.floor(nx)
        ty1 = math.spline2D(noise[i - 1], y, z, h)
        ty2 = math.spline2D(noise[i    ], y, z, h)
        ty3 = math.spline2D(noise[i + 1], y, z, h)
        ty4 = math.spline2D(noise[i + 2], y, z, h)
        return math.spline1D([ty1, ty2, ty3, ty4], (nx - i) * h + h, h)
    def spline4D(noise: list, x, y, z, w, h) -> float:  # this is untested but should work and smoothly interpolates at a point between other points on a 4D list
        nx = x / h
        i = math.floor(nx)
        ty1 = math.spline3D(noise[i - 1], y, z, w, h)
        ty2 = math.spline3D(noise[i    ], y, z, w, h)
        ty3 = math.spline3D(noise[i + 1], y, z, w, h)
        ty4 = math.spline3D(noise[i + 2], y, z, w, h)
        return math.spline1D([ty1, ty2, ty3, ty4], (nx - i) * h + h, h)
    def min1D(list: list):  # gets the min of a list thats dimetion is stated
        return min(list)
    def min2D(list: list):  # gets the min of a 2d array
        layers = []
        for x in list:
            layers.append(min(x))
        return min(layers)
    def min3D(list: list):  # gets the min of a 3d array
        layers = []
        for x in list:
            newLayer = []
            for y in x:
                newLayer.append(min(y))
            layers.append(min(newLayer))
        return min(layers)
    def min4D(list: list):  # gets the min of a 4d array
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
    def max1D(list: list):  # gets the max of a list thats dimetion is stated
        return max(list)
    def max2D(list: list):  # gets the max of a 2d array
        layers = []
        for x in list:
            layers.append(max(x))
        return max(layers)
    def max3D(list: list):  # gets the max of a 3d array
        layers = []
        for x in list:
            newLayer = []
            for y in x:
                newLayer.append(max(y))
            layers.append(max(newLayer))
        return max(layers)
    def max4D(list: list):  # gets the max of a 4d array
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
    def RGBtoKCMY(color: vec3) -> vec4:  # converts rgb to kcmy(paint color format)
        # Conversoin formula from: https://www.rapidtables.com/convert/color/rgb-to-cmyk.html
        G = math.divide0(color.g, 255)
        B = math.divide0(color.b, 255)
        R = math.divide0(color.r, 255)
        
        k = 1 - max([R, G, B])
        c = math.divide0((1 - R - k), (1 - k))
        m = math.divide0((1 - G - k), (1 - k))
        y = math.divide0((1 - B - k), (1 - k))
        
        return Vec4(k, c, m, y)


class dists:  # multipl distance functions for different shapes
    def distToCircularPoint(pos, center, r):  # gets the distance to a sphere/circle/hypershpere from a point (negitive when in the circle)
        return length(pos - center) - r
    def distToPoint(pos, point_pos):  # gets the distance to a point from a point
        return length(pos - point_pos)


class numberGradient:  # a gradient for numbers
    def __init__(self, maxGap = 50):
        self.points = {}
        self.maxGap = maxGap
    def add(self, point, number):  # adds a point to the gradient
        self.points[str(point)] = number
    def grade(self, point):  # gets the number at point on the gradient
        point = int(point)
        p = point
        color1 = None
        for x in range(self.maxGap):
            try:
                color1 = self.points[str(p)]
                break
            except KeyError:
                p -= 1
        
        if abs(point - p) == self.maxGap - 1 or color1 == None:
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
        
        pointInSpace = math.smoothstep(math.divide0((point - p), distBetweenPoints))

        return math.mix(color1, color2, pointInSpace)  # try using a smoothstep funciton to create a smoother change in gradient
    def gradeL(self, point):  # gets the number at point on the gradient
        point = int(point)
        p = point
        color1 = None
        for x in range(self.maxGap):
            try:
                color1 = self.points[str(p)]
                break
            except KeyError:
                p -= 1
        
        if abs(point - p) == self.maxGap - 1 or color1 == None:
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
        
        pointInSpace = (math.divide0((point - p), distBetweenPoints))

        return math.mix(color1, color2, pointInSpace)  # try using a smoothstep funciton to create a smoother change in gradient


class colorGradient:  # you can add points (only works in 1D) and then sample at points to craete a smooth color transition with multiple colors each with different distances apart
    def __init__(self, maxGap = 50):  # make it so if color1 dosent hit anything it raises and invalid position
        self.points = {}
        self.maxGap = maxGap
    def add(self, point, color):  # adds a point to the gradient
        self.points[str(point)] = color
    def grade(self, point):  # gets the color/vector a point in space
        point = int(point)
        p = point
        color1 = Vec4(None, None, None, None)
        for x in range(self.maxGap):
            try:
                color1 = self.points[str(p)]
                break
            except KeyError:
                p -= 1
        
        if abs(point - p) == self.maxGap - 1 or color1 == Vec4(None, None, None, None):
            raise SyntaxError("Invalid Postion")
        
        distBetweenPoints = abs(point - p)
        
        color2 = Vec4(None, None, None, None)
        p2 = point
        for x in range(self.maxGap):
            try:
                color2 = self.points[str(p2)]
                break
            except KeyError:
                p2 += 1
        
        if color2 == Vec4(None, None, None, None):
            raise SyntaxError("Invalid Postion")
        
        distBetweenPoints += abs(point - p2)
        
        pointInSpace = math.smoothstep(math.divide0((point - p), distBetweenPoints))

        return mix(color1, color2, pointInSpace)
    def gradeL(self, point):  # gets the color/vector a point in space
        point = int(point)
        p = point
        color1 = Vec4(None, None, None, None)
        for x in range(self.maxGap):
            try:
                color1 = self.points[str(p)]
                break
            except KeyError:
                p -= 1
        
        if abs(point - p) == self.maxGap - 1 or color1 == Vec4(None, None, None, None):
            raise SyntaxError("Invalid Postion")
        
        distBetweenPoints = abs(point - p)
        
        color2 = Vec4(None, None, None, None)
        p2 = point
        for x in range(self.maxGap):
            try:
                color2 = self.points[str(p2)]
                break
            except KeyError:
                p2 += 1
        
        if color2 == Vec4(None, None, None, None):
            raise SyntaxError("Invalid Postion")
        
        distBetweenPoints += abs(point - p2)
        
        pointInSpace = (math.divide0((point - p), distBetweenPoints))

        return mix(color1, color2, pointInSpace)


class gradient:  # a way to make gradients that specifies what they are being used for
    def color(maxGap = 50) -> colorGradient:  # gives you a color gradient
        return colorGradient(maxGap)
    def number(maxGap = 50) -> numberGradient:  # gives you a number gradient
        return numberGradient(maxGap)
    def vector(maxGap = 50) -> colorGradient:  # gives you a vector gradient
        return colorGradient(maxGap)


class noise:  # contains perlin noise functions that take in a list of random numbers thats the same dimention as the function, than the x, y, z, and w (only put the one that belong there for the demention of the function) and finaly the distance between points
    def perlin1D(randNoise: list, h, x) -> float:  # perlin noise at the dimention stated
        return math.spline1D(randNoise, x, h)
    def perlin2D(randNoise: list, h, x, y) -> float:
        return math.spline2D(randNoise, x, y, h)
    def perlin3D(randNoise: list, h, x, y, z) -> float:
        return math.spline3D(randNoise, x, y, z, h)
    def perlin4D(randNoise: list, h, x, y, z, w) -> float:
        return math.spline4D(randNoise, x, y, z, w, h)
    def ridge1D(randNoise: list, h, x) -> float:  # ridge noise aka perlin noise with abrupt ridges (like that of mountains)
        noise = math.spline1D(randNoise, x, h)
        noise = -1 * abs(noise)
        return noise
    def ridge2D(randNoise: list, h, x, y) -> float:
        noise = math.spline2D(randNoise, x, y, h)
        noise = -1 * abs(noise)
        return noise
    def ridge3D(randNoise: list, h, x, y, z) -> float:
        noise = math.spline3D(randNoise, x, y, z, h)
        noise = -1 * abs(noise)
        return noise
    def ridge4D(randNoise: list, h, x, y, z, w) -> float:
        noise = math.spline4D(randNoise, x, y, z, w, h)
        noise = -1 * abs(noise)
        return noise
    def crystal2D(size: Vec2, scale: float, minHeight: float = -1, maxHeight: float = 1) -> list:  # a crystaly noise pattern (generates hole list)
        scale = Vec2(scale, scale)
        cells = ceil(size / scale)
        grid = []
        for x in range(cells.x + 2):
            layer = []
            for y in range(cells.y + 2):
                layer.append((random.uniform(0, scale.x), random.uniform(0, scale.y)))
            grid.append(layer)
        worlyNoise = []
        for x in range(size.x):
            layer = []
            for y in range(size.y):
                cellPos = (x / scale.x, y / scale.y)
                currentCell = (math.floor(cellPos[0]), math.floor(cellPos[1]))
                dists = []
                for X in range(-1, 2):
                    for Y in range(-1, 2):
                        NX = X + currentCell[0]
                        NY = Y + currentCell[1]
                        if NX >= 0 and NX < cells.x + 1 and NY >= 0 and NY < cells.y + 1:
                            PointPos = grid[NX + 1][NY + 1]
                            nx = (X * scale.x) + PointPos[0] + currentCell[0] * scale.x
                            ny = (Y * scale.y) + PointPos[1] + currentCell[1] * scale.y
                            distX = (nx - x) ** 2
                            distY = (ny - y) ** 2
                            dists.append(distX + distY)
                del dists[dists.index(min(dists))]
                layer.append(math.sqrt(min(dists)))
            worlyNoise.append(layer)
        worlyNoise = math.map2D(worlyNoise, minHeight, maxHeight)
        return worlyNoise
    def worly2D(size: Vec2, scale: float, minHeight: float = -1, maxHeight: float = 1) -> list:  # a worly noise pattern (generates hole list)
        scale = Vec2(scale, scale)
        cells = ceil(size / scale)
        grid = []
        for x in range(cells.x + 2):
            layer = []
            for y in range(cells.y + 2):
                layer.append((random.uniform(0, scale.x), random.uniform(0, scale.y)))
            grid.append(layer)
        worlyNoise = []
        for x in range(size.x):
            layer = []
            for y in range(size.y):
                cellPos = (x / scale.x, y / scale.y)
                currentCell = (math.floor(cellPos[0]), math.floor(cellPos[1]))
                dists = []
                for X in range(-1, 2):
                    for Y in range(-1, 2):
                        NX = X + currentCell[0]
                        NY = Y + currentCell[1]
                        if NX >= 0 and NX < cells.x + 1 and NY >= 0 and NY < cells.y + 1:
                            PointPos = grid[NX + 1][NY + 1]
                            nx = (X * scale.x) + PointPos[0] + currentCell[0] * scale.x
                            ny = (Y * scale.y) + PointPos[1] + currentCell[1] * scale.y
                            distX = (nx - x) ** 2
                            distY = (ny - y) ** 2
                            dists.append(distX + distY)
                layer.append(math.sqrt(min(dists)))
            worlyNoise.append(layer)
        worlyNoise = math.map2D(worlyNoise, minHeight, maxHeight)
        return worlyNoise
    def crystal3D(size: Vec3, scale: float, minHeight: float = -1, maxHeight: float = 1) -> list:
        scale = Vec3(scale, scale, scale)
        cells = ceil(size / scale)
        grid = []
        for x in range(cells.x + 2):
            layer = []
            for y in range(cells.y + 2):
                layer2 = []
                for z in range(cells.z + 2):
                    layer2.append((random.uniform(0, scale.x), random.uniform(0, scale.y), random.uniform(0, scale.z)))
                layer.append(layer2)
            grid.append(layer)
        worlyNoise = []
        for x in range(size.x):
            layer = []
            for y in range(size.y):
                layer2 = []
                for z in range(size.z):
                    cellPos = (x / scale.x, y / scale.y, z / scale.z)
                    currentCell = (math.floor(cellPos[0]), math.floor(cellPos[1]), math.floor(cellPos[2]))
                    dists = []
                    for X in range(-1, 2):
                        for Y in range(-1, 2):
                            for Z in range(-1, 2):
                                NX = X + currentCell[0]
                                NY = Y + currentCell[1]
                                NZ = Z + currentCell[2]
                                PointPos = grid[NX + 1][NY + 1][NZ + 1]
                                nx = (X * scale.x) + PointPos[0] + currentCell[0] * scale.x
                                ny = (Y * scale.y) + PointPos[1] + currentCell[1] * scale.y
                                nz = (Z * scale.x) + PointPos[2] + currentCell[2] * scale.z
                                distX = (nx - x) ** 2
                                distY = (ny - y) ** 2
                                distZ = (nz - z) ** 2
                                dists.append(distX + distY + distZ)
                    del dists[dists.index(min(dists))]
                    layer2.append(math.sqrt(min(dists)))
                layer.append(layer2)
            worlyNoise.append(layer)
        worlyNoise = math.map3D(worlyNoise, minHeight, maxHeight)
        return worlyNoise
    def worly3D(size: Vec3, scale: float, minHeight: float = -1, maxHeight: float = 1) -> list:
        scale = Vec3(scale, scale, scale)
        cells = ceil(size / scale)
        grid = []
        for x in range(cells.x + 2):
            layer = []
            for y in range(cells.y + 2):
                layer2 = []
                for z in range(cells.z + 2):
                    layer2.append((random.uniform(0, scale.x), random.uniform(0, scale.y), random.uniform(0, scale.z)))
                layer.append(layer2)
            grid.append(layer)
        worlyNoise = []
        for x in range(size.x):
            layer = []
            for y in range(size.y):
                layer2 = []
                for z in range(size.z):
                    cellPos = (x / scale.x, y / scale.y, z / scale.z)
                    currentCell = (math.floor(cellPos[0]), math.floor(cellPos[1]), math.floor(cellPos[2]))
                    dists = []
                    for X in range(-1, 2):
                        for Y in range(-1, 2):
                            for Z in range(-1, 2):
                                NX = X + currentCell[0]
                                NY = Y + currentCell[1]
                                NZ = Z + currentCell[2]
                                PointPos = grid[NX + 1][NY + 1][NZ + 1]
                                nx = (X * scale.x) + PointPos[0] + currentCell[0] * scale.x
                                ny = (Y * scale.y) + PointPos[1] + currentCell[1] * scale.y
                                nz = (Z * scale.x) + PointPos[2] + currentCell[2] * scale.z
                                distX = (nx - x) ** 2
                                distY = (ny - y) ** 2
                                distZ = (nz - z) ** 2
                                dists.append(distX + distY + distZ)
                    layer2.append(math.sqrt(min(dists)))
                layer.append(layer2)
            worlyNoise.append(layer)
        worlyNoise = math.map3D(worlyNoise, minHeight, maxHeight)
        return worlyNoise


def array(size, type: str, number) -> list:  # atomticaly fills in and array with numbers, the types are as following with the next input in brackets: constant (number), random int ([min number, max number]), random float ([min number, max number]), perlin ([[min height, max height, distance between points, height alteration method, (this paramiter is only if using mix) percentage (0 - 1)], more octaves that are same as last])   the demention of the array is determind by the len of size which can be a list or vector type.
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
                rNoise = array([math.ceil(size[0] / octave[2]) + 2], 'random float', [octave[0], octave[1]])
                if octave[3] == 'add':
                    for x in range(size[0]):
                        list[x] = noise.perlin1D(rNoise, octave[2], x) + list[x]
                elif octave[3] == 'sub':
                    for x in range(size[0]):
                        list[x] = noise.perlin1D(rNoise, octave[2], x) - list[x]
                elif octave[3] == 'mix':
                    for x in range(size[0]):
                        list[x] = math.mix(noise.perlin1D(rNoise, octave[2], x), list[x], octave[4])
            return list
        elif type == 'ridge':
            list = array(size, 'constant', 0)
            for octave in number:  # [[min, max, h, octave alteration method, (if using mix) mix amount (0 - 1)], nextOctaveSameAsLast]
                rNoise = array([math.ceil(size[0] / octave[2]) + 2], 'random float', [octave[0], octave[1]])
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
            size = vectorize(size)
            list = array(size, 'constant', 0)
            for octave in number:  # [[min, max, h, octave alteration method, (if using mix) mix amount (0 - 1)], nextOctaveSameAsLast]
                rNoise = array(ceil(size / Vec2(octave[2], octave[2])) + Vec2(2, 2), 'random float', [octave[0], octave[1]])
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
            size = vectorize(size)
            list = array(size, 'constant', 0)
            for octave in number:  # [[min, max, h, octave alteration method, (if using mix) mix amount (0 - 1)], nextOctaveSameAsLast]
                rNoise = array(ceil(size / Vec2(octave[2], octave[2])) + Vec2(2, 2), 'random float', [octave[0], octave[1]])
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
            size = vectorize(size)
            list = array(size, 'constant', 0)
            for octave in number:  # [[min, max, h, octave alteration method, (if using mix) mix amount (0 - 1)], nextOctaveSameAsLast]
                rNoise = array(ceil(size / Vec3(octave[2], octave[2], octave[2])) + Vec3(2, 2, 2), 'random float', [octave[0], octave[1]])
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
            size = vectorize(size)
            list = array(size, 'constant', 0)
            for octave in number:  # [[min, max, h, octave alteration method, (if using mix) mix amount (0 - 1)], nextOctaveSameAsLast]
                rNoise = array(ceil(size / Vec3(octave[2], octave[2], octave[2])) + Vec3(2, 2, 2), 'random float', [octave[0], octave[1]])
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
            size = vectorize(size)
            list = array(size, 'constant', 0)
            for octave in number:  # [[min, max, h, octave alteration method, (if using mix) mix amount (0 - 1)], nextOctaveSameAsLast]
                rNoise = array(ceil(size / Vec4(octave[2], octave[2], octave[2], octave[2])) + Vec4(2, 2, 2, 2), 'random float', [octave[0], octave[1]])
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
            size = vectorize(size)
            list = array(size, 'constant', 0)
            for octave in number:  # [[min, max, h, octave alteration method, (if using mix) mix amount (0 - 1)], nextOctaveSameAsLast]
                rNoise = array(ceil(size / Vec4(octave[2], octave[2], octave[2], octave[2])) + Vec4(2, 2, 2, 2), 'random float', [octave[0], octave[1]])
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
    def fromArray(list: list, name: str) -> im.fromarray:  # converts a 2d array of colors into a png image
        img_w, img_h = [len(list), len(list[0])]
        data = np.zeros((img_h, img_w, 3), dtype=np.uint8)
        data[100, 100] = [255, 0, 0]
        
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
    def getArray(imageFile: str) -> list:  # creates a 2d array of the pixel colors of a png
        surf = pygame.Surface(Vec2(5000, 3000))
        image = surf.blit(pygame.image.load(imageFile), Vec2(0, 0))
        size = Vec2(image.size[0], image.size[1])
        newList = array(size, 'constant', None)
        for x in range(size.x):
            for y in range(size.y):
                newList[x][y] = surf.get_at((x, y))
                newList[x][y] = Vec4(newList[x][y][0], newList[x][y][1], newList[x][y][2], newList[x][y][3])
        return newList


def vectorize(list: list):  # converts a list/tuple into a vector
    length = len(list)
    if length == 2:
        return Vec2(list[0], list[1])
    elif length == 3:
        return Vec3(list[0], list[1], list[2])
    elif length == 4:
        return Vec4(list[0], list[1], list[2], list[3])
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
    def read(file: str) -> list:  # returns a list of each line in a file
        return open(file).read().split('\n')
    def delete(file: str, line: int) -> None:  # deltes a line for a file
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
    def write(file: str, line: int, Text: str) -> None:  # writes a new line onto a file
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

