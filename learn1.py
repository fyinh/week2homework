
# -*- coding: UTF-8 -*-

import os
import sys
#import jieba
import re
reload(sys)
sys.setdefaultencoding('utf-8')




def getfile(path,charset = 'utf-8'):
    with open(path) as f:
        lines = [line.strip().decode(charset) for line in f.readlines()]
    f.close()
    return lines

if __name__ == '__main__':
    dict_word = {}

    path = "/home/gaolao/homework/biaozhu/"
    dirs = os.listdir(path)
    for i in dirs:
        pos_words = getfile(i)
        for j in pos_words:
            if j:
                dict_word[j] = 0
                print j

    article = open('article.txt')

    for doc in article:
        words = jieba.cut(doc)
        for word in words:
            for pos_word in dict_word:
                if word == pos_word:
                    dict_word[pos_word] += 1


    for i in dict_word:
        print i + "这个词出现了" + str(dict_word[i]) + "次"
