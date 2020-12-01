import math as Math  # imports the math library to add cos, sin, sqrt, ect...
 

def divide(value1, value2):  # divides and returns 0 on division by zero error
    try:
        return value1 / value2
    except ZeroDivisionError:
        return 0

 
class vec4:  # this function stores and operates an a tuple/list containing four items (class functions gone over in the vec2 class)
    def __init__(self, x=None, y=None, z=None, w=None):
        if None in [x, y, z, w]:
            if x == None:
                raise SyntaxError("Position is undefined, please put an x or an x and y or an x, y, z, and w")
            elif y == None:
                y = x
                z = x
                w = x
            elif z == None:
                z = x
                w = y
            elif w == None:
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
        return vec4(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)
    def __sub__(self, other):
        return vec4(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)
    def __mul__(self, other):
        return vec4(self.x * other.x, self.y * other.y, self.z * other.z, self.w * other.w)
    def __truediv__(self, other):
        return vec4(divide(self.x, other.x), divide(self.y, other.y), divide(self.z, other.z), divide(self.w, other.w))
    def __floordiv__(self, other):
        return vec4(self.x//other.x, self.y//other.y, self.z//other.z, self.w//other.w)
    def __mod__(self, other):
        return vec4(self.x%other.x, self.y%other.y, self.z%other.z, self.w%other.w)
    def __pow__(self, other):
        return vec4(self.x**other.x, self.y**other.y, self.z**other.z, self.w**other.w)
    def __rshift__(self, other):
        return vec4(self.x>>other.x, self.y>>other.y, self.z>>other.z, self.w>>other.w)
    def __lshift__(self, other):
        return vec4(self.x<<other.x, self.y<<other.y, self.z<<other.z, self.w<<other.w)
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
        return vec4(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)
    def __iadd__(self, other):
        return vec4(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)
    def __imult__(self, other):
        return vec4(self.x * other.x, self.y * other.y, self.z * other.z, self.w * other.w)
    def __idiv__(self, other):
        return vec4(divide(self.x, other.x), divide(self.y, other.y), divide(self.z, other.z), divide(self.w, other.w))
    def __ifloordiv__(self, other):
        return vec4(self.x//other.x, self.y//other.y, self.z//other.z, self.w//other.w)
    def __imod__(self, other):
        return vec4(self.x%other.x, self.y%other.y, self.z%other.z, self.w%other.w)
    def __ipow__(self, other):
        return vec4(self.x**other.x, self.y**other.y, self.z**other.z, self.w**other.w)
    def __irshift__(self, other):
        return vec4(self.x >> other.x, self.y >> other.y, self.z >> other.z, self.w >> other.w)
    def __ilshift__(self, other):
        return vec4(self.x << other.x, self.y << other.y, self.z << other.z, self.w << other.w)
    def __neg__(self):
        return vec4(-self.x, -self.y, -self.z, -self.w)
    def __pos__(self, other):
        return vec4(+self.x, +self.y, +self.z, +self.w)
    def __abs__(self):
        return vec4(abs(self.x), abs(self.y), abs(self.z), abs(self.w))
    def __str__(self):
        return 'vec4(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ', ' + str(self.w) + ')'
    def mix(self, other, percentage):
        return vec4(math.mix(self.x, other.x, percentage), math.mix(self.y, other.y, percentage), math.mix(self.z, other.z, percentage), math.mix(self.w, other.w, percentage))
    def clamp(self, min_, max_):
        return vec4(math.clamp(self.x, min_, max_), math.clamp(self.y, min_, max_), math.clamp(self.z, min_, max_), math.clamp(self.w, min_, max_))
    def sqrt(self):
        return vec4(math.sqrt(self.x), math.sqrt(self.y), math.sqrt(self.z), math.sqrt(self.w))
    def tan(self):
        return vec4(math.tan(self.x), math.tan(self.y), math.tan(self.z), math.tan(self.w))
    def sin(self):
        return vec4(math.sin(self.x), math.sin(self.y), math.sin(self.z), math.sin(self.w))
    def cos(self):
        return vec4(math.cos(self.x), math.cos(self.y), math.cos(self.z), math.cos(self.w))
    def length(self):
        return lengthOfList(self.xyzw)
    def floor(self):
        return vec4(math.floor(self.x), math.floor(self.y), math.floor(self.z), math.floor(self.w))
    def fract(self):
        return vec4(math.fract(self.x), math.fract(self.y), math.fract(self.z), math.fract(self.w))
    def __len__(self):
        return 4
    def __getitem__(self, key):
        return self.xyzw[key]
 
 
class vec3:  # this function stores and operates an a tuple/list containing three items (class functions gone over in the vec2 class)
    def __init__(self, x=None, y=None, z=None):
        if None in [x, y, z]:
            if x == None:
                raise SyntaxError("Position is undefined, please put an x or an x, y and z")
            elif y == None:
                y = x
                z = x
            elif z == None:
                raise SyntaxError("Requires more information, please put an x or an x, y and z")
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
        return vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        return vec3(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, other):
        return vec3(self.x * other.x, self.y * other.y, self.z * other.z)
    def __truediv__(self, other):
        return vec3(divide(self.x, other.x), divide(self.y, other.y), divide(self.z, other.z))
    def __floordiv__(self, other):
        return vec3(self.x//other.x, self.y//other.y, self.z//other.z)
    def __mod__(self, other):
        return vec3(self.x%other.x, self.y%other.y, self.z%other.z)
    def __pow__(self, other):
        return vec3(self.x**other.x, self.y**other.y, self.z**other.z)
    def __rshift__(self, other):
        return vec3(self.x>>other.x, self.y>>other.y, self.z>>other.z)
    def __lshift__(self, other):
        return vec3(self.x<<other.x, self.y<<other.y, self.z<<other.z)
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
        return vec3(self.x - other.x, self.y - other.y, self.z - other.z)
    def __iadd__(self, other):
        return vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    def __imult__(self, other):
        return vec3(self.x * other.x, self.y * other.y, self.z * other.z)
    def __idiv__(self, other):
        return vec3(divide(self.x, other.x), divide(self.y, other.y), divide(self.z, other.z))
    def __ifloordiv__(self, other):
        return vec3(self.x//other.x, self.y//other.y, self.z//other.z)
    def __imod__(self, other):
        return vec3(self.x%other.x, self.y%other.y, self.z%other.z)
    def __ipow__(self, other):
        return vec3(self.x**other.x, self.y**other.y, self.z**other.z)
    def __irshift__(self, other):
        return vec3(self.x >> other.x, self.y >> other.y, self.z >> other.z)
    def __ilshift__(self, other):
        return vec3(self.x << other.x, self.y << other.y, self.z << other.z)
    def __neg__(self):
        return vec3(-self.x, -self.y, -self.z)
    def __pos__(self, other):
        return vec3(+self.x, +self.y, +self.z)
    def __abs__(self):
        return vec3(abs(self.x), abs(self.y), abs(self.z))
    def __str__(self):
        return 'vec3(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.z) + ')'
    def mix(self, other, percentage):
        return vec3(math.mix(self.x, other.x, percentage), math.mix(self.y, other.y, percentage), math.mix(self.z, other.z, percentage))
    def clamp(self, min_, max_):
        return vec3(math.clamp(self.x, min_, max_), math.clamp(self.y, min_, max_), math.clamp(self.z, min_, max_))
    def sqrt(self):
        return vec3(math.sqrt(self.x), math.sqrt(self.y), math.sqrt(self.z))
    def tan(self):
        return vec3(math.tan(self.x), math.tan(self.y), math.tan(self.z))
    def cross(self, other):  # returns the cross product of two vectors
        val1 = (self.y * other.z) - (self.z * other.y)
        val2 = (self.z * other.x) - (self.x * other.z)
        val3 = (self.x * other.y) - (self.y * other.x)
        return vec3(val1, val2, val3)
    def sin(self):
        return vec3(math.sin(self.x), math.sin(self.y), math.sin(self.z))
    def cos(self):
        return vec3(math.cos(self.x), math.cos(self.y), math.cos(self.z))
    def length(self):
        return lengthOfList(self.xyz)
    def floor(self):
        return vec3(math.floor(self.x), math.floor(self.y), math.floor(self.z))
    def fract(self):
        return vec3(math.fract(self.x), math.fract(self.y), math.fract(self.z))
    def __len__(self):
        return 3
    def __getitem__(self, key):
        return self.xyz[key]
 
 
class vec2:  # this function stores and operates an a tuple/list containing two items
    def __init__(self, x=None, y=None):  # initializing the tuple/list
        if None in [x, y]:  # filling in the empty places of the vector
            if x == None:
                raise SyntaxError("Position is undefined, please put an x or an x and y")
            elif y == None:
                y = x
        # defining the values of the vector
        self.x = x
        self.y = y
        self.z = 0
        self.w = 0
        self.xy = [x, y]
        
        self.r = x
        self.g = y
        self.rg = [x, y]
    def __add__(self, other):  # adding two list like vector1 + vector2
        return vec2(self.x + other.x, self.y + other.y)
    def __sub__(self, other):  # subtracting two vectors like vector1 - vector2
        return vec2(self.x - other.x, self.y - other.y)
    def __mul__(self, other):  # multiplying two vectors like vector1 * vector2
        return vec2(self.x * other.x, self.y * other.y)
    def __truediv__(self, other):  # divides two vectors like vector1 / vector2
        return vec2(divide(self.x, other.x), divide(self.y, other.y))
    def __floordiv__(self, other):  # divides two vectors and returns the int of the division like vector1 // vector2
        return vec2(self.x//other.x, self.y//other.y)
    def __mod__(self, other):  # gets the mod of two vectors like vector1 % vector2
        return vec2(self.x%other.x, self.y%other.y)
    def __pow__(self, other):  # gets the power of two vectors like vector1 ** vector2
        return vec2(self.x**other.x, self.y**other.y)
    def __rshift__(self, other):  # bit shifts to the right like vector1 >> vector2
        return vec2(self.x>>other.x, self.y>>other.y)
    def __lshift__(self, other):  # bit shifts to the left like vector1 << vector2
        return vec2(self.x<<other.x, self.y<<other.y)
    def __lt__(self, other):  # compares two vectors magnitudes/dot products like vector1 < vector2
        dot1 = (self.x * self.x) + (self.y * self.y)
        dot2 = (other.x * other.x) + (other.y * other.y)
        if dot1 < dot2:
            return True
        else:
            return False
    def __gt__(self, other):  # compares two vectors magnitudes/dot products like vector1 > vector2
        dot1 = (self.x * self.x) + (self.y * self.y)
        dot2 = (other.x * other.x) + (other.y * other.y)
        if dot1 > dot2:
            return True
        else:
            return False
    def __le__(self, other):  # compares two vectors magnitudes/dot products like vector1 <= vector2
        dot1 = (self.x * self.x) + (self.y * self.y)
        dot2 = (other.x * other.x) + (other.y * other.y)
        if dot1 <= dot2:
            return True
        else:
            return False
    def __ge__(self, other):  # compares two vectors magnitudes/dot products like vector1 >= vector2
        dot1 = (self.x * self.x) + (self.y * self.y)
        dot2 = (other.x * other.x) + (other.y * other.y)
        if dot1 >= dot2:
            return True
        else:
            return False
    def __eq__(self, other):  # checks if two vectors are equal like vector1 == vector2
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False
    def __ne__(self, other):
        if self.x != other.x and self.y != other.y:  # checks if the vectors are not equal like vector1 != vector2
            return True
        else:
            return False
    def __isub__(self, other):  # subtracts a vector from another vector by using vector1 -= vector2
        return vec2(self.x - other.x, self.y - other.y)
    def __iadd__(self, other):  # adds two vectors by using vector1 += vector2
        return vec2(self.x + other.x, self.y + other.y)
    def __imult__(self, other):  # multiples the vector by another vector by putting vector1 *= vector2
        return vec2(self.x * other.x, self.y * other.y)
    def __idiv__(self, other):  # returns the vector divided by another vector by puting vector1 /= vector2
        return vec2(divide(self.x, other.x), divide(self.y, other.y))
    def __ifloordiv__(self, other):  # gets the int of the divided product by using vector1 //= vector2
        return vec2(self.x//other.x, self.y//other.y)
    def __imod__(self, other):  # gets the mod of the vector and another vector using vector1 %= vector2
        return vec2(self.x%other.x, self.y%other.y)
    def __ipow__(self, other):  # puts the vector to the power of another vector using vector1 **= vector2
        return vec2(self.x**other.x, self.y**other.y)
    def __irshift__(self, other):  # bit shifts to the right by using >>=
        return vec2(self.x >> other.x, self.y >> other.y)
    def __ilshift__(self, other):  # bit shifts to the left by using <<=
        return vec2(self.x << other.x, self.y << other.y)
    def __neg__(self):  # makes the vector negative when you use -vector
        return vec2(-self.x, -self.y)
    def __pos__(self, other):  # makes the vector positive when you use +vector
        return vec2(+self.x, +self.y)
    def __abs__(self):  # returns the absolute value of the vector when you use abs()
        return vec2(abs(self.x), abs(self.y))
    def __str__(self):  # this function makes it return the position as a string when printing (using the print("text") in python) the vector
        return 'vec2(' + str(self.x) + ', ' + str(self.y) + ')'
    def mix(self, other, percentage):  # mixes the vector with another vector based on a percentage
        return vec2(math.mix(self.x, other.x, percentage), math.mix(self.y, other.y, percentage))
    def clamp(self, min_, max_):  # clamps the vector
        return vec2(math.clamp(self.x, min_, max_), math.clamp(self.y, min_, max_))
    def sqrt(self):  # returns the square root of the vector
        return vec2(math.sqrt(self.x), math.sqrt(self.y))
    def tan(self):  # returns the tangent of the vector
        return vec2(math.tan(self.x), math.tan(self.y))
    def sin(self):  # returns the sign of the vector
        return vec2(math.sin(self.x), math.sin(self.y))
    def cos(self):  # returns the cosine of the vector
        return vec2(math.cos(self.x), math.cos(self.y))
    def length(self):  # gets the length of the vector (length(vector) also works)
        return lengthOfList(self.xy)
    def floor(self):  # gets the floor of the vector
        return vec2(math.floor(self.x), math.floor(self.y))
    def fract(self):  # gets the decimal value of the number
        return vec2(math.fract(self.x), math.fract(self.y))
    def __len__(self):  # returns the length of the vector when you use the len() function
        return 2
    def __getitem__(self, key):
        return self.xy[key]


def getPos(vector, indexes):
    new_list = []
    for i in indexes:
        new_list.append(vector[i])
    
    return new_list


def Int(vector):
    return floor(vector)


def clamp(vector, min_, max_):
    return vector.clamp(min_, max_)


def fract(vector):
    return vector.fract()


def sqrt(vector):
    return vector.sqrt()


def floor(vector):
    return vector.floor()


def cos(vector):
    return vector.cos()


def sin(vector):
    return vector.sin()


def tan(vector):
    return vector.tan()


def normalize(vector):
    mag = length(vector)
    return vector / vec4(mag)


def length(vector):  # gets the length of a vector (using the pythagorean theorem)
    return vector.length()


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
        try:
            return Math.sqrt(value)
        except ValueError:
            return value


def lengthOfList(poses):  # gets the distance of the imputed values (using the pythagorean theorem)
    dist = poses[0]
    for vector in poses:
        dist = math.sqrt((dist * dist) + (vector * vector))
    return dist


def normalizeList(values):  # normalizes a list of values (for this function you need to put in the .xyz value of the vector, the functions above do this for you)
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


spheres = []
planes = []


class object:
    def addSphere(pos, r, col):
        global spheres
        spheres.append([pos, r, col])
    def addInfFlatPlain(height, col):
        global planes
        planes.append([height, col])


class march:
    def ray(rd, o, max_steps = 100, min_depth = 0.1, max_dist = 100):
        dfo = 0
        for steps in range(max_steps):
            pos = (rd * vec3(dfo)) + o
            
            data = march.getDist(pos)
            
            min_dist = data.x
            col = data.y
            
            dfo += min_dist
            
            if min_dist < min_depth or dfo > max_dist:
                break
        
        return vec2(dfo, col)
    def getDist(pos):
        object_colors = []
        dist_to_objects = []
        for sphere in spheres:
            dist_to_objects.append(dists.distToCircularPoint(pos, sphere[0], sphere[1]))
            object_colors.append(sphere[2])
        
        for plane in planes:
            dist_to_objects.append(pos.y - plane[0])
            object_colors.append(plane[1])
        
        min_dist = min(dist_to_objects)
        col = object_colors[dist_to_objects.index(min_dist)]
        return vec2(min_dist, col)

