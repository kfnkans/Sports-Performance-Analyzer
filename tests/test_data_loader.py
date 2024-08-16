import unittest 
from src.data_loader import load_data 

class TestDataLoader(unittest.TestCase): 
    def test_load_data_valid_file(self): 
        data = load_data('data/raw/stock_data.csv') 
        self.assertGreater(len(data), 0) 
    
    def test_load_data_missing_file(self): 
        with self.assertRaises(FileNotFoundError): 
            load_data('data/raw/non_exisistent.csv') 

if __name__ == '__main__': 
    unittest.main() 

