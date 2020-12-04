# Vector Types in Python3 + More

OctiveNoise is a sub package of PyVectors and provides a 1D and 2D octive noise functions. The output of these functions can create amazing terrain and more. To import the package do the following:

    from OctiveNoise import *

To create a noise map, do the following:

    getSmoothNoise2D(vec2_size, getRandNoise2D(vec2_size, optional seed), octives, optional scaling_bias)

The functions and classes and their details are as following:

 ## *getRandNoise1D*
 Returns a map of 1D random noise for use with the octive noise functions. Input of size and an optional seed.
 ## *getSmoothNoise1D*
 Returns a 2D map of smooth noise. Takes in size, random noise, number of octives and an optional scaling bias (2 is defualt)
 ## *getRandNoise2D*
 Returns a map of 2D random noise for use with the octive noise functions. Input of vec2 size and an optional seed.
 ## *getSmoothNoise2D*
 Returns a 2D map of smooth noise. Takes in vec2 size, random noise, number of octives and an optional scaling bias (2 is defualt)

Click the following link to see my example posted on repl.it. [repl.it](https://repl.it/talk/share/Octave-Perlin-Noise/84127).
