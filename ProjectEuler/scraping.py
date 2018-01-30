import requests
from bs4 import BeautifulSoup as bs
import urllib3
urllib3.disable_warnings()

def get_soup(url) :
	
	headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7',
	}	

	res = requests.get(url, headers=headers,verify=False)	
	
	if res.status_code == 200 :
		soup = bs(res.text,"lxml")
		return soup
	else :
		msg = "Problem at get_soup"
		return "request_error : " + str(res.status_code)


'''
result = requests.get("http://theverge.com",verify=False)
if result.status_code == 200:
	print(result.status_code)

	c = result.content

	soup = BeautifulSoup(c)
	samples = soup.find_all("cell col span-1-2 alignBot right-col")
	print(samples)

else:
	print(result.status_code)
'''

url = 'https://projecteuler.net/countries'
soup = get_soup(url)

print(soup)
'''
jobTitle = soup.find_all('div',attrs={'class' : 'jobTitle strong noMargTop margBotLg'})

title_l = []
for title in jobTitle:
	title_l.append(title.text)

links = soup.find_all('div',attrs={'class' : 'cell col span-1-2 noPadLt'})

salary = []
for link in links:
	if "Median Base Salary" in link.text:
		
		salary.append(link.text)

for t in salary:
	text = t.replace("Median Base Salary","")
	tt = text.replace(",","")
	print(tt[1:])


print(len(salary))
'''