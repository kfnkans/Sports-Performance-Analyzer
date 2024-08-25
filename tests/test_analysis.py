# contains unit tests for analysis.py script. These tests ensure that the analysis functions return correct and expected results based on the input data 
import unittest 
from src.analysis import average_closing_price, average_volume, highest_volume_day

class TestAnalysis(unittest.TestCase): 
    def test_average_closing_price(self): 
        data = [
            {'date': '2024-08-12', 'symbol': 'AAPL', 'close':'146.00'}, 
            {'date': '2024-08-13', 'symbol': 'AAPL', 'close': '148.00'}, 
            {'date': '2024-08-14', 'symbol': 'AAPL', 'close': '144.00'}
        ] 
        avg_price = average_closing_price(data, 'AAPL') 
        self.assertEqual(avg_price, 144.00)  
        #self.assertEqual(avg_price, 147.00)  

    def test_highest_volume_day(self):
        data = [
            {'date': '2024-08-12', 'symbol': 'AAPL', 'volume': '50000000'},
            {'date': '2024-08-13', 'symbol': 'AAPL', 'volume': '55000000'},
        ]
        highest_vol_day = highest_volume_day(data, 'AAPL') 
        self.assertEqual(highest_vol_day['date'], '2024-08-13')
        # self.assertEqual(highest_vol['volume'], '55000000') 
    def test_average_volume(self):
        data = [
            {'date': '2024-08-12', 'symbol': 'AAPL', 'volume': '50000000'},
            {'date': '2024-08-13', 'symbol': 'AAPL', 'volume': '55000000'},
            {'date': '2024-08-14', 'symbol': 'AAPL', 'volume': '52000000'},
        ]
        avg_volume = average_volume(data, 'AAPL')
        self.assertEqual(avg_volume, 52333333.33)


if __name__ == '__main__': 
    unittest.main()