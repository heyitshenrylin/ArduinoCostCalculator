# Authors: Eric Claerhout, Henry Lin
# Student IDs: 1532360, 1580649
# CMPUT 274 Fall 2018
#
# Final Project: Price Finder

###########
# Imports #
###########
from googleapiclient.discovery import build


#############
# Functions #
#############
def googleSearch(searchTerm, apiKey, cseId, **kwargs):
    """ Google search function
    This function interfaces with Google's Client API Library to do a
    Google search using the specified search term. Returns a dictionary
    containing the attributes of the results. If a result cannot be
    found, returns None.

    Using a custom search engine from the google developers console
    under admin's name:
    https://cse.google.com/cse?cx=012462952568133975478:6f88fk6n_rg

    The custom search API was enabled and the API key is also on the
    developer console. Currently the API key is set without restrictions
    for the use in this project only.

    Source: https://stackoverflow.com/a/49122258

    Args:
    - searchTerm: The string to be searched with the custom search
                  engine.
    - apiKey: The API key to access the Google APIs.
    - cseID: The custom search engine ID to access the unique
             search engine.
    - **kwargs: Other arguments to be passed. Examples include using
                'num=#' to specify the number of results to return.

    Returns:
    - res['items']: Large dictionary containing the attributes of the
                    search, including the URLs under the key 'link'.
    """
    # Build and use the API service.
    service = build("customsearch", "v1", developerKey=apiKey)
    res = service.cse().list(q=searchTerm, cx=cseId, **kwargs).execute()

    try:
        return res['items']
    except KeyError:
        # No results found
        return None


########
# Main #
########
if __name__ == "__main__":
    # Get user input for testing
    searchTerm = input("Search term: ")
    apiKey = input("API Key: ")
    cseId = input("CSE ID: ")

    # Run 'googleSearch'
    try:
        results = googleSearch(searchTerm, apiKey, cseId, num=1)
        print(" --- Begin Results --- ")
        print(results)
    except KeyError as e:
        print("customSearch encountered the following KeyError:")
        print(e)
        print("This is most likely because no results were found")
    except Exception as e:
        print("customSearch encountered the following error:")
        print(e)
