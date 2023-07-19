"""
Functional Programming 
"""
import pandas as pd 
import numpy as np 
import yfinance as yahoo

# plot libraries
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.family'] = 'serif'
plt.style.use('fivethirtyeight')



def SimpleMovingAverage(symbol , num_days):
    """Simple Moving Average for num_days given"""
    data = pd.DataFrame(yahoo.download(f'{symbol}', period="1y")["Adj Close"].fillna(method="ffill"))
    data.columns = [i.replace('Adj Close',f'{symbol}') for i in data.columns] 
    bot = pd.DataFrame(data.values,columns=[f'{symbol}'],index=data.index)
    bot[f'SMA{num_days}'] = data[f'{symbol}'].rolling(round(num_days),min_periods=1).mean()
    return bot
    
def Momentum(symbol, num_days):
    """Provide financial 'symbol' to look data 
       Choose number of days for the metric"""
    data = pd.DataFrame(yahoo.download(f'{symbol}', period="1y")["Adj Close"].fillna(method="ffill"))
    data.columns = [i.replace('Adj Close',f'{symbol}') for i in data.columns] 
    bot = pd.DataFrame(data.values,columns=[f'{symbol}'],index=data.index)
    bot['Momentum'] = data[f'{symbol}'] / data[f'{symbol}'].rolling(round(num_days),min_periods=1).mean()
    return bot
    
def BollingerBands(symbol, num_days,stdev_factor):
    """Provide financial 'symbol' to look data 
       Choose number of days for the metric
       number of factors for stdev to apply"""
    data = pd.DataFrame(yahoo.download(symbol, period="1y")["Adj Close"].fillna(method="ffill"))
    data.columns = [i.replace('Adj Close',f'{symbol}') for i in data.columns] 
    bot = pd.DataFrame(data.values,columns=[f'{symbol}'],index=data.index)
    bot['MiddleBand'] = bot[f'{symbol}'].rolling(round(num_days),min_periods=1).mean()
    bot['UpperBand'] = (bot['MiddleBand'] + int(stdev_factor) * bot[f'{symbol}'].rolling(round(num_days),min_periods=1).std())
    bot['LowerBand'] = (bot['MiddleBand'] - int(stdev_factor) * bot[f'{symbol}'].rolling(round(num_days),min_periods=1).std())
    return bot
  
def StandardDeviation(symbol , num_days):
    """Provide financial 'symbol' to look data 
       Choose number of days for the metric"""
    data = pd.DataFrame(yahoo.download(f'{symbol}', period="1y")["Adj Close"].fillna(method="ffill"))
    data.columns = [i.replace('Adj Close',f'{symbol}') for i in data.columns] 
    bot = pd.DataFrame(data.values,columns=[f'{symbol}'],index=data.index)
    bot[f'StDev{num_days}'] = data[f'{symbol}'].rolling(round(num_days),min_periods=1).std()
    return bot
  
def AbsolutePriceOscillator(symbol, short, long):
    """Differences between short-term & long-term
       moving averages to current price,  
       Choose short & long period days"""
    data = pd.DataFrame(yahoo.download(f'{symbol}', period="1y")["Adj Close"].fillna(method="ffill"))
    data.columns = [i.replace('Adj Close',f'{symbol}') for i in data.columns] 
    bot = pd.DataFrame(data.values,columns=[f'{symbol}'],index=data.index)
    bot[f'shortAPO{short}'] = data[f'{symbol}'] - data[f'{symbol}'].rolling(round(short),min_periods=1).mean()
    bot[f'longAPO{long}'] = data[f'{symbol}'] - data[f'{symbol}'].rolling(round(long),min_periods=1).mean()
    return bot
      
def RelativeStrenghtIndex(symbol, time_period):
    """RSI = 100 - (100 / (1 + RS))"""
    data = pd.DataFrame(yahoo.download(f'{symbol}', period="1y")["Adj Close"].fillna(method="ffill"))
    data.columns = [i.replace('Adj Close',f'{symbol}') for i in data.columns] 
    bot = pd.DataFrame(data.values,columns=[f'{symbol}'],index=data.index)
    bot['difference'] = bot[f'{symbol}'].diff()
    bot['loss'] = bot.difference[bot.difference<=0]
    bot['gain'] = bot.difference[bot.difference>=0]
    bot = bot.fillna(0)
    average_gain = pd.Series(bot.gain.rolling(round(time_period),min_periods=1).mean())
    average_loss = pd.Series(bot.loss.rolling(round(time_period),min_periods=1).mean())
    rs = average_gain / -average_loss
    bot[f'{symbol} RSI'] = 100 - (100 /  (1 + rs))
    bot = bot[[f'{symbol}',f'{symbol} RSI']]
    return bot

def MovingAverageConvergenceDivergence(symbol, short, long):
    """Return one line oscillator, betweeen short & long averages, provide periods"""
    data = pd.DataFrame(yahoo.download(f'{symbol}', period="1y")["Adj Close"].fillna(method="ffill"))
    data.columns = [i.replace('Adj Close',f'{symbol}') for i in data.columns] 
    bot = pd.DataFrame(data.values,columns=[f'{symbol}'],index=data.index)
    bot[f'MACD {symbol}'] = data[f'{symbol}'].rolling(round(short),min_periods=1).mean() - data[f'{symbol}'].rolling(round(long),min_periods=1).mean()
    return bot


def plot(bot):
        bot = bot
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
 
