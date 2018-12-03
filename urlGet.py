from requests import get
from requests.exceptions import RequestException
from contextlib import closing


# Source:
# https://realpython.com/python-web-scraping-practical-introduction/
def simple_get(url):
    """
        Attempts to get the content at 'url' by making an HTTP GET request.
        If the content-type of response is some kind of HTML/XML, return the
        text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
        Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
        printing log error
    """
    print(e)


if __name__ == "__main__":
    url = input("Enter a URL to request: ")

    content = simple_get(url)
    print(" --- Begin Results --- ")
    print(content)
    print(" --- End of URL content --- ")
