from PyVectors import *

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
            pos = (rd * Vec3(dfo)) + o
            
            data = march.getDist(pos)
            
            min_dist = data.x
            col = data.y
            
            dfo += min_dist
            
            if min_dist < min_depth or dfo > max_dist:
                break
        
        return Vec2(dfo, col)
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
        return Vec2(min_dist, col)

