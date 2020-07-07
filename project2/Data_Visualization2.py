
import codecs
import re
from matplotlib import pyplot 
import datetime
import time
import numpy as np
import codecs
import argparse

def test_for_sys(fil,memory,cpu,summary):
    def mmm(f,m):##############################
        tim=[]
        mem=[]
        memfree=[]
        list_file1=[]
        dat="none"
        with codecs.open("%s"%(fil),"r","gbk") as fileText:
            text=fileText.readlines()
        for fileline in text:
            list_TIM=re.findall("ZZZZ",fileline,re.S)
            if list_TIM:
                list_file1.append(fileline)
        for t in list_file1:
            m=[time for time in re.split('[,]',t)]
            tim.append(m[2])
            dat=m[3]
        for fileline in text:
            list_MEM=re.findall("MEM,T",fileline,re.S)
            if list_MEM:
                mem.append(fileline)
        memtotal=0
        for t in mem:
            m=[i for i in re.split('[,]',t)]
            memfree.append(m[6])
            memtotal=m[2]

        memfree=list(map(eval,memfree))
        ti=[i for i in range(len(tim))]

        pyplot.rcParams['figure.figsize'] = (15.00, 6.00)
        pyplot.plot(tim,memfree,linewidth=2)
        pyplot.title("Memory MB localhost %s "%(dat))
        pyplot.xlabel('time series')
        pyplot.ylabel('memfree(memtotal:%s)'%(memtotal))
        pyplot.xticks(tim[::3],rotation=90)
        pyplot.legend(["memfree"], loc="best")
        if not ".png" in str(memory):
            pass   
        else:
            pyplot.savefig("%s"%(memory))
        pyplot.clf()
    mmm(fil,memory)
    def ccc(f,c):#####################################
        tim=[]
        list_file1=[]
        dat="none"
        with codecs.open("%s"%(fil),"r","gbk") as fileText:
            text=fileText.readlines()

        for fileline in text:
            list_TIM=re.findall("ZZZZ",fileline,re.S)
            if list_TIM:
                list_file1.append(fileline)
        for t in list_file1:
            m=[time for time in re.split('[,]',t)]
            tim.append(m[2])
            dat=m[3]

        ccpu=[]
        for fileline in text:
            cpuu=re.findall("CPU_ALL",fileline,re.S)
            if cpuu:
                ccpu.append(fileline)

        a=[]
        b=[]
        c=[]
        d=[]
        e=[]
        f=[]
        al=[a,b,c,d,e,f]
        for t in ccpu:
            m=[i for i in re.split('[,]',t)]
            a.append(m[2])
            b.append(m[3])
            c.append(m[4])
            d.append(m[5])
            e.append(m[6])
            f.append(m[7])   
        for y in al:
            y.remove(y[0])
        a=np.array(list(map(eval,a)))
        b=np.array(list(map(eval,b)))
        c=np.array(list(map(eval,c)))
        d=np.array(list(map(eval,d)))
        e=np.array(list(map(eval,e)))
        CPU=[]
        for i in range(0,len(a)):
            summm=float(a[i])+float(b[i])
            CPU.append(summm)############


        num = 1   #这里指的是柱子粗细
        ti=np.array([i for i in range(len(tim))])
        pyplot.rcParams['figure.figsize'] = (15,6)
        pyplot.bar(ti, a, num, color = 'blue')
        pyplot.bar(ti, b, num, bottom = a,           
                color = 'orange', label = 'b')
        pyplot.bar(ti, c, num, bottom = (b+a),
                color = 'grey', alpha = 0.5,label = 'c')
        pyplot.bar(ti, d, num, bottom = (b+a+c), 
                color = 'gold', alpha = 0.5,label = 'c')
        pyplot.bar(ti, e, num, bottom = (b+a+c+d), 
                color = 'red', alpha = 0.5,label = 'c')
        pyplot.xticks(np.arange(1,len(tim),3),tim[::3],rotation=90)#####
        pyplot.legend()
        pyplot.title("CPU Total localhost %s"%(dat))
        pyplot.xlabel("time series")
        pyplot.ylabel("Utilization (%)")
        pyplot.legend(["User%","Sys%","Wait%","Idle%","Steal%","Busy"], loc="best")
        
        if not ".png" in str(cpu):
            pass
        else:
            pyplot.savefig("%s"%(cpu))#CPU
        pyplot.clf()
    ccc(fil,cpu)

    def sss(f,s):

        tim=[]
        list_file1=[]
        dat="none"
        with codecs.open("%s"%(fil),"r","gbk") as fileText:
            text=fileText.readlines()

        for fileline in text:
            list_TIM=re.findall("ZZZZ",fileline,re.S)
            if list_TIM:
                list_file1.append(fileline)
        for t in list_file1:
            m=[time for time in re.split('[,]',t)]
            tim.append(m[2])
            dat=m[3]

        ccpu=[]
        for fileline in text:
            cpuu=re.findall("CPU_ALL",fileline,re.S)
            if cpuu:
                ccpu.append(fileline)

        a=[]
        b=[]
        c=[]
        d=[]
        e=[]
        f=[]
        al=[a,b,c,d,e,f]
        for t in ccpu:
            m=[i for i in re.split('[,]',t)]
            a.append(m[2])
            b.append(m[3])
            c.append(m[4])
            d.append(m[5])
            e.append(m[6])
            f.append(m[7])   
        for y in al:
            y.remove(y[0])
        a=np.array(list(map(eval,a)))
        b=np.array(list(map(eval,b)))
        c=np.array(list(map(eval,c)))
        d=np.array(list(map(eval,d)))
        e=np.array(list(map(eval,e)))
        CPU=[]
        for i in range(0,len(a)):
            summm=float(a[i])+float(b[i])
            CPU.append(summm)############
        ddisk=[]

        for fileline in text:
            diskk=re.findall("DISKXFER,T",fileline,re.S)
            if diskk:
                ddisk.append(fileline)
        D1=[]
        D2=[]
        D3=[]
        D4=[]
        D5=[]
        D6=[]
        D7=[]
        D8=[]
        E8=[]

        for t in ddisk:
            m=[i for i in re.split('[,]',t)]
            D1.append(m[2])
            D2.append(m[3])
            D3.append(m[4])
            D4.append(m[5])
            D5.append(m[6])
            D6.append(m[7])
            D7.append(m[8])
            D8.append(m[9])
        for d5 in D5:
            r=re.sub("[\n]", "", d5) 
            E8.append(r)#去掉\n
        D1=list(map(eval,D1))
        D2=list(map(eval,D2))
        D3=list(map(eval,D3))
        D4=list(map(eval,D4))
        D5=list(map(eval,D5))
        D6=list(map(eval,D6))
        D7=list(map(eval,D7))
        E8=list(map(eval,E8))
        
        y2=[]
        for dd in range(0,len(D1)):
            summm=D1[dd]+D2[dd]+D3[dd]+D4[dd]+D5[dd]+D6[dd]+D7[dd]+E8[dd]
            y2.append(summm)
        y1= CPU 

        fig,ax1 = pyplot.subplots()
        ax2 = ax1.twinx()           # 做镜像处理
        ax1.plot(tim,y1,'b-',linewidth=2.5)
        ax2.plot(tim,y2,'m-',linewidth=2.5)
        ax1.set_xlabel('Time series')    #设置x轴标题
        ax1.set_ylabel("usr%s+sys%s"%("%","%"),color = 'b')   #设置Y1轴标题
        ax2.set_ylabel('Disk xfers',color = 'm')  
        ax1.set_ylim(0, 100)#用此方法来修改刻度 获得更好的对比效果
        for tick in ax1.get_xticklabels():
            tick.set_rotation(90)
        pyplot.xticks(tim[::3])
        pyplot.rcParams['figure.figsize'] = (20,8)
        pyplot.title("System Summary perftest %s"%(dat))
        
        
        if not ".png" in str(summary):
            pass
        else:
            pyplot.savefig("%s"%(summary))#CPU
        pyplot.clf()
    sss(fil,summary)


parser = argparse.ArgumentParser(description='Test for argparse')
parser.add_argument('--fil', '-f', help='导入nmon文件 必要')
parser.add_argument('--memory', '-m', help='内存性能 非必要')
parser.add_argument('--cpu', '-c', help='CPU性能 非必要')
parser.add_argument('--summary', '-s', help="性能概要 非必要")
args = parser.parse_args()
if __name__ == '__main__':
    try:
        test_for_sys(args.fil,args.memory, args.cpu, args.summary)
    except Exception as e:
        print(e)
#eg：python Data_VIsualization2.py -f eg.nmon -m mem.png -c cpu.png -s summary.png 
