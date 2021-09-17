from typing import Dict, List, Optional
import requests
import json

INVASIONS_ENDPOINT="https://www.toontownrewritten.com/api/invasions"
POPULATION_ENDPOINT="https://www.toontownrewritten.com/api/population"
SILLYMETER_ENDPOINT="https://www.toontownrewritten.com/api/sillymeter"

"""
API Wrapper for the Toontown Rewritten API, using their four endpoints:
-Invasions
-Population
-Silly Meter Status
"""
def _get_data(url) -> Dict:
    json_data = requests.get(url)
    data_dict = json.loads(json_data)
    return data_dict


class ToontownRewrittenInvasion:
    """
    Class that gets all of the data for toontown rewritten invasions
    """
    def __init__(self) -> None:
        self.data=_get_data(INVASIONS_ENDPOINT)

    def refresh(self) -> None:
        """
        Refreshes the API call to get the new data
        """
        self.__init__()

    def last_updated(self) -> Optional(int, None):
        """Returns the last updated time of the API call

        Returns:
            int: timestamp of the last updated time
            or
            None: if there is error and this field doesn't show up
        """
        return self.data.get("lastUpdated", None)

    def error(self) -> Optional(str, None):
        """Returns the error message as a string, or None if there is
        no error message

        Returns:
            An error message as a string, or None
        """
        return self.data.get("error", None)

    def invasions(self, as_array:bool=False) -> Optional(Dict, List, None):
        """Returns the dictionary of ongoing invasions,
        where each Key is the district of the invasion (str), and 
        the corresponding value is a dictionary with 
        `asof`, `type` and `progress` values:

        asof (int): timestamp of when the invasion started
        type (str): type of cog in the invasion
        progress (str): string containing the number defeated/total number
        in the invasion, i.e "500/2000"

        Args:
            as_array: whether or not the invasions data should be formatted
            as an array (list of lists), with the following format:
            [
                ["District", "Cog Type", "Progress]
                ...
            ]
        Returns:
            Dict or List: Dictionary of invasions data or Array with 
            specifications above if as_array is True
            or
            None: if there is error and this field doesn't show up
        """
        invasions_dict = self.data.get("invasions", None)
        if invasions_dict is None:
            return None
        
        if as_array is False:
            return invasions_dict
        else:
            array = []
            for district, invasion_data in invasions_dict.items():
                array.append([district, invasion_data["type"], invasion_data["progress"]])
            return array


class ToontownRewrittenPopulation:
    """
    Class that gets all of the data for the Toontown Rewritten Population
    """
    def __init__(self) -> None:
        self.data = _get_data(POPULATION_ENDPOINT)
    
    def refresh(self) -> None:
        """
        Refreshes the API call to get the new data
        """
        self.__init__()

    def last_updated(self) -> Optional(int, None):
        """Returns the last updated time of the API call

        Returns:
            int: timestamp of the last updated time
            or
            None: if there is error and this field doesn't show up
        """
        return self.data.get("lastUpdated", None)

    def error(self) -> Optional(str, None):
        """Returns the error message as a string, or None if there is
        no error message

        Returns:
            An error message as a string, or None
        """
        return self.data.get("error", None)
    
    def total_population(self) -> Optional(int, None):
        """Returns the total population in the game

        Returns:
            int: Total population
            or 
            None: if there is error and this field doesn't show up
        """
        return self.data.get("totalPopulation", None)
    
    def population_by_district(self) -> Optional(Dict, None):
        """If there are no errors, returns a dictionary with 
        the names of the districts as keys and the population
        of the district as the corresponding value

        Returns:
            Dict: Population dictionary broken down by district
            or
            None: if there is an error and this field doesn't show up
        """
        return self.data.get("populationByDistrict", None)


        
        

