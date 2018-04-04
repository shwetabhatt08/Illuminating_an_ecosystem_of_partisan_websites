#!/usr/bin/env python
import requests
import xmltodict, json
import xmljson
from xmljson import badgerfish as bf
import json
from json import dumps
from xml.etree.ElementTree import fromstring
import pandas
import io
import os.path
try:
	to_unicode = unicode
except NameError:
	to_unicode = str

# read the excel file in pandas
df = pandas.read_excel('PartisanSites.xlsx')
# extract website names in a list
websites = df['site'].values


for each_url in websites:
    # remove trailing '/'
	if each_url[-1] == '/':
		each_url = each_url[:-1]
	if not os.path.exists('%s.json' %(each_url)):
        # get the response for each website
		response = requests.get('http://data.alexa.com/data?cli=10&dat=snbamz&url=%s' %(str(each_url)))
        # convert xml to json
		data =  bf.data(fromstring(response.content))
        # save the contents in a json file
		with open('%s.json' %(str(each_url)), 'w') as outfile:
			json.dump(data, outfile)
		print each_url
print "Completed!"



