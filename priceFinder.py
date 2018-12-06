# Authors: Eric Claerhout, Henry Lin
# Student IDs: 1532360, 1580649
# CMPUT 274 Fall 2018
#
# Final Project: Price Finder

###########
# Imports #
###########
import sys
import os

# Local imports from the 'modules' folder
sys.path.append(os.path.join(os.getcwd(), "modules"))
from csvIO import getSupportedSites, getPartsList, writeOutput
from webScraping import getSoup, priceGet


##################
# User Variables #
##################
# Henry's Google API keys and
# apiKey = "AIzaSyD7H29aH47QGEk10KNZKsKH1DZQ8CJhbyI"  # API Key 1
# apiKey = "AIzaSyBpAVxvWwzQGEQBed8ppqdjQPgP1-A-c5w"  # API Key 2

# Eric's Google API keys [DO NOT CHANGE]
# apiKey = "AIzaSyBEyy6-aFEzGLMMtq9kuTm5k0yCqD7TsFs"  # API Key 1
apiKey = "AIzaSyDek6VKnGwOKUesIHeeMfYo0rGGsKpqQ_4"  # API Key 2

# Henry's Custom Search Engine [DO NOT CHANGE]
cseID = "012462952568133975478:6f88fk6n_rg"


#############
# Functions #
#############
def getOutput(siteInfo, searchTerm):
    """
    FIX THIS AND THIS NAME
    getResults?

    returns none if it runs out of attempts or if no results can be found
    """
    # Fill 'resultsDict' with information already known
    resultsDict = {}
    resultsDict["Product"] = searchTerm
    resultsDict["Site"] = siteInfo["site"]
    resultsDict["Currency"] = siteInfo["currency"]

    # Loop for error checking
    for i in range(1, 4):
        # Find a webpage, get the URL of the page and its soup
        resultsDict["URL"], soup = getSoup(siteInfo["site"], searchTerm, i,
                                           apiKey, cseID)

        # If no search results can be found, return None
        if resultsDict["URL"] is None and soup is None:
            print("No search results for '{}' on '{}'. Moving on to the next "
                  "site.".format(searchTerm, siteInfo["site"]))
            return None

        # If the search result is not HTML, move onto the next result
        elif resultsDict["URL"] is not None and soup is None:
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
            print(resultsDict["URL"] + "\n")
            continue

        # FIXME
        elif foundPrice is None and i == 3:
            print("Couldn't find anything after 3 attempts")
            return None

        # If price was successfully found, save it and move onto the
        # next site.
        else:
            resultsDict["Price"] = foundPrice
            break

    # Output / Save the results
    return(resultsDict)


########
# Main #
########

# Get input
supportedSites = getSupportedSites()
partsList = getPartsList()

results = []

# Find prices for all part types
for partType in partsList:

    partPrices = []
    # Find prices for all parts (and their alternatives) in a part type
    for part in partType:
        print("Getting prices for '{}'".format(part), end=" ")

        # Find prices from all of the supported sites
        for siteInfo in supportedSites:
            partPrices.append(getOutput(siteInfo, part))

    # Save the partPrices.
    results.append(list(filter(None, partPrices)))

results = list(filter(None, results))

writeOutput(results, ["Product", "Site", "Price", "Currency", "URL"])


# Part prices is a list of dictionaries -> all results for a given type
# Results = list of list of dictionaries
