from typing import Dict, List, Optional
import requests

DISTRICTS_ENDPOINT = "https://corporateclash.net/api/v1/districts.js"
NEWS_ENDPOINT="https://corporateclash.net/api/v1/launcher/news"

"""
API Wrapper for the Corporate Clash API, using two endpoints:
- Districts
- News
"""

def _get_data(url) -> Dict:
    data = requests.get(url).json()
    return data

class CorporateClashAPI:
    """
    Class that gets the corporate clash data
    """
    def __init__(self) -> None:
        try:
            self.clash_districts = _get_data(DISTRICTS_ENDPOINT)
        except:
            self.clash_districts = None
        try:
            self.clash_news = _get_data(NEWS_ENDPOINT)
        except:
            self.clash_news = None
        

    def refresh(self) -> None:
        """
        Refreshes the API call to get the new data

        DO NOT EXCESSIVELY CALL THIS- You do not want to rate limit
        the API. The standard call time should be once per 5-15 minutes.
        """
        self.__init__()
    
    def districts(self):
        """Returns a List of Dictionaries, where each Dictionary is a
        District Object

        District Objects have the following keys:
        -name: District name (str)
        -online: Whether or not the district is online (Boolean)
        -population: District Population (int)
        -invasion_online: If there is an invasion in this district (Boolean)
        -last_update: Time for last updated in UTC (int)
        -cogs_attacking: Name of the cog attacking (str) 
        -count_defeated: Amount of Cogs defeated in the district (int)
        (refreshes upon invasion)
        -count_total: Total amount of cogs in an invasion (int)
        (defaults to 0 in an invasion without a district)
        -remaining_time: Amount of time before invasion ends, in seconds (int)

        Args:
            list: List of the district objects
            or
            None: If there is some Error
        """
        return self.clash_districts
        

    def news(self) -> Optional[List]:
        """Returns a List of Dictionaries, Where each Dictionary is a news article
        News articles have the following keys:
        -id: ID of the article (int)
        -author: Author of the article (str)
        -posted: date of when article was posted (str, in format "yyyy-mm-dd hh:mm:ss")
        -image_url: URL of the article image (str)
        -title: Title of the article (str)
        -summary: Summary of the article (str)
        -category: Category of topic the article falls under (str)

        Args:
            list: List of news objects
            or
            None: If there is some error
        """
        return self.clash_news

