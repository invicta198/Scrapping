import bs4
import requests
import click
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def display_data(Products):
	for i in Products:
		
		try:
			productName=i.find("span", {"class":"a-size-base-plus a-color-base a-text-normal"}).text
		except:
			productName=i.find("span", {"class":"a-size-medium a-color-base a-text-normal"}).text
		rating=i.find("span", {"class":"a-icon-alt"}).text
		totalVotes=i.find("span", {"class":"a-size-base"}).text
		price1=i.find("span", {"class":"a-price-whole"}).text
		price2=i.find("span", {"class":"a-price-fraction"}).text

		print("Product : {}".format(productName))
		print("Rating : {}".format(rating))
		print("Toatl Votes : {}".format(totalVotes))
		print("Price : ${}.{}".format(price1, price2))
		print("********************")


@click.command()
@click.option('--product', prompt="ENTER PRODUCT ", help='Name of Item you Wish to Search')
def startTask(product):
	product=product.strip()
	
	driver=webdriver.Chrome(executable_path="E:\chromedriver.exe")
	my_url = "https://www.amazon.com"
	driver.get(my_url)

	driver.maximize_window()
	time.sleep(2)
	
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
		Products=page.find_all("div", {"class": "s-result-list sg-row"})

		print("Total Products : {}".format(len(Products)))
		display_data(Products)

	except Exception as e:
		print("Error Occurred {}".format(e))

if __name__ == '__main__':
    startTask()
