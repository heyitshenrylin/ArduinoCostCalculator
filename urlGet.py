# Authors: Eric Claerhout, Henry Lin
# Student IDs: 1532360, 1580649
# CMPUT 274 Fall 2018
#
# Final Project: Cost Calculator

###########
# Imports #
###########
from requests import get
from requests.exceptions import RequestException
from contextlib import closing


#############
# Functions #
#############
# Source:
# https://realpython.com/python-web-scraping-practical-introduction/
def simpleGet(url):
    """
        Attempts to get the content at 'url' by making an HTTP GET
        request. If the content-type of response is some kind of
        HTML/XML, return the text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if isGoodResponse(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        logError('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def isGoodResponse(resp):
    """
    Returns true if the response seems to be HTML, false otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def logError(e):
    """
        printing log error
    """
    print(e)
    print('Please check your connection to the URL')


if __name__ == "__main__":
    url = input("Enter a URL to request: ")

    content = simpleGet(url)
    print(" --- Begin Results --- ")
    if(content is None):
        print('None object received, check your URL to see if it is valid')
    else:
        print(content)
    print(" --- End of URL content --- ")
