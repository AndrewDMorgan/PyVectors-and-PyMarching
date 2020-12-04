# Vector Types in Python3 + More

PyMarching is a sub package of PyVectors meaning you need PyVectors to run PyMarching. PyMarching is a basic ray marcher that allows you to cast a ray and return information on the collition. It currently only allows for flat infinite planes and sphere but more shapes are being added. It also is very basic but is going to be improved to be a much more advanced ray marcher. To import it you want to do the following:

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
