from bs4 import BeautifulSoup
from sys import exit
from csv import DictReader
from urlGet import simple_get
from customSearch import google_search

# Henry's Google API key and custom search engine ID
# DO NOT CHANGE
apiKey = "AIzaSyD7H29aH47QGEk10KNZKsKH1DZQ8CJhbyI"
cseID = "012462952568133975478:6f88fk6n_rg"


def getSoup(site, searchTerm, apiKey, cseID):
    """Get Soup Function
    Uses a custom google search to find a webpage result for the given
    search term from the given website. Returns the URL of the found
    webpage and a soup (a BeautifulSoup tree object) of that webpage.

    #FIXME
    ADD REDUNDANCY AND ERROR CHECKING

    Args:
    - site: The root website URL (minus the leading https://www.) from
            which the search result should be found. [string]
    - searchTerm: The product name to search on the given site. [string]
    - apiKey: The Google API key for the Google search [string]
    - cseID: The Google custom search ID [string]

    Returns:
    - url: The found URL
    - soup: The BeautifulSoup tree object of the found website.
    """
    # Calls the google_search function from customSearch.py to find a
    # suitable URL
    searchResults = google_search("site:{} {}".format(site, searchTerm),
                                  apiKey, cseID, num=1)
    url = searchResults[0]["link"]

    # Calls the simple_get function from urlGet.py to get the raw
    # (plaintext) HTML content of the found URL
    htmlRaw = simple_get(url)

    # Creates a soup from the raw HTML
    soup = BeautifulSoup(htmlRaw, 'html.parser')

    return url, soup


def priceGet(soup, bsSearchDict):
    """ Price Get Function
    Returns the price of a product from that product's webpage. Uses
    BeautifulSoup's find with the specified 'bsSearchDict' to get the
    price from the given soup, and then cleans the output to only return
    a numeric price value.

    Args:
    soup: The BeautifulSoup soup (tree object) from which to find the
          price.

    bsSearchDict: A single element dictionary of the form
                  {keyword argument: keyword value} that acts as the
                  argument for BeautifulSoup's .find() method.
                  For example, {id, "price"} will be implemented as
                  soup.find(id="price").

    Returns:
    cleanedPrice: The price of the product with any symbols or spaces
                  removed. [string]
    """
    # Get the price from the soup (HTML)
    foundPrice = soup.find(**bsSearchDict)

    # Clean the text before returning it
    cleanedPrice = ''.join(i for i in foundPrice.text if i in '1234567890.')
    return cleanedPrice


def getSupportedSites():
    """ Get Supported Sites Function

    Returns a list of dictionaries w/ site and BS search ID
    """
    supportedSites = []
    try:
        with open('supportedSites.csv', newline='', mode='r') as csvFile:
            csvReader = DictReader(csvFile)
            for row in csvReader:
                supportedSites.append(dict(row))
        return supportedSites

    # Exceptions
    except FileNotFoundError:
        print("supportedSites.csv could not be found.")
        print("Quitting...")
        exit()
    except Exception as e:
        print("getSupportedSites encountered the following error:")
        print(e)
        print("Quitting...")
        exit()


# Currently a placeholder to be able to run the code
# Should check all supportedSites but may error out if something
# can't be found. "Yellow LED" works
supportedSites = getSupportedSites()
searchTerm = input("What are you looking for? ")

prices = []
for siteInfo in supportedSites:
    # Fill 'resultsDict' with information already known
    resultsDict = {}
    resultsDict["site"] = siteInfo["site"]
    resultsDict["currency"] = siteInfo["currency"]

    # Find a webpage, get the URL of the page and its soup
    resultsDict["url"], soup = getSoup(siteInfo["site"], searchTerm, apiKey,
                                       cseID)

    # Get the price of the product
    bsSearchDict = {siteInfo["bsSearchKwArg"]: siteInfo["bsSearchValue"]}
    resultsDict["price"] = priceGet(soup, bsSearchDict)

    # Output / Save the results
    print(resultsDict)
    prices.append(resultsDict)
