from os import name
from typing import Union, NewType, Tuple, List  # for creating/using types for better documentation
import numpy as np  # importing numpy to allow creation of png's unsing PIL (png.fromArray)
from PIL import Image as im  # importing PIL to create png's (png.fromArray)
import random, pygame
from numpy.lib.type_check import nan_to_num  # importing random for perlin noise (noise.perlin or noise.ridge) and more and importing pygame to get the colors of a png (png.getArray)
import threading  # for casting threads (for the pythreading disperse method)
import math  # importing the pyMath library to add cos, sin, sqrt, ect... (pyMath.pyMathType)

# 2 types for functions and objects
function = NewType('function', Tuple[any])
object   = NewType('object'  , Tuple[any])
vector4  = NewType('vector4' , Tuple[any, any, any, any])
vector3  = NewType('vector3' , Tuple[any, any, any])
vector2  = NewType('vector2' , Tuple[any, any])
vector   = NewType('vector'  , Tuple[any])


#-----------------------------------------VECTOR CLASSES WITH AUTO COMPLETE-----------------------------------------

class vec4:  # this class stores and operates an a tuple/list containing four items (class functions gone over in the Vec2 class)
    def __init__(self, x: any = None, y: any = None, z: any = None, w: any = None) -> None:
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
        
        self.xy = [self.x, self.y]
        self.xyz = [self.x, self.y, self.z]
        self.xyzw = [self.x, self.y, self.z, self.w]
        
        self.yz = [self.y, self.z]
        self.xy = [self.x, self.y]
        self.xz = [self.x, self.z]
        
        self.r = self.x
        self.g = self.y
        self.b = self.z
        self.a = self.w
        self.rgb = [self.x, self.y, self.z]
        self.rgba = [self.x, self.y, self.z, self.w]
    def __add__(self, other: vector) -> vector4:
        return Vec4(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)
    def __sub__(self, other: vector) -> vector4:
        return Vec4(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)
    def __mul__(self, other: vector) -> vector4:
        return Vec4(self.x * other.x, self.y * other.y, self.z * other.z, self.w * other.w)
    def __truediv__(self, other: vector) -> vector4:
        return Vec4(pyMath.divideT(self.x, other.x), pyMath.divideT(self.y, other.y), pyMath.divideT(self.z, other.z), pyMath.divideT(self.w, other.w))
    def __floordiv__(self, other: vector) -> vector4:
        return Vec4(self.x//other.x, self.y//other.y, self.z//other.z, self.w//other.w)
    def __mod__(self, other: vector) -> vector4:
        return Vec4(self.x%other.x, self.y%other.y, self.z%other.z, self.w%other.w)
    def __pow__(self, other: vector) -> vector4:
        return Vec4(self.x**other.x, self.y**other.y, self.z**other.z, self.w**other.w)
    def __rshift__(self, other: vector) -> vector4:
        return Vec4(self.x>>other.x, self.y>>other.y, self.z>>other.z, self.w>>other.w)
    def __lshift__(self, other: vector) -> vector4:
        return Vec4(self.x<<other.x, self.y<<other.y, self.z<<other.z, self.w<<other.w)
    def __lt__(self, other: vector) -> bool:
        dot1 = (self.x * self.x) + (self.y * self.y) + (self.z * self.z) + (self.w * self.w)
        dot2 = (other.x * other.x) + (other.y * other.y) + (other.z * other.z) + (other.w * other.w)
        if dot1 < dot2:
            return True
        else:
            return False
    def __gt__(self, other: vector) -> bool:
        dot1 = (self.x * self.x) + (self.y * self.y) + (self.z * self.z) + (self.w * self.w)
        dot2 = (other.x * other.x) + (other.y * other.y) + (other.z * other.z) + (other.w * other.w)
        if dot1 > dot2:
            return True
        else:
            return False
    def __le__(self, other: vector) -> bool:
        dot1 = (self.x * self.x) + (self.y * self.y) + (self.z * self.z) + (self.w * self.w)
        dot2 = (other.x * other.x) + (other.y * other.y) + (other.z * other.z) + (other.w * other.w)
        if dot1 <= dot2:
            return True
        else:
            return False
    def __ge__(self, other: vector) -> bool:
        dot1 = (self.x * self.x) + (self.y * self.y) + (self.z * self.z) + (self.w * self.w)
        dot2 = (other.x * other.x) + (other.y * other.y) + (other.z * other.z) + (other.w * other.w)
        if dot1 >= dot2:
            return True
        else:
            return False
    def __eq__(self, other: vector) -> bool:
        if self.x == other.x and self.y == other.y and self.z == other.z and self.w == other.w:
            return True
        else:
            return False
    def __ne__(self, other: vector) -> bool:
        if self.x != other.x and self.y != other.y and self.z != other.z and self.w != other.w:
            return True
        else:
            return False
    def __isub__(self, other: vector) -> vector4:
        return Vec4(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)
    def __iadd__(self, other: vector) -> vector4:
        return Vec4(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)
    def __imult__(self, other: vector) -> vector4:
        return Vec4(self.x * other.x, self.y * other.y, self.z * other.z, self.w * other.w)
    def __idiv__(self, other: vector) -> vector4:
        return Vec4(pyMath.divideT(self.x, other.x), pyMath.divideT(self.y, other.y), pyMath.divideT(self.z, other.z), pyMath.divideT(self.w, other.w))
    def __ifloordiv__(self, other: vector) -> vector4:
        return Vec4(self.x//other.x, self.y//other.y, self.z//other.z, self.w//other.w)
    def __imod__(self, other: vector) -> vector4:
        return Vec4(self.x%other.x, self.y%other.y, self.z%other.z, self.w%other.w)
    def __ipow__(self, other: vector) -> vector4:
        return Vec4(self.x**other.x, self.y**other.y, self.z**other.z, self.w**other.w)
    def __irshift__(self, other: vector) -> vector4:
        return Vec4(self.x >> other.x, self.y >> other.y, self.z >> other.z, self.w >> other.w)
    def __ilshift__(self, other: vector) -> vector4:
        return Vec4(self.x << other.x, self.y << other.y, self.z << other.z, self.w << other.w)
    def __neg__(self) -> vector4:
        return Vec4(-self.x, -self.y, -self.z, -self.w)
    def __pos__(self) -> vector4:
        return Vec4(+self.x, +self.y, +self.z, +self.w)
    def __abs__(self) -> vector4:
        return Vec4(abs(self.x), abs(self.y), abs(self.z), abs(self.w))
    def __str__(self) -> str:
        return 'Vec4(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ', ' + str(self.w) + ')'
    def mix(self, other: vector, percentage: float) -> vector4:
        return Vec4(pyMath.mix(self.x, other.x, percentage), pyMath.mix(self.y, other.y, percentage), pyMath.mix(self.z, other.z, percentage), pyMath.mix(self.w, other.w, percentage))
    def clamp(self, min_: Union[float, int], max_: Union[float, int]) -> vector4:
        return Vec4(pyMath.clamp(self.x, min_, max_), pyMath.clamp(self.y, min_, max_), pyMath.clamp(self.z, min_, max_), pyMath.clamp(self.w, min_, max_))
    def sqrt(self) -> vector4:
        return Vec4(math.sqrt(self.x), math.sqrt(self.y), math.sqrt(self.z), math.sqrt(self.w))
    def tan(self) -> vector4:
        return Vec4(math.tan(self.x), math.tan(self.y), math.tan(self.z), math.tan(self.w))
    def sin(self) -> vector4:
        return Vec4(math.sin(self.x), math.sin(self.y), math.sin(self.z), math.sin(self.w))
    def cos(self) -> vector4:
        return Vec4(math.cos(self.x), math.cos(self.y), math.cos(self.z), math.cos(self.w))
    def length(self) -> float:
        return pyMath.length(self.xyzw)
    def floor(self) -> vector4:
        return Vec4(math.floor(self.x), math.floor(self.y), math.floor(self.z), math.floor(self.w))
    def fract(self) -> vector4:
        return Vec4(pyMath.fract(self.x), pyMath.fract(self.y), pyMath.fract(self.z), pyMath.fract(self.w))
    def __len__(self) -> int:
        return 4
    def __getitem__(self, key: int) -> any:
        return self.xyzw[key]
    def dot(self, other: vector) -> Union[float, int]:
        return (self.x * other.x + self.y * other.y + self.z * other.z + self.w * other.w)
    def __round__(self) -> vector4:
        return Vec4(round(self.x), round(self.y), round(self.z), round(self.w))
    def ceil(self) -> vector4:
        return Vec4(math.ceil(self.x), math.ceil(self.y), math.ceil(self.z), math.ceil(self.w))
    def copy(self) -> vector4:
        return Vec4(self.x, self.y, self.z, self.w)
    def __setitem__(self, i: int, v: any) -> None:
        self.xyzw[i] = v
        self.x = self.xyzw[0]
        self.y = self.xyzw[1]
        self.z = self.xyzw[2]
        self.w = self.xyzw[3]
        self.rgba = self.xyzw
        self.r = self.xyzw[0]
        self.g = self.xyzw[1]
        self.b = self.xyzw[2]
        self.a = self.xyzw[3]
    def __hash__(self) -> str:
        return hash(str(self))


class vec3:  # this class stores and operates an a tuple/list containing three items (class functions gone over in the Vec2 class except for .cross)
    def __init__(self, x: any = None, y: any = None, z: any = None) -> None:
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
    def __add__(self, other: vector) -> vector3:
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other: vector) -> vector3:
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, other: vector) -> vector3:
        return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)
    def __truediv__(self, other: vector) -> vector3:
        return Vec3(pyMath.divideT(self.x, other.x), pyMath.divideT(self.y, other.y), pyMath.divideT(self.z, other.z))
    def __floordiv__(self, other: vector) -> vector3:
        return Vec3(self.x//other.x, self.y//other.y, self.z//other.z)
    def __mod__(self, other: vector) -> vector3:
        return Vec3(self.x%other.x, self.y%other.y, self.z%other.z)
    def __pow__(self, other: vector) -> vector3:
        return Vec3(self.x**other.x, self.y**other.y, self.z**other.z)
    def __rshift__(self, other: vector) -> vector3:
        return Vec3(self.x>>other.x, self.y>>other.y, self.z>>other.z)
    def __lshift__(self, other: vector) -> vector3:
        return Vec3(self.x<<other.x, self.y<<other.y, self.z<<other.z)
    def __lt__(self, other: vector) -> bool:
        dot1 = (self.x * self.x) + (self.y * self.y) + (self.z * self.z)
        dot2 = (other.x * other.x) + (other.y * other.y) + (other.z * other.z)
        if dot1 < dot2:
            return True
        else:
            return False
    def __gt__(self, other: vector) -> bool:
        dot1 = (self.x * self.x) + (self.y * self.y) + (self.z * self.z)
        dot2 = (other.x * other.x) + (other.y * other.y) + (other.z * other.z)
        if dot1 > dot2:
            return True
        else:
            return False
    def __le__(self, other: vector) -> bool:
        dot1 = (self.x * self.x) + (self.y * self.y) + (self.z * self.z)
        dot2 = (other.x * other.x) + (other.y * other.y) + (other.z * other.z)
        if dot1 <= dot2:
            return True
        else:
            return False
    def __ge__(self, other: vector) -> bool:
        dot1 = (self.x * self.x) + (self.y * self.y) + (self.z * self.z)
        dot2 = (other.x * other.x) + (other.y * other.y) + (other.z * other.z)
        if dot1 >= dot2:
            return True
        else:
            return False
    def __eq__(self, other: vector) -> bool:
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False
    def __ne__(self, other: vector) -> bool:
        if self.x != other.x and self.y != other.y and self.z != other.z:
            return True
        else:
            return False
    def __isub__(self, other: vector) -> vector3:
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
    def __iadd__(self, other: vector) -> vector3:
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    def __imult__(self, other: vector) -> vector3:
        return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)
    def __idiv__(self, other: vector) -> vector3:
        return Vec3(pyMath.divideT(self.x, other.x), pyMath.divideT(self.y, other.y), pyMath.divideT(self.z, other.z))
    def __ifloordiv__(self, other: vector) -> vector3:
        return Vec3(self.x//other.x, self.y//other.y, self.z//other.z)
    def __imod__(self, other: vector) -> vector3:
        return Vec3(self.x%other.x, self.y%other.y, self.z%other.z)
    def __ipow__(self, other: vector) -> vector3:
        return Vec3(self.x**other.x, self.y**other.y, self.z**other.z)
    def __irshift__(self, other: vector) -> vector3:
        return Vec3(self.x >> other.x, self.y >> other.y, self.z >> other.z)
    def __ilshift__(self, other: vector) -> vector3:
        return Vec3(self.x << other.x, self.y << other.y, self.z << other.z)
    def __neg__(self) -> vector3:
        return Vec3(-self.x, -self.y, -self.z)
    def __pos__(self) -> vector3:
        return Vec3(+self.x, +self.y, +self.z)
    def __abs__(self) -> vector3:
        return Vec3(abs(self.x), abs(self.y), abs(self.z))
    def __str__(self) -> str:
        return 'Vec3(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'
    def mix(self, other: vector, percentage: float) -> vector3:
        return Vec3(pyMath.mix(self.x, other.x, percentage), pyMath.mix(self.y, other.y, percentage), pyMath.mix(self.z, other.z, percentage))
    def clamp(self, min_: Union[float, int], max_: Union[float, int]) -> vector3:
        return Vec3(pyMath.clamp(self.x, min_, max_), pyMath.clamp(self.y, min_, max_), pyMath.clamp(self.z, min_, max_))
    def sqrt(self) -> vector3:
        return Vec3(math.sqrt(self.x), math.sqrt(self.y), math.sqrt(self.z))
    def tan(self) -> vector3:
        return Vec3(math.tan(self.x), math.tan(self.y), math.tan(self.z))
    def cross(self, other: vector3) -> vector3:  # returns the cross product of two Vectors
        val1 = (self.y * other.z) - (self.z * other.y)
        val2 = (self.z * other.x) - (self.x * other.z)
        val3 = (self.x * other.y) - (self.y * other.x)
        return Vec3(val1, val2, val3)
    def sin(self) -> vector3:
        return Vec3(math.sin(self.x), math.sin(self.y), math.sin(self.z))
    def cos(self) -> vector3:
        return Vec3(math.cos(self.x), math.cos(self.y), math.cos(self.z))
    def length(self) -> float:
        return pyMath.length(self.xyz)
    def floor(self) -> vector3:
        return Vec3(math.floor(self.x), math.floor(self.y), math.floor(self.z))
    def fract(self) -> vector3:
        return Vec3(pyMath.fract(self.x), pyMath.fract(self.y), pyMath.fract(self.z))
    def __len__(self) -> int:
        return 3
    def __getitem__(self, key: int) -> any:
        return self.xyz[key]
    def dot(self, other: vector) -> Union[float, int]:
        return (self.x * other.x + self.y * other.y + self.z * other.z)
    def __round__(self) -> vector3:
        return Vec3(round(self.x), round(self.y), round(self.z))
    def ceil(self) -> vector3:
        return Vec3(math.ceil(self.x), math.ceil(self.y), math.ceil(self.z))
    def copy(self) -> vector3:
        return Vec3(self.x, self.y, self.z)
    def __setitem__(self, i: int, v: any) -> None:
        self.xyz[i] = v
        self.x = self.xyz[0]
        self.y = self.xyz[1]
        self.z = self.xyz[2]
        self.rgb = self.xyz
        self.r = self.xyz[0]
        self.g = self.xyz[1]
        self.b = self.xyz[2]
    def __hash__(self) -> str:
        return hash(str(self))


class vec2:  # this class stores and operates on a tuple/list containing two items
    def __init__(self, x: any = None, y: any = None) -> None:  # initializing the tuple/list
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
    def __add__(self, other: vector) -> vector2:  # adding two list like Vector1 + Vector2
        return Vec2(self.x + other.x, self.y + other.y)
    def __sub__(self, other: vector) -> vector2:  # subtracting two Vectors like Vector1 - Vector2
        return Vec2(self.x - other.x, self.y - other.y)
    def __mul__(self, other: vector) -> vector2:  # multiplying two Vectors like Vector1 * Vector2
        return Vec2(self.x * other.x, self.y * other.y)
    def __truediv__(self, other: vector) -> vector2:  # divides two Vectors like Vector1 / Vector2
        return Vec2(pyMath.divideT(self.x, other.x), pyMath.divideT(self.y, other.y))
    def __floordiv__(self, other: vector) -> vector2:  # divides two Vectors and returns the int of the division like Vector1 // Vector2
        return Vec2(self.x//other.x, self.y//other.y)
    def __mod__(self, other: vector) -> vector2:  # gets the mod of two Vectors like Vector1 % Vector2
        return Vec2(self.x%other.x, self.y%other.y)
    def __pow__(self, other: vector) -> vector2:  # gets the power of two Vectors like Vector1 ** Vector2
        return Vec2(self.x**other.x, self.y**other.y)
    def __rshift__(self, other: vector) -> vector2:  # bit shifts to the right like Vector1 >> Vector2
        return Vec2(self.x>>other.x, self.y>>other.y)
    def __lshift__(self, other: vector) -> vector2:  # bit shifts to the left like Vector1 << Vector2
        return Vec2(self.x<<other.x, self.y<<other.y)
    def __lt__(self, other: vector) -> bool:  # compares two Vectors magnitudes/dot products like Vector1 < Vector2
        dot1 = (self.x * self.x) + (self.y * self.y)
        dot2 = (other.x * other.x) + (other.y * other.y)
        if dot1 < dot2:
            return True
        else:
            return False
    def __gt__(self, other: vector) -> bool:  # compares two Vectors magnitudes/dot products like Vector1 > Vector2
        dot1 = (self.x * self.x) + (self.y * self.y)
        dot2 = (other.x * other.x) + (other.y * other.y)
        if dot1 > dot2:
            return True
        else:
            return False
    def __le__(self, other: vector) -> bool:  # compares two Vectors magnitudes/dot products like Vector1 <= Vector2
        dot1 = (self.x * self.x) + (self.y * self.y)
        dot2 = (other.x * other.x) + (other.y * other.y)
        if dot1 <= dot2:
            return True
        else:
            return False
    def __ge__(self, other: vector) -> bool:  # compares two Vectors magnitudes/dot products like Vector1 >= Vector2
        dot1 = (self.x * self.x) + (self.y * self.y)
        dot2 = (other.x * other.x) + (other.y * other.y)
        if dot1 >= dot2:
            return True
        else:
            return False
    def __eq__(self, other: vector) -> bool:  # checks if two Vectors are equal like Vector1 == Vector2
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
    def __ne__(self, other: vector) -> bool:  # checks if the Vectors are not equal like Vector1 != Vector2
        if self.x != other.x and self.y != other.y:
            return True
        else:
            return False
    def __isub__(self, other: vector) -> vector2:  # subtracts a Vector from another Vector by using Vector1 -= Vector2
        return Vec2(self.x - other.x, self.y - other.y)
    def __iadd__(self, other: vector) -> vector2:  # adds two Vectors by using Vector1 += Vector2
        return Vec2(self.x + other.x, self.y + other.y)
    def __imult__(self, other: vector) -> vector2:  # multiples the Vector by another Vector by putting Vector1 *= Vector2
        return Vec2(self.x * other.x, self.y * other.y)
    def __idiv__(self, other: vector) -> vector2:  # returns the Vector divided by another Vector by puting Vector1 /= Vector2
        return Vec2(pyMath.divideT(self.x, other.x), pyMath.divideT(self.y, other.y))
    def __ifloordiv__(self, other: vector) -> vector2:  # gets the int of the divided product by using Vector1 //= Vector2
        return Vec2(self.x//other.x, self.y//other.y)
    def __imod__(self, other: vector) -> vector2:  # gets the mod of the Vector and another Vector using Vector1 %= Vector2
        return Vec2(self.x%other.x, self.y%other.y)
    def __ipow__(self, other: vector) -> vector2:  # puts the Vector to the power of another Vector using Vector1 **= Vector2
        return Vec2(self.x**other.x, self.y**other.y)
    def __irshift__(self, other: vector) -> vector2:  # bit shifts to the right by using >>=
        return Vec2(self.x >> other.x, self.y >> other.y)
    def __ilshift__(self, other: vector) -> vector2:  # bit shifts to the left by using <<=
        return Vec2(self.x << other.x, self.y << other.y)
    def __neg__(self) -> vector2:  # makes the Vector negative when you use -Vector
        return Vec2(-self.x, -self.y)
    def __pos__(self) -> vector2:  # makes the Vector positive when you use +Vector
        return Vec2(+self.x, +self.y)
    def __abs__(self) -> vector2:  # returns the absolute value of the Vector when you use abs()
        return Vec2(abs(self.x), abs(self.y))
    def __str__(self) -> str:  # this function makes it return the position as a string when printing (using the print("text") in python) the Vector
        return 'Vec2(' + str(self.x) + ', ' + str(self.y) + ')'
    def mix(self, other: vector, percentage: float) -> vector2:  # mixes the Vector with another Vector based on a percentage
        return Vec2(pyMath.mix(self.x, other.x, percentage), pyMath.mix(self.y, other.y, percentage))
    def clamp(self, min_: Union[float, int], max_: Union[float, int]) -> vector2:  # clamps the Vector
        return Vec2(pyMath.clamp(self.x, min_, max_), pyMath.clamp(self.y, min_, max_))
    def sqrt(self) -> vector2:  # returns the square root of the Vector
        return Vec2(math.sqrt(self.x), math.sqrt(self.y))
    def tan(self) -> vector2:  # returns the tangent of the Vector
        return Vec2(math.tan(self.x), math.tan(self.y))
    def sin(self) -> vector2:  # returns the sign of the Vector
        return Vec2(math.sin(self.x), math.sin(self.y))
    def cos(self) -> vector2:  # returns the cosine of the Vector
        return Vec2(math.cos(self.x), math.cos(self.y))
    def length(self) -> float:  # gets the length of the Vector (length(Vector) also works)
        return pyMath.length(self.xy)
    def floor(self) -> vector2:  # gets the floor of the Vector
        return Vec2(math.floor(self.x), math.floor(self.y))
    def fract(self) -> vector2:  # gets the decimal value of the number
        return Vec2(pyMath.fract(self.x), pyMath.fract(self.y))
    def __len__(self) -> int:  # returns the length of the Vector when you use the len() function
        return 2
    def __getitem__(self, key: int) -> any:  # gets the item at an index
        return self.xy[key]
    def dot(self, other) -> Union[float, int]:  # returns the dot product of tow vectors
        return (self.x * other.x + self.y * other.y)
    def __round__(self) -> vector2:  # rounds the vector
        return Vec2(round(self.x), round(self.y))
    def ceil(self) -> vector2:  # gets the ceiling of a vector
        return Vec2(math.ceil(self.x), math.ceil(self.y))
    def copy(self) -> vector2:
        return Vec2(self.x, self.y)
    def __setitem__(self, i: int, v: any) -> None:
        self.xy[i] = v
        self.x = self.xy[0]
        self.y = self.xy[1]
        self.rg = self.xy
        self.r = self.xy[0]
        self.g = self.xy[1]
    def __hash__(self) -> str:
        return hash(str(self))


#-----------------------------------------VECTOR CLASSES-----------------------------------------

class Vec4:  # this class stores and operates an a tuple/list containing four items (class functions gone over in the Vec2 class)
    def __init__(self, x: any, y: any, z: any, w: any) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        
        self.xy = [self.x, self.y]
        self.xyz = [self.x, self.y, self.z]
        self.xyzw = [self.x, self.y, self.z, self.w]
        
        self.yz = [self.y, self.z]
        self.xy = [self.x, self.y]
        self.xz = [self.x, self.z]
        
        self.r = self.x
        self.g = self.y
        self.b = self.z
        self.a = self.w
        self.rgb = [self.x, self.y, self.z]
        self.rgba = [self.x, self.y, self.z, self.w]
    def __add__(self, other: vector) -> vector4:
        return Vec4(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)
    def __sub__(self, other: vector) -> vector4:
        return Vec4(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)
    def __mul__(self, other: vector) -> vector4:
        return Vec4(self.x * other.x, self.y * other.y, self.z * other.z, self.w * other.w)
    def __truediv__(self, other: vector) -> vector4:
        return Vec4(pyMath.divideT(self.x, other.x), pyMath.divideT(self.y, other.y), pyMath.divideT(self.z, other.z), pyMath.divideT(self.w, other.w))
    def __floordiv__(self, other: vector) -> vector4:
        return Vec4(self.x//other.x, self.y//other.y, self.z//other.z, self.w//other.w)
    def __mod__(self, other: vector) -> vector4:
        return Vec4(self.x%other.x, self.y%other.y, self.z%other.z, self.w%other.w)
    def __pow__(self, other: vector) -> vector4:
        return Vec4(self.x**other.x, self.y**other.y, self.z**other.z, self.w**other.w)
    def __rshift__(self, other: vector) -> vector4:
        return Vec4(self.x>>other.x, self.y>>other.y, self.z>>other.z, self.w>>other.w)
    def __lshift__(self, other: vector) -> vector4:
        return Vec4(self.x<<other.x, self.y<<other.y, self.z<<other.z, self.w<<other.w)
    def __lt__(self, other: vector) -> bool:
        dot1 = (self.x * self.x) + (self.y * self.y) + (self.z * self.z) + (self.w * self.w)
        dot2 = (other.x * other.x) + (other.y * other.y) + (other.z * other.z) + (other.w * other.w)
        if dot1 < dot2:
            return True
        else:
            return False
    def __gt__(self, other: vector) -> bool:
        dot1 = (self.x * self.x) + (self.y * self.y) + (self.z * self.z) + (self.w * self.w)
        dot2 = (other.x * other.x) + (other.y * other.y) + (other.z * other.z) + (other.w * other.w)
        if dot1 > dot2:
            return True
        else:
            return False
    def __le__(self, other: vector) -> bool:
        dot1 = (self.x * self.x) + (self.y * self.y) + (self.z * self.z) + (self.w * self.w)
        dot2 = (other.x * other.x) + (other.y * other.y) + (other.z * other.z) + (other.w * other.w)
        if dot1 <= dot2:
            return True
        else:
            return False
    def __ge__(self, other: vector) -> bool:
        dot1 = (self.x * self.x) + (self.y * self.y) + (self.z * self.z) + (self.w * self.w)
        dot2 = (other.x * other.x) + (other.y * other.y) + (other.z * other.z) + (other.w * other.w)
        if dot1 >= dot2:
            return True
        else:
            return False
    def __eq__(self, other: vector) -> bool:
        if self.x == other.x and self.y == other.y and self.z == other.z and self.w == other.w:
            return True
        else:
            return False
    def __ne__(self, other: vector) -> bool:
        if self.x != other.x and self.y != other.y and self.z != other.z and self.w != other.w:
            return True
        else:
            return False
    def __isub__(self, other: vector) -> vector4:
        return Vec4(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)
    def __iadd__(self, other: vector) -> vector4:
        return Vec4(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)
    def __imult__(self, other: vector) -> vector4:
        return Vec4(self.x * other.x, self.y * other.y, self.z * other.z, self.w * other.w)
    def __idiv__(self, other: vector) -> vector4:
        return Vec4(pyMath.divideT(self.x, other.x), pyMath.divideT(self.y, other.y), pyMath.divideT(self.z, other.z), pyMath.divideT(self.w, other.w))
    def __ifloordiv__(self, other: vector) -> vector4:
        return Vec4(self.x//other.x, self.y//other.y, self.z//other.z, self.w//other.w)
    def __imod__(self, other: vector) -> vector4:
        return Vec4(self.x%other.x, self.y%other.y, self.z%other.z, self.w%other.w)
    def __ipow__(self, other: vector) -> vector4:
        return Vec4(self.x**other.x, self.y**other.y, self.z**other.z, self.w**other.w)
    def __irshift__(self, other: vector) -> vector4:
        return Vec4(self.x >> other.x, self.y >> other.y, self.z >> other.z, self.w >> other.w)
    def __ilshift__(self, other: vector) -> vector4:
        return Vec4(self.x << other.x, self.y << other.y, self.z << other.z, self.w << other.w)
    def __neg__(self) -> vector4:
        return Vec4(-self.x, -self.y, -self.z, -self.w)
    def __pos__(self) -> vector4:
        return Vec4(+self.x, +self.y, +self.z, +self.w)
    def __abs__(self) -> vector4:
        return Vec4(abs(self.x), abs(self.y), abs(self.z), abs(self.w))
    def __str__(self) -> str:
        return 'Vec4(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ', ' + str(self.w) + ')'
    def mix(self, other: vector, percentage: float) -> vector4:
        return Vec4(pyMath.mix(self.x, other.x, percentage), pyMath.mix(self.y, other.y, percentage), pyMath.mix(self.z, other.z, percentage), pyMath.mix(self.w, other.w, percentage))
    def clamp(self, min_: Union[float, int], max_: Union[float, int]) -> vector4:
        return Vec4(pyMath.clamp(self.x, min_, max_), pyMath.clamp(self.y, min_, max_), pyMath.clamp(self.z, min_, max_), pyMath.clamp(self.w, min_, max_))
    def sqrt(self) -> vector4:
        return Vec4(math.sqrt(self.x), math.sqrt(self.y), math.sqrt(self.z), math.sqrt(self.w))
    def tan(self) -> vector4:
        return Vec4(math.tan(self.x), math.tan(self.y), math.tan(self.z), math.tan(self.w))
    def sin(self) -> vector4:
        return Vec4(math.sin(self.x), math.sin(self.y), math.sin(self.z), math.sin(self.w))
    def cos(self) -> vector4:
        return Vec4(math.cos(self.x), math.cos(self.y), math.cos(self.z), math.cos(self.w))
    def length(self) -> float:
        return pyMath.length(self.xyzw)
    def floor(self) -> vector4:
        return Vec4(math.floor(self.x), math.floor(self.y), math.floor(self.z), math.floor(self.w))
    def fract(self) -> vector4:
        return Vec4(pyMath.fract(self.x), pyMath.fract(self.y), pyMath.fract(self.z), pyMath.fract(self.w))
    def __len__(self) -> int:
        return 4
    def __getitem__(self, key: int) -> any:
        return self.xyzw[key]
    def dot(self, other: vector) -> Union[float, int]:
        return (self.x * other.x + self.y * other.y + self.z * other.z + self.w * other.w)
    def __round__(self) -> vector4:
        return Vec4(round(self.x), round(self.y), round(self.z), round(self.w))
    def ceil(self) -> vector4:
        return Vec4(math.ceil(self.x), math.ceil(self.y), math.ceil(self.z), math.ceil(self.w))
    def copy(self) -> vector4:
        return Vec4(self.x, self.y, self.z, self.w)
    def __setitem__(self, i: int, v: any) -> None:
        self.xyzw[i] = v
        self.x = self.xyzw[0]
        self.y = self.xyzw[1]
        self.z = self.xyzw[2]
        self.w = self.xyzw[3]
        self.rgba = self.xyzw
        self.r = self.xyzw[0]
        self.g = self.xyzw[1]
        self.b = self.xyzw[2]
        self.a = self.xyzw[3]
    def __hash__(self) -> str:
        return hash(str(self))


class Vec3:  # this class stores and operates an a tuple/list containing three items (class functions gone over in the Vec2 class except for .cross)
    def __init__(self, x: any, y: any, z: any) -> None:
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
    def __add__(self, other: vector) -> vector3:
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other: vector) -> vector3:
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, other: vector) -> vector3:
        return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)
    def __truediv__(self, other: vector) -> vector3:
        return Vec3(pyMath.divideT(self.x, other.x), pyMath.divideT(self.y, other.y), pyMath.divideT(self.z, other.z))
    def __floordiv__(self, other: vector) -> vector3:
        return Vec3(self.x//other.x, self.y//other.y, self.z//other.z)
    def __mod__(self, other: vector) -> vector3:
        return Vec3(self.x%other.x, self.y%other.y, self.z%other.z)
    def __pow__(self, other: vector) -> vector3:
        return Vec3(self.x**other.x, self.y**other.y, self.z**other.z)
    def __rshift__(self, other: vector) -> vector3:
        return Vec3(self.x>>other.x, self.y>>other.y, self.z>>other.z)
    def __lshift__(self, other: vector) -> vector3:
        return Vec3(self.x<<other.x, self.y<<other.y, self.z<<other.z)
    def __lt__(self, other: vector) -> bool:
        dot1 = (self.x * self.x) + (self.y * self.y) + (self.z * self.z)
        dot2 = (other.x * other.x) + (other.y * other.y) + (other.z * other.z)
        if dot1 < dot2:
            return True
        else:
            return False
    def __gt__(self, other: vector) -> bool:
        dot1 = (self.x * self.x) + (self.y * self.y) + (self.z * self.z)
        dot2 = (other.x * other.x) + (other.y * other.y) + (other.z * other.z)
        if dot1 > dot2:
            return True
        else:
            return False
    def __le__(self, other: vector) -> bool:
        dot1 = (self.x * self.x) + (self.y * self.y) + (self.z * self.z)
        dot2 = (other.x * other.x) + (other.y * other.y) + (other.z * other.z)
        if dot1 <= dot2:
            return True
        else:
            return False
    def __ge__(self, other: vector) -> bool:
        dot1 = (self.x * self.x) + (self.y * self.y) + (self.z * self.z)
        dot2 = (other.x * other.x) + (other.y * other.y) + (other.z * other.z)
        if dot1 >= dot2:
            return True
        else:
            return False
    def __eq__(self, other: vector) -> bool:
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False
    def __ne__(self, other: vector) -> bool:
        if self.x != other.x and self.y != other.y and self.z != other.z:
            return True
        else:
            return False
    def __isub__(self, other: vector) -> vector3:
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
    def __iadd__(self, other: vector) -> vector3:
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    def __imult__(self, other: vector) -> vector3:
        return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)
    def __idiv__(self, other: vector) -> vector3:
        return Vec3(pyMath.divideT(self.x, other.x), pyMath.divideT(self.y, other.y), pyMath.divideT(self.z, other.z))
    def __ifloordiv__(self, other: vector) -> vector3:
        return Vec3(self.x//other.x, self.y//other.y, self.z//other.z)
    def __imod__(self, other: vector) -> vector3:
        return Vec3(self.x%other.x, self.y%other.y, self.z%other.z)
    def __ipow__(self, other: vector) -> vector3:
        return Vec3(self.x**other.x, self.y**other.y, self.z**other.z)
    def __irshift__(self, other: vector) -> vector3:
        return Vec3(self.x >> other.x, self.y >> other.y, self.z >> other.z)
    def __ilshift__(self, other: vector) -> vector3:
        return Vec3(self.x << other.x, self.y << other.y, self.z << other.z)
    def __neg__(self) -> vector3:
        return Vec3(-self.x, -self.y, -self.z)
    def __pos__(self) -> vector3:
        return Vec3(+self.x, +self.y, +self.z)
    def __abs__(self) -> vector3:
        return Vec3(abs(self.x), abs(self.y), abs(self.z))
    def __str__(self) -> str:
        return 'Vec3(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'
    def mix(self, other: vector, percentage: float) -> vector3:
        return Vec3(pyMath.mix(self.x, other.x, percentage), pyMath.mix(self.y, other.y, percentage), pyMath.mix(self.z, other.z, percentage))
    def clamp(self, min_: Union[float, int], max_: Union[float, int]) -> vector3:
        return Vec3(pyMath.clamp(self.x, min_, max_), pyMath.clamp(self.y, min_, max_), pyMath.clamp(self.z, min_, max_))
    def sqrt(self) -> vector3:
        return Vec3(math.sqrt(self.x), math.sqrt(self.y), math.sqrt(self.z))
    def tan(self) -> vector3:
        return Vec3(math.tan(self.x), math.tan(self.y), math.tan(self.z))
    def cross(self, other: vector3) -> vector3:  # returns the cross product of two Vectors
        val1 = (self.y * other.z) - (self.z * other.y)
        val2 = (self.z * other.x) - (self.x * other.z)
        val3 = (self.x * other.y) - (self.y * other.x)
        return Vec3(val1, val2, val3)
    def sin(self) -> vector3:
        return Vec3(math.sin(self.x), math.sin(self.y), math.sin(self.z))
    def cos(self) -> vector3:
        return Vec3(math.cos(self.x), math.cos(self.y), math.cos(self.z))
    def length(self) -> float:
        return pyMath.length(self.xyz)
    def floor(self) -> vector3:
        return Vec3(math.floor(self.x), math.floor(self.y), math.floor(self.z))
    def fract(self) -> vector3:
        return Vec3(pyMath.fract(self.x), pyMath.fract(self.y), pyMath.fract(self.z))
    def __len__(self) -> int:
        return 3
    def __getitem__(self, key: int) -> any:
        return self.xyz[key]
    def dot(self, other: vector) -> Union[float, int]:
        return (self.x * other.x + self.y * other.y + self.z * other.z)
    def __round__(self) -> vector3:
        return Vec3(round(self.x), round(self.y), round(self.z))
    def ceil(self) -> vector3:
        return Vec3(math.ceil(self.x), math.ceil(self.y), math.ceil(self.z))
    def copy(self) -> vector3:
        return Vec3(self.x, self.y, self.z)
    def __setitem__(self, i: int, v: any) -> None:
        self.xyz[i] = v
        self.x = self.xyz[0]
        self.y = self.xyz[1]
        self.z = self.xyz[2]
        self.rgb = self.xyz
        self.r = self.xyz[0]
        self.g = self.xyz[1]
        self.b = self.xyz[2]
    def __hash__(self) -> str:
        return hash(str(self))


class Vec2:  # this class stores and operates on a tuple/list containing two items
    def __init__(self, x: any, y: any) -> None:  # initializing the tuple/list
        # defining the values of the Vector
        self.x = x
        self.y = y
        self.z = 0
        self.w = 0
        self.xy = [x, y]
        
        self.r = x
        self.g = y
        self.rg = [x, y]
    def __add__(self, other: vector) -> vector2:  # adding two list like Vector1 + Vector2
        return Vec2(self.x + other.x, self.y + other.y)
    def __sub__(self, other: vector) -> vector2:  # subtracting two Vectors like Vector1 - Vector2
        return Vec2(self.x - other.x, self.y - other.y)
    def __mul__(self, other: vector) -> vector2:  # multiplying two Vectors like Vector1 * Vector2
        return Vec2(self.x * other.x, self.y * other.y)
    def __truediv__(self, other: vector) -> vector2:  # divides two Vectors like Vector1 / Vector2
        return Vec2(pyMath.divideT(self.x, other.x), pyMath.divideT(self.y, other.y))
    def __floordiv__(self, other: vector) -> vector2:  # divides two Vectors and returns the int of the division like Vector1 // Vector2
        return Vec2(self.x//other.x, self.y//other.y)
    def __mod__(self, other: vector) -> vector2:  # gets the mod of two Vectors like Vector1 % Vector2
        return Vec2(self.x%other.x, self.y%other.y)
    def __pow__(self, other: vector) -> vector2:  # gets the power of two Vectors like Vector1 ** Vector2
        return Vec2(self.x**other.x, self.y**other.y)
    def __rshift__(self, other: vector) -> vector2:  # bit shifts to the right like Vector1 >> Vector2
        return Vec2(self.x>>other.x, self.y>>other.y)
    def __lshift__(self, other: vector) -> vector2:  # bit shifts to the left like Vector1 << Vector2
        return Vec2(self.x<<other.x, self.y<<other.y)
    def __lt__(self, other: vector) -> bool:  # compares two Vectors magnitudes/dot products like Vector1 < Vector2
        dot1 = (self.x * self.x) + (self.y * self.y)
        dot2 = (other.x * other.x) + (other.y * other.y)
        if dot1 < dot2:
            return True
        else:
            return False
    def __gt__(self, other: vector) -> bool:  # compares two Vectors magnitudes/dot products like Vector1 > Vector2
        dot1 = (self.x * self.x) + (self.y * self.y)
        dot2 = (other.x * other.x) + (other.y * other.y)
        if dot1 > dot2:
            return True
        else:
            return False
    def __le__(self, other: vector) -> bool:  # compares two Vectors magnitudes/dot products like Vector1 <= Vector2
        dot1 = (self.x * self.x) + (self.y * self.y)
        dot2 = (other.x * other.x) + (other.y * other.y)
        if dot1 <= dot2:
            return True
        else:
            return False
    def __ge__(self, other: vector) -> bool:  # compares two Vectors magnitudes/dot products like Vector1 >= Vector2
        dot1 = (self.x * self.x) + (self.y * self.y)
        dot2 = (other.x * other.x) + (other.y * other.y)
        if dot1 >= dot2:
            return True
        else:
            return False
    def __eq__(self, other: vector) -> bool:  # checks if two Vectors are equal like Vector1 == Vector2
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
    def __ne__(self, other: vector) -> bool:  # checks if the Vectors are not equal like Vector1 != Vector2
        if self.x != other.x and self.y != other.y:
            return True
        else:
            return False
    def __isub__(self, other: vector) -> vector2:  # subtracts a Vector from another Vector by using Vector1 -= Vector2
        return Vec2(self.x - other.x, self.y - other.y)
    def __iadd__(self, other: vector) -> vector2:  # adds two Vectors by using Vector1 += Vector2
        return Vec2(self.x + other.x, self.y + other.y)
    def __imult__(self, other: vector) -> vector2:  # multiples the Vector by another Vector by putting Vector1 *= Vector2
        return Vec2(self.x * other.x, self.y * other.y)
    def __idiv__(self, other: vector) -> vector2:  # returns the Vector divided by another Vector by puting Vector1 /= Vector2
        return Vec2(pyMath.divideT(self.x, other.x), pyMath.divideT(self.y, other.y))
    def __ifloordiv__(self, other: vector) -> vector2:  # gets the int of the divided product by using Vector1 //= Vector2
        return Vec2(self.x//other.x, self.y//other.y)
    def __imod__(self, other: vector) -> vector2:  # gets the mod of the Vector and another Vector using Vector1 %= Vector2
        return Vec2(self.x%other.x, self.y%other.y)
    def __ipow__(self, other: vector) -> vector2:  # puts the Vector to the power of another Vector using Vector1 **= Vector2
        return Vec2(self.x**other.x, self.y**other.y)
    def __irshift__(self, other: vector) -> vector2:  # bit shifts to the right by using >>=
        return Vec2(self.x >> other.x, self.y >> other.y)
    def __ilshift__(self, other: vector) -> vector2:  # bit shifts to the left by using <<=
        return Vec2(self.x << other.x, self.y << other.y)
    def __neg__(self) -> vector2:  # makes the Vector negative when you use -Vector
        return Vec2(-self.x, -self.y)
    def __pos__(self) -> vector2:  # makes the Vector positive when you use +Vector
        return Vec2(+self.x, +self.y)
    def __abs__(self) -> vector2:  # returns the absolute value of the Vector when you use abs()
        return Vec2(abs(self.x), abs(self.y))
    def __str__(self) -> str:  # this function makes it return the position as a string when printing (using the print("text") in python) the Vector
        return 'Vec2(' + str(self.x) + ', ' + str(self.y) + ')'
    def mix(self, other: vector, percentage: float) -> vector2:  # mixes the Vector with another Vector based on a percentage
        return Vec2(pyMath.mix(self.x, other.x, percentage), pyMath.mix(self.y, other.y, percentage))
    def clamp(self, min_: Union[float, int], max_: Union[float, int]) -> vector2:  # clamps the Vector
        return Vec2(pyMath.clamp(self.x, min_, max_), pyMath.clamp(self.y, min_, max_))
    def sqrt(self) -> vector2:  # returns the square root of the Vector
        return Vec2(math.sqrt(self.x), math.sqrt(self.y))
    def tan(self) -> vector2:  # returns the tangent of the Vector
        return Vec2(math.tan(self.x), math.tan(self.y))
    def sin(self) -> vector2:  # returns the sign of the Vector
        return Vec2(math.sin(self.x), math.sin(self.y))
    def cos(self) -> vector2:  # returns the cosine of the Vector
        return Vec2(math.cos(self.x), math.cos(self.y))
    def length(self) -> float:  # gets the length of the Vector (length(Vector) also works)
        return pyMath.length(self.xy)
    def floor(self) -> vector2:  # gets the floor of the Vector
        return Vec2(math.floor(self.x), math.floor(self.y))
    def fract(self) -> vector2:  # gets the decimal value of the number
        return Vec2(pyMath.fract(self.x), pyMath.fract(self.y))
    def __len__(self) -> int:  # returns the length of the Vector when you use the len() function
        return 2
    def __getitem__(self, key: int) -> any:  # gets the item at an index
        return self.xy[key]
    def dot(self, other) -> Union[float, int]:  # returns the dot product of tow vectors
        return (self.x * other.x + self.y * other.y)
    def __round__(self) -> vector2:  # rounds the vector
        return Vec2(round(self.x), round(self.y))
    def ceil(self) -> vector2:  # gets the ceiling of a vector
        return Vec2(math.ceil(self.x), math.ceil(self.y))
    def copy(self) -> vector2:
        return Vec2(self.x, self.y)
    def __setitem__(self, i: int, v: any) -> None:
        self.xy[i] = v
        self.x = self.xy[0]
        self.y = self.xy[1]
        self.rg = self.xy
        self.r = self.xy[0]
        self.g = self.xy[1]
    def __hash__(self) -> str:
        return hash(str(self))


#-----------------------------------------VECTOR MATH FUNCTIONS-----------------------------------------

def ceil(vector: vector) -> vector:  # gets the ceiling of a vector
    return vector.ceil()

def mix(vector1: vector, vector2: vector, percentage: float) -> vector:  # mixes two vectors based on a percentage
    return vector1.mix(vector2, percentage)

def Int(Vector: vector) -> vector:  # gets the floor/int of a vector
    return floor(Vector)

def clamp(Vector: vector, min_: Union[float, int], max_: Union[float, int]):  # clamps a vector between two values
    return Vector.clamp(min_, max_)

def fract(Vector: vector) -> vector:  # gets the fract of a vector (vector - int(vector))
    return Vector.fract()

def sqrt(Vector: vector) -> vector:  # gets the square root of a vector
    return Vector.sqrt()

def floor(Vector: vector) -> vector:  # gets the floor of a vector
    return Vector.floor()

def cos(Vector: vector) -> vector:  # gets the cosine of a vector
    return Vector.cos()

def sin(Vector: vector) -> vector:  # gets the sin of a vector
    return Vector.sin()

def tan(Vector: vector) -> vector:  # gets the tangint of a vector
    return Vector.tan()

def dot(vector1, vector2: vector) -> vector:  # gets the dot product of two vectors
    return vector1.dot(vector2)

def cross(vector1: vector3, vector2) -> vector3:  # gets the cross product of two vectors (only works a vec3 types)
    return vector1.cross(vector2)

def normalize(Vector: vector) -> vector:  # normalizes a vector
    mag = pyMath.divide0(1, length(Vector))
    return Vector * Vec4(mag, mag, mag, mag)

def length(Vector: vector) -> float:  # gets the length of a Vector (using the pythagorean theorem  a^2 + b^2 = c^2)
    return Vector.length()


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


#-----------------------------------------SIGNED DISTANCE FUNCTIONS-----------------------------------------

class dists:  # multipl distance functions for different shapes
    def distToCircularPoint(pos, center, r):  # gets the distance to a sphere/circle/hypershpere from a point (negitive when in the circle)
        return length(pos - center) - r
    def distToPoint(pos, point_pos):  # gets the distance to a point from a point
        return length(pos - point_pos)


#-----------------------------------------MATH AND OTHER FUNCTIONS FOR LISTS-----------------------------------------

class lists:  # a class do do pyMath operations across an entire list at the same time
    def copy1D(list2: List[any]) -> List[any]:  # copys a list
        size = len(list2)
        list1 = array([size], 'constant', None)
        for x in range(len(list1)):
            list1[x] = list2[x]
        return list1
    def copy2D(list2: List[any]) -> List[any]:  # copys a list
        size = Vec2(len(list2), len(list2[0]))
        list1 = array(size, 'constant', None)
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] = list2[x][y]
        return list1
    def copy3D(list2: List[any]) -> List[any]:  # copys a list
        size = Vec3(len(list2), len(list2[0]), len(list2[0][0]))
        list1 = array(size, 'constant', None)
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] = list2[x][y][z]
        return list1
    def copy4D(list2: List[any]) -> List[any]:  # copys a list
        size = Vec4(len(list2), len(list2[0]), len(list2[0][0]), len(list2[0][0][0]))
        list1 = array(size, 'constant', None)
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] = list2[x][y][z][w]
        return list1
    def clamp1D(list1: List[any], nMin: float, nMax: float) -> List[any]:  # clamps a list
        for x in range(len(list1)):
            list1[x] = pyMath.clamp(list1[x], nMin, nMax)
        return list1
    def clamp2D(list1: List[any], nMin: float, nMax: float) -> List[any]:  # clamps a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] = pyMath.clamp(list1[x][y], nMin, nMax)
        return list1
    def clamp3D(list1: List[any], nMin: float, nMax: float) -> List[any]:  # clamps a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] = pyMath.clamp(list1[x][y][z], nMin, nMax)
        return list1
    def clamp4D(list1: List[any], nMin: float, nMax: float) -> List[any]:  # clamps a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] = pyMath.clamp(list1[x][y][z][w], nMin, nMax)
        return list1
    def min1D(list1: List[any], nMin: float) -> List[any]:  # sets the min of a list
        for x in range(len(list1)):
            list1[x] = min(list1[x], nMin)
        return list1
    def min2D(list1: List[any], nMin: float) -> List[any]:  # sets the min of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] = min(list1[x][y], nMin)
        return list1
    def min3D(list1: List[any], nMin: float) -> List[any]:  # sets the min of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] = min(list1[x][y][z], nMin)
        return list1
    def min4D(list1: List[any], nMin: float) -> List[any]:  # sets the min of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] = min(list1[x][y][z][w], nMin)
        return list1
    def max1D(list1: List[any], nMax: float) -> List[any]:  # sets the max of a list
        for x in range(len(list1)):
            list1[x] = max(list1[x], nMax)
        return list1
    def max2D(list1: List[any], nMax: float) -> List[any]:  # sets the max of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] = max(list1[x][y], nMax)
        return list1
    def max3D(list1: List[any], nMax: float) -> List[any]:  # sets the max of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] = max(list1[x][y][z], nMax)
        return list1
    def max4D(list1: List[any], nMax: float) -> List[any]:  # sets the max of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] = max(list1[x][y][z][w], nMax)
        return list1
    def mix1D(list1: List[any], list2: List[any], list3: List[any]) -> List[any]:  # mixes 3 lists together
        for x in range(len(list1)):
            list1[x] = pyMath.mix(list1[x], list2[x], list3[x])
        return list1
    def mix2D(list1: List[any], list2: list, k: float) -> List[any]:  # mixes 3 lists together
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] = pyMath.mix(list1[x][y], list2[x][y], k)
        return list1
    def mix3D(list1: List[any], list2: List[any], k: float) -> List[any]:  # mixes 3 lists together
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] = pyMath.mix(list1[x][y][z], list2[x][y][z], k)
        return list1
    def mix4D(list1: List[any], list2: List[any], k: float) -> List[any]:  # mixes 3 lists together
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] = pyMath.mix(list1[x][y][z][w], list2[x][y][z][w], k)
        return list1
    def floor_div1D(list1: List[any], list2: List[any]) -> List[any]:  # floor divides two lists
        for x in range(len(list1)):
            list1[x] = list1[x] // list2[x]
        return list1
    def floor_div2D(list1: List[any], list2: List[any]) -> List[any]:  # floor divides two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] = list1[x][y] // list2[x][y]
        return list1
    def floor_div3D(list1: List[any], list2: List[any]) -> List[any]:  # floor divides two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] = list1[x][y][z] // list2[x][y][z]
        return list1
    def floor_div4D(list1: List[any], list2: List[any]) -> List[any]:  # floor divides two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] = list1[x][y][z][w] // list2[x][y][z][w]
        return list1
    def mod1D(list1: List[any], list2: List[any]) -> List[any]:  # mods two lists
        for x in range(len(list1)):
            list1[x] = list1[x] % list2[x]
        return list1
    def mod2D(list1: List[any], list2: List[any]) -> List[any]:  # mods two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] = list1[x][y] % list2[x][y]
        return list1
    def mod3D(list1: List[any], list2: List[any]) -> List[any]:  # mods two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] = list1[x][y][z] % list2[x][y][z]
        return list1
    def mod4D(list1: List[any], list2: List[any]) -> List[any]:  # mods two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] = list1[x][y][z][w] % list2[x][y][z][w]
        return list1
    def pow1D(list1: List[any], list2: List[any]) -> List[any]:  # gets the power of two lists
        for x in range(len(list1)):
            list1[x] = list1[x] ** list2[x]
        return list1
    def pow2D(list1: List[any], list2: List[any]) -> List[any]:  # gets the power of two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] = list1[x][y] ** list2[x][y]
        return list1
    def pow3D(list1: List[any], list2: List[any]) -> List[any]:  # gets the power of two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] = list1[x][y][z] ** list2[x][y][z]
        return list1
    def pow4D(list1: List[any], list2: List[any]) -> List[any]:  # gets the power of two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] = list1[x][y][z][w] ** list2[x][y][z][w]
        return list1
    def round1D(list1: List[any]) -> List[any]:  # rounds a list
        for x in range(len(list1)):
            list1[x] = round(list1[x])
        return list1
    def round2D(list1: List[any]) -> List[any]:  # rounds a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] = round(list1[x][y])
        return list1
    def round3D(list1: List[any]) -> List[any]:  # rounds a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] = round(list1[x][y][z])
        return list1
    def round4D(list1: List[any]) -> List[any]:  # rounds a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] = round(list1[x][y][z][w])
        return list1
    def str1D(list1: List[any]) -> List[any]:  # casts a list to a string type
        for x in range(len(list1)):
            list1[x] = str(list1[x])
        return list1
    def str2D(list1: List[any]) -> List[any]:  # casts a list to a string type
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] = str(list1[x][y])
        return list1
    def str3D(list1: List[any]) -> List[any]:  # casts a list to a string type
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] = str(list1[x][y][z])
        return list1
    def str4D(list1: List[any]) -> List[any]:  # casts a list to a string type
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] = str(list1[x][y][z][w])
        return list1
    def int1D(list1: List[any]) -> List[any]:  # casts a list to a int type
        for x in range(len(list1)):
            list1[x] = int(list1[x])
        return list1
    def int2D(list1: List[any]) -> List[any]:  # casts a list to a int type
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] = int(list1[x][y])
        return list1
    def int3D(list1: List[any]) -> List[any]:  # casts a list to a int type
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] = int(list1[x][y][z])
        return list1
    def int4D(list1: List[any]) -> List[any]:  # casts a list to a int type
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] = int(list1[x][y][z][w])
        return list1
    def fract1D(list1: List[any]) -> List[any]:  # gets the fract of a list
        for x in range(len(list1)):
            list1[x] = pyMath.fract(list1[x])
        return list1
    def fract2D(list1: List[any]) -> List[any]:  # gets the fract of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] = math.floor(fract[x][y])
        return list1
    def fract3D(list1: List[any]) -> List[any]:  # gets the fract of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] = pyMath.fract(list1[x][y][z])
        return list1
    def fract4D(list1: List[any]) -> List[any]:  # gets the fract of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] = pyMath.fract(list1[x][y][z][w])
        return list1
    def ceil1D(list1: List[any]) -> List[any]:  # gets the ceil of a list
        for x in range(len(list1)):
            list1[x] = math.ceil(list1[x])
        return list1
    def ceil2D(list1: List[any]) -> List[any]:  # gets the ceil of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] = math.ceil(list1[x][y])
        return list1
    def ceil3D(list1: List[any]) -> List[any]:  # gets the ceil of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] = math.ceil(list1[x][y][z])
        return list1
    def ceil4D(list1: List[any]) -> List[any]:  # gets the ceil of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] = math.ceil(list1[x][y][z][w])
        return list1
    def floor1D(list1: List[any]) -> List[any]:  # gets the floor of a list
        for x in range(len(list1)):
            list1[x] = math.floor(list1[x])
        return list1
    def floor2D(list1: List[any]) -> List[any]:  # gets the floor of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] = math.floor(list1[x][y])
        return list1
    def floor3D(list1: List[any]) -> List[any]:  # gets the floor of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] = math.floor(list1[x][y][z])
        return list1
    def floor4D(list1: List[any]) -> List[any]:  # gets the floor of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] = math.floor(list1[x][y][z][w])
        return list1
    def abs1D(list1: List[any]) -> List[any]:  # gets the absulute value of a list
        for x in range(len(list1)):
            list1[x] = abs(list1[x])
        return list1
    def abs2D(list1: List[any]) -> List[any]:  # gets the absulute value of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] = abs(list1[x][y])
        return list1
    def abs3D(list1: List[any]) -> List[any]:  # gets the absulute value of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] = abs(list1[x][y][z])
        return list1
    def abs4D(list1: List[any]) -> List[any]:  # gets the absulute value of a list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] = abs(list1[x][y][z][w])
        return list1
    def mult1D(list1: List[any], list2: List[any]) -> List[any]:  # multiplies two list
        for x in range(len(list1)):
            list1[x] *= list2[x]
        return list1
    def mult2D(list1: List[any], list2: List[any]) -> List[any]:  # multiplies two list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] *= list2[x][y]
        return list1
    def mult3D(list1: List[any], list2: List[any]) -> List[any]:  # multiplies two list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] *= list2[x][y][z]
        return list1
    def mult4D(list1: List[any], list2: List[any]) -> List[any]:  # multiplies two list
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] *= list2[x][y][z][w]
        return list1
    def div1D(list1: List[any], list2: List[any]) -> List[any]:  # divides two lists
        for x in range(len(list1)):
            list1[x] /= list2[x]
        return list1
    def div2D(list1: List[any], list2: List[any]) -> List[any]:  # divides two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] /= list2[x][y]
        return list1
    def div3D(list1: List[any], list2: List[any]) -> List[any]:  # divides two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] /= list2[x][y][z]
        return list1
    def div4D(list1: List[any], list2: List[any]) -> List[any]:  # divides two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] /= list2[x][y][z][w]
        return list1
    def sub1D(list1: List[any], list2: List[any]) -> List[any]:  # subtracts two lists
        for x in range(len(list1)):
            list1[x] -= list2[x]
        return list1
    def sub2D(list1: List[any], list2: List[any]) -> List[any]:  # subtracts two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] -= list2[x][y]
        return list1
    def sub3D(list1: List[any], list2: List[any]) -> List[any]:  # subtracts two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] -= list2[x][y][z]
        return list1
    def sub4D(list1: List[any], list2: List[any]) -> List[any]:  # subtracts two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] -= list2[x][y][z][w]
        return list1
    def add1D(list1: List[any], list2: List[any]) -> List[any]:  # adds two lists
        for x in range(len(list1)):
            list1[x] += list2[x]
        return list1
    def add2D(list1: List[any], list2: List[any]) -> List[any]:  # adds two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                list1[x][y] += list2[x][y]
        return list1
    def add3D(list1: List[any], list2: List[any]) -> List[any]:  # adds two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    list1[x][y][z] += list2[x][y][z]
        return list1
    def add4D(list1: List[any], list2: List[any]) -> List[any]:  # adds two lists
        for x in range(len(list1)):
            for y in range(len(list1[x])):
                for z in range(len(list1[x][y])):
                    for w in range(len(list1[x][y][z])):
                        list1[x][y][z][w] += list2[x][y][z][w]
        return list1
    def map1D(list: Union[List[float], List[int]], fromMin: Union[float, int], fromMax: Union[float, int], toMin: Union[float, int] = None, toMax: Union[float, int] = None) -> Union[List[float], List[int]]:  # changes the range of a 1d array of data (while keeping the detail of the numbers)
        if None in [toMin, toMax]:
            if toMin == None and toMax == None:
                toMin = fromMin
                toMax = fromMax
                fromMin = lists.min1D(list)
                fromMax = lists.max1D(list)
            else:
                raise SyntaxError("Invalid Input")
        for x in range(len(list)):
            list[x] -= fromMin
        
        scaler = pyMath.divide0((toMax - toMin), max(list))
        for x in range(len(list)):
            list[x] *= scaler
            list[x] += toMin
        
        return list
    def map2D(list: Union[List[float], List[int]], fromMin: Union[float, int], fromMax: Union[float, int], toMin: Union[float, int] = None, toMax: Union[float, int] = None) -> Union[List[float], List[int]]:  # changes the range of a 2d array of data (while keeping the detail of the numbers)
        if None in [toMin, toMax]:
            if toMin == None and toMax == None:
                toMin = fromMin
                toMax = fromMax
                fromMin = lists.min2D(list)
                fromMax = lists.max2D(list)
            else:
                raise SyntaxError("Invalid Input")
        maxOfList = []
        for x in range(len(list)):
            for y in range(len(list[x])):
                list[x][y] -= fromMin
            maxOfList.append(max(list[x]))
        
        maxOfList = max(maxOfList)
        scaler = pyMath.divide0((toMax - toMin), maxOfList)
        for x in range(len(list)):
            for y in range(len(list[x])):
                list[x][y] *= scaler
                list[x][y] += toMin
        
        return list
    def map3D(list: Union[List[float], List[int]], fromMin: Union[float, int], fromMax: Union[float, int], toMin: Union[float, int] = None, toMax: Union[float, int] = None) -> Union[List[float], List[int]]:  # changes the range of a 3d array of data (while keeping the detail of the numbers)
        if None in [toMin, toMax]:
            if toMin == None and toMax == None:
                toMin = fromMin
                toMax = fromMax
                fromMin = lists.min3D(list)
                fromMax = lists.max3D(list)
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
        
        scaler = scaler = pyMath.divide0((toMax - toMin), maxOfList)
        for x in range(len(list)):
            for y in range(len(list[x])):
                for z in range(len(list[x][y])):
                    list[x][y][z] *= scaler
                    list[x][y][z] += toMin
        
        return list
    def map4D(list: Union[List[float], List[int]], fromMin: Union[float, int], fromMax: Union[float, int], toMin: Union[float, int] = None, toMax: Union[float, int] = None) -> Union[List[float], List[int]]:  # changes the range of a 4d array of data (while keeping the detail of the numbers)
        if None in [toMin, toMax]:
            if toMin == None and toMax == None:
                toMin = fromMin
                toMax = fromMax
                fromMin = lists.min4D(list)
                fromMax = lists.max4D(list)
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
        
        scaler = pyMath.divide0((toMax - toMin), maxOfList)
        for x in range(len(list)):
            for y in range(len(list[x])):
                for z in range(len(list[x][y])):
                    for w in range(len(list[x][y][z])):
                        list[x][y][z][w] *= scaler
                        list[x][y][z][w] += toMin
        
        return list
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


