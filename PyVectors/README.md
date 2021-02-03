# Vector Types And More In Python3

# *General Features:*

### PyVectors allows for vec2, vec3 and vec4 types in python3. It also overloads the math operators to allow you to easily do math with vectors show as the following:

    vector1,vector2,vector3 = vec3(1, 3, 5),vec3(2, 8, 3),vec3(1, 5, 3)
    vector1 += vector2 / vector3

### Instead of:

    vector1,vector2,vector3 = [1, 3, 5],[2, 8, 3],[1, 5, 3]
    vector1 = [vector1[0] + (vector2[0] / vector3[0]), vector1[1] + (vector2[1] / vector3[1]), vector1[2] + (vector2[2] / vector3[2])]

### It also works a list and can be used in pygame (and other librarys) instead of using lists. An example of this is the following:

    point = vec2(1, 5)
    size = vec2(5)
    pygame.draw.rect(displaySurface, vec3(255, 255, 0), vec4(point, size))

### instead of:

    point = [1, 5]
    size = [5, 5]
    pygame.draw.rect(displaySurface, [255, 255, 0], [point[0], point[1], size[0], size[1]])

### PyVectors also allows math to be done with different types of vectors. This is shown as the following (all the vector types can do this with any of the other vector types):

    v1 = vec2(5)
    v2 = vec4(2)
    v3 = v2 + v1  # creates a vec4 of v2.xyzw + vec4(v1.x, v1.y, 0, 0)  (Note that the code after the "#" will not work but is shown as an example of what it dose)
    v4 = v1 + v2  # creates a vec2 of v1.xy + v2.xy  (Note that the code after the "#" will not work but is shown as an example of what it dose)

### To import and use this package, you want to do the following (to do this, have the PyVectors python file in the same directory as the current script your using is):

    from PyVectors import *

# *Planned Features:*

 ## *A Way To Delete txt And png Files*
  > This function will be under the txt and png class named as remove taking in a file name (with .png or .txt)
 ## *Have The Perlin Noise Generator Under The Array Class Not Generate Extra Numbers (a bug fix)*
  > This will not affect the perlin noise, it will just make it run quicker as it dosent have to generate unused random numbers (there are thousands of extra numbers and generating and creating random numbers in mass amounts in very slow)
 ## *A faster version of perlin noise*
  > This new version of perlin noise is in the works and will use the math.mix function and the math.smoothstep function to create smooth veriating terrain with less computaional complexity/intensity.
 ## *Smooth min and max functions*
  > This will smoothly get the min/max of two values or a list
 ## *3D and 4D worly and cystal noise*
  > I am planning to add 3D and maybe 4D cystal and worly noise. 1D would be the same as linear interpolation and 4D is very complex.

# *New Features:*

 ## *Current Commit*
  > Added crystal noise 2D (worly noise where the take the second smallest distance) under the noise class (crystal2D). This new noise type has been fully optimised.
  
  > Added worly noise 2D under the noise class (worly2D). This new noise type has been fully optimised.
  
  > Added worly noise under the math class. It calculates worly noise at a single position based on the inputs
  
  > Added crystal noise under the math class. It calculates crystal noise at a single position based on the inputs

 ## *Last Commit*
  > Fixed the length function
  
  > Added a map function under the math class taking in a number, min val, max val, new min, new max
  
  > Fixed the vectorize function
  
  > Fixed the clamp, min and max (1D - 4D) functions under the lists class. They now take in one list and the rest intagers/floats
  
  > Fixed the smoothstep function under the math class
  
  > Added a gradeL function to the number, vector and color gradient classes (liniearly interplates instead of using a smoothstep for curvature)
  
  > Changed the grade function for number, vector and color gradients to use non linear interpolation.

