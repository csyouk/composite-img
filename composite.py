import os
from wand.image import Image

'''
fb image 1200 * 630 px
original constellation image is 1250 * 1250
shrink original image into 630 * 630
add 285 * 630 px left and right
'''

bg ="background.PNG"
sample = "sample.png"
first = 0


def resize(img_file):
    with Image(filename=img_file) as img:
        img.resize(630, 630)

def composite(background, layered):
    print("background file : {} / layer file : {}".format(background, layered))
    layered_img_without_extension = layered.split(".")[first]
    converted_img = "converted_{0}.png".format(layered_img_without_extension)
    with Image(filename=background) as bg_img:
        with Image(filename=layered) as layered_img:
            bg_img.composite(layered_img, left=285, top=0)
        bg_img.save(filename=converted_img)
    print("============ Composited Img Created : {} ============".format(converted_img))


png_files = [f for f in os.listdir('.') if os.path.isfile(f) and (f.endswith(".png") or f.endswith(".PNG"))]
print("List of image files in this directory ======")
for f in png_files:
    if bg in f:
        continue
    resize(f)
    composite(bg, f)
print("============================================")


