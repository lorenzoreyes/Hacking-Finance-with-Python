import pandas as pd 
import numpy as np 
import yfinance as yahoo
# plot libraries
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.family'] = 'serif'
plt.style.use('fivethirtyeight')



class Strategy():
    """
    Strategy is a class that gathers 6 technicals indicators
    by providing the name of the stock and the quantity of
    days to apply the indicator 
    """
    def __init__(self, symbol, num_days):
        """
        Common attributes
        symbol: str = string of the stock to analyze
        num_days: int = integer as quantity of days to apply
        """
        self.symbol = symbol
        self.num_days = num_days
        self.data = pd.DataFrame(yahoo.download(f'{symbol}', period="1y")["Adj Close"].fillna(method="ffill"))
        self.data.columns = [i.replace('Adj Close',f'{symbol}') for i in self.data.columns] 
        self.bot = pd.DataFrame(self.data.values,columns=[f'{symbol}'],index=self.data.index)
        
    
    """Using self in inner methods we have the scope of the instance"""
    
    def simple_moving_average(self):
        """Simple Moving Average for num_days given"""  
        bot,symbol,num_days = self.bot, self.symbol, self.num_days
        bot[f'SMA {num_days}'] = bot[f'{symbol}'].rolling(round(num_days),min_periods=1).mean()
        return bot
      
    def momentum(self):
        """Provide financial 'symbol' to look data 
           Choose number of days for the metric"""
        bot,symbol,num_days = self.bot, self.symbol, self.num_days
        bot['momentum'] = bot[f'{symbol}'] / bot[f'{symbol}'].rolling(round(num_days),min_periods=1).mean()
        return bot
      
    def bollinger_bands(self, stdev_factor):
        """Choose number of factors for stdev to apply"""
        bot,symbol,num_days = self.bot, self.symbol, self.num_days
        bot['MiddleBand'] = bot[f'{symbol}'].rolling(round(num_days),min_periods=1).mean()
        bot['UpperBand'] = (bot['MiddleBand'] + int(stdev_factor) * bot[f'{symbol}'].rolling(round(num_days),min_periods=1).std())
        bot['LowerBand'] = (bot['MiddleBand'] - int(stdev_factor) * bot[f'{symbol}'].rolling(round(num_days),min_periods=1).std())
        return bot
    
    def standard_deviation(self):
        """Provide financial 'symbol' to look data 
           Choose number of days for the metric"""
        bot,symbol,num_days = self.bot, self.symbol, self.num_days
        bot[f'StDev {num_days}'] = bot[f'{symbol}'].rolling(round(num_days),min_periods=1).std()
        return bot
    
    def absolute_price_oscillator(self, short, long):
        """Differences between short-term & long-term
           moving averages to current price,  
           Choose short & long period days"""
        bot,symbol,num_days = self.bot, self.symbol, self.num_days
        bot[f'shortAPO {short}'] = bot[f'{symbol}'] - bot[f'{symbol}'].rolling(round(short),min_periods=1).mean()
        bot[f'longAPO {long}'] = bot[f'{symbol}'] - bot[f'{symbol}'].rolling(round(long),min_periods=1).mean()
        return bot
        
    def relative_strenght_index(self):
        """RSI = 100 - (100 / (1 + RS))"""
        bot,symbol,num_days = self.bot, self.symbol, self.num_days
        bot['difference'] = bot[f'{symbol}'].diff()
        bot['loss'] = bot.difference[bot.difference<=0]
        bot['gain'] = bot.difference[bot.difference>=0]
        bot = bot.fillna(0)
        average_gain = pd.Series(bot.gain.rolling(round(num_days),min_periods=1).mean())
        average_loss = pd.Series(bot.loss.rolling(round(num_days),min_periods=1).mean())
        rs = average_gain / -average_loss
        bot[f'{symbol} RSI'] = 100 - (100 /  (1 + rs))
        bot = bot[[f'{symbol}',f'{symbol} RSI']]
        return bot 

    def macd(self, short, long):
        """Moving Average Convergence Divergence.
        Provide Integers for Short & Long Oscillators"""
        bot,symbol,num_days = self.bot, self.symbol, self.num_days
        bot[f'MACD Short {short} {symbol}'] = bot[f'{symbol}'].rolling(round(short),min_periods=1).mean()
        bot[f'MACD Long {long} {symbol}'] = bot[f'{symbol}'].rolling(round(long),min_periods=1).mean()
        return bot
    
    def plot(self):
        bot,symbol,num_days = self.bot, self.symbol, self.num_days
        fig = plt.figure(figsize=(30,15))
        ax1 = fig.add_subplot(111)
        bot.plot(ax=ax1, lw=6.)
        title = ' '.join(bot.columns.to_list())
        ax1.set_title(title, fontsize=50, fontweight='bold')
        ax1.grid(True,color='k',linestyle='-.',linewidth=2)
        ax1.legend(loc=0, bbox_to_anchor=(1.1, 0.5),fontsize=40)
        ax1.set(xlabel='Año',ylabel='Precio')
        plt.xticks(size=30, rotation=10)
        plt.yticks(size=60, rotation=10)
        plt.savefig(f"{title}.png")
        plt.show()
