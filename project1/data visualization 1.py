import seaborn as sns 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
import time
import argparse
def test_for_sys(test,reference, output):
    def draw(a,b,c):
        font1 = {
        'weight' : 'normal',
        'size'   : 8
        }
        font2 = {
        'weight':'normal',
        'size': 8}
        plt.rcParams['figure.figsize'] = (10.24, 7.68)
        plt.rcParams['image.cmap'] = 'Red'
        plt.rcParams.update({"font.size":8,'font.weight' : 'normal'})
        sns.set_style("whitegrid")
        names=["Date","Case1","Case2","Case3","Case4","Case5"]        
        Ref=pd.read_csv("%s"%(b),names=names,dtype={"Date":object})
        Exp=pd.read_csv("%s"%(a),names=names,dtype={"Date":object})
        plt.subplots_adjust(hspace=0.2,wspace=0.4)
        plt.subplot(2,1,1)
        dates = list(Exp["Date"])
        #dates = [ str(x) for x in dates ]
        #date =list((datetime.strptime(a, '%Y%m%d').strftime('%m/%d/%Y') for a in dates)) 
        #转化成'06/16/2020‘这种格式
        plt.plot(dates,list(Exp['Case1']),marker= '+',label='Case1',linestyle='-',linewidth=1.5,ms=4)
        labels=dates
        plt.xticks(dates, labels)
        plt.plot(dates,Exp['Case1'],marker= '<',label='Case2',linestyle='-',linewidth=1.5,ms=4)
        plt.plot(dates,Exp['Case3'],marker= 'D',label='Case3',linestyle='-',linewidth=1.5,ms=4)
        plt.plot(dates,Exp['Case4'],marker= '*',label='Case4',linestyle='-',linewidth=1.5,ms=4)
        plt.plot(dates,Exp['Case5'],marker= 'd',label='Case5',linestyle='-',linewidth=1.5,ms=4)
        plt.legend(loc='best')
        plt.xlabel('Date',font1)
        plt.ylabel('value',font1)
        Bar_Compare=Ref.append(Exp.iloc[-1]) 
        plt.subplot(2,5,6)
        sns.barplot(x="Date",y="Case1",data=Bar_Compare,hue=["before","after"])
        plt.xlabel('Case1',font2)
        plt.ylabel('value',font2)
        plt.subplot(2,5,7)
        sns.barplot(x="Date",y="Case2",data=Bar_Compare,hue=["before","after"])
        plt.xlabel('Case2',font2)
        plt.ylabel('value',font2)
        plt.subplot(2,5,8)
        sns.barplot(x="Date",y="Case3",data=Bar_Compare,hue=["before","after"])
        plt.xlabel('Case3',font2)
        plt.ylabel('value',font2)
        plt.subplot(2,5,9)
        sns.barplot(x="Date",y="Case4",data=Bar_Compare,hue=["before","after"])
        plt.xlabel('Case4',font2)
        plt.ylabel('value',font2)
        plt.subplot(2,5,10)
        sns.barplot(x="Date",y="Case5",data=Bar_Compare,hue=["before","after"])#hue:legend
        plt.xlabel('Case5',font2)
        plt.ylabel('value',font2)
        plt.savefig("%s"%(c))#自动保存图片
        plt.show()
    draw(test,reference, output)
parser = argparse.ArgumentParser(description='Test for argparse')
parser.add_argument('--test', '-s', help='name 属性 必要参数 实验文件')
parser.add_argument('--reference', '-r', help='year 属性，必要参数 参照文件')
parser.add_argument('--output', '-o', help='body 属性，非必要参数 导出图片')
args = parser.parse_args()
if __name__ == '__main__':
    try:
        test_for_sys(args.test, args.reference, args.output)
    except Exception as e:
        print(e)
#eg：python 11.py -s C:\Users\jg\Desktop\test.csv -r C:\Users\jg\Desktop\ref.csv -o fsfs.png
