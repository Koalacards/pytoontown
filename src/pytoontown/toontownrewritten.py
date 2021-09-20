from typing import Dict, List, Optional, Union
import requests

INVASIONS_ENDPOINT="https://www.toontownrewritten.com/api/invasions"
POPULATION_ENDPOINT="https://www.toontownrewritten.com/api/population"
SILLYMETER_ENDPOINT="https://www.toontownrewritten.com/api/sillymeter"

"""
API Wrapper for the Toontown Rewritten API, using three endpoints:
-Invasions
-Population
-Silly Meter Status
"""
def _get_data(url) -> Dict:
    data_dict = requests.get(url).json()
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

        DO NOT EXCESSIVELY CALL THIS- You do not want to rate limit
        the API. The standard call time should be once per 5-15 minutes.
        """
        self.__init__()

    def last_updated(self) -> Optional[int]:
        """Returns the last updated time of the API call

        Returns:
            int: timestamp of the last updated time
            or
            None: if there is error and this field doesn't show up
        """
        return self.data.get("lastUpdated", None)

    def error(self) -> Optional[str]:
        """Returns the error message as a string, or None if there is
        no error message

        Returns:
            An error message as a string, or None
        """
        return self.data.get("error", None)

    def invasions(self, as_array:bool=False) -> Union[Dict, List, None]:
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

        DO NOT EXCESSIVELY CALL THIS- You do not want to rate limit
        the API. The standard call time should be once per 5-15 minutes.
        """
        self.__init__()

    def last_updated(self) -> Optional[int]:
        """Returns the last updated time of the API call

        Returns:
            int: timestamp of the last updated time
            or
            None: if there is error and this field doesn't show up
        """
        return self.data.get("lastUpdated", None)

    def error(self) -> Optional[str]:
        """Returns the error message as a string, or None if there is
        no error message

        Returns:
            An error message as a string, or None
        """
        return self.data.get("error", None)
    
    def total_population(self) -> Optional[int]:
        """Returns the total population in the game

        Returns:
            int: Total population
            or 
            None: if there is error and this field doesn't show up
        """
        return self.data.get("totalPopulation", None)
    
    def population_by_district(self) -> Optional[Dict]:
        """If there are no errors, returns a dictionary with 
        the names of the districts as keys and the population
        of the district as the corresponding value

        Returns:
            Dict: Population dictionary broken down by district
            or
            None: if there is an error and this field doesn't show up
        """
        return self.data.get("populationByDistrict", None)

class ToontownRewrittenSillyMeter:
    """
    Class that gets the Toontown Rewritten Silly Meter information
    """

    def __init__(self) -> None:
        self.data = _get_data(SILLYMETER_ENDPOINT)

    def refresh(self) -> None:
        """
        Refreshes the API call to get the new data

        DO NOT EXCESSIVELY CALL THIS- You do not want to rate limit
        the API. The standard call time should be once per 5-15 minutes.
        """
        self.__init__()

    def as_of(self) -> Optional[int]:
        """Returns the generated time of the API call

        Returns:
            int: timestamp of the time when API was called
            or
            None: if there is error and this field doesn't show up
        """
        return self.data.get("lastUpdated", None)

    def error(self) -> Optional[str]:
        """Returns the error message as a string, or None if there is
        no error message

        Returns:
            An error message as a string, or None
        """
        return self.data.get("error", None)

    def state(self) -> Optional[str]:
        """
        Returns the Silly Meter State ("Active", "Reward", or "Inactive")
        if the data field exists.

        Returns:
            str: The state of the silly meter
            or
            None: if there is error and this field doesn't show up
        """
        return self.data.get("state", None)
    
    def hp(self) -> Optional[int]:
        """
        Returns the current HP of the silly meter, ranging from
        0-5,000,000.

        Returns:
            int: the HP of the silly meter
            or
            None: if there is error and this field doesn't show up
        """
        return self.data.get("hp", None)

    def rewards(self) -> Optional[List]:
        """
        Returns the Silly meter rewards as a list of three strings
        that the players are eligible to join. These are rerolled when
        the silly meter exits the "Reward" state

        Returns:
            list: The list of the three rewards, as strings
            or
            None: if there is error and this field doesn't show up
        """
        return self.data.get("rewards", None)

    def reward_descriptions(self) -> Optional[List]:
        """
        Returns the Silly meter reward descriptions as a list of 
        three strings describing the current teams that the players 
        are eligible to join. These are updated depending on the 
        current Silly Teams.

        Returns:
            list: The list of the three reward descriptions, as strings
            or
            None: if there is error and this field doesn't show up
        """
        return self.data.get("rewardDescriptions", None)

    def winner(self) -> Optional[str]:
        """
        Returns the willing Silly Team whose reward is currently active.
        Will return None if the state is not set to "Reward"

        Returns:
            str: Willing silly team, as string
            or
            None: if the silly meter is not in the "Reward" state,
            or if there is an error and this field doesn't show up
        """

        return self.data.get("winner", None)

    def reward_points(self) -> Optional[List]:
        """Returns a list of length 3 with the points that each
        Silly Team has acquired. Points are from 0 to 5,000,000.
        This will return [None, None, None] if the state is not
        set to "Reward"

        Returns:
            List: A list of 3 integers representing the points each
            team has acquired, or a list of 3 None's if the state
            is not "Reward"
            or
            None: if there is an error and this field doesn't show up
        """

        return self.data.get("rewardPoints", None)
    
    def next_update_time_stamp(self) -> Optional[int]:
        """
        Returns the timestamp (in seconds) of when the Silly Meter
        will updateitself next. Depends on the state:
        -In the Active state, this indicates the next time that Silly
        Points will be calculated and added in to the current HP
        -In the Reward state, this indicates when the rewards end
        -In the Inactive state, this indicates when the Silly Meter
        will re-enter the Active State

        Returns:
            int: the timestamp (in seconds) of the next update
            or
            None: if there is an error and this field doesn't show up
        """
        return self.data.get("nextUpdateTimestamp", None)
