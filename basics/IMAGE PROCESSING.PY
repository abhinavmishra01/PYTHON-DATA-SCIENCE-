from PIL import Image


im= Image.open(r'C:\Users\picture\abhinav.jpeg')   # relative addr 
im2= Image.open(r'C:\Users\picture\abhinav.jpeg')  #absolute addr

print(im)
print(im2)

print('resolution',im.size)
print('height',im.height)
print('width',im.width)
print('mode',im.mode)
print('format',im.format)
print ('exif',im.info)

# im.convert('L').show()
# im.resize((100,100)).show()
# # im.resize((5000.5000)).show()
# im.resize((im.width*5,im.height*5)).save('abhinav.jpg')

im.show()