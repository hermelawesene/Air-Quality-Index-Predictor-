import os
import sys
import pandas as pd
from bs4 import BeautifulSoup
import csv
from Plot_AQI import avg_data_2013, avg_data_2014, avg_data_2015, avg_data_2016, avg_data_2017, avg_data_2018, avg_data_2019

def met_data(month, year):
    file_path = 'Datae/Html_Data/{}/{}.html'.format(year, month)
    print(f"Attempting to read file: {os.path.abspath(file_path)}")  # Debugging
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return []
    
    with open(file_path, 'rb') as file_html:
        plain_text = file_html.read()

    tempD = []
    finalD = []

    soup = BeautifulSoup(plain_text, "lxml")
    tables = soup.find_all('table', {'class': 'medias mensuales numspan'})
    
    if not tables:
        print(f"No tables found in {file_path}")
        return []

    for table in tables:
        for tbody in table:
            for tr in tbody:
                a = tr.get_text()
                tempD.append(a)

    rows = len(tempD) / 15

    for times in range(round(rows)):
        newtempD = []
        for i in range(15):
            if tempD:  # Check if tempD is not empty
                newtempD.append(tempD[0])
                tempD.pop(0)
        finalD.append(newtempD)

    length = len(finalD)

    if length > 1:
        finalD.pop(length - 1)
        finalD.pop(0)
    else:
        print(f"Not enough data in {file_path} to pop elements.")
        return []

    for a in range(len(finalD)):
        if len(finalD[a]) > 13:  # Ensure the list has enough elements
            finalD[a].pop(6)
            finalD[a].pop(13)
            finalD[a].pop(12)
            finalD[a].pop(11)
            finalD[a].pop(10)
            finalD[a].pop(9)
            finalD[a].pop(0)
        else:
            print(f"Not enough elements in finalD[{a}] to pop.")
            return []

    return finalD

def data_combine(year, cs):
    file_path = 'Datae/Real-Data/real_' + str(year) + '.csv'
    print(f"Attempting to read file: {os.path.abspath(file_path)}")  # Debugging
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return []
    
    for a in pd.read_csv(file_path, chunksize=cs):
        df = pd.DataFrame(data=a)
        mylist = df.values.tolist()
    return mylist

if __name__ == "__main__":
    if not os.path.exists("Datae/Real-Data"):
        os.makedirs("Datae/Real-Data")
    
    # Process data for years 2013 to 2019
    for year in range(2013, 2020):
        final_data = []
        with open('Datae/Real-Data/real_' + str(year) + '.csv', 'w') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            wr.writerow(['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        
        for month in range(1, 13):
            temp = met_data(month, year)
            if temp:  # Only add non-empty data
                final_data = final_data + temp
            
        function_name = 'avg_data_{}'.format(year)
        print(f"Trying to call function: {function_name}")
        if hasattr(sys.modules[__name__], function_name):
            pm = getattr(sys.modules[__name__], function_name)()
        else:
            print(f"Function {function_name} not found")
            continue

        # Debugging: Check lengths of final_data and pm
        print(f"Length of final_data for {year}: {len(final_data)}")
        print(f"Length of pm for {year}: {len(pm)}")

        if len(pm) == 364:
            pm.insert(364, '-')

        # Ensure final_data and pm are not empty
        if not final_data or not pm:
            print(f"Skipping year {year} due to missing data.")
            continue

        # Ensure pm has enough elements for final_data
        if len(pm) < len(final_data):
            print(f"Warning: pm has fewer elements than final_data for {year}. Padding with zeros.")
            pm.extend([0] * (len(final_data) - len(pm)))

        for i in range(len(final_data)-1):
            final_data[i].insert(8, pm[i])

        with open('Datae/Real-Data/real_' + str(year) + '.csv', 'a') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            for row in final_data:
                flag = 0
                for elem in row:
                    if elem == "" or elem == "-":
                        flag = 1
                if flag != 1:
                    wr.writerow(row)
                    
    # Combine data for all years (2013 to 2019)
    data_2013 = data_combine(2013, 600)
    data_2014 = data_combine(2014, 600)
    data_2015 = data_combine(2015, 600)
    data_2016 = data_combine(2016, 600)
    data_2017 = data_combine(2017, 600)
    data_2018 = data_combine(2018, 600)
    #data_2019 = data_combine(2019, 600)
     
    total = data_2013 + data_2014 + data_2015 + data_2016 + data_2017 + data_2018 + data_2019
    
    # Write combined data to a new CSV file
    with open('Datae/Real-Data/Real_Combine.csv', 'w') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        wr.writerows(total)
        
    df = pd.read_csv('Datae/Real-Data/Real_Combine.csv')
    print("Data processing completed successfully.")