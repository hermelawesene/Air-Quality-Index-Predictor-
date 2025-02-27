import pandas as pd
import os

def avg_data_2013():
    file_path = 'Data/AQI/aqi2013.csv'
    print(f"Attempting to read file: {os.path.abspath(file_path)}")  # Debugging
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        # Return a list of 365 zeros as a placeholder
        return [0] * 365
    
    temp_i = 0
    average = []
    for rows in pd.read_csv(file_path, chunksize=24):
        add_var = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data=rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var += i
            elif type(i) is str:
                if i not in ['NoData', 'PwrFail', '---', 'InVld']:
                    temp = float(i)
                    add_var += temp
        avg = add_var / 24
        temp_i += 1
        average.append(avg)
    return average

def avg_data_2014():
    file_path = 'Data/AQI/aqi2014.csv'
    print(f"Attempting to read file: {os.path.abspath(file_path)}")  # Debugging
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        # Return a list of 365 zeros as a placeholder
        return [0] * 365
    
    temp_i = 0
    average = []
    for rows in pd.read_csv(file_path, chunksize=24):
        add_var = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data=rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var += i
            elif type(i) is str:
                if i not in ['NoData', 'PwrFail', '---', 'InVld']:
                    temp = float(i)
                    add_var += temp
        avg = add_var / 24
        temp_i += 1
        average.append(avg)
    return average

def avg_data_2015():
    file_path = 'Data/AQI/aqi2015.csv'
    print(f"Attempting to read file: {os.path.abspath(file_path)}")  # Debugging
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        # Return a list of 365 zeros as a placeholder
        return [0] * 365
    
    temp_i = 0
    average = []
    for rows in pd.read_csv(file_path, chunksize=24):
        add_var = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data=rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var += i
            elif type(i) is str:
                if i not in ['NoData', 'PwrFail', '---', 'InVld']:
                    temp = float(i)
                    add_var += temp
        avg = add_var / 24
        temp_i += 1
        average.append(avg)
    return average

def avg_data_2016():
    file_path = 'Data/AQI/aqi2016.csv'
    print(f"Attempting to read file: {os.path.abspath(file_path)}")  # Debugging
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        # Return a list of 365 zeros as a placeholder
        return [0] * 365
    
    temp_i = 0
    average = []
    for rows in pd.read_csv(file_path, chunksize=24):
        add_var = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data=rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var += i
            elif type(i) is str:
                if i not in ['NoData', 'PwrFail', '---', 'InVld']:
                    temp = float(i)
                    add_var += temp
        avg = add_var / 24
        temp_i += 1
        average.append(avg)
    return average

def avg_data_2017():
    file_path = 'Data/AQI/aqi2017.csv'
    print(f"Attempting to read file: {os.path.abspath(file_path)}")  # Debugging
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        # Return a list of 365 zeros as a placeholder
        return [0] * 365
    
    temp_i = 0
    average = []
    for rows in pd.read_csv(file_path, chunksize=24):
        add_var = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data=rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var += i
            elif type(i) is str:
                if i not in ['NoData', 'PwrFail', '---', 'InVld']:
                    temp = float(i)
                    add_var += temp
        avg = add_var / 24
        temp_i += 1
        average.append(avg)
    return average

def avg_data_2018():
    file_path = 'Data/AQI/aqi2018.csv'
    print(f"Attempting to read file: {os.path.abspath(file_path)}")  # Debugging
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        # Return a list of 365 zeros as a placeholder
        return [0] * 365
    
    temp_i = 0
    average = []
    for rows in pd.read_csv(file_path, chunksize=24):
        add_var = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data=rows)
        for index, row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var += i
            elif type(i) is str:
                if i not in ['NoData', 'PwrFail', '---', 'InVld']:
                    temp = float(i)
                    add_var += temp
        avg = add_var / 24
        temp_i += 1
        average.append(avg)
    return average

if __name__ == "__main__":
    lst2013 = avg_data_2013()
    lst2014 = avg_data_2014()
    lst2015 = avg_data_2015()
    lst2016 = avg_data_2016()
    lst2017 = avg_data_2017()
    lst2018 = avg_data_2018()
    print("Data processed successfully.")