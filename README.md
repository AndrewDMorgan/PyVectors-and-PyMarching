# Vector Types in Python3 + More

The first package, PyVectors allows for vec2, vec3 and vec4 types in python3. It also overloads the math operators to allow easy math show as the following:

    vector1,vector2,vector3 = vec3(1, 3, 5),vec3(2, 8, 3),vec3(1, 5, 3)
    vector1 += vector2 / vector3

Instead of:

    vector1,vector2,vector3 = [1, 3, 5],[2, 8, 3],[1, 5, 3]
    vector1 = [vector1[0] + (vector2[0] / vector3[0]), vector1[1] + (vector2[1] / vector3[1]), vector1[2] + (vector2[2] / vector3[2])]

To import and use this package, you want to do the following:

    from PyVectors import *

The functions are as following with their descriptions:

## *vec2*
 Stores an x and y position
 Takes an input of x or x and y
## *vec3*
 Stores an x, y and z position
 takes an inout of x or x, y and z
## *vec4*
 Stores an x, y, z and w position
 takes an input of x or x and y or x, y, z, and w
## *cos*
 returns the cosine of a vector
 takes an input of a vector
## *sin*
 returns the sin of a vector
 takes an input of a vector
## *tan*
 returns the tangent of a vector
 takes an input of a vector
## *clamp*
 clamps a vector between a minimum and maximum
 takes an input of a vector, minimum and maximum
## *normalize*
 normalizes a vector
 takes an input of a vector
## *mix*
 mixes two vectors based on a float
 takes an input of two vectors and a float (0 - 1)
## *Int*
 makes the numebrs of a vector whole
 takes an input of a vector
## *floor*
 returns the floor of a vector
 takes an input of a vector
## *fract*
 returns the decimal value of a vector
 takes an input of a vector
## *dot*
 returns the dot product of a vector
 takes an input of two vectors
## *length*
 returns the length/distance of a vector
 takes an input of a vector
## *lengthOfList*
 returns the length/dist of a list
 takes an input of a list
## *normalizeList*
 normalizes a list
 takes an input of a list
## *math*
 > ## *cos*
  > returns te cosine of a number
  > takes an input of a number
 > ## *sin*
  > returns the sin of a number
  > takes an input of a number
 > ## *tan*
  > returns the tangent of a number
  > takes an input of a number
 > ## *mix*
  > mixes two numbers based on a float
  > takes an input of two numbers and a float (0 - 1)
 > ## *clamp*
  > clamps a number between a minimum and maximum
  > takes an input of a number, minimum and maximum
 > ## *fract*
  > returns the decimal value of number
  > takes an input of a number
 > ## *floor*
  > returns the floor of a number
  > takes an input of a number
 > ## *sqrt*
  > returns the square root of a number
  > takes an input of a number
## *dists*
 > ## *distToCircularPoint*
  > returns the distance to a circle/sphere/hypersphere
  > takes an input of two vectors and a radius
 > ## *distToPoint*
  > returns the distance to a point
  > takes an input of two vectors

More will be coming to this package even possibly a vec5 type. I'm also working on making it as quick and easy to write and complie/run. For more information, go to [repl.it](https://repl.it/talk/share/Vector-Types-in-Python3/83032) to see an example of PyVectors in use and how to use it.
