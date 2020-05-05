from PIL import Image

im=Image.open("1.jpg")
#im=im.rotate(1)
im.save("e.jpg")
im2=im.convert("L")
im2.save("b.jpg")
threshold = 200
im = im2.point(lambda p: p > threshold and 255)
im.save("d.jpg")
img="d.jpg"