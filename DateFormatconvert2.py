class DateFormatHelper2():
	def str2date(str_date):
		str_date=str_date.strip()
		year=1900
		month=1
		day=1
		if(len(str_date)>11):
			str_date=str_date[:11]
		if len(str_date)==4 or len(str_date)==5:
			str_date = str_date.strip()
			year = str_date[:4]
			return year
		if(str_date.find('-')>0):
			year=str_date[:4]
			if(year.isdigit()):
				year=int(year)
			else:
				year=0
				#year = None
			month=str_date[5:str_date.rfind('-')]
			if(month.isdigit()):
				month=int(month)
			else:
				month=0
				#month = None
			if(str_date.find(' ')==-1):
				day=str_date[str_date.rfind('-')+1:]
			else:
				day=str_date[str_date.rfind('-')+1:str_date.find(' ')]
			if(day.isdigit()):
				day=int(day)
			else:
				day=0
				#day = None
		elif(str_date.find('年')>0):
			year=str_date[:4]
			if(year.isdigit()):
				year=int(year)
			else:
				year=0
				#year = None
			month=str_date[5:str_date.rfind('月')]
			if(month.isdigit()):
				month=int(month)
			else:
				month=0
				#month = None
			day=str_date[str_date.rfind('月')+1:str_date.rfind('日')]
			if(day.isdigit()):
				day=int(day)
			else:
				day=0
				#day = None
		elif(str_date.find('/')>0):
			year=str_date[:4]
			if(year.isdigit()):
				year=int(year)
			else:
				year=0
				#year = None
			month=str_date[5:str_date.rfind('/')]
			if(month.isdigit()):
				month=int(month)
			else:
				month=0
				#month = None
			if(str_date.find(' ')==-1):
				day=str_date[str_date.rfind('/')+1:]
			else:
				day=str_date[str_date.rfind('/')+1:str_date.find(' ')]
			if(day.isdigit()):
				day=int(day)
			else:
				day=0
				#month = None
		elif(str_date.find('.')>0):
			year=str_date[:4]
			if(year.isdigit()):
				year=int(year)
			else:
				year=0
				#year = None
			month=str_date[5:str_date.rfind('.')]
			if(month.isdigit()):
				month=int(month)
			else:
				month=0
				#month = None
			if(str_date.find(' ')==-1):
				day=str_date[str_date.rfind('.')+1:]
			else:
				day=str_date[str_date.rfind('.')+1:str_date.find(' ')]
			if(day.isdigit()):
				day=int(day)
			else:
				day=0
				#day = None
		else:
			year=1900
			month=1
			day=1
		if month<10:
			month=str(month)
		if day<10:
			day=str(day)
		return '%s-%s-%s' % (year,month,day)