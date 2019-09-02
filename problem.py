#python中的id函数，hash函数，以及hash，mad5？
a=1
b=1
hash_a=hash(a)
id_a=id(a)
hash_b=hash(b)
id_b=id(b)
print("a=1\nhash_value:{},\nid_value:{}".format(hash_a,id_a))
print("-"*20)
print("b=1\nhash_value:{},\nid_value:{}".format(hash_b,id_b))
#----------------------------------------------------------------
a=int(1)
b=float(1)

a=int(1)
b=bool(1)

a=int(1)
b=str(1)

a=int(1)
b=complex(1)

a='1'
b=str(1)
#a与b的哈希值相同，地址不同
#python中只有不可变的数据类型才有哈希值

a='1'
b=('1')

a=1
b=1
#a与b的哈希值与地址相同
#哈希运算是将任意长度的二进制值映射为较短的固定长度的二进制值。这个二进制值称为哈希值。
#哈希算法又称摘要算法，散列算法。python的库hashlib有哈希算法：md5,sha-1,sha-256,sha-384,sha-512。

a=('1')
b='1'
a_ascii=ord(a)
b_ascii=ord(b)
print("ascii:{}".format(a_ascii))
print("-"*20)
print("ascii:{}".format(b_ascii))
#得到a与b所对应的ascii值是49，查表后得知也就是字符1。且只有字符型，元组里的单个字符才有ascii码

def avg():
	return 1
hash(avg()) 
#avg函数哈希值为1

def avg(a):
	return sum(a)/len(a)
a=[1,2,3]
hash(avg(a))
#哈希值为2

class calc:
	def avg():
		return 1
hash(calc)
hash(calc.avg())
#证明类，类的方法，函数都是有哈希值的。如果有return的话，哈希值就是return的那个值。

with open("D:/14682/Documents/copy_leslielee.txt") as file1:
	print(hash(file1),id(file1))
with open("D:/14682/Documents/leslielee.txt") as file2:
	print(hash(file2),id(file2))
with open("D:/14682/Documents/save_leslielee.txt") as file3:
	print(hash(file3),id(file3))
with open("D:/14682/Documents/false_leslielee.txt") as file4:
	print(hash(file4),id(file4))
#四个文件的地址很近，哈希值复制与另存的很接近，哈希值原版与原样重写后的相近

import hashlib

with open("D:/14682/Documents/圆的渐开线.dwg",'rb') as file1:
	md5_val=hashlib.md5(file1.read())
	print('md5:',md5_val.hexdigest())
	print("hash:",hash(file1.read()))
	print('-'*20)
with open("D:/14682/圆的渐开线.dwg",'rb') as file2:
	md5_val=hashlib.md5(file2.read())
	print('md5:',md5_val.hexdigest())
	print("hash:",hash(file2.read()))
	print('-'*20)
#相同文件的哈希值相同，即使重新改一个名字


# python与matlab数据类型比较
# python:
# immutable:number(int,float,bool,complex),string,tuple
# mutable:list,set,dictionary
# md5,id(),hash()

# matlab:
# number:int(int8,uint8,16,32,64),float(single,double),logical,char,[],{},struct,function,class,java class

# 注：single和double区别是字节不同，所表示的数值范围就不同

# python中的id函数，hash函数，以及hash，mad5？
#编写一个函数，手动输入文件名，然后获取所有文件哈希值

# from PIL import Image

# path = "D:/tmp/1.jpg"
# img = Image.open(path)
# img.save(path, quality=95) 
# 保存图片时的质量最大为100，但是95也看不出差异，而且文件体积更精简。可以通过修改图片质量而修改了哈希值

#符号编码系统ascii gbk unicode utf-8