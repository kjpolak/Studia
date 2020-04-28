from PIL import Image
import matplotlib.pyplot as plt
import itertools

def encode(image, message, newimage_name):
    image = Image.open(image)
    newimage = image.copy()
    data = [format(ord(letter), '08b') for letter in message]
    pixels = list(itertools.chain(*[pix[:3] for pix in image.getdata()]))
    changedpix=[]
    for i in range(len(data)):
        binletter = data[i]
        threepix = pixels[i*9:(i+1)*9]
        for j in range(8):
            if binletter[j]=='1':
                threepix[j]-=1
        if i==len(data)-1:
            threepix[8]-=2
        changedpix+=threepix
    changedpix = [tuple(changedpix[i:i+3]) for i in range(0, len(changedpix), 3)]
    w = newimage.size[0]
    x, y = 0,0
    for pixel in changedpix:
        newimage.putpixel((x, y), pixel)
        if x==w-1:
            x=0
            y+=1
        else:
            x+=1
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
    pixels1 = list(itertools.chain(*[list(pix[:3]) for pix in image1.getdata()]))
    pixels2 = list(itertools.chain(*[list(pix[:3]) for pix in image2.getdata()]))
    img1 = True
    for i in range(8):
        if pixels1[i]>pixels2[i]:
            img1=False
            break
    if img1:
        return _decode(pixels1, pixels2)
    else:
        return _decode(pixels2, pixels1)

def _decode(pixels1, pixels2):
    message = ''
    for i in range(int(len(pixels1)/9)):
        threepix1 = pixels1[i*9:(i+1)*9]
        threepix2 = pixels2[i*9:(i+1)*9]
        binstr = ''
        for i in range(8):
            if threepix1[i]!=threepix2[i]:
                binstr+='1'
            else:
                binstr+='0'
        message += chr(int(binstr, 2))
        if threepix1[8]+2==threepix2[8]:
            break
    print(message)
        
