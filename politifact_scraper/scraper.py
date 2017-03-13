"""
Author: Adam Hamrick
3/13/2017
Python 3.5.2
Scrapes politifact statements within their requests to "be kind".
Then places requests in a CSV.
"""

import os.path
import csv

FILE_NAME = "./statements.csv"

def main():
    """Main driver for the scraper.

    Builds statements and places them in CSV file.
    """
    if os.path.isfile(FILE_NAME):
        read_csv()

def read_csv():
    """Finds place in existing csv file

    This is depending on how politifact wants me to work its API.
    The intent is to keep place in the CSV file to adhere to their wishes.
    But their API won't allow me an offset, so we'll see.
    """
    statement_file = open(FILE_NAME)
    for row in statement_file:
        print row

if __name__ == "__main__":
    main()
