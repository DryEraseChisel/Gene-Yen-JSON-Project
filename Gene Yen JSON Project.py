# JSON exercise
# Using data in file 'data/world_bank_projects.json' and the techniques demonstrated above,

# 1.	Find the 10 countries with most projects
# 2.	Find the top 10 major project themes (using column 'mjtheme_namecode')
# 3.	In 2. above you will notice that some entries have only the code and the name is missing. Create a dataframe with the missing names filled in.

import pandas as pd 
import numpy as np 
import json
import requests
from collections import Counter
#	first step: import world bank data

url = 'https://raw.githubusercontent.com/DryEraseChisel/Gene-Yen-JSON-project/master/world_bank_projects.json'
r = requests.get(url)
worldbank_data = r.json()
worldbank_raw = pd.DataFrame(worldbank_data)

# Export to excel file to help better visualize the data structure
# from pandas import ExcelWriter

# writer = ExcelWriter('worldbank_raw.xlsx')
# worldbank_raw.to_excel(writer, 'Sheet1')
# writer.save()

#### Question 1. #### 

most_projects = worldbank_raw['countrycode'].value_counts(dropna=False)
print("Country with most projects ", most_projects[0:1])

#### Question 2. ####

theme_count = {}

for r in worldbank_raw['mjtheme_namecode']:
	for e in r:
		if e['code'] in theme_count:
			theme_count[e['code']] += 1
		else:
			theme_count[e['code']] = 1
print(theme_count)
print(dict(Counter(theme_count).most_common(10)))

theme_name = {}

for r in worldbank_raw['mjtheme_namecode']:
	for e in r:
		if e['code'] not in theme_name:
			if e['name'] != '':
				theme_name[e['code']] = e['name']

print(theme_name)

#### Question 3. #####

for r in worldbank_raw['mjtheme_namecode']:
	for e in r:
		if e['name'] == '':
			e['name'] = theme_name[e['code']]

print(worldbank_raw['mjtheme_namecode'][0])
