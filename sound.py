import requests
from bs4 import BeautifulSoup
import csv

# Define the URL of the website to scrape
url = 'https://www.worldometers.info/world-population/population-by-country/'

# Send a request to the website and get the HTML response
response = requests.get(url)
html = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find the table containing the population data
table = soup.find('table', {'id': 'example2'})

# Create a CSV file and write the headers to it
with open('population_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Country', 'State/Province', 'City', 'Population'])

    # Find all the rows in the table and loop through them
    for row in table.find_all('tr')[1:]:
        # Extract the country, state/province, city, and population data for the row
        columns = row.find_all('td')
        country_name = columns[1].text.strip()
        state_name = columns[0].text.strip()
        city_name = columns[2].text.strip()
        population_data = columns[3].text.strip().replace(',', '')

        # Write the population data to the CSV file
        writer.writerow([country_name, state_name, city_name, population_data])

# Print a confirmation message to the console
print('Population data for all countries, states, and cities saved to population_data.csv.')
