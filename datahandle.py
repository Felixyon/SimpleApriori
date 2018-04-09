# coding=utf-8
import json
import newapriori
import sys
reload(sys)
sys.setdefaultencoding("utf8")
def readfile(str):
    with open(str) as f:
        alllines=f.readlines()
        text=''.join(alllines)
        jsonarray=json.loads(text)
        arraynum=len(jsonarray)
        id1=jsonarray[0]["OrderID"]
        finallist=[]
        element=[]
        for num in range(0,arraynum):
            if(jsonarray[num]["OrderID"]==id1):
                element.append(jsonarray[num]["ProductName"])
            else:
                finallist.append(element)
                element=[]
                id1=jsonarray[num]["OrderID"]
                element.append(jsonarray[num]["ProductName"])
        linenum=1
        lineheader='购物单 {}'
        for each in finallist:
            print(lineheader.format(linenum))
            print(','.join(each))
            linenum=linenum+1

        return finallist



if __name__ == '__main__':
    D=readfile('data.json')
    F=newapriori.apriori(D,0.009)
    print('\n频繁项目集：')
    for each in F:
        print(','.join(each))
    print('\n 关联规则元素集：\n')
    ##处理D集合
    miniD=[]
    for eeg in D:
        for eegg in eeg:
            item=eegg
            miniD.append(item)

    for each2 in F:
        if(len(each2)>1):
            print(','.join(each2))
            if(len(each2)==2):
                former=each2[0]
                latter=each2[1]
                num1=miniD.count(former)##统计former出现的次数
                num2=0  ##统计latter和former同时出现的次数
                num3=0  ##统计latter直接出现的次数
                for nng in D:
                    if((nng.count(former)>0)and(nng.count(latter)>0)):
                        num2=num2+1
                for ngg in D:
                    if((ngg.count(latter)>0)):
                        num3=num3+1
                word='置信度为：{}'
                rate=num2*1.000/num1
                print(word.format(rate))
                word2='支持度为：{}'
                rate2=num2*1.000/num3
                print(word2.format(rate2))
