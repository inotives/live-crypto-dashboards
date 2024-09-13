import ta 
import pandas as pd 

def data_prep(data):
    
    # make sure date as index
    data['metric_date'] = pd.to_datetime(data['metric_date'])
    data.set_index('metric_date', inplace=True)
    
    # Sort the data by timestamp
    data.sort_index(inplace=True)

    return data


# Adding Technical Indicator to OHLCV Dataframe
def add_technical_indicitors(data):
    """Add commonly technical indicator to improve OHLCV data."""

    '''data prep '''
    data = data_prep(data)

    '''price_change: price changes during the trading period '''
    data['price_change'] = data['close'] - data['open']

    '''price_range: price volatilty during the trading period. higher = more volatile '''
    data['price_range'] = data['high'] - data['low']

    '''price_momentum: day-over-day price changes. positive momentum = upward trend, negative=downward trend '''
    data['price_momentum'] = data['close'].diff()


    '''typical_price: average price of the period. '''
    data['typical_price'] = (data['open']+data['high']+data['low']+data['close']) / 4


    '''volume_change (VROC): day-over-day change of trading volume'''
    data['volume_change'] = data['volume'].diff()

    '''market_cap_change: day-over-day change of market cap '''
    data['mkcap_change'] = data['market_cap'].diff()

    '''Volume Weighted Average Price (VWAP)
    VWAP is a technical analysis indicator that represents the average price a asset has traded at
    throughout the day, weighted by volume. It is calculated by taking the sum of the product of price
    and volume for each trade, divided by the total volume traded for that day.'''
    data['vwap'] = ta.volume.volume_weighted_average_price(data['high'], data['low'], data['close'], data['volume'])

    '''daily_return: day-over-day price changes in % or rate of changes. positive=upward trend, negative=downward-trend
    cummulative_return : total return achieved over a period, considering the compounding of returns.
    calculate by taking the cumulative product of the daily returns plus one (to represent the return for each day).
    '''
    data['daily_return'] = data['close'].pct_change()
    data['cumulative_return'] = (1 + data['daily_return']).cumprod() - 1


    '''Average True Range (ATR) 
    ATR is a technical indicator that measures volatility by calculating the average True Range (TR)
    over a specific period (typically 14 days). A high ATR indicates a volatile market with large price swings.
    A low ATR suggests a less volatile market with smaller price movements.'''
    data['atr'] = ta.volatility.average_true_range(data['high'], data['low'], data['close'], window=14)

    '''Moving Average (MA) or Simpe Moving Average (SMA)
    Moving averages (MAs) are technical indicators that smooth out price data by calculating
    the average price over a specific period. They are widely used in technical analysis
    to identify trends, support and resistance levels, and potential reversal points.
    '''
    data['ma_20'] = data['close'].rolling(window=20, min_periods=1).mean()
    data['ma_50'] = data['close'].rolling(window=50, min_periods=1).mean()
    data['ma_100'] = data['close'].rolling(window=100, min_periods=1).mean()
    data['ma_200'] = data['close'].rolling(window=200, min_periods=1).mean()
    
    '''Exponential Moving Average (EMA)
    EMA gives more weight to recent prices, making it more responsive to price changes. Usually used with crossover between 2 EMA period. 
    Common used crossover period: 
    - Shorter term - EMA 7 & EMA 14
    - Longer term - EMA 14 & EMA 28
    '''
    data['ema_7'] = data['close'].ewm(span=7, adjust=False).mean()
    data['ema_14'] = data['close'].ewm(span=14, adjust=False).mean()
    data['ema_20'] = data['close'].ewm(span=20, adjust=False).mean()
    data['ema_28'] = data['close'].ewm(span=28, adjust=False).mean()
    data['ema_50'] = data['close'].ewm(span=50, adjust=False).mean()

    ''' WMA (Weighted Moving Average)
    Common used WMA window: 
    - Short-term (5) and Long-term (20): This combination is popular for capturing short-term trends and identifying potential buy or sell signals.
    - Short-term (12) and Long-term (26): This is often used in conjunction with the MACD indicator, which uses these same window sizes.
    '''
    data['wma_5'] = ta.trend.WMAIndicator(data['close'], window=5).wma() # use for short-term crossover
    data['wma_7'] = ta.trend.WMAIndicator(data['close'], window=7).wma() # use for short-term crossover
    data['wma_12'] = ta.trend.WMAIndicator(data['close'], window=12).wma() # use for short-term crossover
    data['wma_14'] = ta.trend.WMAIndicator(data['close'], window=14).wma() # use for short-term crossover
    data['wma_20'] = ta.trend.WMAIndicator(data['close'], window=20).wma() # use for longer-term crossover
    data['wma_26'] = ta.trend.WMAIndicator(data['close'], window=26).wma() # use for longer-term crossover

    ''' Standard Deviation
    Standard deviation is a statistical measure that quantifies the amount of variation or dispersion in a set of data values.
    It tells you how much the data points deviate from the mean (average) of the dataset.
    We will apply the standard deviation calculation over a set window (20, 50) to measure the volatility level.
    '''
    data['std_20'] = data['close'].rolling(window=20, min_periods=1).std()
    data['std_50'] = data['close'].rolling(window=50, min_periods=1).std()

    '''Relative Strengh Index (RSI)
    RSI is a momentum oscillator that measures the speed and change of price movements.
    It helps identify overbought or oversold conditions in an asset.
    '''
    data['rsi'] = ta.momentum.rsi(data['close'], window=14)

    '''Bollinger Bands
    Bollinger Bands are a technical analysis tool that plots bands around a simple moving average (SMA)
    of an asset's price. They are based on standard deviations from the SMA. it creates a band of
    three lines (SMA, upper band, and lower band), which can indicate overbought or oversold conditions
    when prices move outside the bands. Typically using Window lenght of 20-days in SMA and Std.Dev
    more can be read here: https://www.britannica.com/money/bollinger-bands-indicator
    '''
    data['bb_upper'] = ta.volatility.bollinger_hband(data['close'], window=20, fillna=True)
    data['bb_lower'] = ta.volatility.bollinger_lband(data['close'], window=20, fillna=True)

    '''Moving Average Convergence Divergence (MACD)
    MACD is a popular TI used in tech analysis to identify changes in momentum and potential trend reversals. 
    It consists of two exponential moving averages (EMAs) and their difference, known as the histogram.
    '''
    data['macd'] = ta.trend.macd(data['close'])


    return data