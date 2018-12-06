# Authors: Eric Claerhout, Henry Lin
# Student IDs: 1532360, 1580649
# CMPUT 274 Fall 2018
#
# Final Project: Cost Calculator

###########
# Imports #
###########
from csvIO import getSupportedSites
from webScraping import getSoup, priceGet

##################
# User Variables #
##################
# Henry's Google API keys and custom search engine [DO NOT CHANGE]
# apiKey = "AIzaSyD7H29aH47QGEk10KNZKsKH1DZQ8CJhbyI"  # API Key 1
apiKey = "AIzaSyBpAVxvWwzQGEQBed8ppqdjQPgP1-A-c5w"  # API Key 2
cseID = "012462952568133975478:6f88fk6n_rg"


########
# Main #
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
