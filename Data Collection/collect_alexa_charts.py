import json
import os
import requests
import glob
import matplotlib.pyplot as plt
import datetime
import collections
from collections import OrderedDict
import pandas as pd
import numpy as np
from numpy import nan as NA
import requests
from selenium import webdriver
import pandas as pandas
import time

df = pandas.read_excel('PartisanSites.xlsx')
websites = list(set(df['site'].values))

s = requests.Session()
counter = 0
# store the session cookie value
cookie = {''} 

for each_url in websites:
    # remove trailing '/' if present
	if each_url[-1] == '/':
		each_url = each_url[:-1]
	if not os.path.exists('%s.json' %(each_url)):
        request = s.get('http://www.alexa.com/comparison?&sites=%s&display=json&useCookie=false&windows[]=rank:1y' (str(each_url)), cookies=cookie)
		response = request.json()
		counter += 1
		with open('%s.json' %(str(each_url)), 'w') as outfile:
			json.dump(response, outfile)
		print each_url
		print " "
		print counter
        # sleep for 2 seconds after each iteration
		time.sleep(2)
        # after 10 iterations sleep for 60 seconds
		if counter % 10 == 0:
			time.sleep(60)

print "Done!"
	


