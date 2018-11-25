from googleapiclient.discovery import build


# Source:
# https://stackoverflow.com/questions/38635419/searching-in-google-with-python
# DO NOT REMOVE
MY_API_KEY = "AIzaSyD7H29aH47QGEk10KNZKsKH1DZQ8CJhbyI"
MY_CSE_ID = "012462952568133975478:6f88fk6n_rg"


def google_search(searchTerm, apiKey, cseId, **kwargs):
    """
        Using a custom search engine from:
        https://cse.google.com/cse?cx=012462952568133975478:6f88fk6n_rg
        from the google developers console under admins name.

        The custom search api was enabled and the api key is also on the
        developer console.
        Currently the API key is set without restrictions for the use in the
        project only.

        Args:
        searchTerm : The string to be searched through the custom search
        engine
        apiKey : The API key for accessing google APIs
        cseID : The custom search engine ID to be able to access the unique
        search engine for the project
        **kwargs : Number of results to return

        Returns:
        res['items'] : Large dictionary of all attributes of the google
        search, includes URLs under the key 'link'
    """
    service = build("customsearch", "v1", developerKey=apiKey)
    res = service.cse().list(q=searchTerm, cx=cseId, **kwargs).execute()
    return res['items']
