# Pytoontown Documentation

Welcome to the official Documentation for Pytoontown. This will be split up into two sections, Toontown Rewritten and Corporate clash. 

# Toontown Rewritten

The Toontown Rewritten api has three classes attached:
* `ToontownRewrittenInvasion`
* `ToontownRewrittenPopulation`
* `ToontownRewrittenSillyMeter`

To initiate these classes nothing is required, just enter the name of the class with parenthesis.

# ToontownRewrittenInvasion

The `ToontownRewrittenInvasion` class has the following methods:

 *def* **refresh**() *returns*  None
 * Refreshes the API call to get the most recent invasion information.

 *def* **last_updated**() *returns* Optional[int]:
 * Returns the last updated time of the API call as an integer timestamp
 * Returns `None` if there is an error with the ToontownRewritten API (if there is an error, only the `error` method will return a non-None value)

 *def* **error**() *returns* Optional[str]:
 * Returns an error message if there is an error with the Toontown Rewritten API, 
 * Returns `None` if there is no error

 *def* **invasions**(*as_array*:bool = False) *returns* Union[Dict, List, None]:
* If *as_array* is False, this method will return a dictionary with the district as the key and the following dictionary as the corresponding value:
    * type (str): The type of the cog
    * asOf (int): The timestamp of when the district last reported invasion status
    * progress (str): The amount of cogs defeated / total number of the cogs in the invasion (i.e 500/2000)
    * Example dictionary return:
    ```json
        {"Splashport":{"asOf":1632146642,"type":"Yesman","progress":"1820/4000"},"Whoosh Rapids":{"asOf":1632146654,"type":"Double Talker","progress":"1803/4000"},"Hiccup Hills":{"asOf":1632146654,"type":"Micromanager","progress":"4590/8000"}}
    ```

* If *as_array* is True, this method will return a list of lists, where each list is of the form: `["District", "Cog Type", "Progress"]`
    * Example list return:
    ```python
        [
            ["Splashport", "Yesman", "1820/4000"],
            ["Whoosh Rapids", "Double Talker", "1803/4000"],
            ["Hiccup Hills", "Micromanager", "4590/8000"]
        ]
    ```

* Returns `None` if there is an error with the ToontownRewritten API (if there is an error, only the `error` method will return a non-None value)

# ToontownRewrittenPopulation

