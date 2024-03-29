# Component Price Finder
Authors: Eric Claerhout, Henry Lin

Student IDs: 1532360, 1580649

CMPUT 274 Fall 2018

## Modules needed:
- BeautifulSoup4 (https://pypi.org/project/beautifulsoup4/)
- requests (https://pypi.org/project/requests/)
- google-api-python-client (https://pypi.org/project/google-api-python-client/)

All needed modules can be installed using
`pip3 install --upgrade beautifulsoup4 requests google-api-python-client`

## Included Files
```
priceFinder.zip
├── modules/
|   ├── csvIO.py [Module dealing with the CSV input and output]
|   ├── customSearch.py [Module handling the Google custom search API]
|   ├── htmlRequest.py [Module handling the HTML Requests]
|   └── webScraping.py [Module handling the scraping with BeautifulSoup]
├── output.csv [Output CSV file]
├── partsList.csv [Input CSV file]
├── priceFinder.py [Main python program]
├── README.md [This file]
└── supportedSites.csv [A CSV file used as a database containing
                        information regarding the supported websites]
```

## Running Instructions
Modify `partsList.csv` to create a list of the parts for which you want
to find prices. Parts on new lines represent completely different part
types, where as parts separated by commas on the same line indicate
equivalent parts, meaning their results will be displayed together.
After running `priceFinder.py`, the results will be outputted to
`output.csv` which can just be opened as a text document, or imported
into another program such as Excel.

## Adding new sites into the search
To add new sites, inspect the HTML of the target site and try to find a
unique id, class, or div that identifies the price for products on that
site. Then, simply add the site name and information into
`supportedSites.csv`, with the element type (id, class, div) as the
`bsSearchKwArg` and the identifier as the `bsSearchValue`.

Note that in the demo, the custom search engine was limited to the 3
supported sites, but the limit has since been removed and the searches
rely solely on our programmed "site:url" search.

## Funcionality Notes
- The Google API keys are limited to 100 searches a day and the CSE is
limited to 10000 searches a day. If the API limit is reached, the
program will throw an error message saying that "billing must be
enabled". To continue running the program, simply comment out a new key
in the `User Variables` section of `priceFinder.py`.

- Amazon.ca scraping doesn't seem to be working properly anymore. This
change occurred without any change in our program code however, so we
believe this may be Amazon blocking requests from our Python program as
per: https://stackoverflow.com/a/41366555

## Comments on Algorithmic Complexity
When originally deciding on this project, we both had a very limited
understanding of BeautifulSoup and webscraping in general. After some
brief reading, we learned that BeautifulSoup (BS) stored its 'soup' in a
tree structure, mimicking the parent-child relationships found in the
HTML. This project was therefore chosen under the assumption that our
algorithmic complexity would originate from the need to create a
tree-search in order to find our prices within the soup.

Further into the project, we learned that BS has its own tree search
built it to it, with it's `.find()` method. We then had to choose
between artificially making our project more difficult by continuing
with our own tree search or using the built in one, sacrificing some
complexity for much cleaner, better designed code.

Before making our decision, we decided to compare the performance of our
options. We were originally intending to use a depth-first search, as
it's one of the only searches we could find that didn't rely on a
specific data structure, and that seemed simple enough for us to
implement. Though it isn't officially documented, by looking into the BS
source code, we believe BS also uses a DFS, though it seems to be
modified in some degree. Therefore, we knew that our tree-search
wouldn't be able to outperform BS's, making a compelling argument to
simply use the built in function.

We next investigated the use of a string search on plain text HTML
instead of using BS at all. After some quick research however, we
learned that Python's `str.find` uses a "fast search/count
implementation, based on a mix between Boyer-Moore and Horspool, with a
few more bells and whistles on the top". This would mean it would have a
time complexity of approximately O(N) on average and a worse case of
O(NM), where M is the length of the substring and N is length of the
larger string. Comparing that to a worst case DFS time complexity of
O(V+E), where V is the number of vertices and E is the number of edges,
it became clear that the BS `.find()` was our best option, especially
when considering the fact that there will be much less vertices and
edges than characters in a complete HTML page. We also verified our
theory using Python's `timeit` module with a handful of test cases.

BeautifulSoup's find was chosen in the end to be used. It gives us much
cleaner and more effective code, and enables us to easily expand our
support for future websites (within ~15 minutes of work or less). We
would still argue however that the multitude of unforeseen individual
steps that were needed for proper webscraping add up to create a
complex end product.


## Project Goals

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

### ✖ Live currency conversion
This was never implemented due to time constraints, but its basis can be
seen in the `currency` item in `supportedSites.csv`. The idea would be
to use an API to get the live exchange rates and then to appropriately
convert currencies.

## Future Improvements
- Live currency conversion
- Scraping product names in addition to prices
- Command line arguments for the input / output files
