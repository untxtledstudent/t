import Screen
from Texture import TextureInterpolation


def Line(start,finish,character,texture=None,points=None,color=(255,255,255)):
        startX, startY = start
        finishX = finish[0]

        startX,finishX =  sorted([startX,finishX])

        for x in range(startX,finishX+1):
            if not(type(texture)==None and type(points)==None):
                Screen.PointToScreen([x,startY],[character,TextureInterpolation(points,texture,[x,startY])[:-1]])
            elif not(type(color)==None):
                Screen.PointToScreen([x,startY],[character,color])
                

def Division(a,b):
    return a / b if b else 0

def BottonFlatTriangle(pointA,pointB,pointC,character,texture=None,color=(255,255,255)):
    slopeAB = Division(pointB[0]-pointA[0],pointB[1]-pointA[1])
    slopeAC = Division(pointC[0]-pointA[0],pointC[1]-pointA[1])

    xAB = pointA[0]
    xAC = pointA[0]
    for y in range(pointA[1],pointB[1]+1):
        Line([round(xAB),y],[round(xAC),y],character,texture,[pointA,pointB,pointC],color)
        xAB += slopeAB
        xAC += slopeAC

def TopFlatTriangle(pointA,pointB,pointC,character,texture=None,color=(255,255,255)):
    slopeCA = Division(pointC[0]-pointA[0],pointC[1]-pointA[1])
    slopeCB = Division(pointC[0]-pointB[0],pointC[1]-pointB[1])
    
    xCA = pointC[0]
    xCB = pointC[0]

    for y in range(pointC[1],pointA[1]-1,-1):
        Line([round(xCA),y],[round(xCB),y],character,texture,[pointA,pointB,pointC],color)
        xCA -= slopeCA
        xCB -= slopeCB
    
def Triangle(vertices,character,scale=1,texture=None,color=(255,255,255)):
    vertices = [[round(axis*scale) for axis in vertex] for vertex in vertices]
    pointA,pointB,pointC = sorted(vertices, key = lambda point: point[1] )

    if pointB[1] == pointC[1]:
        BottonFlatTriangle(pointA,pointB,pointC,character,texture,color)
    elif pointA[1] == pointB[1]:
        TopFlatTriangle(pointA,pointB,pointC,character,texture,color)
    else:
        pointD = [round((pointA[0]+((pointB[1]-pointA[1])/(pointC[1]-pointA[1]))*(pointC[0]-pointA[0]))),pointB[1]]
        BottonFlatTriangle(pointA,pointB,pointD,character)
        TopFlatTriangle(pointB,pointD,pointC,character)

def Quad(vertices,character,scale=1,texture=None,color=(255,255,255)):
    # if not Screen.faceVisible(vertices):
    #     return
    for point in vertices:
        Screen.PointToScreen(point,vertices.index(point))
    Triangle([vertices[0],vertices[1],vertices[3]],character,scale,texture,color)
    Triangle([vertices[1],vertices[2],vertices[3]],character,scale,texture,color)