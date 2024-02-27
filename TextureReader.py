import PIL.Image
import ast
import os
import numpy as np

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

# def TextureData(path,new_width=100):
#     try:
#         img = PIL.Image.open('Textures/'+path)
#     except:
#         print(path,"Unable to find image")
    
#     width, height = img.size
#     aspect_ratio = height/width
#     new_height = aspect_ratio * new_width * 0.55
#     img = img.resize((new_width, int(new_height)))
    
#     with open("Textures/Data/"+path[:-4]+"_data.txt", "w") as f:
#         for row in range(int(new_height)):
#             row_list = []
#             for pixel in range(new_width):
#                 row_list.append(str(img.getpixel((pixel, row))))
#             f.write('/'.join(row_list)+'\n')

# def Read(path):
#     image_text = []
#     with open("Textures/Data/"+path[:-4]+"_data.txt", "r") as f:
#         for y,row in enumerate(f.readlines()):
#             image_text.append([])
#             for pixel in row.split('/'):
#                 image_text[y].append([int(value) for value in ast.literal_eval(pixel)][:-1])
#     return image_text

def Display(image_text):
    RESET = '\033[0m'
    def get_color_escape(r, g, b, background=False):
        return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)
    for row in image_text:
        for x in row:
            #print(x[:-1])
            print(get_color_escape(*x[:-1])+"@"+RESET,end=' ')
        print()

class Texture:
    def __init__(self,path,scale=1):
        self.image = PIL.Image.open('Textures/'+path)

    def get_array(self):
        if self.image:
            return np.asarray(self.image)
        
    def Scale(self,scale):
        self.image.resize([scale*size for size in self.image.size])