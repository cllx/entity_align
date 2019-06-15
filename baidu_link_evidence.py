# 通过百度百科辅助对齐
import urllib.request
from urllib.parse import quote,unquote
import lxml
import lxml.etree
import time
import socket
class get_baike_page_citiao():
	# 用于在百科页面搜索是否有该关键字对应的词条，如果有则提取出词条对比
	def get_baike_page_citiao(word1, word2):
		timeout = 20    
		socket.setdefaulttimeout(timeout)#这里对整个socket层设置超时时间。后续文件中如果再使用到socket，不必再设置
		url = 'https://baike.baidu.com/item/'
		# word_1 = urllib.parse.urlencode(word1) #编码成字符串
		word_1 = urllib.parse.quote(word1)
		word_2 = urllib.parse.quote(word2)
		newurl1 = url + word_1 #拼接网址
		newurl2 = url + word_2 #拼接网址
		try:
			#time.sleep(1)
			request1 = urllib.request.Request(newurl1) #发起请求
			request2 = urllib.request.Request(newurl2)
			request1 = urllib.request.urlopen(request1)
			request2 = urllib.request.urlopen(request2)
			page1 = request1.read().decode('utf-8') #打开连接，读取信息
			page2 = request2.read().decode('utf-8')
			html1 = lxml.etree.HTML(page1) #处理文本
			html2 = lxml.etree.HTML(page2) #处理文本
			res1 = html1.xpath("//h1/text()") #res是一个列表 包含所有元素
			res2 = html2.xpath("//h1/text()") #res是一个列表 包含所有元素
			value1 = res1[0].find('百度百科错误页')
			value2 = res2[0].find('百度百科错误页')
			re_res = []
			re_res.append(value1)
			re_res.append(value2)
			re_res.append(res1[0])
			re_res.append(res2[0])
			re_res.append(html1)
			re_res.append(html2)
			request1.close()
			request2.close()
			return re_res
		except:
			re_res = [1,1]
			return re_res