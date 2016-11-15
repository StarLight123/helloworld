# -*- coding: utf-8 -*-

x1=1
d=3
sum=0
i=0
for i in range(5):
	sum=sum+x1
	x1=x1+d
	i=i+1
print sum

print r'''"to be or not to be":that is the question.
Whether it 's nobler in the mind to suffer
djsahfdngakdhgl
'''

print u"中"

# %d整数,%f浮点数,%s字符串,%x十六进制整数 格式化规则 %作%的转义
print "hello %s ,are you %d years old!" %(u"厅",15)
print "hello %s ,are you %d years old! %%" %("sdga",15)

#python 的布尔运算是只要能提前确定的计算结果，就自然不会再往下计算，直接返回确定的值
#python 把0 空字符串 None(空字符串)当作false
a="python"
print 'hello',a or 'world'

b=''
print "hello,",b or "world"
