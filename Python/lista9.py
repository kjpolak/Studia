from PIL import Image
import random
import itertools
		
def encode(image, message):
    img = image.copy()
    data = [format(ord(letter), '08b') for letter in message]
    x = random.sample(range(img.size[0]), len(data)*3)
    y = random.sample(range(img.size[1]), len(data)*3)
    places = sorted(list(zip(x, y)), key=lambda k: [k[0], k[1]])
    #print(places)
    choose_pixels = [img.getpixel(place)[:3] for place in places]
    #print(choose_pixels[:7])
    three_pixels = list(zip(choose_pixels[::3], choose_pixels[1::2], choose_pixels[2::3]))
    new_pixels = []
    for i in range(len(data)):
        a,b,c = three_pixels[i]
        letter, trio = data[i], list(a+b+c)
        #print("orzed", trio[0], "  ", trio[1])
        for j in range(8):
            if letter[j]=='0' and trio[j]%2!=0:
                trio[j]-=1
            elif letter[j]=='1' and trio[j]%2==0:
                trio[j]-=1
        if i==len(data)-1:
            if trio[-1]%2==0:
                trio[-1]-=1
        else:
            if trio[-1]%2!=0:
                trio[-1]-=1
        
        #trio[8]-=2
        #print("po", trio[0], "  ", trio[1])
        #print(trio)
        new_pixels.append(trio[:3])
        new_pixels.append(trio[3:6])
        new_pixels.append(trio[6:])
    print(new_pixels)
    for i in range(len(places)):
        #pixel = list(img.getpixel(places[i]))
        #pixel = tuple(pixel)#(new_pixels[i][0], new_pixels[i][1], new_pixels[i][2], pixel[3])
        img.putpixel(places[i], tuple(new_pixels[i]))
    new_img_name = input("Enter the name of new image(with extension): ") 
    img.save(new_img_name, str(new_img_name.split(".")[1].upper())) 
    img.show()
    
def _decode(pixels):
    data = ''
    for j in range(int(len(pixels)/9)):
        print(pixels[j*9:(j+1)*9])
        tmp = pixels[j*9:(j+1)*9][:8]
        #print(tmp)
        binstr = ''
        for i in tmp:
            if i%2 == 0:
                binstr+='0'
            else:
                binstr+='1'
        data+=chr(int(binstr, 2))
    print(data)
        
def decode(image1, image2):
    pixels1 = [pix for pix in image1.getdata()]
    #test = [pix for pix in image1.getdata()]
    #print(pixels1==test)
    pixels2 = [pix for pix in image2.getdata()]
    img12 = list(zip(pixels1, pixels2))
    diff1, diff2 = [], []
    for _pixel in img12:
        if _pixel[0]!=_pixel[1]:
            diff1.append(_pixel[0])
            diff2.append(_pixel[1])
    test1=[]
    test2=[]
    test=[]
    for i in range(image1.size[0]):
        for j in range(image1.size[1]):
            if image1.getpixel((i, j))!=image2.getpixel((i, j)):
                #print((i,j))
                test.append((i,j))
                test1.append(image1.getpixel((i, j)))
                test2.append(image2.getpixel((i, j)))
    #print(pixels1[:7])
    #print(test1[:7])
    #print(test)
    print(diff2)
    test1 = list(itertools.chain(*[list(x[:3]) for x in diff1]))
    test2 = list(itertools.chain(*[list(x[:3]) for x in diff2]))
    img1 = True
    for i in range(8):
        if test1[i]>test2[i]:
            img1=False
            break
    print(img1)
    if img1:
        return _decode(test1)
    else:
        return _decode(test2)
    
def _decode3(_pixels):
    data = ''
    for j in range(int(len(_pixels)/9)):
        pixels = _pixels[j*9:(j+1)*9]
        binstr = ''
        for i in pixels[:8]:
            if i%2==0:
                binstr+='0'
            else:
                binstr+='1'

        data+=chr(int(binstr, 2))

        if pixels[-1]%2!=0:
            print(data)
            break

def decode3(image):
    pixels1 = [pix for pix in image1.getdata()]
    test1 = list(itertools.chain(*[list(x[:3]) for x in pixels1]))
    return(_decode3(test1))

image1 = Image.open('test.png')
image2 = Image.open('test3.png')
decode(image1, image2)
#decode3(image2)
#encode(image1, 'makaka')
