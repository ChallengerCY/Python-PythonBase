#coding=utf-8

#pickle腌制过程
import pickle



#开始腌制，使用dumps(object)将对象序列化
messageA=["hello","Challenger","CY"]
messageB=pickle.dumps(messageA)
print(messageB)

#loads(object)将数据（对象和类型）都原样恢复
messageC=pickle.loads(messageB)
print(messageC)

#使用dump(object,file)将数据序列化到文件中
messageD=("hello","Challenger","CY")
file1=file("1.pk1",'wb')
pickle.dump(messageD,file1,)
file1.close()

#使用load(object,file)将文件中的数据恢复
file2=file("1.pk1",'rb')
messageE=pickle.load(file2)
print(messageE)
file2.close()