from PIL import Image
from PIL import ImageFilter
import os
import sys
import emoji
import alltojpeg

b = 0


def exit1():
    b = 1


def f(o):
    try:
        operator.get(o)()
    except:
        print('请输入合法字符！\n')
    return


operator = {'1': alltojpeg.list_pic, '2': alltojpeg.process1, '3': emoji.eomjidown,
            '4': emoji.eomjidown_live, '0': exit1}

while b != 1:
    print('欢迎使用图片转换jpg小程序')
    print('\n请选择功能'
          '\n1: 查看图片文件'
          '\n2: 转换图片为jpg'
          '\n3: b站表情导入'
          '\n4: b站大舰队表情导入'
          '\n0: 退出'
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
