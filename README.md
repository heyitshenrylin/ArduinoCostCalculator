# Component Price Finder
Authors: Eric Claerhout, Henry Lin
Student IDs: 1532360, 1580649
CMPUT 274 Fall 2018

## Modules needed:
- BeautifulSoup4 (https://pypi.org/project/beautifulsoup4/)
- requests (https://pypi.org/project/requests/)
- google-api-python-client (https://pypi.org/project/google-api-python-client/)

All modules can be installed using
`pip3 install --upgrade beautifulsoup4 requests google-api-python-client`



## Notes
Need to add data to supportedSites.csv *and* update the CSE to support a new
site

A string search was tested but it wasn't any faster and it complicated things
a lot, plus isn't modular

Google API is limited to 100 searches a day. CSE is limited to 10,000 searches
a day.


## Achieved Project Goals

### ✔ Simple yet powerful user interaction
CSV files were chosen for input and output as they provides a simple,
text based interaction while allowing a platform for more power-user
features through the use of programs like Excel. The use of CSV's also
allowed us to implement support for equivalent products.

### ✔ Storing the results in a simple format
This was an important consideration so that the data could be easily
used by another program or function. This was achieved in two manners:

1) Keeping Python data relatively simple. The results for a given part
on a given website are stored as a dictionary with the keys being the
same as the field headers in the output CSV. Dictionaries containing the
same part or an equivalent part are grouped together in a list, known as
a "Part Type" in the code comments. Finally, all the multiple part types
lists are then stored in one master list, containing all of the
information.

2) Outputting to CSV means any other program can easily import the data
if the Python data is not suitable.

### ✔ Support for equivalent products
The ability to specify equivalent products was an important step so that
multiple, closly related search results could be grouped together
accordingly. For example, if both a 220 ohm resistor and a 240 ohm
resistor are applicable in your project, assigning them as equivalent
products allows the results of both to be stored and shown together.

### ✔ Creating a modular system to enable easy support of further sites
Using BeautifulSoup's find method in combination with the CSV site data
allows sites to be easily added as long as there is an identifying HTML
element for the price.


## Future Improvements
- Live currency conversion
- Scraping product names in addition to prices
- Command line arguments for the input / output files

## Readme To Do
- Sequence diagram
