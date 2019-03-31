import bs4
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib
import time

def display_data(Products):

	for i in allProducts:
		detailProduct=i.find("div", {"class": "sg-col-inner"})
		print(detailProduct.text)
		print("********************") 

	print(driver.title)

if __name__ == '__main__':
	
	driver=webdriver.Chrome(executable_path="E:\chromedriver.exe")
	my_url = "https://www.amazon.com"
	driver.get(my_url)

	driver.maximize_window()
	time.sleep(2)
	
	product = input("ENTER PRODUCT : ").strip()
	webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
	query=driver.find_element_by_id("twotabsearchtextbox")
	
	if(query.is_displayed()):
		print("SEARCH BAR DISPLAYED")
	if(query.is_enabled()):
		print("SEARCH BAR ENABLED")
		query.send_keys(product)
		query.send_keys(Keys.ENTER)
		print("ENTERED AND CLICKED")
	
	html=None
	my_url=driver.current_url
	allProducts=None

	try:
		response = requests.get(my_url)
		if response.status_code == 200:
			html = response.content.decode()

		page=bs4.BeautifulSoup(html, "html.parser")
		allProducts=page.find("div", {"class": "s-result-list sg-row"})

		display_data(allProducts)

	except Exception as e:
		print("Error Occurred {}".format(e))

	#html = urllib.request.urlopen(my_url).read()					#HTTP Error 503: Service Unavailable
	#print(driver.current_url)

'''		div id = title_feature_div
		div id = averageCustomerReviews_feature_div
		div id = desktop_unifiedPrice
		div id = featurebullets_feature_div '''