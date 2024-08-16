import csv 

def load_data(file_path):  
    """ Load stock data from a CSV file. 
        Args:  
        file_path(str): path to the csv file. 
        Returns: 
            list[dict]: List of rows as dictionaries
    """  
    try: 
        with open(file_path, mode='r') as file: 
            reader = csv.DictReader(file) 
            data = [row for row in reader] 
        return data  
    except FileNotFoundError: 
        print(f"Error: The file{file_path} was not found.") 
        return []



""" 
import pandas as pd 
def load_data(file_path): 
    return pd.read_csv(file_path)


 """