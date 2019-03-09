import bs4
# Use `requests` as it is a standard in python ecosystem for sending HTTP Requests.
import requests


def first_method(product_details):

    for product_detail in product_details:

        data = product_detail.findAll("div", {"class":"col col-7-12"})

        for datum in data:
            name = datum.div
            print(name.text)  # PRINTING NAME OF EACH PRODUCT FOUND

            rating = datum.find("div", {"class":"hGSR34"})
            print(rating.text)  # PRINTING RATING OF EACH PRODUCT FOUND

            detail = datum.findAll("li", {"class":"tVe95H"})
            for k in detail:
                print(k.text)

            print("\n")


def second_method(content):
    product_line = content.findAll("div", {"class":"_3O0U0u"})

    print(len(product_line))

    # This shortcut save I/O Read as I/O is done all at once.
    product = [j.text for i in product_line for j in i]
    print(product)


if __name__ == '__main__':
    product_name = input("ENTER PRODUCT : ").strip()
    my_url = "https://www.flipkart.com/search?q={}".format(product_name)
    html = None

    # Use exception handling to handle any runtime exception
    try:
        # It's a pythonic way to use context statement `with` whenever opening or closing a resource.
        response = requests.get(my_url)

        if response.status_code == 200:
            html = response.content.decode()

        page = bs4.BeautifulSoup(html, "html.parser")
        print(page.prettify())

        details = page.find_all("div", {"class": "_1-2Iqu row"})

        if len(details) != 0:
            first_method(details)
        else:
            second_method(page)

        print(my_url)
    except Exception as e:
        print("Error Occurred {}".format(e))
