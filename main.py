import Screen
import time
import Draw

import Texture as texture

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
    weights = TriangularInterpolation(triangle_indices,p)

    tsize = [len(texture_list), len(texture_list[0])]
    x,y = [round(size*weight) for weight,size in zip(weights,tsize)]
    return texture_list[y-1][x-1]

t = time.time()

texture_list = texture.Texture('smile.png').get_array()

points = [[-25,25],[-25,-25],[25,-25],[25,25]]

# Quad = []
# for y in range(h):
#     Quad.append([])
#     for x in range(w):
#         if x+y <= y*2:
#             #Quad[y].append(ColorInterpolation([[0,49],[49,49],[0,0]],
#             #                                [[255,0,0],[0,255,0],[0,0,255]],[x,y]))
#             Quad[y].append(TextureInterpolation([points[0],points[1],points[2]],texture_list,[x,y]))
#         else:
#             #Quad[y].append(ColorInterpolation([[49,0],[49,49],[0,0]],
#              #                               [[0,0,0],[0,255,0],[0,0,255]],[x,y]))
#             Quad[y].append(TextureInterpolation([points[0],points[1],points[2]],texture_list,[x,y]))
# texture.Display(Quad)
# print(time.time()-t)

#Draw.Triangle(points[:-1],'#',texture=texture_list)
Draw.Quad(points,'#',texture=texture_list)
Screen.Project()