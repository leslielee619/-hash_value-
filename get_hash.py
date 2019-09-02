import hashlib

class get_hash:

	def __init__(self,names,types,url):
		'''
		names是一个列表，url与types是一个字符串
		比如D:/14682/Documents/python/cookbook.txt
		其中url是"D:/14682/Documents/python/"
		names是"cookbook"
		types是".txt"
		'''
		self.names=names
		self.types=types
		self.url=url

	def total_url(self):

		total_url=list()
		for name in self.names:
			file_url=self.url+name+self.types
			total_url.append(file_url)
		return total_url

	def get_md5(self):

		total_md5=dict()
		total_url=self.total_url()
		for url in total_url:
			with open(url,'rb') as file:
				md5_val=hashlib.md5(file.read())
				total_md5[url]=md5_val.hexdigest()   #用16进制来表示md5得到的哈希值
				file.close()
		return total_md5

	def save_md5(self):

		results=self.get_md5()
		save_url=self.url+"MD5_results.txt"
		for result_key,result_val in results.items():
			summary=result_key+' '*5+result_val+'\n'
			with open(save_url,'a+') as file:
				file.write(summary)
				file.close()

	def comments(self):

		save_url=self.url+"Comments.txt"
		results=self.get_md5()
		self.save_md5()
		md5s=list()
		false_md5s=list()
		false_names=list()
		for result_key,result_val in results.items():
			md5s.append(result_val)
		for md5 in md5s:
			if md5s.count(md5) >= 2:
				false_md5s.append(md5)
		for md5 in false_md5s:
			for result_key,result_val in results.items():
				if md5 == result_val:
					false_names.append(result_key)
		if len(false_names) == 0 :
			print("Today,there was noboday copy")
		else:
			false_names=set(false_names)
			print('嫌疑作业：\n',false_names)
			
		for false_name in false_names:
			cut=slice(len(self.url),len(false_name)-len(self.types))
			name=false_name[cut]
			with open(save_url,'a+') as file:
				file.write(name+'\n')
				file.close()





if __name__ == '__main__':
	names=['add_lot','dele_little','dele_lot','faye','jacky','move']
	types=".dwg"
	url="D:/14682/Documents/"
	get_hash(names,types,url).comments()

#运行了之后，可见文本只要再加一个空行就可以有不一样的哈希值，而音频，图片，视频更可以改动像素，质量等等，使得在与原版看起来差不多的前提下做到哈希值不同。
#cad中'另存为'以后哈希值就不一样了，除非只是重命名不打开cad，则哈希值相同









