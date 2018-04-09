# SimpleApriori
Apriori的简单实现，修正多次，python27可直接运行。

需求库：json

## newApriori.py

该部分提供了输入简单元素集合list的接口，调用方法为

```list=newApriori.apriori(D,minSub)```

返回的list为所有符合minsub支持度的频繁项集合

D的例子如下：

```D=[["a","b","c"],["a","c","d"],["a","d"]]```

该部分代码注释非常详细，中间有注释修改之前的代码，可供入门的同学参考

解决了多个元素之间生成频繁项剪枝与连接计数出现的问题，经过多次测试，可以应对多元素频繁项的关联规则分析。

## datahandle.py

readfile部分实现了将json转化为上述输入的list类型

main函数下方，有对关联规则和置信度，支持度的计算。原理及其简单



提供了输入的json文件，data.json，直接运行datahandle即可。