def average_closing_price(data: list[dict], symbol: str) -> float:  
    """ Calculate the average closing price for a given stock symbol.
        Args: 
            data(list[dict]): List of stock data. 
            symbol(str): Stock symbol to calculate the average for.  

        Returns: 
            float: Average closing price.
         
     """
    symbol_data = [float(entry['close']) for entry in data if entry['symbol'] == symbol] 
    return sum(symbol_data) / len(symbol_data) if symbol_data else None 
 
def highest_volume_day(data, symbol): 
    """ Find the day with the highest trading volume for a given stock symbol.
        Args: 
            data(list[dict]): List of stock data. 
            symbol(str): Stock symbol to analyze 
        Returns: 
            dict: Row with the highest trading volume.
     """ 
    symbol_data = [entry for entry in data if entry['symbol'] == symbol] 
    return max(symbol_data, key=lambda x: int(x['volume'])) if symbol_data else None
# apple_avg_price = average_closing_price(stock_data, 'AAPL') 
# googl_highest_vol = highest_volume_day(stock_data, 'GOOGL')