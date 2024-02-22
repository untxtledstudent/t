import os
import time

import TextureReader as texture
# for file in os.listdir('Textures/'):
#     if os.path.isfile(os.path.join('Textures/',file)):
#         texture.TextureData(file,20)


t = time.time()

tex = None
for x in range(1000):
    tex = texture.Textures['smile.png']
#print(time.time()-t)

texture.Display(tex)