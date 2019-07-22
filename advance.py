#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xubobo
@license: Apache Licence
@contact: xubobo@gmail.com
@site: http://www.yxreader.com
@software: PyCharm
@file: basic.py
@time: 2019-07-20 21:30
@description：一键抠图 removebg
"""

from removebg import RemoveBg
from PIL import Image

api_key = '自己申请的api'


def ps_a_img(bg_color_value):
    file_path = './img/source.jpeg'
    output_path = './img/source.jpeg_no_bg.png'

    rmbg = RemoveBg(api_key, "error.log")
    rmbg.remove_background_from_img_file(file_path)

    if bg_color_value != (0, 0, 0):
        print('设置背景颜色')
        # 给背景加入颜色
        # 利用 PIL 库来给 PNG 图片设置背景颜色
        im = Image.open(output_path)
        width, height = im.size

        try:
            p = Image.new('RGBA', im.size, bg_color_value)
            p.paste(im, (0, 0, width, height), im)
            p.save('./img/output.png')
        except Exception as e:
            pass
    else:
        print('保持图片透明')


if __name__ == '__main__':
    bg_color = input('请输入背景颜色？（b:蓝色，r：红色，w：白色，其他：透明）')
    bg_color_value = (0, 0, 0)
    if bg_color == 'b':
        bg_color_value = (0, 0, 255)
    elif bg_color == 'r':
        bg_color_value = (255, 0, 0)
    elif bg_color == 'w':
        bg_color_value = (255, 255, 255)
    else:
        bg_color_value = (0, 0, 0)

    ps_a_img(bg_color_value)
