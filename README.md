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

> *vec2*
> Stores an x and y position
> *vec3*
> Stores an x, y and z position
> *vec4*
> Stores an x, y, z and w position
> *cos*
returns the cosine of a vector
> *sin*
returns the sin of a vector
> *tan*
returns the tangent of a vector
> *clamp*
clamps a vector between a minimum and maximum
> *normalize*
normalizes a vector
> *mix*
mixes two vectors based on a float
> *Int*
makes the numebrs of a vector whole
> *floor*
returns the floor of a vector
> *fract*
returns the decimal value of a vector
> *dot*
returns the dot product of a vector
> *length*
returns the length/distance of a vector
> *lengthOfList*
returns the length/dist of a list
> *normalizeList*
normalizes a list
> *math*
    > *cos*
    > returns te cosine of a number
    > *sin*
    > returns the sin of a number
    > *tan*
    > returns the tangent of a number
    > *mix*
    > mixes two numbers based on a float
    > *clamp*
    > clamps a number between a minimum and maximum
    > *fract*
    > returns the decimal value of number
    > *floor*
    > returns the floor of a number
    > *sqrt*
    > returns the square root of a number
> *dists*
    > *distToCircularPoint*
    > returns the distance to a circle/sphere/hypersphere
    > *distToPoint*
    > returns the distance to a point
