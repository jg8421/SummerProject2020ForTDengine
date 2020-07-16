"""
abc.xml是示例文件 里面也需要更改
filepath:html文件的存放目录
index：网页主页
open('files/abc.xml',"r+")：xml文件目录
fil = open('files/abc.xml','w+')此行比较靠下 在第70行左右 也需要根据实际更改xml文件目录
start一行可以根据需求改变author名称、网页标题名称 原本是用年月日时间作为标题（python内置time模块）
需要pip下载以下模块
xml文件中不可以写入注释文件（否则出现'gbk' codec can't decode byte 0xa4 in position 326: illegal multibyte sequence错误）
xml文件中第四行需要修改网站主页地址，第1,2,6和文档的最后两行不可更改 文件中有一个示例item 
实际测试时，RSS更新有十几分钟的延迟
xml文件更新命令行操作：     python update.py
原理：每次执行此文件，程序会自动比对报告文件目录下文件和xml文件中已有文件的差别，将xml中没有，而文件目录中有的文件编译成xml格式并写入xml文档，实现更新
"""
import os
import time
import datetime
import argparse

def update_RSS():
    def readname():
        filePath = 'files'##此处更改文件的存放目录######################
        name = os.listdir(filePath)
        return name
    file_listt=[]
    if __name__ == "__main__":
        name = readname()
        file_listt.append(name)
    fil=[]
    for i in file_listt:
        fil=i
    files=[]
    for i in fil:
        if "TestReport" in i and ".html" in i:
            files.append(i)
    #print(files)#此处为文件夹中的所有文件
    #以上实现将名称装进列表
    webs=[]
    index="http://www.runoob.com"##此处更改部署服务器主页###############################
    for i in files:
        webs.append(index+"/"+i)
    #print(webs)#此处为根据网站主页生成的网址
    with open('files/abc.xml',"r+") as f:###此处更改xml文件##################################
        st = f.readlines() 
    #print(st[-2])
    it=[]
    lin=[]
    for row in st:
        if index in row:
            lin.append(row)
    linn=[]
    for i in lin:
        m=i.replace("<link>","")
        n=m.replace("</link>","")
        linn.append(n)
    add_=list(set(webs).difference(set(linn)))#前面列表有 后面列表中没有的 生成新的列表cha
    start="\n<item>\n<title>%s</title>\n<author>tester</author>\n"%(time.strftime("%Y/%m/%d")+" "+ time.strftime("%H:%M:%S"))
    ##start一行可以根据需求改变author名称、网页标题名称###############################
    end="\n</item>"
    updates=[]
    for t in add_:
        updates.append(start+"<link>"+t+"</link>"+end)
    #print(updates)
    updates.append("\n</channel>")
    updates.append("\n</rss>")
    #print(updates)
    st[-2:]=""
    #此处需要注意是两次删除最后一行 即删除最后两行
    f.close()
    fil = open('files/abc.xml','w+')##此处也要更改xml文件地址#####################################
    fil.writelines(st)
    fil.writelines(updates)

parser = argparse.ArgumentParser(description='update_the_xml_file')
args = parser.parse_args()
if __name__ == '__main__':
    try:
        update_RSS()
    except Exception as e:
        print(e)







