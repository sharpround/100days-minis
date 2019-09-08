# USA names
Analyzing all the names in the USA social security records.

Names have been aggregated by state and year.

## todo
* develop api to name data (100 days of code)
* download name synonyms
    * get API key
    * connect and download one
    * connect and download all
* set up graph database
    * load name synonym data into database

## nice to have
* move from apistar 0.5.41 most recent release
    * update to using different server, e.g. starlette.io
* automate bigquery query

## done
* download name data from google
* configure environment
* download last name data from census
    * https://www2.census.gov/topics/genealogy/2010surnames/