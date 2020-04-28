from PIL import Image
import matplotlib.pyplot as plt
import itertools

def encode(image, message, newimage_name):
    image = Image.open(image)
    newimage = image.copy()
    data = [format(ord(letter), '08b') for letter in message]
    pixels = [pix[:3] for pix in image.getdata()]
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
        
def decode(image):
    image = Image.open(image)
    message = ''
    pixels = [pix[:3] for pix in image.getdata()]
    for i in range(int(len(pixels)/3)):
        threepix = list(itertools.chain(*pixels[i*3:(i+1)*3]))
        binstr = ''
        for i in threepix[:8]:
            if i%2==0:
                binstr+='0'
            else:
                binstr+='1'
        message += chr(int(binstr, 2))
        if threepix[8]%2!=0:
            print(message)
            break
    
