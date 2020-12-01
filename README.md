# Vector-Types-in-Python3-More

This python3 code adds vector types and more to make your code easier and quicker to write.


The first and in my opinion the best functions/classes are the vector classes containing vec2, vec3, and vec4 classes that have on a basic level store a tuple. The fancy thing about the vector classes is that it overloads the math operators meaning you can do the following:

    Vector1 += vector2 / vector3

This makes writing 2D an 3D programs easier as otherwise you would have to do the following:

    vector1 = [vector1[0] + (vector2[0] / vector3[0]), vector1[1] + (vector2[1] / vector3[1]), vector1[2] + (vector2[2] / vector3[2])]

Now that we went over the bulk of the program lets go over some of the rest of it. For starters, it also has a few functions such as cos, sin, normalize, mix, clamp, ect... for vector types. All of those functions except normalize also exsist in the math class but for none vector types which you call with math.function. The final two classes are march and object and work together. These two function allow you to cast a ray using ray marching which is just a faster way of ray tracing. To do that you need to do march.ray(ray_direction, ray_orgin) and that casts a ray. The ray_direction and ray_orgin virables do have to be vector types. The object class adds objects to the scene. It currently only has two shapes but that will be changing. Those two functions are addSphere(pos, r, color) and addInfFlatPlain(height, color).
