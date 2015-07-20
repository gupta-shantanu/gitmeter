from PIL import Image,ImageDraw, ImageFont
from io import BytesIO as byt
def createNew(string):
    """
    creates image according to given information
    """
    image=Image.open('imageGenerator/images/images.jpg').convert('RGBA')

    fnt = ImageFont.truetype("fonts/arial.ttf", 25)
    d = ImageDraw.Draw(image)

    d.text((10,10), string, font=fnt, fill=(255,255,255,128))

    d.text((10,60), "World",  fill=(255,255,255,255))
    file=byt()
    image.save(file,'jpeg')
    return file.getvalue()


