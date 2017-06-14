#coding=utf-8

#逻辑行和物理行

#以下是物理行
print "abc"
print "789"
print "777"

#以下是一个物理行 三个逻辑行，所有的逻辑行都要有分号，但是每个物理行的行末可以省略
print "abc" ;print "789" ; print "777"

#以下是一个逻辑行,三个理行
print """1
2
3"""

#使用\可以进行行链接
print"1\
     2 \
     3"

