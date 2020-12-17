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
        return math.lengthOfList(self.xy)
    def floor(self):  # gets the floor of the Vector
        return Vec2(math.floor(self.x), math.floor(self.y))
    def fract(self):  # gets the decimal value of the number
        return Vec2(math.fract(self.x), math.fract(self.y))
    def __len__(self):  # returns the length of the Vector when you use the len() function
        return 2
    def __getitem__(self, key):
        return self.xy[key]
    def dot(self, other):
        return (self.x * other.x + self.y * other.y)
    def __round__(self):
        return Vec2(round(self.x), round(self.y))


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


def mix(vector1, vector2, percentage):
    return vector1.mix(vector2, percentage)


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


def dot(vector1, vector2):
    return vector1.dot(vector2)


def normalize(Vector):
    mag = length(Vector)  # this may need to be the dot product
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
    def map2D(list, fromMin, fromMax, toMax):  # add a toMin
        min_height = fromMin
        max_height = fromMax - min_height
        scaler = (toMax / max_height)
        for x in range(len(list)):
            for y in range(len(list[x])):
                list[x][y] -= min_height
                list[x][y] *= scaler
        return list
    def minOf2D(list):
        mins = []
        for x in list:
            mins.append(min(x))
        return min(mins)
    def maxOf2D(list):
        maxs = []
        for x in list:
            maxs.append(max(x))
        return max(maxs)
    def smooth(heights, smoothing = 100):
        for s in range(smoothing):
            for i in range(len(heights)):
                if i not in [0, len(heights) - 1]:
                    height1 = heights[i - 1]
                    height3 = heights[i + 1]
                    heights[i] = (heights[i] * 0.1) + (height1 * 0.45) + (height3 * 0.45)
        return heights
    def interpalate3(h, x, list):
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
    def interpalate5(h, x, list):
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
    def smoothstep(x, p1, p2):
        t = min(max((x - p1) / (p2 - p1), 0), 1)
        return t * t * (3 - 2 * t)
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
    def spline1D(noise, x, h):
        nx = x / h
        p1 = int(nx)
        p2 = p1 + 1
        p3 = p1 + 2
        p0 = p1 - 1
        t = nx - p1
        tt = t * t
        ttt = tt * t
        q1 = -ttt + 2*tt - t
        q2 = 3*ttt - 5*tt + 2
        q3 = -3*ttt + 4*tt + t
        q4 = ttt - tt
        ty = 0.5 * (noise[p0] * q1 + noise[p1] * q2 + noise[p2] * q3 + noise[p3] * q4)
        return ty
    def spline2D(noise, x, y, h):
        nx = x / h
        i = int(nx)
        ty1 = math.spline1D(noise[i - 1], y, h)
        ty2 = math.spline1D(noise[i    ], y, h)
        ty3 = math.spline1D(noise[i + 1], y, h)
        ty4 = math.spline1D(noise[i + 2], y, h)
        return math.spline1D([ty1, ty2, ty3, ty4], (nx - i) * h + h, h)
    def spline3D(noise, x, y, z, h):
        nx = x / h
        i = int(nx)
        ty1 = math.spline2D(noise[i - 1], y, z, h)
        ty2 = math.spline2D(noise[i    ], y, z, h)
        ty3 = math.spline2D(noise[i + 1], y, z, h)
        ty4 = math.spline2D(noise[i + 2], y, z, h)
        return math.spline1D([ty1, ty2, ty3, ty4], (nx - i) * h + h, h)


class dists:
    def distToCircularPoint(pos, center, r):  # gets the distance to a sphere/circle/hypershpere from a point (negitive when in the circle)
        return length(pos - center) - r
    def distToPoint(pos, point_pos):  # gets the distance to a point from a point
        return length(pos - point_pos)


class colorGradient:
    def __init__(self):
        self.grades = []
        self.grade_points = []
    def addPoint(self, point, color):
        self.grades.append(color)
        self.grade_points.append(point)
    def gradeAt(self, point):  # imporve this so the colors dont hve a harsh cutoff
        closest1 = 10000000
        closest2 = 10000000
        index1 = -1
        index2 = -1
        i = 0
        for grade in self.grade_points:
            dist_to_grade = abs(point - grade)
            if dist_to_grade < closest1:
                closest1 = dist_to_grade
                index1 = i
            elif dist_to_grade < closest2:
                closest2 = dist_to_grade
                index2 = i
            i += 1
        
        max_dist = closest1 + closest2
        
        percent = 1 - (closest1 / max_dist)
        
        return mix(self.grades[index2], self.grades[index1], percent)


class noise:
    def perlin1D(randNoise, h, x):
        return math.spline(randNoise, x, h)
    def perlin2D(randNoise, h, x, y):  # add this to PyVectors (change to be 3d)
        return math.spline2D(randNoise, x, y, h)
    def perlin3D(randNoise, h, x, y, z):
        return math.spline3D(randNoise, x, y, z, h)

