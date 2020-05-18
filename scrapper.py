from bs4 import BeautifulSoup
import requests
from csv import writer


URL="http://books.toscrape.com/"
response = requests.get(URL)
#print(response.text)

soup =BeautifulSoup(response.text, 'html.parser')

products=soup.find_all(class_="col-xs-6")


with open('books.csv','w') as csv_file:
	csv_writer=writer(csv_file)
	headers=['Name','Price','Stock Availability','link']
	csv_writer.writerow(headers)

	for product in products:
		name=product.find('h3').find('a').get_text()
		price= product.find(class_="product_price").find(class_="price_color").get_text()
		stock_availability= product.find(class_="product_price").find(class_="instock").get_text().strip()
		link="http://books.toscrape.com/"+ product.find(class_="image_container").find('a')['href']
		csv_writer.writerow([name,price,stock_availability,link])
		print(f"{name}---{price}---{stock_availability}---{link}")