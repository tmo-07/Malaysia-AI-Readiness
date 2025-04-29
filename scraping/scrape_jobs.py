# scrape_jobs.py

import requests 
from bs4 import BeautifulSoup 
import random 
import pandas as pd 

title = "AI Demand in Malaysia" 
location = "Malaysia" 

list_url = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=ai&location=Malaysia&start=75"  

response = request.get(list_url)   