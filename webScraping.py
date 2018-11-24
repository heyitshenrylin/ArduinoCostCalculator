from urlGet import simple_get
from bs4 import BeautifulSoup

# Currently working with adafruit for the arduino mega board
# Finds and prints the price from an adafruit site
raw_html = simple_get('https://www.adafruit.com/product/191')
html = BeautifulSoup(raw_html, 'html.parser')
prodDiv = html.find(id="prod-price")
print(prodDiv.text)