#-----------------------------------------MATH FUNCTIONS FOR FLOATS AND INTAGERS-----------------------------------------

class pyMath:  # pyMath operations for non vectors (includes some functions from the pyMath library but also new ones like fract, mix, map 1D-4D, ect...)
    def worly(grid: List[vector3], scale: Union[float, int], x: Union[float, int], y: Union[float, int]) -> float:
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
    def crystal(grid: List[vector3], scale: Union[float, int], x: Union[float, int], y: Union[float, int]) -> float:
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
    def divideT(value1: Union[float, int], value2: Union[float, int]) -> float:  # divides and avoids divition by zero errors (when dividing by zero, returns numbers near infity)
        small_num = 0.00000000000000001
        return (value1 + small_num) / (value2 + small_num)
    def divide0(value1: Union[float, int], value2: Union[float, int]) -> Union[float, int]:  # divides two numbers but on divtion by zero returns 0 (the divide0 function will return numbers near to infinity this one wont)
        try:
            return value1 / value2
        except ZeroDivisionError:
            return 0.0
    def ceil(value: float) -> int:  # returns the ceiling of a number
        return math.ceil(value)
    def mix(value1: Union[float, int], value2: Union[float, int], percentage: float) -> float:  # mixes two numbers based on a number ranging from 1 - 0
        percentage = pyMath.clamp(percentage, 0, 1)
        return value1 * (1 - percentage) + value2 * percentage
    def tan(value: Union[float, int]) -> float:  # returns the tangent of a number
        return math.tan(value)
    def sin(value: Union[float, int]) -> float:  # returns the sign of a number
        return math.sin(value)
    def cos(value: Union[float, int]) -> float:  # returns the cosine of a number
        return math.cos(value)
    def fract(value: float) -> float:  # returns the decimal of the value
        return value - math.floor(value)
    def floor(value: float) -> int:  # returns the floor of the value
        return math.floor(value)
    def clamp(val: Union[float, int], min_: Union[float, int], max_: Union[float, int]) -> Union[float, int]:  # sets the max and min of a number
        return min(max(val, min_), max_)
    def sqrt(value: Union[float, int]) -> float:  # square root
        return math.sqrt(value)
    def map(val: Union[float, int], cMin: Union[float, int], cMax: Union[float, int], nMin: Union[float, int], nMax: Union[float, int]) -> float:  # mapping function
        nVal = val - cMin
        nVal *= pyMath.divide0((nMax - nMin), (cMax - cMin))
        nVal += nMin
        return nVal
    
    """
    
        from when I was making the the perlin noise inplementation, currently it uses splines (1d, 2d, 3d or 4d depending on the noises demention)

    def smooth1D(heights: Union[List[float], List[int]], smoothing: int = 100) -> List[float]:  # smooths a list of numbers making them more uniform/reducing spikes in numbers
        for s in range(smoothing):
            for i in range(len(heights)):
                if i not in [0, len(heights) - 1]:
                    height1 = heights[i - 1]
                    height3 = heights[i + 1]
                    heights[i] = (heights[i] * 0.1) + (height1 * 0.45) + (height3 * 0.45)
        return heights
    def interpalate3(h: Union[float, int], x: Union[float, int], list: Union[List[float], List[int]]) -> float:  # interpolates smoothly between 3 points (use the pyMath.smooth function to fixs small glitches)
        index2 = int(x / h)
        index1 = index2 - 1
        index3 = index2 + 1
        
        height1 = list[index1]
        height2 = list[index2]
        height3 = list[index3]
        
        #x1 = index1 * h
        x2 = index2 * h
        #x3 = index3 * h
        
        a0 = height2
        a1 = (height3 - height1) / (h * 2)
        a2 = (height1 - 2 * height2 + height3) / ((h ** 2) * 2)
        
        height_out = a0 + a1 * (x - x2) + a2 * (x - x2) ** 2
        
        return height_out
    def interpalate5(h: Union[float, int], x: Union[float, int], list: Union[List[float], List[int]]) -> float:  # interpolates smoothly between 5 points (use the pyMath.smooth function to fix glitches)
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
        
        #x1 = index1 * h
        #x2 = index2 * h
        x3 = index3 * h
        #x4 = index4 * h
        #x5 = index5 * h
        
        a0 = height3
        a1 = (height4 - height2) / (h * 2)
        a2 = (-height5 + 16 * height4 - 30 * height3 + 16 * height2 - height1) / (24 * (h ** 2))
        a3 = (height5 - 2 * height4 + 2 * height2 - height1) / (12 * (h ** 3))
        
        height = a0 + a1 * (x - x3) + a2 * (x - x3) ** 2 + a3 * (x - x3) ** 3
        
        return height
    """
    def smoothstep(x: Union[float, int]) -> float:  # a function to smoothly step between 0 and 1
        k = pyMath.clamp(x, 0, 1)
        return k ** 2 * (3 - 2 * k)
    def length(poses: Union[List[float], List[int]]) -> float:  # gets the distance of the imputed values (using the pythagorean theorem)
        squared = 0
        for point in poses:
            squared += point * point
        return math.sqrt(squared)
    def normalize(values: Union[List[float], List[int]]) -> List[float]:  # normalizes a list of values (for this function you need to put in the .xyz value of the Vector, the functions above do this for you)
        mag = pyMath.divide0(1, pyMath.length(values))  # gets the magnitude
        new_values = []
        for old_value in values:
            new_values.append(old_value * mag)  # changes the values by the magnitude
        return new_values
    def RGBtoKCMY(color: vec3) -> vec4:  # converts rgb to kcmy(paint color format)
        # Conversoin formula from: https://www.rapidtables.com/convert/color/rgb-to-cmyk.html
        G = pyMath.divide0(color.g, 255)
        B = pyMath.divide0(color.b, 255)
        R = pyMath.divide0(color.r, 255)
        
        k = 1 - max([R, G, B])
        c = pyMath.divide0((1 - R - k), (1 - k))
        m = pyMath.divide0((1 - G - k), (1 - k))
        y = pyMath.divide0((1 - B - k), (1 - k))
        
        return Vec4(k, c, m, y)


