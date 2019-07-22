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

# 依赖：pip3 install removebg

api = '申请的api'


def ps_a_img():
    rmbg = RemoveBg(api, "error.log")  # 引号内是你获取的API
    rmbg.remove_background_from_img_file("./img/source.jpeg")  # 图片地址


if __name__ == '__main__':
    ps_a_img()
