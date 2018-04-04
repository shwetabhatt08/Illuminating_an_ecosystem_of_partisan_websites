from bs4 import BeautifulSoup
import requests
import urllib
import pandas
import pandas as pandas
import unicodedata   
from time import sleep
import json

df = pandas.read_excel('PartisanSites.xlsx')
websites = list(set(df['site'].values))
id_referers = "keywords_upstream_site_table"
id_sites_linked = "linksin_table"

def get_table(table_id):
	for each_url in websites:
		a_dict = {}
		url = 'http://www.alexa.com/siteinfo/%s' %(str(each_url))
		upstream_list = []
		top_referrers = []
		page  = requests.get(url)
		data = page.text
		soup = BeautifulSoup(data, 'html.parser')
		upstream_table = soup.find(id=table_id).get_text()
		convert_upstream = unicodedata.normalize('NFKD', upstream_table).encode('ascii','ignore')
		upstream_data = convert_upstream.split("\n")
		for each_item in upstream_data:
			if each_item != '':
				upstream_list.append(each_item)
		referrer_list = upstream_list[2:]
		if table_id == "keywords_upstream_site_table":
			for each_referrer in referrer_list:
				top_referrers.append(each_referrer.split(' ')[4])
			a_dict[each_url] = top_referrers
			print each_url
			print "\n"
			with open('referrers.json') as f:
				data = json.load(f)
			
			data.update(a_dict)

			with open('referrers.json', 'w') as f:
				json.dump(data, f)

			print "data written"
			sleep(5)
	print "Done!"

get_table(id_referers)



