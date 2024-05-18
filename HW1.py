import feedparser
import pprint

# Parse the RSS feed for tomorrow's fuel prices
feed1 = feedparser.parse('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Suburb=Cloverdale&Day=tomorrow')

data = feed1.entries

#for record in data:
	#pprint.pprint(record)

data1 = []

for record in data:
	address = record.get('address')
	brand = record.get('brand')
	price = record.get('price')

	record['day'] = 'tomorrow'

	sorted_data = {'brand1' : brand, 'address1' : address, 'price1' : price, 'day' : 'tomorrow'}

	data1.append(sorted_data)
	

print("==================")
pprint.pprint(data1)

