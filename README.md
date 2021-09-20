# pytoontown
A Python API Wrapper for popular toontown games (Toontown Rewritten, Toontown: Corporate Clash). Get data on invasions, population, districts, news and more!

## Features

The Toontown Rewritten API Features 3 Classes:
* `ToontownRewrittenInvasion`
* `ToontownRewrittenPopulation`
* `ToontownRewrittenSillyMeter`

The Corporate Clash API features one class, `CorporateClashAPI`, which contains information on districts and the latest corporate clash news.

## Installing

`python3 -m pip install --upgrade pytoontown`

## Documentation

Read the documentation [here](./DOCS.md)

## Code Example

```python
    from pytoontown.toontownrewritten import *
    from pytoontown.corporateclash import *
    from time import sleep

    invasion = ToontownRewrittenInvasion()
    population = ToontownRewrittenPopulation()
    sillymeter = ToontownRewrittenSillyMeter()
    clash = CorporateClashAPI()

    #Refreshes all of the API data
    def refresh():
        invasion.refresh()
        population.refresh()
        sillymeter.refresh()
        clash.refresh()

    #Print out all of the API Data
    def print_data():
        refresh()
        #Retrieve the invasion data as an array.
        #For more information on `as_array`, view the documentation.
        print(f"TTR Invasions: {invasion.invasions(as_array=True)}")

        #Total population in TTR
        print(f"Total Population: {population.total_population}")

        #Population by district in TTR, represented as a dictionary
        print(f"Population by District: {population.population_by_district}")

        #TTR Silly Meter State, which is either "Active", "Reward", or "Inactive"
        print(f"Silly meter state: {sillymeter.state()}")

        #TTR Silly meter rewards (the three silly teams available)
        print(f"Silly Meter rewards: {sillymeter.rewards()}")

        #Description of the Silly teams available
        print(f"Silly meter reward descriptions: {sillymeter.reward_descriptions()}")

        #Silly Team winner (if in reward state)
        print(f"Silly meter winner: {sillymeter.winner()}")

        #how many points each silly team has
        print(f"Silly meter reward points: {sillymeter.reward_points()}"})

        #Corporate clash district breakdown, represented by an array of district objects (dictionaries) (read documentation for more information)
        print(f"Corporate clash districts: {clash.districts()}")

        #Corporate clash news articles, represneted by an array of news articles (dictionaries) (read documentation for more information)
        print(f"Corporate clash news: {clash.news()}")

    
    #Print out the API data every 10 minutes
    while(True):
        print_data()
        time.sleep(600)

```

