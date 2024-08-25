import csv  
import os

def load_data(file_path):  
    """ Load stock data from a CSV file. 
        Args:  
        file_path(str): path to the csv file. 
        Returns: 
            list[dict]: List of rows as dictionaries
    """   

    if not os.path.exists(file_path): 
        raise FileNotFoundError(f"The file {file_path} was not found.")  
    with open(file_path, mode='r') as file: 
        reader = csv.DictReader(file) 
        data = [row for row in reader]   

        # validate the data 
    required_columns = ['date', 'symbol', 'close', 'volume'] 
    for column in required_columns: 
        if column not in reader.filednames: 
            raise ValueError(f"Missing required column: {column}")
    return data  

def handle_missing_data(data): 
    cleaned_data = [] 
    for row in data: 
        if all(row.values()): # Check if there are no missing values 
            cleaned_data.append(row) 
    return cleaned_data

"""     try: 
        with open(file_path, mode='r') as file: 
            reader = csv.DictReader(file) 
            data = [row for row in reader] 
        return data  
    except FileNotFoundError: 
        print(f"Error: The file{file_path} was not found.") 
        return []
 """


""" 
import pandas as pd 
def load_data(file_path): 
    return pd.read_csv(file_path)


 """