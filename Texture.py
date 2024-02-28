import PIL.Image
import ast
import os
import numpy as np
import Screen

def TextureColor(path,new_width=100):
    try:
        img = PIL.Image.open('Textures/'+path)
    except:
        print(path,"Unable to find image")

    width, height = img.size
    aspect_ratio = height/width
    new_height = aspect_ratio * new_width
    img = img.resize((new_width, int(new_height)))

    return np.asarray(img)

Textures = {}
for file in os.listdir('Textures/'):
    if os.path.isfile(os.path.join('Textures/',file)):
        Textures[file] = TextureColor(file,50)

class Texture:
    def __init__(self,path,scale=1):
        self.image = PIL.Image.open('Textures/'+path)

    def get_array(self):
        if self.image:
            return np.asarray(self.image)
        
    def Scale(self,scale):
        self.image.resize([scale*size for size in self.image.size])

def TriangularInterpolation(triangle_indices,p):
    a,b,c = triangle_indices
    w1 = ((b[1]-c[1])*(p[0]-c[0]) + (c[0]-b[0])*(p[1]-c[1]))/(
        (b[1]-c[1])*(a[0]-c[0]) + (c[0]-b[0])*(a[1]-c[1]))
    w2 = ((c[1]-a[1])*(p[0]-c[0]) + (a[0]-c[0])*(p[1]-c[1]))/(
        (b[1]-c[1])*(a[0]-c[0]) + (c[0]-b[0])*(a[1]-c[1]))
    w3 = 1 - w1 - w2
    return w1,w2,w3

def ColorInterpolation(triangle_indices,colors,p):
    weights = TriangularInterpolation(triangle_indices,p)
    color_value = [0,0,0]

    for index,color in enumerate(colors):
        weighted_color = [round(weights[index]*value) for value in color]
        color_value = [a+b for a,b in zip(weighted_color,color_value)]
    color_value.append(255)
    return color_value

def TextureInterpolation(triangle_indices,texture_list,p):
    points = []
    for point in triangle_indices:
        points.append([point[0]+(Screen.WIDTH/2),-point[1]+(Screen.HEIGHT/2)])
    print(triangle_indices,points)
    weights = TriangularInterpolation(points,p)

    tsize = [len(texture_list), len(texture_list[0])]
    values = [[round(axis*weight)for axis in point]  for weight,point in zip(weights,points)]
    print(weights,values)

    x=1+'a'
    return texture_list[sum([y for x,y in values])-1][sum([x for x,y in values])-1]