# *Info On All The Functions/Classes:*

 ## *vec2*
 Stores an x and y position. Takes an input of x or x and y
 ## *vec3*
 Stores an x, y and z position. Takes an inout of x or x, y and z (you can also input a number and vec2 in any order)
 ## *vec4*
 Stores an x, y, z and w position. Takes an input of x or x and y or x, y, z, and w (you can also input two vec2s or numbers and vec2s or a number and a vec3 all in any order)
 ## *cos*
 Returns the cosine of a vector. Takes an input of a vector
 ## *sin*
 Returns the sin of a vector. Takes an input of a vector
 ## *tan*
 Returns the tangent of a vector. Takes an input of a vector
 ## *ceil*
 Rounds the vector up. Takes in a vector
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
 ## *lists*
   > ## *clamp (1D - 4D)*
   > Clamps a list, takes in a list and two numbers
   > ## *min (1D - 4D)*
   > Sets the min of a list. Takes in a list and number
   > ## *max (1D - 4D)*
   > Sets the max of a list. Takes in a list and number
   > ## *str (1D - 4D)*
   > Casts a list to a string types. Takes in a list
   > ## *mix (1D - 4D)*
   > Mixes two lists by a third list. Takes in three lists with the last one ranging from 0 - 1
   > ## *add (1D - 4D)*
   > Adds two lists. Takes in two lists
   > ## *sub (1D - 4D)*
   > Subtracts two lists. Takes in two lists
   > ## *div (1D - 4D)*
   > Divides two lists. Takes in two lists
   > ## *mult (1D - 4D)*
   > Multiples two lists. Takes in two lists
   > ## *pow (1D - 4D)*
   > Puts one list to the power of the other list. Takes in two lists
   > ## *floor_div (1D - 4D)*
   > Floor divides two lists. Takes in two lists
   > ## *mod (1D - 4D)*
   > Mods two lists. Takes in two lists
   > ## *int (1D - 4D)*
   > Intergerises a list. Takes in two lists
   > ## *round (1D - 4D)*
   > Rounds a list. Takes in two lists
   > ## *floor (1D - 4D)*
   > Floors a list. Takes in two lists
   > ## *ceil (1D - 4D)*
   > Gets the ceil of a list. Takes in two lists
   > ## *abs (1D - 4D)*
   > Gets the absulute of a list. Takes in two lists
   > ## *fract (1D - 4D)*
   > Gets the fract a list. Takes in two lists
 ## *math*
   > ## *worly*
   > Generates worly noise at a position in space. Takes in a 2D grid/list (of numbers ranging from 0 to scale), the scale, the x and the y.
   > ## *crystal*
   > Generates crystal noise at a position in space. Takes in a 2D grid/list (of numbers ranging from 0 to scale), the scale, the x and the y.
   > ## *cos*
   > Returns te cosine of a number. Takes an input of a number
   > ## *sin*
   > Returns the sin of a number. Takes an input of a number
   > ## *ceil*
   > Returns the ceil of a number. Takes in a number
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
   > ## *length*
   > Returns the length/dist of a list. Takes an input of a list
   > ## *normalizeList*
   > Normalizes a list. Takes an input of a list
   > ## *map*
   > Maps a number based on a min, max, new min and new max.
   > ## *map1D*
   > Scales/streches a 1D list of numbers to a new range of numbers. Takes an input of a list, min of list, max of list, new min, new max
   > ## *map2D*
   > Scales/streches a 2D list of numbers to a new range of numbers. Takes an input of a list, min of list, max of list, new min, new max
   > ## *map3D*
   > Scales/streches a 3D list of numbers to a new range of numbers. Takes an input of a list, min of list, max of list, new min, new max
   > ## *map4D*
   > Scales/streches a 4D list of numbers to a new range of numbers. Takes an input of a list, min of list, max of list, new min, new max
   > ## *smooth*
   > Makes the numebrs in a list more uniform/smooth and less spiky. Takes an input of a list and the number of soothing itterations
   > ## *interplate2*
   > Linearly interplates between two points based on a point inbetween. takes and input of the distance between points (a single number), the position inbetween numbers and a list of the two points
   > ## *interplate3*
   > Non linearly interplates between three points. Takes an input of the distance between points, the position in between points and the points (the points list can be infinitly long and it will hash for the two points around the given point)
   > ## *interplate5*
   > Non linearly interplates between five points. Takes an input of the distance between points, the position in between points and the points (the points list can be infinitly long and it will hash for the two points around the given point)
   > ## *smoothstep*
   > Smoothly steps from 0 - 1. Takes an input of the position between points, point1 and point2
   > ## *spline1D*
   > Splines on a 1D level between two points in a list that surround the given position. Takes an input of a list of values to spline, the position between points (x) and the distance between points
   > ## *spline2D*
   > Splines on a 2D level between two points in a list that surround the given position. Takes an input of a list of values to spline, the position between points (x, y) and the distance between points
   > ## *spline3D*
   > Splines on a 3D level between two points in a list that surround the given position. Takes an input of a list of values to spline, the position between points (x, y, z) and the distance between points
   > ## *spline4D*
   > Splines on a 4D level between two points in a list that surround the given position. Takes an input of a list of values to spline, the position between points (x, y, z, w) and the distance between points
   > ## *min1D*
   > Gets the min of a 1D array. Takes in a list
   > ## *min2D*
   > Gets the min of a 2D array. Takes in a list
   > ## *min3D*
   > Gets the min of a 3D array. Takes in a list
   > ## *min4D*
   > Gets the min of a 4D array. Takes in a list
   > ## *max1D*
   > Gets the max of a 1D array. Takes in a list
   > ## *max2D*
   > Gets the max of a 2D array. Takes in a list
   > ## *max3D*
   > Gets the max of a 3D array. Takes in a list
   > ## *max4D*
   > Gets the max of a 4D array. Takes in a list
 ## *dists*
   > ## *distToCircularPoint*
   > Returns the distance to a circle/sphere/hypersphere. Takes an input of two vectors and a radius
   > ## *distToPoint*
   > Returns the distance to a point. Takes an input of two vectors
