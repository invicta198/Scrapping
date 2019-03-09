import bs4
# Use `requests` as it is a standard in python ecosystem for sending HTTP Requests.
import requests


def first_method(product_details):
    for i in productDetail:
        data=i.findAll("div", {"class":"col col-7-12"})
        for j in data:
            name=j.div
            print(name.text)                                #PRINTING NAME OF EACH PRODUCT FOUND 
            
            try:
                rating=j.find("div", {"class":"hGSR34"})
                print(rating.text)                          #PRINTING RATING OF EACH PRODUCT FOUND
            except:
                print("No reviews")

            details=j.findAll("li", {"class":"tVe95H"})     #PRINTING DETAILS OF EACH PRODUCT FOUND
            for k in details:
                print(k.text)
                
            print("\n")


def second_method(content):
    productLine=page.findAll("div", {"class":"_3O0U0u"})
    print(len(productLine))
    for i in productLine:
        for j in i:
            productName=j.div.find("a", {"class":"_2cLu-l"})['title']
            print (productName)         #PRINTING NAME OF EACH PRODUCT FOUND
            
            try:
                rating=j.div.find("div", {"class":"niH0FQ _36Fcw_"}).text
                print(rating)           #PRINTING RATING OF EACH PRODUCT FOUND
            except:
                print("No reviews")

            try:
                details=j.div.find("a", {"class":"_1Vfi6u"}).text
                print(details)          #PRINTING DETAILS OF EACH PRODUCT FOUND
            except:
                print("No Other Detail")

            print ("\n")
        print ("********************")


if __name__ == '__main__':
    product_name = input("ENTER PRODUCT : ").strip()
    product_name= product_name.replace(" ", "%20")
    my_url = "https://www.flipkart.com/search?q={}".format(product_name)
    html = None

    # Use exception handling to handle any runtime exception
    try:
        # It's a pythonic way to use context statement `with` whenever opening or closing a resource.
        response = requests.get(my_url)

        if response.status_code == 200:
            html = response.content.decode()

        page = bs4.BeautifulSoup(html, "html.parser")
        #print(page.prettify())

        details = page.find_all("div", {"class": "_1-2Iqu row"})

        if len(details) != 0:
            first_method(details)
        else:
            second_method(page)

        print(my_url)
    except Exception as e:
        print("Error Occurred {}".format(e))