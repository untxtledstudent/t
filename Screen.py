import os

WIDTH, HEIGHT = 50,50

empty_pixel = ' '

Display = [[empty_pixel for pixel in range(WIDTH)] for row in range(HEIGHT)]

def PointToScreen(point,text):
    x,y = point
    screenPointY,screenPointX = round(-y+(HEIGHT/2)),round(x+(WIDTH/2))
    
    if min(screenPointX,screenPointY) >= 0 and screenPointY < HEIGHT and screenPointX < WIDTH:
        Display[screenPointY][screenPointX] = text

def Project():
    RESET = '\033[0m'
    def get_color_escape(r, g, b, background=False):
        return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)
    
    for row in Display:
        for pixel in row:
            if pixel != empty_pixel:
                print(get_color_escape(*pixel[1])+pixel[0]+RESET,end=' ')
            else:
                print(empty_pixel,end=' ')
        print()
        
def Refresh():
    os.system('clear')
    Project()
    Display = [[empty_pixel for pixel in range(WIDTH)] for row in range(HEIGHT)]