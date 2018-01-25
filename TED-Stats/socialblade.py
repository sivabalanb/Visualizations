__author__ = "Sivabalan B"
__copyright__ = "Copyright 2017, @K7Computing"
__email__ = "sivabalan.b@k7computing.com"
__status__ = "test"

"""
	* Downloading the apks from apkmirror
	* Try to get the links to download the file and normalize it
	* Download the files using the direct download link and wget
"""

import requests
import time
import configparser
import sys
import os
import logging
import logging.handlers
import urllib3
urllib3.disable_warnings()


#sys.path.append('E:\Whitelist_Crawler\download\Apkmirror\Utils\FileHex')
#from FileHex import Calculation
#BS4 will not work as the program was created using BS3 and using its functions
from BeautifulSoup import BeautifulSoup as bs
import pickle
# Pickle is used to store the appPageUrls to keep track of urls being downloaded so the number of requests are reduced
#PIK = "pickle.dat"

# Read the contents of ini file and store it in dictionary format
def read_config_as_dict(iniFile) : 
	confDict = {}
	config=ConfigParser.ConfigParser()
	config.read(iniFile)
	for i in config.sections() :
		tempDict = {}
		for k,v in config.items(i) :
			tempDict.update({k : v})
		confDict.update({i : tempDict})
	return confDict

# Used to increase the page number in the ini file
def set_config(sec,opt,val) :
	config = ConfigParser.ConfigParser()
	config.read(iniFile)
	config.set(sec,opt,val)
	fw = open(iniFile,"wb")
	config.write(fw)
	fw.close()

# BS which sends requests to generate the soup for a given URL
def get_soup(url) :
	
	res = requests.get(url,verify=False)
	
	if res.status_code == 200 :
		soup = bs(res.text)
		return soup
	# When you try to hit the server continuously it gives you 'Rate Limited' page
	elif res.status_code == 429 :
		msg = "Rate limited at url: \t" + str(url)
		logger.error(msg)
		sys.exit()
	else :
		msg = "Problem at get_soup"
		logger.error(msg)
		sys.exit()
		return "request_error : " + str(res.status_code)


"""
	* Fetch the URL which can be used to download files
	* return the appPageUrls which is used to download the files
"""
def get_app_page_urls() :
	logger.info("Fetching the required data")
	# Starting page from which the download links are fetched
	# The page from which the files are downloaded
	# The page till which the files are downloaded


	return appPageUrls,pageNumEnd

if __name__ == "__main__" :
	try:
		baseDir = os.path.dirname(sys.argv[0])
		fileName = os.path.basename(sys.argv[0])
		iniFile = os.path.join(baseDir,"socialblade.ini")
		# Read the Ini file and safe it in a dictionary
		confDict = read_config_as_dict(iniFile)

		print(confDict)
		
		# Fetch the number of pages 
		#pageCount = get_app_page_urls()
		
	except Exception as e:
		print("Error encountered in Main function:\t" + str(e))