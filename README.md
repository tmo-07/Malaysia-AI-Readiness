# Malaysia-AI-Readiness
Analysing AI adoption readiness across Malaysian industries using job listing data and web scraping.

# Malaysia AI Readiness Analysis

## Project Overview:
This project assesses AI adoption readiness in Malaysian industries using web-scraped job listings and additional public datasets.

## Objectives:
- Identify industries leading in AI adoption.
- Explore trends in demand for AI skills.
- Inform policy makers, strategists, and potential investors.

## Data Sources:
- Job listings: JobStreet, Indeed Malaysia, LinkedIn Jobs
- Supplementary: Reports (MDEC, DOSM, World Bank)

## Methodology:
- Web scraping of job listing websites
- NLP for keyword extraction
- Sector-level readiness scoring
- Cluster analysis (K-means, PCA)
- Data visualisation

## Project Structure:
malaysia-ai-readiness/
├── data/                 #   Raw and cleaned datasets
│   ├── raw/              #   └── Unprocessed scraped data
│   └── cleaned/          #   └── Preprocessed sector-level features
│
├── notebooks/            # 📓 Jupyter notebooks for analysis, EDA, and scoring
│   └── exploration.ipynb #     Initial data exploration and visualisation
│
├── scraping/             #   Python scripts for web scraping job listings
│   └── scrape_jobs.py    #     Main scraper (e.g., JobStreet, LinkedIn)
│
├── output/               # 📊 Final charts, tables, model outputs
│   ├── plots/            #     Static visual outputs for blog
│   └── tables/           #     Generated data tables
│
├── blog.qmd              # 📝 Final Quarto blog post (or blog.ipynb)
├── README.md             # 📘 Project overview, goals, replication steps
├── requirements.txt      # 📦 Python dependencies (for reproducibility)
└── venv/                 # 🔐 Python virtual environment (not pushed to GitHub)

## Replication Instructions:
1. Clone this repository:
git clone https://github.com/tmo-07/Malaysia-AI-Readiness.git

2. Activate the virtual environment:
source venv/bin/activate

3. Install requirements:
pip install -r requirements.txt

4. Run scripts/notebooks as detailed.

## Author:
[Ryan Faiz](www.linkedin.com/in/ryanfaiz)

