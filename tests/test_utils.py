import unittest 
from src.utils import format_date, handle_missing_data 

class TestUtils(unittest.TestCase): 

    def test_format_date(self):
        date_str = '2024-08-12' 
        date_obj = format_date(date_str) 
        self.assertEqual(date_obj.year, 2024) 
        self.assertEqual(date_obj.month, 8) 
        self.assertEqual(date_obj.day, 12) 
    
    def test_handle_missing_data(self): 
        data = [
            {'date': '2024-08-12', 'symbol': 'AAPL', 'close':'146.00', 'volume': '50000000'}, 
            {'date': '2024-08-13', 'symbol': '', 'close': '148.00', 'volume': '60000000'}
        ] 
        cleaned_data = handle_missing_data(data) 
        self.assertEqual(len(cleaned_data), 1) 

if __name__ == '__main__': 
    unittest.main() 


