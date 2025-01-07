import os
import random
from PIL import Image, ImageDraw, ImageFont

MEME_TEXTS = os.path.join("..", "data", "memes-newline.txt")
MEME_IMAGES = os.path.join("..", "data", "images")
MEME_FONT = os.path.join("..", "data", "Anton-Regular.ttf")     # a TTF file is a font file format created by Apple, but it is used on both Macintosh and Windows platforms. The size can be adjusted freely without compromising quality, and when printed, it looks the same as it does on the screen.

# list meme texts if a line contains text
memes = []
with open(MEME_TEXTS, "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if len(line) >= 1:
            memes.append(line)

# list images if it is a jpg
images = []
for image in os.listdir(MEME_IMAGES):
    if image.lower().endswith(".jpg") or image.lower().endswith("jpeg"): 
        images.append(image)

# choose a random image and a random meme-text
image = random.choice(images)
meme = random.choice(memes).replace(" - ", "\n")

with Image.open(os.path.join(MEME_IMAGES, image)) as im:
    # half_width of the image is neccessary to align the font in the centre (centre=half_width)
    width, height = im.size
    half_width = int(width/2)
    # get a font
    fnt_tmp = ImageFont.truetype(MEME_FONT, 100)                    # temporary font to calculate the length of the font given a font-size
    fnt_len = 0                                                     # initialise ftn_len
    for meme_line in meme.split("\n"):                              # create a list: if there is a line break the list contains two items
        fnt_len = max(fnt_len, fnt_tmp.getlength(meme_line))        # 1st loop: max of 0 and length of 1st line
                                                                    # 2nd loop: max of length of 1st line and 2nd line
    
    fnt_factor = width / fnt_len                                    # calculate a factor which adjusts the font size matching the width of the image
    font_size = int(100*fnt_factor*0.9)                             # new font size (0.9 ensures that there´s a little distance to the image frame)
    fnt = ImageFont.truetype(MEME_FONT, font_size)                  # new font with new font size

    # get a drawing context
    d = ImageDraw.Draw(im)
    # draw mulitline text: first black font moved by a factor (font_size*0.05) in all directions, then white font
    d.multiline_text((half_width - font_size * 0.05, 10), meme, font=fnt, fill=(0, 0, 0), anchor="ma", align='center')  # to the left
    d.multiline_text((half_width + font_size * 0.05, 10), meme, font=fnt, fill=(0, 0, 0), anchor="ma", align='center')  # to the right
    d.multiline_text((half_width, 10 - font_size * 0.05), meme, font=fnt, fill=(0, 0, 0), anchor="ma", align='center')  # up
    d.multiline_text((half_width, 10 + font_size * 0.05), meme, font=fnt, fill=(0, 0, 0), anchor="ma", align='center')  # down
    d.multiline_text((half_width - font_size * 0.05, 10 - font_size * 0.05), meme, font=fnt, fill=(0, 0, 0), anchor="ma", align='center')   # diagonal
    d.multiline_text((half_width + font_size * 0.05, 10 + font_size * 0.05), meme, font=fnt, fill=(0, 0, 0), anchor="ma", align='center')   # diagonal
    d.multiline_text((half_width - font_size * 0.05, 10 + font_size * 0.05), meme, font=fnt, fill=(0, 0, 0), anchor="ma", align='center')   # diagonal
    d.multiline_text((half_width + font_size * 0.05, 10 - font_size * 0.05), meme, font=fnt, fill=(0, 0, 0), anchor="ma", align='center')   # diagonal
    # white
    d.multiline_text((half_width, 10), meme, font=fnt, fill=(255, 255, 255), anchor="ma", align='center')
    
    im.save("bild.jpg")