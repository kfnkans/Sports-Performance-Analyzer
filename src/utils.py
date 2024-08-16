from datetime import datetime  
# use format_date to convert dates when filtering data by date ranges.
def format_date(date_str: str) -> datetime: #convert a string date to datetime object 
    """ Convert a string (YYYY-MM-DD) to a datetime object. 
        Args:  
            date_str(str): Date as a string. 
        Returns: 
            datetime: Date as a datetime object.
       
     """ 
    return datetime.strptime(date_str, '%Y-%m-%d')