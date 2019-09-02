
import hashlib

file1='D:/14682/Documents/faye.dwg'
file2='D:/14682/Documents/leslie.dwg'
file3='D:/14682/Documents/jacky.dwg'
file_urls=[file1,file2,file3]

class divide_into:

	def __init__(self,names,types,url):
		self.names=names
		self.types=types
		self.url=url

	def get_binary(self):
		binary_list=list()
		hash_list=list()
		file_urls=list()
		hash_dict=dict()
		for name in self.names:
			file_url=self.url+name+self.types
			file_urls.append(file_url)
			with open(file_url,'rb') as file:
				binary_list=file.read().splitlines()
				for binary in binary_list:
					md5_value=hashlib.md5(binary).hexdigest()
				# sha256_value=hashlib.sha256(md5_value.encode('utf-8')).hexdigest()
					hash_list.append(md5_value)
			hash_dict[name]=hash_list                #将二进制文件的每行转为md5再将md5转化为sha256
			hash_list=list()                         #此方法将列表清空，且不删除原来列表所赋的值
		# print(hash_dict)
		return hash_dict

	def compare(self,repeat=0.5):
		name1_list=list()
		name2_list=list()
		false_names=list()
		hash_dict=self.get_binary()

		for name1 in self.names:
			name1_list=hash_dict[name1]
			for name2 in self.names:
				name2_list=hash_dict[name2]
				name1_set=set(name1_list)
				name2_set=set(name2_list)
				same=len(name1_set-name2_set)+len(name2_set-name1_set)
				percent1=same/len(name1_list)
				percent2=same/len(name2_list)
				if percent1 >= repeat and percent2 >= repeat and name1 != name2 and percent2<=1 and percent1<=1:
					false_names.append(name1+'-'*5+name2)
					# false_names.append(name2)
		if set(false_names)!=set():
			return set(false_names)
		else:
			sentence="没有查出互相抄袭，请降低重复度继续查询"
			return sentence




if __name__ == '__main__':
	url='D:/14682/Documents/'
	names=[]                        
	types=''                #'.txt'
	repeat=0.1
	hash_dict=divide_into(names,types,url).compare(repeat)
	print(hash_dict)

#现在想实现：比较字典的每个值，这个值是列表，如果哪几个列表重复度高达80%，则判定这几个列表相似
#学习到了集合的运算
#cad文件另存为，两文件重复度为0.7
#三个完全不同零件，其cad文件的重复度为0

