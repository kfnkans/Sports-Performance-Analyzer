def average_closing_price(data: list[dict], symbol: str) -> float:  
    """ Calculate the average closing price for a given stock symbol.
        Args: 
            data(list[dict]): List of stock data. 
            symbol(str): Stock symbol to calculate the average for.  

        Returns: 
            float: Average closing price.
         
     """ 
    
    """ def average_closing_price(data, symbol):
            total = 0
            count = 0
            for row in data:
                if row['symbol'] == symbol:
                    total += float(row['close'])
                    count += 1
            return total / count if count > 0 else 0 """
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
    """ def highest_volume_day(data, symbol):
    highest_vol_day = None
    highest_vol = 0
    for row in data:
        if row['symbol'] == symbol:
            volume = int(row['volume'])
            if volume > highest_vol:
                highest_vol = volume
                highest_vol_day = row
    return highest_vol_day
 """
    symbol_data = [entry for entry in data if entry['symbol'] == symbol] 
    return max(symbol_data, key=lambda x: int(x['volume'])) if symbol_data else None 

def lowest_closest_price(data: list[dict], symbol: str) -> float: 
    """Find the lowest closing price for a given stock symbol. 
    Args: 
        data(list[dict]): List of stock data. 
        symbol (str): Stock symbol to analyze. 
    
    Returns: 
        float: Lowest closing price.
    """ 
    symbol_data = [float(entry['close']) for entry in data if entry['symbol'] == symbol] 
    return min(symbol_data) if symbol_data else None 

def average_volume(data: list[dict], symbol: str) -> float: 
    """Calculate the average trading volume for a given stock symbol. 
    Args:  
        data(list[dict]): List of stock data. 
        symbol(str): Stock symbol to analyze.
    
    Returns: 
        float: Average trading volume.
    """ 
    symbol_data = [int(entry['volume']) for entry in data if entry['symbol'] == symbol] 
    return sum(symbol_data) / len(symbol_data) if symbol_data else None
# apple_avg_price = average_closing_price(stock_data, 'AAPL') 
# googl_highest_vol = highest_volume_day(stock_data, 'GOOGL')