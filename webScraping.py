from urlGet import simple_get
from customSearch import google_search
from bs4 import BeautifulSoup

# Henry's Google API account key and custom search engine
# DO NOT CHANGE
MY_API_KEY = "AIzaSyD7H29aH47QGEk10KNZKsKH1DZQ8CJhbyI"
MY_CSE_ID = "012462952568133975478:6f88fk6n_rg"


def priceGet(currentSite, searchTerm):
    """
        Get a price of an item from one of the supported sites.
        The BeautifulSoup object is a tree object whose search
        efficiency can be increased through the implementation of a
        breadth first search.

        To add a site to the supported sites, they would also need to be
        added into the custom search engine to be able to implement the
        new site.

        Args:
        currentSite : The site to search in the form "site:currentSite"
            - String value
        searchTerm : The query to be searched; an electronics part
            - String value

        Returns:
        The price and site as a tuple
        currentSite : The site searched
        productPrice.text : The unformatted string for the price
            - Currently unformatted and doesn't strip any symbols
    """
    # Calls the google_search function from customSearch.py
    results = google_search(
        "site:{} {}".format(currentSite, searchTerm),
        MY_API_KEY, MY_CSE_ID, num=1)
    # Calls the simple_get function from urlGet.py
    htmlRaw = simple_get(results[0]["link"])
    # html is the BeautifulSoup tree of the given URL
    itemPage = BeautifulSoup(htmlRaw, 'html.parser')

    # Current dictionary of supported sites
    supportedSites = {
        'amazon.ca': itemPage.find(id="priceblock_ourprice"),
        'adafruit.com': itemPage.find(id="prod-price"),
        'canadarobotix.com': itemPage.find(class_="price-container")
    }

    productPrice = supportedSites[currentSite]
    stripped = ''.join(i for i in productPrice.text if i in '1234567890.')
    return currentSite, stripped


# Currently a placeholder to be able to run the code
# Changing the site and the search should let you search anything you
# want on amazon.ca, adafruit.com, or canadarobotix.com
bigBoys = priceGet('adafruit.com', 'red LED')
print(bigBoys)
