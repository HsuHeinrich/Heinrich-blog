# 常用hive函数

## 行列转换

​	[行列转换](https://blog.csdn.net/JThink_/article/details/38853573)

1. 行转列：collect_list,concat_ws
2. 列转行：select id,colAliasName  from  t1 t LATERAL VIEW explode(split(t.name,',')) tableAliasName as colAliasName

## 不同维度汇总

[不同维度汇总](http://lxw1234.com/archives/2015/04/193.htm)

GROUPING SETS,GROUPING__ID,CUBE,ROLLUP

## sql执行顺序

[sql执行顺序](https://blog.csdn.net/u014044812/article/details/51004754)

## 窗口函数原理

[窗口函数原理](https://blog.csdn.net/xiepeifeng/article/details/42676567)

## 常用hive函数

1. [常用hive函数](https://www.jianshu.com/p/62ce912e209f?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation)
2. [常用hive函数-字符串函数](https://blog.csdn.net/Zonzereal/article/details/79116800)