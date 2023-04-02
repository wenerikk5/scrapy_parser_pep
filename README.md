# scrapy_parser_pep

## Description

A Scrapy parser for collecting information about PEP documentation (static pages). Outcomes will be saved in results directory in 2 csv files:
- with number, name and actual status info ('pep_...csv');
- with quantities of docs in each status ('status_summary_...csv').

## Set up and use

'''
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# Install required dependencies
pip install -r requirements.txt

# Start parsing by command
scrapy crawl pep
'''

Outcome files will be stored in 'project_name/results' directory.

## Additional info

Created for educational purposes. 
