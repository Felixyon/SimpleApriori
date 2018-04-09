# coding=utf-8

def apriori(D, minSup):
    '''频繁项集用keys表示，
    key表示项集中的某一项，
    cutKeys表示经过剪枝步的某k项集。
    C表示某k项集的每一项在事务数据库D中的支持计数
    '''

    C1 = {}##设计对象，统计每个元素（作为键）的频数（值）
    for T in D:
        for I in T:
            if I in C1:
                C1[I] += 1
            else:
                C1[I] = 1
    print('\n元素频数统计：\n')
    for key, values in C1.items():
        print key, values
    _keys1 = C1.keys()#将所有的元素赋值给_key1生成新的list

    keys1 = []
    for i in _keys1:
        keys1.append([i])##将每个元素转化为list存入keys1

    n = len(D)#输入购物清单的数量
    cutKeys1 = []
    for k in keys1[:]:
        if C1[k[0]] * 1.000 / n >= minSup:
            cutKeys1.append(k)  #第一步剥离，将所有元素集合中支持度超过设定的元素首先存放到cutkeys1的list里面

    cutKeys1.sort()#证明该排序仅仅是通过list中存放元素的首字母进行排序

    keys = cutKeys1 #将排序好的第一步剥离的单个符合支持度的元素赋值给keys
    all_keys = []
    while keys != []:
        C = getC(D, keys)#C为得到的keys的计数数组list
        print(len(keys))#输出当前keys的长度
        cutKeys = getCutKeys(keys, C, minSup, len(D))
        print('剪枝后keys长度')
        print(len(cutKeys))
        print(cutKeys)
        for key in cutKeys:
            all_keys.append(key)#所有频繁项目集的元素
        keys = aproiri_gen(cutKeys)

    return all_keys


def getC(D, keys):
    '''对keys中的每一个key进行计数'''
    C = []
    for key in keys:
        c = 0
        # for T in D:
        #     have = True
        #     for k in key:
        #         if k not in T:
        #             have = False##发现问题，该过程只适用于单个键值的匹配
        #             break
        #     if have:
        #         c += 1
        for each in D:
            num1 = 0
            for eac in key:
                num1 = num1 + each.count(eac)
            if (num1 == len(key)):
                c+=1
        C.append(c)
    print(C)
    return C


def getCutKeys(keys, C, minSup, length):
    '''剪枝步'''
    #本来remove的逻辑就是有问题的，应该尝试把成功的部分放入新的数组
    newkeys=[]
    for i, key in enumerate(keys):
        if (((C[i]*1.000/length)< minSup)!=True):
            newkeys.append(key)
    return newkeys


def keyInT(key, T):
    '''判断项key是否在数据库中某一元组T中'''
    for k in key:
        if k not in T:
            return False
    return True


def aproiri_gen(keys1):
    '''连接步'''
    keys2 = []
    for k1 in keys1:
        for k2 in keys1:
            if k1 != k2:
                key = []
                for k in k1:
                    if k not in key:
                        key.append(k)
                for k in k2:
                    if k not in key:
                        key.append(k)
                key.sort()
                if key not in keys2:
                    keys2.append(key) #非常简单的连接过程，将任意数量的key连接
    return keys2