# -*- coding: utf-8 -*-
"""
Created on Fri May 10 01:57:05 2024

@author: ChelseySSS
"""

#look at this list of best-selling artists, particularly the table
#for those with more than 250m records sold:
#https://en.wikipedia.org/wiki/List_of_best-selling_music_artists

#1. Are we allowed to scrape the data from this page with a program?
#what two things should we check?

import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_best-selling_music_artists'

# Sending a GET request to the URL
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Locating the table for artists with more than 250 million records sold
table = soup.find_all('table', {'class': 'wikitable'})[0]  

# Extracting the rows of the table
rows = table.find_all('tr')

# Parsing each row for data
artists = []
for row in rows[1:]:  
    cols = row.find_all('td')
    if cols:
        artist_name = cols[0].text.strip()
        record_sold = cols[1].text.strip()
        artists.append((artist_name, record_sold))

# Printing the list of artists and records sold
for artist in artists:
    print(artist)
    



#2. Once verifying that we're allowed to, collect the 250m+ table
#into a csv document.

import requests
from bs4 import BeautifulSoup
import csv

url = 'https://en.wikipedia.org/wiki/List_of_best-selling_music_artists'

# File to write the CSV data
csv_file_path = 'artists_250m_plus.csv'

# Creating a CSV file and writing the data
with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Writing header row
    writer.writerow(['Artist Name', 'Records Sold'])

    # Parsing each row for data and writing to CSV
    for row in rows[1:]:  
        cols = row.find_all('td')
        if cols:
            artist_name = cols[0].text.strip()
            record_sold = cols[1].text.strip()
            writer.writerow([artist_name, record_sold])

print(f'Data successfully written to {csv_file_path}')