The `ToontownRewrittenPopulation` class has the following methods:

 *def* **refresh**() *returns* None
 * Refreshes the API call to get the most recent invasion information.

 *def* **last_updated**() *returns* Optional[int]:
 * Returns the last updated time of the API call as an integer timestamp
 * Returns `None` if there is an error with the ToontownRewritten API (if there is an error, only the `error` method will return a non-None value)

 *def* **error**() *returns* Optional[str]:
 * Returns an error message if there is an error with the Toontown Rewritten API, 
 * Returns `None` if there is no error

 *def* **total_population**() *returns* Optional[int]:
 * Returns the total in-gamepopulation of Toontown Rewritten
 * Returns `None` if there is an error with the ToontownRewritten API (if there is an error, only the `error` method will return a non-None value)

 *def* **population_by_district**() *returns* Optional[Dict]:
 * Returns a dictionary, with the keys being district names and values being integers representing the district population
 * Returns `None` if there as an error with the ToontownRewritten API (if there is an error, only the `error` method will return a non-None value)

 # ToontownRewrittenSillyMeter

 The `ToontownRewrittenSillyMeter` class has the following methods:

 *def* **refresh**() *returns* None
 * Refreshes the API call to get the most recent invasion information.

 *def* **last_updated**() *returns* Optional[int]:
 * Returns the last updated time of the API call as an integer timestamp
 * Returns `None` if there is an error with the ToontownRewritten API (if there is an error, only the `error` method will return a non-None value)

 *def* **error**() *returns* Optional[str]:
 * Returns an error message if there is an error with the Toontown Rewritten API, 
 * Returns `None` if there is no error

 *def* **state**() *returns* Optional[str]:
 * Returns the Silly meter state, which is one of: `Active`, `Reward`, or `Inactive`. 
 * Returns `None` if there as an error with the ToontownRewritten API (if there is an error, only the `error` method will return a non-None value)

 *def* **hp**() *returns* Optional[int]:
 * Returns the HP of the Silly Meter (from 0 to 5,000,000)
 * Returns `None` if there as an error with the ToontownRewritten API (if there is an error, only the `error` method will return a non-None value)

 *def* **rewards**() *returns* Optional[List]:
 * Returns a list of the three Silly Meter rewards (as strings) that the players are eligibile to join. These are rerolled when the silly meter exists the "Reward" state
 * Returns `None` if there as an error with the ToontownRewritten API (if there is an error, only the `error` method will return a non-None value)

 *def* **reward_descriptions**() *returns* Optional[List]:
 * Returns a list of descriptions (strings) corresponding to the Silly Meter rewards in **rewards*(). 
 * Returns `None` if there as an error with the ToontownRewritten API (if there is an error, only the `error` method will return a non-None value)

 *def* **winner**() *returns* Optional[str]:
 * Returns the winning Silly Team whose reward is currently active if the Silly Meter state is in `Reward`. Returns `None` in any other state
 * Returns `None` if there as an error with the ToontownRewritten API (if there is an error, only the `error` method will return a non-None value)

 *def* **reward_points**() *returns* Optional[List]:
 * Returns a list with 3 integers representing the points that each Silly Team has required (`Reward` state only). Will return `[None, None, None]` if the state is not `Reward`
 * Returns `None` if there as an error with the ToontownRewritten API (if there is an error, only the `error` method will return a non-None value)

 *def* **next_update_time_stamp**() *returns* Optional[int]
 * Returns the timestamp (in seconds) of when the Silly Meter will update itself next. Depends on the Silly Meter state:
    * In the Active state, this indicates the next time that Silly Points will be calculated and added in to the current HP
    * In the Reward state, this indicates when the rewards end
    * In the Inactive state, this indicates when the Silly Meter will re-enter the Active State
 * Returns `None` if there as an error with the ToontownRewritten API (if there is an error, only the `error` method will return a non-None value)


# Corporate Clash

The Corporate Clash API has one class, `CorporateClashAPI`.

# CorporateClashAPI

The `CorporateClashAPI` class has the following methods:

 *def* **refresh**() *returns* None
 * Refreshes the API call to get the most recent invasion information.

 *def* **districts**() *returns* Optional[List]:
 * Returns a list of Dictionaries, where each dictionary represents a district object. The district object has the following key/value pairs:
    * name (str): The name of the district
    * online (boolean): Whether or not the district is online (almost always True)
    * population (int): The population of the district
    * invasion_online (boolean): Whether or not there is an invasion in the district
    * last_updated (int): Last updated timestamp in UTC
    * cogs_attacking (str): Name of the cogs attacking if there is an invasion
    * count_defeated (int): Amount of cogs defeated in the district, refreshes to `0` when a new invasion starts
    * count_total (int): The total amount of cogs in an invasion, defaults to `0` if there is not an invasion happening
    * remaining_time (int): The remaining time in the invasion, defaults to `0` if there is not an invasion
 * Returns `None` if there is some error with the Corporate Clash API

 *def* **news** *returns* Optional[List]:
 * Returns a list of Dictionaries, where each dictionary represents a news article. The news article has the following key/value pairs:
    * id (int): Unique ID of the article
    * author (str): Author of the article
    * posted (str): Date of when the article was posted, in the format: `yyyy-mm-dd hh:mm:ss`
    * image_url (str): URL of the article image
    * title (str): Title of the article
    * summary (str): Summary of the article
    * category (str): Category that the article falls under
* Returns `None` if there is some error with the Corporate Clash API


