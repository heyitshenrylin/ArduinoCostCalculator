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

## Other Notes
- The Google API keys are limited to 100 searches a day. The CSE is
limited to 10,000 searches a day.
- Amazon.ca scraping doesn't seem to be working on the virtual machine


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
- Document input formatting
