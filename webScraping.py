# Authors: Eric Claerhout, Henry Lin
# Student IDs: 1532360, 1580649
# CMPUT 274 Fall 2018
#
# Final Project: Price Finder

###########
# Imports #
###########
from bs4 import BeautifulSoup

from htmlRequest import getHTML
from customSearch import googleSearch


#############
# Functions #
#############
def getSoup(site, searchTerm, resultNum, apiKey, cseID):
    """ Get Soup Function
    Uses a custom google search to find a webpage result for the given
    search term from the given website. Returns the URL of the found
    webpage and a soup (a BeautifulSoup tree object) of that webpage.

    If no search results can be found, both values will be returned as
    None. If a URL can be found but it isn't an HTML webpage, the URL
    will be retuned but the soup will be of type None.

    Args:
    - site: The root website URL (minus the leading https://www.) from
            which the search result should be found. [string]
    - searchTerm: The product name to search on the given site. [string]
    - resultNum: Which Google result to use. (2 -> 2nd result). [int]
    - apiKey: The Google API key for the Google search. [string]
    - cseID: The Google custom search ID. [string]

    Returns:
    - url: The found URL
    - soup: The BeautifulSoup tree object of the found website.
    """
    # Calls the googleSearch function from customSearch.py to find a
    # suitable URL
    searchResults = googleSearch("site:{} {}".format(site, searchTerm),
                                 apiKey, cseID, num=(resultNum))

    # If no search results could be found
    if searchResults is None:
        return None, None

    # resultNum - 1 as the list indexing starts at 0
    url = searchResults[resultNum - 1]["link"]

    # Calls the getHTML function from urlGet.py to get the raw
    # HTML content of the found URL
    htmlRaw = getHTML(url)

    # If the search result was not HTML (PDF, XML, etc.)
    if htmlRaw is None:
        return url, None

    # Creates a soup from the raw HTML
    soup = BeautifulSoup(htmlRaw, 'html.parser')

    return url, soup


def priceGet(soup, bsSearchDict):
    """ Price Get Function
    Returns the price of a product from that product's webpage. Uses
    BeautifulSoup's find with the specified 'bsSearchDict' to get the
    price from the given soup, and then cleans the output to only return
    a numeric price value. Returns None if no price can be found.

    Args:
    - soup: The BeautifulSoup soup (tree object) from which to find the
            price.
    - bsSearchDict: A single element dictionary of the form
                    {keyword argument: keyword value} that acts as the
                    argument for BeautifulSoup's .find() method.
                    For example, {id, "price"} will be implemented as
                    soup.find(id="price").

    Returns:
    - cleanedPrice: The price of the product with any symbols or spaces
                    removed. [string]
    """
    # Get the price from the soup (HTML)
    foundPrice = soup.find(**bsSearchDict)

    # If the price could not be found
    if foundPrice is None:
        return None

    # Clean the text before returning it
    cleanedPrice = ''.join(i for i in foundPrice.text if i in '1234567890.')

    return cleanedPrice
