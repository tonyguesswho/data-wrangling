## Data Wrangling Test


## Description
A script for generating daily and monthly Henry Hub gas prices.



## Dependencies
- requests


## Data
- Data comes from the EIA open data  https://www.eia.gov/dnav/ng/hist/rngwhhdm.htm


- Link to OKFN labs explorer [Explorer](http://explorer.okfnlabs.org/#tonyguesswho/data-wrangling/edit/master/data/daily_prices.csv/view/grid) 

- CSV ouputs for the daily and monthly prices are located in the data folder and can be updated by successfully running the script again

## Links on Datahub

- [Daily Prices](https://datahub.io/anthonyugwu234/daily_prices-itchy-yak-89) 
- [Monthly Prices](https://datahub.io/anthonyugwu234/monthly_prices-thin-mole-59/v/1) 


## Setup Instructions


-   Check that python 3 is installed:

    ```
    python --version
    ```

-   Clone the repo and cd into it:

    ```
    git clone https://github.com/tonyguesswho/data-wrangling.git
    ```

-   Set up a python virtual enviroment:

    ```
    use virtualenv or pipenv
    ```

-   Install dependencies from requirements.txt file:

    ```
    pip install -r requirements.txt

    ```

-   Run the script:

    ```
    python lib/script.py

    ```


## Author
Anthony Ugwu