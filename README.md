# Scrapy Tutorial Starter
Starter project for scrapy at https://github.com/Chekiria1/dejods

## dejobs
Project for scrapy job vacancies at site dejobs.org (start url - https://dejobs.org/jobs/ajax/joblisting/?num_items=15&offset=).
I save data to csv and json file and SQLite database.

## Dependencies
Python 3.7
Scrapy
apscheduler
json
sqlalchemy
logging
time
datetime


## Running
To run spiders just execute script run.py.
The script will run every day at 11:55
And result will write to the csv, json file "de_jobs (current date and time)" and append to database - dejobs, table - jobs.

## SQLite
Database include 1 table - jobs with 9 column:
id - Integer, primary_key=True
crawled_date - DateTime
url - Text
job_title - Text 
company_name - Text
job_description - Text
location - Text
country - Text
date_posted - Text
https://prnt.sc/qz24ok
