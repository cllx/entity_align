#description: 从字符串中提取省市县等名称,用于从纯真库中解析解析地理数据
import re
import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
#匹配规则必须含有u,可以没有r
#这里第一个分组的问号是懒惰匹配,必须这么做
#注意在linux下PATTERN = ur're'
def split_place(data_list):
    PATTERN = r'([\u4e00-\u9fa5]{2,5}?(?:省|自治区|市)){0,1}([\u4e00-\u9fa5]{2,7}?(?:区|县|州)){0,1}([\u4e00-\u9fa5]{2,7}?(?:村|镇|街道)){1}'
    for data in data_list:
        #data_utf8 = data.decode('utf8')
        data_utf8 = data
        print ("   ",data_utf8)
        country = data
        province = ''
        city = ''
        district = ''
        #pattern = re.compile(PATTERN3)
        pattern = re.compile(PATTERN)
        m = pattern.search(data_utf8)
        if not m:
            print ("   ",country + '|||')
            continue
        #print m.group()
        country = '中国'
        if m.lastindex >= 1:
            province = m.group(1)
        if m.lastindex >= 2:
            city = m.group(2)
        if m.lastindex >= 3:
            district = m.group(3)
        out = '%s|%s|%s|%s' %(country, province, city, district)
        print ("   ",out)
    pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)