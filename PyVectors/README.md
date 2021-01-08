# Vector Types in Python3 + More

PyVectors allows for vec2, vec3 and vec4 types in python3. It also overloads the math operators to allow easy math show as the following:

    vector1,vector2,vector3 = vec3(1, 3, 5),vec3(2, 8, 3),vec3(1, 5, 3)
    vector1 += vector2 / vector3

Instead of:

    vector1,vector2,vector3 = [1, 3, 5],[2, 8, 3],[1, 5, 3]
    vector1 = [vector1[0] + (vector2[0] / vector3[0]), vector1[1] + (vector2[1] / vector3[1]), vector1[2] + (vector2[2] / vector3[2])]

To import and use this package, you want to do the following:

    from PyVectors import *

The functions and classes are as following with their descriptions:

 ## *vec2*
 Stores an x and y position. Takes an input of x or x and y
 ## *vec3*
 Stores an x, y and z position. Takes an inout of x or x, y and z
 ## *vec4*
 Stores an x, y, z and w position. Takes an input of x or x and y or x, y, z, and w
 ## *cos*
 Returns the cosine of a vector. Takes an input of a vector
 ## *sin*
 Returns the sin of a vector. Takes an input of a vector
 ## *tan*
 Returns the tangent of a vector. Takes an input of a vector
 ## *clamp*
 Clamps a vector between a minimum and maximum. Takes an input of a vector, minimum and maximum
 ## *normalize*
 Normalizes a vector. Takes an input of a vector
 ## *mix*
 Mixes two vectors based on a float. Takes an input of two vectors and a float (0 - 1)
 ## *Int*
 Makes the numebrs of a vector whole. Takes an input of a vector
 ## *floor*
 Returns the floor of a vector. Takes an input of a vector
 ## *fract*
 Returns the decimal value of a vector. Takes an input of a vector
 ## *dot*
 Returns the dot product of a vector. Takes an input of two vectors
 ## *length*
 Returns the length/distance of a vector. Takes an input of a vector
 ## *math.*
   > ## *cos*
   > Returns te cosine of a number. Takes an input of a number
   > ## *sin*
   > Returns the sin of a number. Takes an input of a number
   > ## *tan*
   > Returns the tangent of a number. Takes an input of a number
   > ## *mix*
   > Mixes two numbers based on a float. Takes an input of two numbers and a float (0 - 1)
   > ## *clamp*
   > Clamps a number between a minimum and maximum. Takes an input of a number, minimum and maximum
   > ## *fract*
   > Returns the decimal value of number. Takes an input of a number
   > ## *floor*
   > Returns the floor of a number. Takes an input of a number
   > ## *sqrt*
   > Returns the square root of a number. Takes an input of a number
   > ## *lengthOfList*
   > Returns the length/dist of a list. Takes an input of a list
   > ## *normalizeList*
   > Normalizes a list. Takes an input of a list
   > ## *map1D*
   > Scales/streches a 1D list of numbers to a new range of numbers. Takes an input of a list, min of list, max of list, new min, new max
   > ## *map2D*
   > Scales/streches a 2D list of numbers to a new range of numbers. Takes an input of a list, min of list, max of list, new min, new max
   > ## *map3D*
   > Scales/streches a 3D list of numbers to a new range of numbers. Takes an input of a list, min of list, max of list, new min, new max
   > ## *map4D*
   > Scales/streches a 4D list of numbers to a new range of numbers. Takes an input of a list, min of list, max of list, new min, new max
   > ## *smooth*
   > makes the numebrs in a list more uniform/smooth and less spiky. Takes an input of a list and the number of soothing itterations
   > ## *interplate2*
   > linearly interplates between two points based on a point inbetween. takes and input of the distance between points (a single number), the position inbetween numbers and a list of the two points
   > ## *interplate3*
   > non linearly interplates between three points. Takes an input of the distance between points, the position in between points and the points (the points list can be infinitly long and it will hash for the two points around the given point)
   > ## *interplate5*
   > non linearly interplates between five points. Takes an input of the distance between points, the position in between points and the points (the points list can be infinitly long and it will hash for the two points around the given point)
   > ## *smoothstep*
   > smoothly steps from 0 - 1. Takes an input of the position between points, point1 and point2
   > ## *spline1D*
   > splines on a 1D level between two points in a list that surround the given position. Takes an input of a list of values to spline, the position between points (x) and the distance between points
   > ## *spline2D*
   > splines on a 2D level between two points in a list that surround the given position. Takes an input of a list of values to spline, the position between points (x, y) and the distance between points
   > ## *spline3D*
   > splines on a 3D level between two points in a list that surround the given position. Takes an input of a list of values to spline, the position between points (x, y, z) and the distance between points
   > ## *spline4D*
   > splines on a 4D level between two points in a list that surround the given position. Takes an input of a list of values to spline, the position between points (x, y, z, w) and the distance between points
   > ## *min1D*
   > gets the min of a 1D array. Takes in a list
   > ## *min2D*
   > gets the min of a 2D array. Takes in a list
   > ## *min3D*
   > gets the min of a 3D array. Takes in a list
   > ## *min4D*
   > gets the min of a 4D array. Takes in a list
   > ## *max1D*
   > gets the max of a 1D array. Takes in a list
   > ## *max2D*
   > gets the max of a 2D array. Takes in a list
   > ## *max3D*
   > gets the max of a 3D array. Takes in a list
   > ## *max4D*
   > gets the max of a 4D array. Takes in a list
 ## *dists.*
   > ## *distToCircularPoint*
   > Returns the distance to a circle/sphere/hypersphere. Takes an input of two vectors and a radius
   > ## *distToPoint*
   > Returns the distance to a point. Takes an input of two vectors
