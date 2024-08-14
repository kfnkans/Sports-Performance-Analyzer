## Data Representation

### Data Overview
This project works with stock market data, represented as structured data in CSV format. The key fields include Date, Stock Symbol, Opening Price, Closing Price, High, Low, and Volume.

### Loading Data
We use the `pandas` library to load and manipulate the data. Here’s an example of how we load the data:

```python
import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('data/raw/stock_data.csv')

# Display the first few rows
print(df.head())
