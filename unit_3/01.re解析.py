import re;
import requests;

# list_=re.findall(r"\d+","我的电话号是：123,")
# print(list_)
#
# #finditer 匹配字符串中所有的内容 返回迭代器
# list_1=re.finditer(r"\d+","我的电话号是：123,他的电话是：456")
# for i in list_1:
#     print(i.group());
#
# # search 找到一个结果就返回 全文匹配
# result=re.search(r"\d+","我的电话号是：123,他的电话是：456")
# print(result)
# print(result.group())
# #match 从头开始匹配
# result_=re.match(r"\d+","我的电话号是：123,他的电话是：456")
# print(result_)
#
#
# #预加载正则表达式
# object=re.compile(r'\d+')
#
# result_1=re.finditer(r"\d+","我的电话号是：123,他的电话是：456");
# for item in result_1:
#     print(item.group())

