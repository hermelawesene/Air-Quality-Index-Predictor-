import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the webpage to scrape
url = 'https://www.aqi.in/dashboard/ethiopia/adis-abeba/addis-ababa'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the relevant data on the page
    # Example: Extracting AQI data from a specific table or section
    # Note: You need to inspect the webpage to find the correct HTML elements
    aqi_data = []
    for row in soup.find_all('tr'):
        cols = row.find_all('td')
        if len(cols) > 0:
            aqi_data.append([col.text.strip() for col in cols])
    
    # Convert the extracted data to a DataFrame
    df = pd.DataFrame(aqi_data, columns=['Location', 'AQI', 'PM2.5', 'PM10', 'NO2', 'SO2',"co"])
    
    # Save the DataFrame to a CSV file
    df.to_csv('addis_ababa_aqi_data.csv', index=False)
    print('Data successfully saved to addis_ababa_aqi_data.csv')
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')