#-----------------------------------------GRADIENTS-----------------------------------------

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
        
        pointInSpace = pyMath.smoothstep(pyMath.divide0((point - p), distBetweenPoints))

        return pyMath.mix(color1, color2, pointInSpace)  # try using a smoothstep funciton to create a smoother change in gradient
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
        
        pointInSpace = (pyMath.divide0((point - p), distBetweenPoints))

        return pyMath.mix(color1, color2, pointInSpace)  # try using a smoothstep funciton to create a smoother change in gradient


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
        
        pointInSpace = pyMath.smoothstep(pyMath.divide0((point - p), distBetweenPoints))

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
        
        pointInSpace = (pyMath.divide0((point - p), distBetweenPoints))

        return mix(color1, color2, pointInSpace)


class gradient:  # a way to make gradients that specifies what they are being used for
    def color(maxGap = 50) -> colorGradient:  # gives you a color gradient
        return colorGradient(maxGap)
    def number(maxGap = 50) -> numberGradient:  # gives you a number gradient
        return numberGradient(maxGap)
    def vector(maxGap = 50) -> colorGradient:  # gives you a vector gradient
        return colorGradient(maxGap)


#-----------------------------------------NOISE FUNCTOINS-----------------------------------------

class noise:  # contains perlin noise functions that take in a list of random numbers thats the same dimention as the function, than the x, y, z, and w (only put the one that belong there for the demention of the function) and finaly the distance between points
    def perlin1D(noise: list, h, x) -> float:  # smoothly interpolates at a point between other points on a 1D list
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
    def perlin2D(noise_array: list, h, x, y) -> float:  # smoothly interpolates at a point between other points on a 2D list
        nx = x / h
        i = math.floor(nx)
        ty1 = noise.perlin1D(noise_array[i - 1], h, y)
        ty2 = noise.perlin1D(noise_array[i    ], h, y)
        ty3 = noise.perlin1D(noise_array[i + 1], h, y)
        ty4 = noise.perlin1D(noise_array[i + 2], h, y)
        return noise.perlin1D([ty1, ty2, ty3, ty4], h, (nx - i) * h + h)
    def perlin3D(noise_array: list, h, x, y, z) -> float:  # smoothly interpolates at a point between other points on a 3D list
        nx = x / h
        i = math.floor(nx)
        ty1 = noise.perlin2D(noise_array[i - 1], h, y, z)
        ty2 = noise.perlin2D(noise_array[i    ], h, y, z)
        ty3 = noise.perlin2D(noise_array[i + 1], h, y, z)
        ty4 = noise.perlin2D(noise_array[i + 2], h, y, z)
        return noise.perlin1D([ty1, ty2, ty3, ty4], h, (nx - i) * h + h)
    def perlin4D(noise_array: list, h, x, y, z, w) -> float:  # this is untested but should work and smoothly interpolates at a point between other points on a 4D list
        nx = x / h
        i = math.floor(nx)
        ty1 = noise.perlin3D(noise_array[i - 1], h, y, z, w)
        ty2 = noise.perlin3D(noise_array[i    ], h, y, z, w)
        ty3 = noise.perlin3D(noise_array[i + 1], h, y, z, w)
        ty4 = noise.perlin3D(noise_array[i + 2], h, y, z, w)
        return noise.perlin1D([ty1, ty2, ty3, ty4], h, (nx - i) * h + h)
    def ridge1D(randNoise: list, h, x) -> float:  # ridge noise aka perlin noise with abrupt ridges (like that of mountains)
        n = noise.perlin1D(randNoise, h, x)
        n = 1 - abs(n)
        return n
    def ridge2D(randNoise: list, h, x, y) -> float:
        n = noise.perlin2D(randNoise, h, x, y)
        n = 1 - abs(n)
        return n
    def ridge3D(randNoise: list, h, x, y, z) -> float:
        n = noise.perlin3D(randNoise, h, x, y, z)
        n = 1 - abs(n)
        return n
    def ridge4D(randNoise: list, h, x, y, z, w) -> float:
        n = noise.perlin4D(randNoise, h, x, y, z, w)
        n = 1 - abs(n)
        return n
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
        worlyNoise = pyMath.map2D(worlyNoise, minHeight, maxHeight)
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
        worlyNoise = pyMath.map2D(worlyNoise, minHeight, maxHeight)
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
        worlyNoise = pyMath.map3D(worlyNoise, minHeight, maxHeight)
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
                                nx = PointPos[0] + NX * scale.x
                                ny = PointPos[1] + NY * scale.y
                                nz = PointPos[2] + NZ * scale.z
                                distX = (nx - x) ** 2
                                distY = (ny - y) ** 2
                                distZ = (nz - z) ** 2
                                dists.append(distX + distY + distZ)
                    layer2.append(math.sqrt(min(dists)))
                layer.append(layer2)
            worlyNoise.append(layer)
        worlyNoise = pyMath.map3D(worlyNoise, minHeight, maxHeight)
        return worlyNoise
    def worly4D(size: Vec4, scale: float, minHeight: float = -1, maxHeight: float = 1) -> list:
        scale = Vec4(scale, scale, scale, scale)
        cells = ceil(size / scale)
        grid = []
        for x in range(cells.x + 2):
            layer = []
            for y in range(cells.y + 2):
                layer2 = []
                for z in range(cells.z + 2):
                    layer3 = []
                    for w in range(cells.w + 2):
                        layer3.append((random.uniform(0, scale.x), random.uniform(0, scale.y), random.uniform(0, scale.z), random.uniform(0, scale.w)))
                    layer2.append(layer3)
                layer.append(layer2)
            grid.append(layer)
        worlyNoise = []
        for x in range(size.x):
            layer = []
            for y in range(size.y):
                layer2 = []
                for z in range(size.z):
                    layer3 = []
                    for w in range(size.w):
                        cellPos = (x / scale.x, y / scale.y, z / scale.z, w / scale.w)
                        currentCell = (math.floor(cellPos[0]), math.floor(cellPos[1]), math.floor(cellPos[2]),  math.floor(cellPos[3]))
                        dists = []
                        for X in range(-1, 2):
                            for Y in range(-1, 2):
                                for Z in range(-1, 2):
                                    for W in range(-1, 2):
                                        NX = X + currentCell[0]
                                        NY = Y + currentCell[1]
                                        NZ = Z + currentCell[2]
                                        NW = W + currentCell[3]
                                        PointPos = grid[NX + 1][NY + 1][NZ + 1][NW + 1]
                                        nx = (X * scale.x) + PointPos[0] + currentCell[0] * scale.x
                                        ny = (Y * scale.y) + PointPos[1] + currentCell[1] * scale.y
                                        nz = (Z * scale.z) + PointPos[2] + currentCell[2] * scale.z
                                        nw = (W * scale.w) + PointPos[3] + currentCell[3] * scale.w
                                        distX = (nx - x) ** 2
                                        distY = (ny - y) ** 2
                                        distZ = (nz - z) ** 2
                                        distW = (nw - w) ** 2
                                        dists.append(distX + distY + distZ + distW)
                        layer3.append(math.sqrt(min(dists)))
                    layer2.append(layer3)
                layer.append(layer2)
            worlyNoise.append(layer)
        worlyNoise = pyMath.map4D(worlyNoise, minHeight, maxHeight)
        return worlyNoise


