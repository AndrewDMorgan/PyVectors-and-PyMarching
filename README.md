# Vector Types in Python3 + More

The first package, PyVectors allows for vec2, vec3 and vec4 types in python3. It also overloads the math operators to allow easy math show as the following:

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
 ## *lengthOfList*
 Returns the length/dist of a list. Takes an input of a list
 ## *normalizeList*
 Normalizes a list. Takes an input of a list
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
 ## *dists.*
   > ## *distToCircularPoint*
   > Returns the distance to a circle/sphere/hypersphere. Takes an input of two vectors and a radius
   > ## *distToPoint*
   > Returns the distance to a point. Takes an input of two vectors

More will be coming to this package even possibly a vec5 type. I'm also working on making it as quick and easy to write and complie/run. For more information, go to [repl.it](https://repl.it/talk/share/Vector-Types-in-Python3/83032) to see an example of PyVectors in use and how to use it.

**_____________________________________________________________________________________________________________**

The second package is PyMarching. PyMarching is a sub package of PyVectors meaning you need PyVectors to run PyMarching. PyMarching is a basic ray marcher that allows you to cast a ray and return information on the collition. It currently only allows for flat infinite planes and sphere but more shapes are being added. It also is very basic but is going to be improved to be a much more advanced ray marcher. To import it you want to do the following:

    from PyMarching import *

And to add objects to your world do the following:

    object.addSphere(vec3(1, 2, 3), 1.25, vec3(255, 0, 0))
    object.addInfFlatPlain(0, vec3(0, 0, 255))

To cast a ray do the following:

    march.ray(vec3(0, 0, 1), vec3(0))

The functions and classes and their details are as following:

 ## *object*
   > ## *addSphere*
   > Adds an sphere to the world. Takes in a pos, radius and color
   > ## *addInfFlatPlain*
   > Adds a infinite flat plane to the world. Takes in a height and color
 ## *march*
   > ## *ray*
   > Cast a ray and returns collition data. Takes in a direction and start position. You can also change the max_steps, min_depth and max_dist
   > ## *getDist*
   > Returns the distance to the closet object. Takes in a positio

There are no examples of this yet.
