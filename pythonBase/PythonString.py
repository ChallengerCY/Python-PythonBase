#coding=utf-8
#单引号
s1='CY'
print s1
#单引号之中可以使用双引号
s2='Challenger"CY"'
print s2

#双引号（双引号之中不可以使用双引号）
s3="ChallengerCY"
print s3

#三引号(可以是三个单引号也可以是三个双引号),三引号字符串可以换行使用
s4='''ChallengerCY'''
print s4
s5="""Challe
nger
CY"""
print s5

#转义符和自然字符串(原样输出字符串)
#(带转义符的字符串)
s6="Chall\nengerCY"
print s6
#(自然字符串)
s7=r"Chall\nengerCY"
print s7

#字符串的重复输出(*重复运算符)
s8="ChallengerCY"
print s8*3

#子字符串
#索引从零开始a[0]
#切片运算[a:b]是指从下标a到b-1结束，起始值为0

a="ChallengerCY"
#输出索引位置
print a[3]

#输出切片运算的值
print a[1:3]