## *gradient*
   > ## *color*
   > Returns a color gradient. Can take ina max gap (the defult is 50)
   > ## *number*
   > Returns a number gradient. Can take ina max gap (the defult is 50)
   > ## *vector*
   > Returns a vector gradient. Can take ina max gap (the defult is 50)
## *numberGradient*
   > ## *add*
   > Adds a point to the gradient. Takes in a point and number
   > ## *grade*
   > Returns the value at the inputed position (uses non linear interpolation). Takes in a point
   > ## *gradeL*
   > Same as the grade function but uses linear interpolation
## *colorGradient*
   > ## *add*
   > Adds a point of color to the gradient. Takes in a point and color
   > Returns the value at the inputed position (uses non linear interpolation). Takes in a point
   > ## *gradeL*
   > Same as the grade function but uses linear interpolation
## *noise*
   > ## *perlin1D*
   > Gives a height based on a 1D list of noise and based on a position. Takes and input of random noise, distance between points and the x position
   > ## *perlin2D*
   > Gives a height based on a 2D list of noise and based on a position. Takes and input of random noise, distance between points and the x, y position
   > ## *perlin3D*
   > Gives a height based on a 3D list of noise and based on a position. Takes and input of random noise, distance between points and the x, y, z position
   > ## *perlin4D*
   > Gives a height based on a 4D list of noise and based on a position (The 4D noise hasnt been tested but should work). Takes and input of random noise, distance between points and the x, y, z, w position
   > ## *ridge1D*
   > Gives a height based on a 1D list of noise and based on a position and generates with noticable ridges. Takes and input of random noise, distance between points and the x position
   > ## *ridge2D*
   > Gives a height based on a 2D list of noise and based on a position and generates with noticable ridges. Takes and input of random noise, distance between points and the x, y position
   > ## *ridge3D*
   > Gives a height based on a 3D list of noise and based on a position and generates with noticable ridges. Takes and input of random noise, distance between points and the x, y, z position
   > ## *ridge4D*
   > Gives a height based on a 4D list of noise and based on a position and generates with noticable ridges (The 4D noise hasnt been tested but should work). Takes and input of random noise, distance between points and the x, y, z, w position
   > ## *crystal2D*
   > Creates noise with a crystal look. Takes in a size (vec2), a scale, and optionaly a min and max size (the defualt is -1 - 1)
   > ## *worly2D*
   > Creates noise with a worly look. Takes in a size (vec2), a scale, and optionaly a min and max size (the defualt is -1 - 1)
## *array*
Returns a filled in array that can be constant, random int, random float or perlin. Takes in a size (vec2, vec3, vec4, tuple and lists work), the type of fill (constant, random int, random float or perlin) and the data for the type in a list, vector or tuple (constant; number (not in list), random int; min, max, random float; min, max, perlin; list of octaves (min 1 octave max inf octaves) each being the following; min, max, distance between points, type (add, sub or mix), if using mix then add the percentage (0 - 1) to mix by, ridge; same as perlin but is ridge noise meaning theres a buch of ridges but still veriation (abs(perlin noise) * -1 = ridge noise))
## *png*
   > ## *fromArray*
   > Creates a png from a 2D list of rgb values (a vec3). Takes in a 2d list of vec3's (or vec4's) and an image name (with .png at the end)
   > ## *getArray*
   > Returns an array of vec4's (rgba) from a png image. Takes in an image (with .png)
## *vector*
Turns a list into a vector
## *copy*
Returns a new vector that identical to the inputed one
## *txt*
   > ## *read*
   > Returns a list of the text on each line of the text file. Takes in a file
   > ## *delete*
   > Deletes a line in a text file. Takes an input of a file then line
   > ## *write*
   > Adds a line to a text file. Takes in a file, line, and the text you want there

This package is far from completion and keeps growing line by line day by day. I wont stop adding to it till I've added everything I could ever add. For more information, go to [repl.it](https://repl.it/talk/share/Vector-Types-in-Python3/83032) to see an example of PyVectors in use and how to use it. Just note that its using an older version (it will still be compatable) and therfore will not be using some of the newer shortcuts.
