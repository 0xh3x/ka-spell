# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 18:30:58 2016

@author: rudolf eremyan
@mail:   eremyan.rudolf@gmail.com
"""

def extractGeorgianWords(s):
    import re
    matches = re.findall('([ხელმძღქწერტყუიოპასდფგჰჯკლზხცვბნმთშჟჩძ]*-[ქწერტყუიოპასდფგჰჯკლზხცვბნმთშჟჩძ]*)|([ხელმძღქწერტყუიოპასდფგჰჯკლზხცვბნმთშჟჩძ]*)', s, re.DOTALL)
    res = [str(i[1]) for i in matches if (len(str(i[1])) > 0)]
    return res