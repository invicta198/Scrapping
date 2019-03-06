import bs4
from bs4 import BeautifulSoup as soup
import urllib.request as req

object=input("ENTER PRODUCT : ")
object=object.strip()

myUrl="https://www.flipkart.com/search?q="+object
uClient=req.urlopen(myUrl)
pageHtml=uClient.read()
uClient.close()

def firstMethod():
	for i in productDetail:
		#data=i.["col col-7-12"].["_3wU53n"].text
		data=i.findAll("div", {"class":"col col-7-12"})
		for j in data:
			name=j.div
			print(name.text) #PRINTING NAME OF EACH PRODUCT FOUND 
			
			rating=j.find("div", {"class":"hGSR34"})
			print(rating.text)  #PRINTING RATING OF EACH PRODUCT FOUND
			
			details=j.findAll("li", {"class":"tVe95H"})
			for k in details:
				print(k.text)
				
			print("\n")
			
def secondMethod():
	productLine=page.findAll("div", {"class":"_3O0U0u"})
	print(len(productLine))
	for i in productLine:
		for j in i:
			product=j.text
			print (product)
			print ("\n")
		print ("********************")
		
page=soup(pageHtml, "html.parser")
#print(page.prettify())
productDetail=page.findAll("div", {"class":"_1-2Iqu row"})
if(len(productDetail)==0):
	secondMethod()
else:
	firstMethod()
print (myUrl)
