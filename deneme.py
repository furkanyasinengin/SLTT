import cv2
import PILasOPENCV as ImageFont

import PILasOPENCV as Image
import PILasOPENCV as ImageDraw
import PILasOPENCV as ImageFont

print(cv2.FONT_ITALIC)



font = ImageFont.truetype("verdana.ttf", 40)
print(font)
im = Image.open("dosyalar/fotograflar/info_window.png")
draw = ImageDraw.Draw(im)
text = "Lena's image"
draw.text((249,455), text, font=font, fill=(0, 0, 0))
# in PIL:
# print(font.getsize(text))
# mask = font.getmask(text)
print(ImageFont.getsize(text, font))
mask = ImageFont.getmask(text, font)
print(type(mask))
cv2.imshow("mask", mask)
im.show()