from PIL import Image
from PIL import ImageFilter
import os
import sys

b = 0

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


def webp_to_jpg(file_name, num, remove_webp=False):        #webp转换
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


def list_webp():                                    #获取webp
    print("Get webp image files ... ", end='\n')

    files = os.listdir(path)
    print(files, end='\n')
    webp_files = []

    for f in files:
        if os.path.isdir(f):
            continue

        if get_file_ext(f).lower() == '.webp':
            webp_files.append(f)

    print("%s found" % len(webp_files))
    print(path, end='\n')
    return webp_files


def process1():                              #转换过程
    webp_files = list_webp()

    print("Convert webp to jpg:")
    num = 0
    for f in webp_files:

        print("\t%s" % f)
        webp_to_jpg(f, num, False)
        num += 1

    print("Done.")
    return

    index += 1

'''
if __name__ == "__main__":

    if len(sys.argv) > 1:
        for n in range(1, len(sys.argv, 1)):
            webp_to_jpg(sys.argv[n], True)
'''

def list_png():                                    #获取webp
    print("Get webp image files ... ", end='\n')

    files = os.listdir(path2)
    print(files, end='\n')
    png_files = []

    for f in files:
        if os.path.isdir(f):
            continue

        if get_file_ext(f).lower() == '.png':
            png_files.append(f)

    print("%s found" % len(png_files))
    print(path, end='\n')
    return png_files

def png_to_jpg(file_name, num, remove_png=False):        #webp转换
    try:
        filein = path2 + '/' + file_name
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

        if remove_png:
            os.remove(file_name)
    except:
        pass

    return

def process2():                              #转换过程
    png_files = list_png()

    print("Convert png to jpg:")
    num = 0
    for f in png_files:

        print("\t%s" % f)
        png_to_jpg(f, num, False)
        num += 1

    print("Done.")
    return

    index += 1

def exit1():
    b = 1

def f(o):
    try:
        operator.get(o)()
    except:
        print('请输入合法字符！\n')
    return

path = os.getcwd() + '/' + 'webp'

if os.path.isdir(path) == False :
    os.mkdir("webp")

path2 = os.getcwd() + '/' + 'png'
if os.path.isdir(path2) == False :
    os.mkdir("png")

save1 = os.getcwd() + '/' + 'jpg'
if os.path.isdir(save1) == False:
    os.mkdir("jpg")

operator = {'1': list_webp, '2': process1, '5': list_png, '6': process2,  '0': exit1}


while b != 1:
    print('欢迎使用webp转换jpg小程序')
    print('\n请选择功能'
          '\n1: 查看webp文件'
          '\n2： 转换webp图片为jpg'
          '\n3: 修改输入相对路径'
          '\n4: 修改输出相对路径'
          '\n5: 查看png文件'
          '\n6： 转换png图片为jpg'
          '\n0：退出'
          )
    optional = str(input("请输入您所需要的功能\n"))
    f(optional)
    if optional == '0':
        print('是否退出？\n'
              '是 请按1\n'
              '否 请按0\n'
              )
        try:
            b = int(input())
        except:
            pass

print('感谢使用!\n')