from PIL import Image

def handler(img):
    bin_help = (128, 64, 32, 16, 8, 4, 2, 1)
    pixil = Image.open(img)
    unity = 0
    i = 0
    i_2 = 0
    print(pixil.size)
    for x in range(pixil.width):
        for y in range(pixil.height):
            pixel = pixil.getpixel((x,y))
            p = 1 if pixel[0] == 255 else 0
            unity += p * bin_help[i]
            i += 1
            if i == 8:
                print(hex(unity), end=',')
                i_2 += 1
                i = 0
                unity = 0
                if i_2 == 8:
                    print()
                    i_2 = 0

if __name__ == '__main__':
    handler('pixil-frame-1.png')
