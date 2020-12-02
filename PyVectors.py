import math as Math  # imports the math library to add cos, sin, sqrt, ect...

small_num = 0.00000000000000001


def divide(value1, value2):  # divides and avoids divition by zero errors
    return (value1 + small_num) / (value2 + small_num)


class vec4:  # this function stores and operates an a tuple/list containing four items (class functions gone over in the Vec2 class)
    def __init__(self, x=None, y=None, z=None, w=None):
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
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.xy = [x, y]
        self.xyz = [x, y, z]
        self.xyzw = [x, y, z, w]
        
        self.r = x
        self.g = y
        self.b = z
        self.rgb = [x, y, z]
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
        return lengthOfList(self.xyzw)
    def floor(self):
        return Vec4(math.floor(self.x), math.floor(self.y), math.floor(self.z), math.floor(self.w))
    def fract(self):
        return Vec4(math.fract(self.x), math.fract(self.y), math.fract(self.z), math.fract(self.w))
    def __len__(self):
        return 4
    def __getitem__(self, key):
        return self.xyzw[key]


class vec3:  # this function stores and operates an a tuple/list containing three items (class functions gone over in the Vec2 class)
    def __init__(self, x=None, y=None, z=None):
        if None in [x, y, z]:
            if y == None:
                y = x
                z = x
            else:
                if x == None:
                    raise SyntaxError("Position is undefined, please put an x or an x, y and z")
                else:
                    SyntaxError("Requires more information, please put an x or an x, y and z")
        self.x = x
        self.y = y
        self.z = z
        self.w = 0
        self.xy = [x, y]
        self.xyz = [x, y, z]
        
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
        return lengthOfList(self.xyz)
    def floor(self):
        return Vec3(math.floor(self.x), math.floor(self.y), math.floor(self.z))
    def fract(self):
        return Vec3(math.fract(self.x), math.fract(self.y), math.fract(self.z))
    def __len__(self):
        return 3
    def __getitem__(self, key):
        return self.xyz[key]


class vec2:  # this function stores and operates an a tuple/list containing two items
    def __init__(self, x=None, y=None):  # initializing the tuple/list
        if None in [x, y]:  # filling in the empty places of the Vector
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
    def __ne__(self, other):
        if self.x != other.x and self.y != other.y:  # checks if the Vectors are not equal like Vector1 != Vector2
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
        return lengthOfList(self.xy)
    def floor(self):  # gets the floor of the Vector
        return Vec2(math.floor(self.x), math.floor(self.y))
    def fract(self):  # gets the decimal value of the number
        return Vec2(math.fract(self.x), math.fract(self.y))
    def __len__(self):  # returns the length of the Vector when you use the len() function
        return 2
    def __getitem__(self, key):
        return self.xy[key]


class Vec4:  # this class dosent use the smart fill in making it slightly faster
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.xy = [x, y]
        self.xyz = [x, y, z]
        self.xyzw = [x, y, z, w]
        
        self.r = x
        self.g = y
        self.b = z
        self.rgb = [x, y, z]
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
        return lengthOfList(self.xyzw)
    def floor(self):
        return Vec4(math.floor(self.x), math.floor(self.y), math.floor(self.z), math.floor(self.w))
    def fract(self):
        return Vec4(math.fract(self.x), math.fract(self.y), math.fract(self.z), math.fract(self.w))
    def __len__(self):
        return 4
    def __getitem__(self, key):
        return self.xyzw[key]


class Vec3:  # this class dosent use the smart fill in making it slightly faster
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.w = 0
        self.xy = [x, y]
        self.xyz = [x, y, z]
        
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
        return lengthOfList(self.xyz)
    def floor(self):
        return Vec3(math.floor(self.x), math.floor(self.y), math.floor(self.z))
    def fract(self):
        return Vec3(math.fract(self.x), math.fract(self.y), math.fract(self.z))
    def __len__(self):
        return 3
    def __getitem__(self, key):
        return self.xyz[key]


class Vec2:  # this class dosent use the smart fill in making it slightly faster
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
    def __floordiv__(self, other): Vector1 // Vector2
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
        return lengthOfList(self.xy)
    def floor(self):
        return Vec2(math.floor(self.x), math.floor(self.y))
    def fract(self):
        return Vec2(math.fract(self.x), math.fract(self.y))
    def __len__(self):
        return 2
    def __getitem__(self, key):
        return self.xy[key]


def getPos(Vector, indexes):
    new_list = []
    for i in indexes:
        new_list.append(Vector[i])
    
    return new_list


def Int(Vector):
    return floor(Vector)


def clamp(Vector, min_, max_):
    return Vector.clamp(min_, max_)


def fract(Vector):
    return Vector.fract()


def sqrt(Vector):
    return Vector.sqrt()


def floor(Vector):
    return Vector.floor()


def cos(Vector):
    return Vector.cos()


def sin(Vector):
    return Vector.sin()


def tan(Vector):
    return Vector.tan()


def normalize(Vector):
    mag = length(Vector)
    return Vector / Vec4(mag)


def length(Vector):  # gets the length of a Vector (using the pythagorean theorem)
    return Vector.length()


class math:
    def mix(value1, value2, percentage):  # mixes two numbers based on a number ranging from 1 - 0
        percentage = math.clamp(percentage, 0, 1)
        return (value1*percentage)+(value2*percentage)
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


class dists:
    def distToCircularPoint(pos, center, r):  # gets the distance to a sphere/circle/hypershpere from a point (negitive when in the circle)
        return length(pos - center) - r
    def distToPoint(pos, point_pos):  # gets the distance to a point from a point
        return length(pos - point_pos)

