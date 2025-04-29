# scrape_jobs.py

import requests 
from bs4 import BeautifulSoup 
import random 
import pandas as pd 
import time 


title = "AI Demand in Malaysia" 
location = "Malaysia"

list_url = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Artificial%2BIntelligence%2B%28AI%29&location=Malaysia&start=275"

response = requests.get(list_url) 

list_data = response.text 
list_soup = BeautifulSoup(list_data, "html.parser")
page_jobs = list_soup.find_all("li")

for job in page_jobs:
    base_card_div = job.find("div", {"class": "base-card"}) 
    job_id = base_card_div.get("data-entity-urn").split(":")[3]
    print(job_id)
    id_list.append(job_id)

job_list = []

for job_id in id_list:
    job_url = f"https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{job_id}"
    job_response = requests.get(job_url) 
    print(job_response.status_code) 
    job_soup = BeautifulSoup(job_response.text, "html.parser") 
    job_post = {}
    try:
        job_post["job_title"] = job_soup.find("h2", {"class": "top-card-layout__title font-sans text-lg papabear:text-xl font-bold leading-open text-color-text mb-0 topcard__title"}).text.strip()
    except:
        job_post["job_title"] = None 
    try:    
        job_post["company_name"] = job_soup.find("a", {"class": "topcard__org-name-link topcard__flavor--black-link"}).text.strip()
    except: 
        job_post["company_name"] = None
    try:
        job_post["time_posted"] = job_soup.find("span", {"class": "posted-time-ago__text topcard__flavor--metadata"}).text.strip()
    except:
        job_post["time_posted"] = None
    try:
        job_post["location"] = job_soup.find("span", {"class": "topcard__flavor topcard__flavor--bullet"}).text.strip()
    except: 
        job_post["location"] = None

        
    job_list.append(job_post) 


jobs_df = pd.DataFrame(job_list) 
jobs_df


jobs_df_clean = jobs_df.dropna(subset=["job_title", "company_name", "location"])

print(f"✅ Total cleaned jobs: {len(jobs_df_clean)}")
jobs_df_clean.head()

jobs_df_clean.loc[:, "time_posted"] = jobs_df_clean["time_posted"].fillna("Not specified")
jobs_df_clean = jobs_df_clean.drop_duplicates()
print(f"✅ Total unique jobs: {len(jobs_df_clean)}")

import os
os.makedirs("../data/processed", exist_ok=True)
jobs_df_clean.to_csv("../data/processed/linkedin_ai_jobs_malaysia_clean.csv", index=False)
jobs_df.to_csv("/Users/t.mo./Desktop/DSEP/Malaysia-AI-Readiness/data/linkedin_ai_jobs_malaysia.csv", index=False)