#-----------------------------------------GENERATING WHOLE ARRAYS OF 1-4 DIMENSTIONS-----------------------------------------

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
                        list[x] = pyMath.mix(noise.perlin1D(rNoise, octave[2], x), list[x], octave[4])
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
                        list[x] = pyMath.mix(noise.ridge1D(rNoise, octave[2], x), list[x], octave[4])
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
                            list[x][y] = pyMath.mix(noise.perlin2D(rNoise, octave[2], x, y), list[x][y], octave[4])
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
                            list[x][y] = pyMath.mix(noise.ridge2D(rNoise, octave[2], x, y), list[x][y], octave[4])
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
                                list[x][y][z] = pyMath.mix(noise.perlin3D(rNoise, octave[2], x, y, z), list[x][y][z], octave[4])
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
                                list[x][y][z] = pyMath.mix(noise.ridge3D(rNoise, octave[2], x, y, z), list[x][y][z], octave[4])
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
                                    list[x][y][z][w] = pyMath.mix(noise.perlin4D(rNoise, octave[2], x, y, z, w), list[x][y][z][w], octave[4])
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
                                    list[x][y][z][w] = pyMath.mix(noise.ridge4D(rNoise, octave[2], x, y, z, w), list[x][y][z][w], octave[4])
            return list
        else:
            raise TypeError("Invalid Fill Type. Please use \"constant\", \"random int\", \"random float\", \"perlin\" or \"ridge\"")


