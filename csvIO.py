# Authors: Eric Claerhout, Henry Lin
# Student IDs: 1532360, 1580649
# CMPUT 274 Fall 2018
#
# Final Project: Cost Calculator

###########
# Imports #
###########
from sys import exit
from csv import DictReader


#############
# Functions #
#############
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
