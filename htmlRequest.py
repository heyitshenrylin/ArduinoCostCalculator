# Authors: Eric Claerhout, Henry Lin
# Student IDs: 1532360, 1580649
# CMPUT 274 Fall 2018
#
# Final Project: Price Finder

###########
# Imports #
###########
from requests import get
from requests.exceptions import RequestException
from contextlib import closing


#############
# Functions #
#############
def getHTML(url):
    """ Get HTML Function
    Attempts to get the HTML content from the given URL by making a HTTP
    GET request. If the content-type of response identified as HTML, the
    content is returned, otherwise None is returned.

    Source:
    https://realpython.com/python-web-scraping-practical-introduction/

    Args:
    - url: The URL from which to pull the content. [string]

    Returns:
    - resp.content: The HTML content from the given URL.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if verifyResponse(resp):
                # Content was verified
                return resp.content
            else:
                # Content was not verified
                return None

    except RequestException as e:
        print('Error during requests to {0} : {1}'.format(url, str(e)))
        print('Please check your connection to the URL')
        return None


def verifyResponse(resp):
    """ Verify Response Function
    Returns True if the response from the URL seems to be HTML, false
    otherwise.

    Args:
    - response: The URL response
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


########
# Main #
########
if __name__ == "__main__":
    url = input("Enter a URL to request: ")

    content = getHTML(url)
    print(" --- Begin Results --- ")
    if(content is None):
        print('None object received, verify that the URL is valid')
    else:
        print(content)
    print(" --- End of URL content --- ")