#-----------------------------------------A CLASS FOR READING AND WRITING PNG IMAGES AND TEXT FILES-----------------------------------------

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


#-----------------------------------------A CLASS FOR MANAGING THREADING-----------------------------------------

class PyThreading:  # to make threading easier
    class PyThread:
        def run() -> None:
            print('Please add a method called "run" to your class')
    # takes a set of functions and runs it over multiple threads as efficently as possible
    class __SpecialList:  # a private class to hold a list
        def __init__(self, l: List[any]) -> None:
            self.l = l
    def __ComputeObjects(objects: List[object], output: List[any], current_index: int) -> None:  # a private function to compute multiple objects (and store their data)
        i = current_index
        for ob in objects:
            output.l[i] = ob.run()
            i += 1
    def Disperse(batch: List[object], max_threads: int = 1024) -> List[any]:  # takes a list of objects (with a run method) and computes their outputs acrosse multiple threads
        length = len(batch)  # all the objects needing to be computed
        batch_size = length // max_threads  # the total threads for each batch size (not including over flow)
        extra_set = length % max_threads  # the extra set
        if batch_size == 0:  # removing extra sets
            max_threads = extra_set
        thread_sizes = []  # all the threads sizes
        for i in range(max_threads):
            thread_sizes.append(batch_size)
        for i in range(extra_set):  # adding on the extra set
            thread_sizes[i] += 1
        threads = []  # the threads
        ar = []
        for i in range(length):
            ar.append(None)
        output = PyThreading.__SpecialList(ar)  # the output of the objects
        i = 0
        for bs in thread_sizes:  # looping through all the batches
            thread_layer = []
            old_i = i
            for ei in range(bs):  # finding all items in the batch
                thread_layer.append(batch[i])
                i += 1
            thread = threading.Thread(target = PyThreading.__ComputeObjects, args = (thread_layer, output, old_i, ))  # creating a thread for it
            thread.daemon = True
            thread.start()  # running the thread
            threads.append(thread)
        for thread in threads:  # joinging the threads
            thread.join()
        return output.l  # returning the output

