Malaysia AI Job Market Analysis

This project is part of an empirical assignment for the Data Science in Economics module at the University of Exeter. It explores the AI job landscape in Malaysia using web scraping, data cleaning, and exploratory data analysis (EDA) to identify key trends in job demand, location hotspots, and role characteristics.


## Project Structure:
Malaysia-AI-Readiness/
│
├── data/
│   ├── raw/                         # Scraped unprocessed job data
│   └── processed/                   # Cleaned data used for analysis
│
├── notebooks/
│   └── Malaysia_AI_Job_Market_Analysis.ipynb  # Main analysis & blog post notebook
│
├── scraping/
│   └── scrape_jobs.py              # LinkedIn job scraper script
│
├── output/                         # Directory for exported visuals (optional)
│
├── requirements.txt               # List of required Python packages
└── README.md                      # Project overview and replication instructions

##Project Objectives:

- Identify where AI jobs are most concentrated across Malaysia.

- Analyse job titles and word frequency to understand role demand.

- Determine which companies are leading in AI hiring.

- Track the recency and freshness of job listings.

## Data Sources:
- Job listings: LinkedIn Jobs


## How to Replicate This Project

1. Clone the Repository

git clone https://github.com/yourusername/Malaysia-AI-Readiness.git
cd Malaysia-AI-Readiness

2. Set Up a Virtual Environment (macOS/Linux)

python3 -m venv venv
source venv/bin/activate

3. Install All Dependencies

pip install -r requirements.txt

4. Run the Scraper (Optional)

If you want to scrape fresh job listings:

cd scraping
python scrape_jobs.py

Output is saved to: data/raw/

NOTE: to scrape more jobs just vary the 'start' number at the end of the list_url and keep scraping. You could use a simple for loop if you're capable of doing so, automating it will save a lot of time!

Your data is now cleaned and ready for you to do some EDA of your choice 

5. Open the Notebook

Jupyter notebook 

Then open:

notebooks/Malaysia_AI_Job_Market_Analysis.ipynb

This notebook includes:

- Full exploratory data analysis

- Visuals and interpretation

- Final blog-style writeup


6. View the Processed Dataset

You can find the cleaned data used for analysis at: 

data/processed/linkedin_ai_jobs_malaysia_clean.csv

Export the Notebook as PDF (Optional)

To export your blog post to PDF:

jupyter nbconvert --to pdf notebooks/Malaysia_AI_Job_Market_Analysis.ipynb

Note: You may need to install Pandoc: https://pandoc.org/installing.html in order to do this 


##Tools Used

Python 3.13

BeautifulSoup & Requests (for scraping)

Pandas (for data manipulation)

Seaborn & Matplotlib (for data visualization)

WordCloud (for textual analysis)

Jupyter Notebook (for documentation and blog writing)



## Visual Insights

This project generated insights through several key visuals:

- Heatmap of companies vs job locations

- Most frequent words in job titles

- Word cloud of job role keywords

- Distribution of postings by age

- Top hiring companies in Malaysia

= Regional analysis of demand (location counts)


## Author 

Author: Ryan Faiz

University of Exeter — BSc Economics and Finance with Industrial Experience

Thanks to the module lead and teaching assistants for their support and guidance throughout this assignment.







