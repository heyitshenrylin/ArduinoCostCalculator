from bs4 import BeautifulSoup
from sys import exit
from csv import DictReader
from urlGet import simpleGet
from customSearch import googleSearch

# Henry's Google API account key and custom search engine
# DO NOT CHANGE
# apiKey = "AIzaSyD7H29aH47QGEk10KNZKsKH1DZQ8CJhbyI"  # API Key 1
apiKey = "AIzaSyBpAVxvWwzQGEQBed8ppqdjQPgP1-A-c5w"  # API Key 2
cseID = "012462952568133975478:6f88fk6n_rg"


def getSoup(site, searchTerm, resultNum, apiKey, cseID):
    """Get Soup Function
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

    # Calls the simpleGet function from urlGet.py to get the raw
    # (plaintext) HTML content of the found URL
    htmlRaw = simpleGet(url)

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


########
# MAIN #
########

# Currently a placeholder to be able to run the code
supportedSites = getSupportedSites()
searchTerm = input("What are you looking for? ")

prices = []
for siteInfo in supportedSites:
    # Fill 'resultsDict' with information already known
    resultsDict = {}
    resultsDict["site"] = siteInfo["site"]
    resultsDict["currency"] = siteInfo["currency"]

    # Loop for error checking
    for i in range(1, 4):
        # Find a webpage, get the URL of the page and its soup
        resultsDict["url"], soup = getSoup(siteInfo["site"], searchTerm, i,
                                           apiKey, cseID)

        # If no search results can be found, move onto the next site
        if resultsDict["url"] is None and soup is None:
            print("No search results for '{}' on '{}'. Moving on to the next "
                  "site.".format(searchTerm, siteInfo["site"]))
            break

        # If the search result is not HTML, move onto the next result
        elif resultsDict["url"] is not None and soup is None:
            print("Search result {} for '{}' on '{}' was not HTML. Trying "
                  "again with the next result.".format(i, searchTerm,
                                                       siteInfo["site"]))
            continue

        # Get the price of the product
        bsSearchDict = {siteInfo["bsSearchKwArg"]: siteInfo["bsSearchValue"]}
        foundPrice = priceGet(soup, bsSearchDict)

        # If price cannot be found, try again
        if foundPrice is None and i != 3:
            print("The product price could not be found on following URL. "
                  "Trying again with the next result.")
            print(resultsDict["url"] + "\n")
            continue

        # FIXME
        elif foundPrice is None and i == 3:
            print("Couldn't find anything after 3 attempts")
            break

        # If price was successfully found, save it and move onto the
        # next site.
        else:
            resultsDict["price"] = foundPrice

            # Add the resultsDict to the final prices list
            prices.append(resultsDict)
            break

    # Output / Save the results
    print(resultsDict)


print("\nFinal data:")
print(prices)
