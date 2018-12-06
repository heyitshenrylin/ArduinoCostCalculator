# Authors: Eric Claerhout, Henry Lin
# Student IDs: 1532360, 1580649
# CMPUT 274 Fall 2018
#
# Final Project: Price Finder

###########
# Imports #
###########
from sys import exit
from csv import reader, DictReader, DictWriter


#############
# Functions #
#############
def getSupportedSites():
    """ Get Supported Sites Function
    Reads the information from supportedSites.csv and generates a list
    of dictionaries where each dictionary contains various information
    regarding a website including its base URL, currency type, and
    price-identifying HTML elements

    Returns
    - supportedSites - A list of dictionaries
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


def getPartsList():
    """ Get Parts List Function
    Reads the information from partsList.csv and generates a list of
    lists. An inner-most list is referred to as a "part type" as it
    contains either a single part or multiple parts that are considered
    equivalent. The outer-most list is therefore considered to be a list
    of various part types.

    Returns
    - partsList- A list of lists
    """
    partsList = []
    try:
        with open('partsList.csv', newline='', mode='r') as csvFile:
            csvReader = reader(csvFile)
            for row in csvReader:
                # Filter is used to remove any the empty strings
                partsList.append(list(filter(None, row)))
        return partsList

    # Exceptions
    except FileNotFoundError:
        print("partsList.csv could not be found.")
        print("Quitting...")
        exit()
    except Exception as e:
        print("getPartsList encountered the following error:")
        print(e)
        print("Quitting...")
        exit()


def writeOutput(results, fieldnames):
    """ Write Output Function
    Outputs the various part prices from the given results to
    output.csv, where 'results' is a list of lists of dictionaries. Each
    dictionary represents the data (prices) for an individual site, the
    inner-most list is a collection of these dictionaries for a given
    part-type, and the outer-most list is a collection of these
    part-type lists. Places blank lines between the various part-types.

    Args:
    - results: A list of lists of dictionaries
    - fieldnames: A list of strings indicating the output fieldnames
                  (column titles) and their order. Values should match
                  what can be found in the dictionaries.
    """
    try:
        with open('output.csv', newline='', mode='w') as csvFile:
            csvWriter = DictWriter(csvFile, fieldnames=fieldnames)
            blankSpace = dict.fromkeys(fieldnames, '')

            # Write the fieldnames into the CSV
            csvWriter.writeheader()

            # Write the part prices
            for partTypePrices in results:
                for partPrice in partTypePrices:
                    csvWriter.writerow(partPrice)
                # Add a blank space between part types
                csvWriter.writerow(blankSpace)

    # Exceptions
    except FileNotFoundError:
        print("output.csv could not be found.")
        print("Quitting...")
        exit()
    except Exception as e:
        print("writeOutput encountered the following error:")
        print(e)
        print("Quitting...")
        exit()


########
# Main #
########
if __name__ == "__main__":
    print(getSupportedSites())
    print(getPartsList())
