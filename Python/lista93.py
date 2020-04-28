from PIL import Image
import matplotlib.pyplot as plt
import random
import itertools

def encode(image, message, newimage_name):
    image = Image.open(image)
    newimage = image.copy()
    data = [format(ord(letter), '08b') for letter in message]
    x = random.sample(range(image.size[0]), len(data)*3)
    y = random.sample(range(image.size[1]), len(data)*3)
    places = sorted(list(zip(x, y)), key=lambda k: [k[0], k[1]])
    pixels = [image.getpixel(place)[:3] for place in places]
    changedpix=[]
    for i in range(len(data)):
        binletter = data[i]
        threepix = list(itertools.chain(*pixels[i*3:(i+1)*3]))
        for j in range(8):
            if binletter[j]=='0' and threepix[j]%2!=0:
                threepix[j]-=1
            elif binletter[j]=='1' and threepix[j]%2==0:
                threepix[j]-=1
        if i==len(data)-1:
            if threepix[8]%2==0:
                threepix[8]-=1
        else:
            if threepix[8]%2!=0:
                threepix[8]-=1
        changedpix+=threepix    
    changedpix = [tuple(changedpix[i:i+3]) for i in range(0, len(changedpix), 3)]
    print('changed', changedpix)
    for i in range(len(changedpix)):
        print(places[i], changedpix[i])
        newimage.putpixel(places[i], changedpix[i])
    newimage.save(newimage_name, str(newimage_name.split(".")[1].upper()))
    f, axarr = plt.subplots(1,2)
    plt.axis('off')
    axarr[0].imshow(image)
    axarr[1].imshow(newimage)
    axarr[0].axis('off')
    axarr[1].axis('off')
    plt.show()
        
def decode(image1, image2):
    image1 = Image.open(image1)
    image2 = Image.open(image2)
    pixels1 = [pix for pix in image1.getdata()]
    pixels2 = [pix for pix in image2.getdata()]
    img12 = list(zip(pixels1, pixels2))
    diff1, diff2 = [], []
    for _pixel in img12:
        if _pixel[0]!=_pixel[1]:
            diff1.append(_pixel[0])
            diff2.append(_pixel[1])
    test1 = list(itertools.chain(*[list(x[:3]) for x in diff1]))
    test2 = list(itertools.chain(*[list(x[:3]) for x in diff2]))
    img1 = True
    for i in range(8):
        if test1[i]>test2[i]:
            img1=False
            break
    if img1:
        return _decode(test1)
    else:
        print(test2)
        return _decode(test2)

def _decode(_pixels):
    message = ''
    for i in range(int(len(_pixels)/9)):
        threepix = (_pixels[i*9:(i+1)*9])
        binstr = ''
        for i in threepix[:8]:
            if i%2==0:
                binstr+='0'
            else:
                binstr+='1'
        message += chr(int(binstr, 2))
    print(message)
        #if threepix[8]%2!=0:
            #print(message)
            #break
