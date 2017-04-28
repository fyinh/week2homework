
# -*- coding:UTF-8 -*-
import re

paths = '/home/gaolao/作业/'
path1 = '/home/gaolao/作业/词典/'
path2 = '/home/gaolao/作业/太空旅客.txt'


js = ['反派','角色','角色中的其他','男主角','女主角','配角']
jq = ['发展','结局','剧情','开头','泪点','笑点']
st = ['动作','画面','镜头','视听','视听效果中的其他','音乐']
zz = ['编剧','出品公司','导演','选景','制作']
zt = ['风格','题材内容','主题']
dic = {'角色':js,'剧情':jq,'视听':st,'制作':zz,'主题':zt}


with open(paths + 'result.txt','a') as result:
    comment_result = {}
    comments = open(path2)
    for name in dic.keys():
        for s_name in dic[name]:
            words = open(path1 + s_name)
            for word in words:
                for comment in comments:
                    if word in comment:
                        comment_result[name] += 1
        result.write(name + ':' + comment_result[name]+'\n')
