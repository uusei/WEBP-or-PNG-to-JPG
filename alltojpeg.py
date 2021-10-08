from PIL import Image
from PIL import ImageFilter
import os
import sys

path = os.getcwd() + '/' + 'pic'

if os.path.isdir(path) == False :
    os.mkdir("pic")

save1 = os.getcwd() + '/' + 'jpg'
if os.path.isdir(save1) == False:
    os.mkdir("jpg")

def get_file_name(file_name):
    dot_pos = file_name.rfind('.')
    if dot_pos == -1:
        fn = file_name
    else:
        fn = file_name[dot_pos:]
    return fn

    return file_name[:file_name.rfind('.')]


def get_file_ext(file_name):
    dot_pos = file_name.rfind('.')
    if dot_pos == -1:
        ext = ''
    else:
        ext = file_name[dot_pos:]

    return ext


def pic_to_jpg(file_name, num, remove_webp=False):        #webp转换
    try:
        filein = path + '/' + file_name
        im = Image.open(filein)

        if im.mode != 'RGBA':
            im = im.convert('RGBA')
        width = im.width
        height = im.height
        image = Image.new('RGB', size=(width, height), color=(255, 255, 255))
        image.paste(im, (0, 0), mask=im)
        im = image.convert('RGB')
        #im = im.resize((500, 500), Image.ANTIALIAS)
        #im = im.filter(ImageFilter.SHARPEN)
        new_name = save1 + '/' + str(num) + '.jpg'
        print(new_name, end='\n')
        im.save(new_name, quality=95, subsampling=0)

        if remove_webp:
            os.remove(file_name)
    except:
        pass

    return

def list_pic():                                    #获取webp
    print("Get image files ... ", end='\n')

    files = os.listdir(path)
    print(files, end='\n')
    pic_files = []

    for f in files:
        if os.path.isdir(f):
            continue

        if get_file_ext(f).lower() == '.webp':
            pic_files.append(f)

        if get_file_ext(f).lower() == '.png':
            pic_files.append(f)


    print("%s found" % len(pic_files))
    print(path, end='\n')
    return pic_files

def process1():                              #转换过程
    pic_files = list_pic()

    print("Convert to jpg:")
    num = 0
    for f in pic_files:

        print("\t%s" % f)
        pic_to_jpg(f, num, False)
        num += 1

    print("Done.")
    return

    index += 1

