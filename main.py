import os
import time

import TextureReader as texture
# for file in os.listdir('Textures/'):
#     if os.path.isfile(os.path.join('Textures/',file)):
#         texture.TextureData(file,20)


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
def TextureInterpolation(triangle_indices,texture,p):
    texture_list = texture.get_array()
    weights = TriangularInterpolation(triangle_indices,p)

    tsize = [len(texture_list), len(texture_list[0])]
    x,y = [round(size*weight) for weight,size in zip(weights,tsize)]
    return texture_list[y][x]
Tri = []
for y in range(50):
    Tri.append([])
    for x in range(50):
        if x+y <= y*2:
            # Tri[y].append(ColorInterpolation([[0,49],[49,49],[0,0]],
            #                                 [[255,0,0],[0,255,0],[0,0,255]],[x,y]))
            Tri[y].append(TextureInterpolation([[0,49],[49,49],[0,0]],texture.Texture('smile.png'),[x,y]))
        else:
            Tri[y].append([255,255,255,255])

t = time.time()

#print(time.time()-t)

texture.Display(Tri)