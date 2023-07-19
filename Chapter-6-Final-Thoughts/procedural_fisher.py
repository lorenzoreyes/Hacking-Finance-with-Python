prompt = '''
Procedural Programming Approach\n
or Imperative, we set a remote control\n
and we dictate how to execute the program 
'''
import os
import oop_fisher as fisher

# plot libraries
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.family'] = 'serif'
plt.style.use('fivethirtyeight')


functions = [i + '()' for i in list(dir(fisher.Strategy)) if '__' not in i]
functions.remove('relative_strenght_index()')

endpoints = {k: v for k, v in enumerate(functions)}

def commands(functions):
    os.system("clear")
    print(prompt)
    [print(f"{i} : {functions[i]}") for i in range(len(functions))]
    cmd = input("\nSELECT ONE INDICATOR TO PLOT\n\n\n>>>\t")

    try:
      cmd = int(cmd)
      symbol = input("\nWhat Stock you want to Analyze?\n\n=>\t") 
      num_days = int(input("\nNumber of Days to use in the indicator?\n\n=>\t"))
      stock = fisher.Strategy(symbol,num_days)
      # instance to ask what switcher the users wants to choose
      if cmd == 0:
          short, long = int(input("\nshort..\t")),int(input("\nlong..\t"))
          stock.absolute_price_oscillator(short, long)
      elif cmd == 1:
          factors = int(input("\nfactors..\t"))
          stock.bollinger_bands(factors)
      elif cmd == 2:
          short, long = int(input("\nshort..\t")),int(input("\nlong..\t"))
          stock.macd(short, long)
      elif cmd == 3:
          stock.momentum()
      elif cmd == 4:
          stock.plot()
      elif cmd == 5:
          stock.simple_moving_average()
      elif cmd == 6:
          stock.standard_deviation()
          
      if cmd != 4:
          stock.plot()
    
    # if not, let run a custom terminal command
    except: 
      os.system(f"{cmd}")
      
    input("\nPRESS [ENTER] in order to continue")
    commands(functions)

if __name__ == '__main__':
  commands(functions)
