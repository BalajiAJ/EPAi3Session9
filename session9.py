from collections import namedtuple, Counter
import random
from faker import Faker
from datetime import date, timedelta, datetime
from dateutil import relativedelta	
import time


# Using namedtuple, calculate the largest blood type, mean-current_location, oldest_person_age, and average age"
def randomprofiles_namedtuple():
	"""
	Creating 10000 fake profile and using named tuple calculating largest blood type, mean-current_location, oldest_person_age, and average age
	""" 
	fake = Faker()
	Profile = namedtuple('Profile', 'bloodgroup location birthdate')
	randomprofiles = namedtuple('randomprofiles', 'largestbloodtype meancurrentlocation oldestpersonage averageage')
	randomprofiles.__doc__ = "Named Tuple With Summary Statistics of Profile"
	randomprofiles.largestbloodtype.__doc__ = "Majority Blood Type"
	randomprofiles.meancurrentlocation.__doc__ = "Mean location of longitude and latitude co-ordinates"
	randomprofiles.oldestpersonage.__doc__ = "Oldest Age of a person in the profile"
	randomprofiles.averageage.__doc__ = "Average age of sample set"
	randprofilelist = [] 
	for i in range(10000):
		profiledata = Profile(fake.profile()["blood_group"], fake.profile()["current_location"], fake.profile()["birthdate"])	
		randprofilelist.append(profiledata)
	randomprofiles.largestbloodtype = max(Counter(elem.bloodgroup for elem in randprofilelist))
	meancurrentlocationx = (sum([x[0][0] for x in zip(elem.location for elem in randprofilelist)])/len(randprofilelist))
	meancurrentlocationy = (sum([x[0][1] for x in zip(elem.location for elem in randprofilelist)])/len(randprofilelist))
	randomprofiles.meancurrentlocation = (meancurrentlocationx,meancurrentlocationy)
	randomprofiles.oldestpersonage = max(abs(relativedelta.relativedelta(elem.birthdate,date.today())).years for elem in randprofilelist)
	randomprofiles.averageage = sum(abs(relativedelta.relativedelta(elem.birthdate,date.today())).years for elem in randprofilelist)/len(randprofilelist)
	return randomprofiles

# Using dictionary, calculate the largest blood type, mean-current_location, oldest_person_age, and average age"
def randomprofiles_dict():
	"""
	Creating 10000 fake profile and using named dictionary calculating largest blood type, mean-current_location, oldest_person_age, and average age
	"""
	fake = Faker()	
	profiledictsummary = dict(largestbloodtype=None,meancurrentlocation=None,oldestpersonage=None,averageage=None)	
	randprofilelist = [] 
	for i in range(10000):
		randomprofile = {}
		randomprofile["bloodgroup"]=fake.profile()["blood_group"]
		randomprofile["location"]=fake.profile()["current_location"]
		randomprofile["birthdate"]=fake.profile()["birthdate"]
		randprofilelist.append(randomprofile)
	profiledictsummary["largestbloodtype"] = max(Counter(elem["bloodgroup"] for elem in randprofilelist))
	meancurrentlocationx = (sum([x[0][0] for x in zip(elem["location"] for elem in randprofilelist)])/len(randprofilelist))
	meancurrentlocationy = (sum([x[0][1] for x in zip(elem["location"] for elem in randprofilelist)])/len(randprofilelist))
	profiledictsummary["meancurrentlocation"] = (meancurrentlocationx,meancurrentlocationy)
	profiledictsummary["oldestpersonage"] = max(abs(relativedelta.relativedelta(elem["birthdate"],date.today())).years for elem in randprofilelist)
	profiledictsummary["averageage"] = sum(abs(relativedelta.relativedelta(elem["birthdate"],date.today())).years for elem in randprofilelist)/len(randprofilelist)
	return profiledictsummary
		


def top100companystock():
	"""
	function that generates day open high and close index of top 100 companies using named tuple
	"""
	top100companylist = top100companydata()
	top100companyindex = namedtuple('top100companyindex', 'open high close')
	top100companyindex.__doc__ = "Represent the Chemical Index"
	top100companyindex.open.__doc__ = "Open Value of the Index"
	top100companyindex.high.__doc__ = "Highest Value of the Index"
	top100companyindex.close.__doc__ = "Closing Value of the Index"

	totalmarketvalue = sum([x.marketcap for x in top100companylist])

	top100companyindex.open = round(sum([x.open*(x.marketcap/totalmarketvalue) for x in top100companylist]),2)
	top100companyindex.high = round(sum([x.high*(x.marketcap/totalmarketvalue) for x in top100companylist]),2)
	top100companyindex.close = round(sum([x.close*(x.marketcap/totalmarketvalue) for x in top100companylist]),2)

	print(f"""top100companyindex Open Value: {top100companyindex.open}""")
	print(f"""top100companyindex High Value: {top100companyindex.high}""")
	print(f"""top100companyindex Close Value: {top100companyindex.close}""")
	print(type(top100companyindex))
	return top100companyindex


def top100companydata():
	"""
	Stock Market Values of top 100 Companies in stock market
	"""
	fake = Faker()
	Stock = namedtuple('Stock','compname marketcap date1 scrip open high close')
	Stock.__doc__ = "Represent the stock values for a particalar day"
	Stock.compname.__doc__ = "company name"
	Stock.marketcap.__doc__ = "market value of the company in billion dollars"
	Stock.date1.__doc__ = "date"
	Stock.scrip.__doc__ = "stock scrip"
	Stock.open.__doc__ = "opening value of the day"
	Stock.high.__doc__ = "highest value during the day"
	Stock.close.__doc__ = "closing value of the day"
	top100complist = []
	for _ in range(100):
		compname= fake.company()
		marketcap = round(random.uniform(1,100),2)
		date1 = str(date.today())
		scrip = compname[0:3]
		open = round(random.uniform(100,3000),2)
		high = open + (open * random.randint(1,5))/100
		close = high + (high * random.randint(-5,0))/100
		stockparam = Stock(compname =compname,
					marketcap=marketcap,
					date1 = date,
					scrip= scrip,
					open=open,
					high=high,
					close=close
					)

		top100complist.append(stockparam)	

	return top100complist


# if __name__ == '__main__':
	# start = time.perf_counter()
	# summaryprofilenamedtup = randomprofiles_namedtuple()
	# print(type(summaryprofilenamedtup.meancurrentlocation))
	# end = time.perf_counter()
	# print("Total Time Taken for Named Tuple:" + str(end-start))
	# print(summaryprofilenamedtup.__doc__)
	# start_dict = time.perf_counter()
	# summaryprofiledict = randomprofiles_dict()
	# end_dict = time.perf_counter()
	# print("Total Time Taken for Dictionary:" + str(end_dict-start_dict))