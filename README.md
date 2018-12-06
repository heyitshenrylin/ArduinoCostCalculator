# ArduinoCostCalculator
Final Project CMPUT274
140 kids in class

## Modules needed:
- BeautifulSoup4 (https://pypi.org/project/beautifulsoup4/)
- requests (https://pypi.org/project/requests/)
- google-api-python-client (https://pypi.org/project/google-api-python-client/)
- contextlib (included with Python)

All modules can be installed using
`pip install --upgrade beautifulsoup4 requests google-api-python-client`


## Notes
Need to add data to supportedSites.csv *and* update the CSE to support a new
site

A string search was tested but it wasn't any faster and it complicated things
a lot, plus isn't modular

Google API is limited to 100 searches a day. CSE is limited to 10,000 searches
a day.


## Project Goals

### ✔ Simple yet powerful user interaction
CSV files were chosen for input and output as they provides a simple,
text based interaction while allowing a platform for more power-user
features. [More here about excel, how we could support equivalent
products, taking multiple inputs]

### ✔ Creating a modular system to enable easy support of further sites
Using BeautifulSoup's find method in combination with the CSV site data
allows sites to be easily added as long as there is an identifying HTML
element for the price. Note that our custom search engine restricts the
results to the supported sites, so the

### ✖ Support for equivalent products
[talk about it] not implemented but infrastructure is in place -> csv style


## Future Improvements
- Live currency conversion
- Scraping product names in addition to prices
- Command line arguments for the input / output files