## *gradient*
   > ## *color*
   > returns a color gradient. Can take ina max gap (the defult is 50)
   > ## *number*
   > returns a number gradient. Can take ina max gap (the defult is 50)
   > ## *vector*
   > returns a vector gradient. Can take ina max gap (the defult is 50)
## *numberGradient*
   > ## *add*
   > adds a point to the gradient. Takes in a point and number
   > ## *grade*
   > returns the value at the inputed position. Takes in a point
## *colorGradient*
   > ## *add*
   > adds a point of color to the gradient. Takes in a point and color
   > ## *grade*
   > returns the color at a position (not working perfectly yet). Takes in a position in the gradient
## *noise*
   > ## *perlin1D*
   > gives a height based on a 1D list of noise and based on a position. Takes and input of random noise, distance between points and the x position
   > ## *perlin2D*
   > gives a height based on a 2D list of noise and based on a position. Takes and input of random noise, distance between points and the x, y position
   > ## *perlin3D*
   > gives a height based on a 3D list of noise and based on a position. Takes and input of random noise, distance between points and the x, y, z position
   > ## *perlin4D*
   > gives a height based on a 4D list of noise and based on a position (The 4D noise hasnt been tested but should work). Takes and input of random noise, distance between points and the x, y, z, w position
   > ## *ridge1D*
   > gives a height based on a 1D list of noise and based on a position and generates with noticable ridges. Takes and input of random noise, distance between points and the x position
   > ## *ridge2D*
   > gives a height based on a 2D list of noise and based on a position and generates with noticable ridges. Takes and input of random noise, distance between points and the x, y position
   > ## *ridge3D*
   > gives a height based on a 3D list of noise and based on a position and generates with noticable ridges. Takes and input of random noise, distance between points and the x, y, z position
   > ## *ridge4D*
   > gives a height based on a 4D list of noise and based on a position and generates with noticable ridges (The 4D noise hasnt been tested but should work). Takes and input of random noise, distance between points and the x, y, z, w position
## *array*
returns a filled in array that can be constant, random int, random float or perlin. Takes in a size (vec2, vec3, vec4, tuple and lists work), the type of fill (constant, random int, random float or perlin) and the data for the type in a list, vector or tuple (constant; number (not in list), random int; min, max, random float; min, max, perlin; list of octaves (min 1 octave max inf octaves) each being the following; min, max, distance between points, type (add, sub or mix), if using mix then add the percentage (0 - 1) to mix by, ridge; same as perlin but is ridge noise meaning theres a buch of ridges but still veriation (abs(perlin noise) * -1 = ridge noise))
## *png*
   > ## *fromArray*
   > creates a png from a 2D list of rgb values (a vec3). Takes in a 2d list of vec3's (or vec4's) and an image name (with .png at the end)
   > ## *getArray*
   > returns an array of vec4's (rgba) from a png image. Takes in an image (with .png)

More will be coming to this package even possibly a vec5 type. I'm also working on making it as quick and easy to write and complie/run. For more information, go to [repl.it](https://repl.it/talk/share/Vector-Types-in-Python3/83032) to see an example of PyVectors in use and how to use it. Just note that the example dose not have all the new functions and classes.
