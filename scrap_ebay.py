import bs4
import requests
import click
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def display_data(Products):
	for i in Products:
		title=i.find("h3", {"class": "s-item__title"})
		print(title.text)

		price=i.find("span", {"class": "s-item__price"})
		print(price.text)

		print("********************") 

@click.command()
@click.option('--product', prompt="ENTER PRODUCT ", help='Name of Item you Wish to Search')
def startTask(product):
	product=product.strip()
	driver=webdriver.Chrome(executable_path="E:\chromedriver.exe")
	my_url="https://www.ebay.com"
	driver.get(my_url)

	driver.maximize_window()
	time.sleep(2)
	
	webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
	query=driver.find_element_by_id("gh-ac")
	
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
		allProducts=page.find_all("div", {"class": "s-item__wrapper clearfix"})

		print("Total Products : {}".format(len(allProducts)))
		display_data(allProducts)

	except Exception as e:
		print("Error Occurred {}".format(e))

if __name__ == '__main__':
    startTask()
