from Plot_AQI import avg_data_2013, avg_data_2014, avg_data_2015, avg_data_2016
import requests
import sys
import pandas as pd
from bs4 import BeautifulSoup
import os
import csv
<<<<<<< HEAD
=======
from Plot_AQI import avg_data_2013, avg_data_2014, avg_data_2015, avg_data_2016
>>>>>>> 41dbcf3393e9a1548155e9781dee2bbf343b4d7f

def met_data(month, year):
    file_path = 'Data/Html_Data/{}/{}.html'.format(year, month)
    print(f"Attempting to read file: {os.path.abspath(file_path)}")  # Debugging
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return []
    
    with open(file_path, 'rb') as file_html:
        plain_text = file_html.read()

    tempD = []
    finalD = []

    soup = BeautifulSoup(plain_text, "lxml")
    for table in soup.find_all('table', {'class': 'medias mensuales numspan'}):
        for tbody in table:
            for tr in tbody:
                a = tr.get_text()
                tempD.append(a)

    rows = len(tempD) / 15

    for times in range(round(rows)):
        newtempD = []
        for i in range(15):
<<<<<<< HEAD
            if tempD:  # Ensure tempD is not empty
                newtempD.append(tempD[0])
                tempD.pop(0)
=======
            newtempD.append(tempD[0])
            tempD.pop(0)
>>>>>>> 41dbcf3393e9a1548155e9781dee2bbf343b4d7f
        finalD.append(newtempD)

    length = len(finalD)

    finalD.pop(length - 1)
    finalD.pop(0)

    for a in range(len(finalD)):
        finalD[a].pop(6)
        finalD[a].pop(13)
        finalD[a].pop(12)
        finalD[a].pop(11)
        finalD[a].pop(10)
        finalD[a].pop(9)
        finalD[a].pop(0)

    return finalD

def data_combine(year, cs):
    file_path = 'Data/Real-Data/real_' + str(year) + '.csv'
    print(f"Attempting to read file: {os.path.abspath(file_path)}")  # Debugging
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return []
    
    for a in pd.read_csv(file_path, chunksize=cs):
        df = pd.DataFrame(data=a)
        mylist = df.values.tolist()
    return mylist

if __name__ == "__main__":
    if not os.path.exists("Data/Real-Data"):
        os.makedirs("Data/Real-Data")
    
    for year in range(2013, 2017):
        final_data = []
        with open('Data/Real-Data/real_' + str(year) + '.csv', 'w') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            wr.writerow(['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        
        for month in range(1, 13):
            temp = met_data(month, year)
            final_data = final_data + temp
            
        function_name = 'avg_data_{}'.format(year)
        print(f"Trying to call function: {function_name}")
        if hasattr(sys.modules[__name__], function_name):
            pm = getattr(sys.modules[__name__], function_name)()
        else:
            print(f"Function {function_name} not found")
            continue

        if len(pm) == 364:
            pm.insert(364, '-')

        # Ensure final_data and pm are not empty
        if not final_data or not pm:
            print(f"Skipping year {year} due to missing data.")
            continue

<<<<<<< HEAD
        # Ensure pm has enough elements for final_data
        if len(pm) < len(final_data):
            print(f"Warning: pm has fewer elements than final_data for {year}. Padding with average values.")
            avg_pm = sum(pm) / len(pm) if pm else 0  # Calculate average PM2.5
            pm.extend([avg_pm] * (len(final_data) - len(pm)))  # Pad with average PM2.5

        for i in range(len(final_data)):
            final_data[i].insert(8, pm[i])

=======
        for i in range(len(final_data)):
            if i < len(pm):  # Ensure we don't exceed the length of pm
                final_data[i].insert(8, pm[i])
            else:
                final_data[i].insert(8, 0)  # Insert a default value if pm is shorter

>>>>>>> 41dbcf3393e9a1548155e9781dee2bbf343b4d7f
        with open('Data/Real-Data/real_' + str(year) + '.csv', 'a') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            for row in final_data:
                flag = 0
                for elem in row:
                    if elem == "" or elem == "-":
                        flag = 1
                if flag != 1:
                    wr.writerow(row)
                    
    data_2013 = data_combine(2013, 600)
    data_2014 = data_combine(2014, 600)
    data_2015 = data_combine(2015, 600)
    data_2016 = data_combine(2016, 600)
     
    total = data_2013 + data_2014 + data_2015 + data_2016
    
    with open('Data/Real-Data/Real_Combine.csv', 'w') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        wr.writerows(total)
        
    df = pd.read_csv('Data/Real-Data/Real_Combine.csv')
    print("Data processing completed successfully.")