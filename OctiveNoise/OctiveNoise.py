from random import *


def getRandNoise2D(size, seed__ = None):
    if seed__ == None:
        seed_ = randint(0, 1000)
    else:
        seed_ = seed__
    seed(seed_)
    list = []
    for x in range(size.x):
        new_list = []
        for y in range(size.y):
            new_list.append(uniform(0.000, 1.000))
        list.append(new_list)
    return list


def getSmoothNoise2D(size, random_noise, octives, scaling_bias = 2):
    smooth_noise = []
    for x in range(size.x):
        smooth_noise_ = []
        for y in range(size.y):
            noise = 0
            scale = 1
            scaleAcc = 0
            for o in range(octives):
                pitch = size.x >> o
                sampleX1 = int(int(x / pitch) * pitch)
                sampleY1 = int(int(y / pitch) * pitch)
                
                sampleX2 = int((sampleX1 + pitch) % size.x)
                sampleY2 = int((sampleY1 + pitch) % size.x)
                
                blendX = (x - sampleX1) / pitch
                blendY = (y - sampleY1) / pitch
                
                sample1 = (1 - blendX) * random_noise[sampleX1][sampleY1] + blendX * random_noise[sampleX2][sampleY1]
                sample2 = (1 - blendX) * random_noise[sampleX1][sampleY2] + blendX * random_noise[sampleX2][sampleY2]
                
                noise += (blendY * (sample2 - sample1) + sample1) * scale
                
                scaleAcc += scale
                scale = scale / scaling_bias
            smooth_noise_.append(noise / scaleAcc)
        smooth_noise.append(smooth_noise_)
    
    return smooth_noise


def getRandNoise1D(size, seed__ = None):
    if seed__ == None:
        seed_ = randint(0, 1000)
    else:
        seed_ = seed__
    seed(seed_)
    list = []
    for x in range(size):
        list.append(uniform(0.000, 1.000))
    
    return list


def getSmoothNoise1D(size, random_noise, octives, scaling_bias):
    smooth_noise = []
    for x in range(size):
        noise = 0
        scale = 1
        scaleAcc = 0
        for o in range(octives):
            pitch = size >> o
            sample1 = int(int(x / pitch) * pitch)
            sample2 = int((sample1 + pitch) % size)
            
            blend = (x - sample1) / pitch
            sample = (1 - blend) * random_noise[sample1] + blend * random_noise[sample2]
            noise += sample * scale
            scaleAcc += scale
            scale = scale / scaling_bias
        smooth_noise.append(noise / scaleAcc)
    
    return smooth_noise

