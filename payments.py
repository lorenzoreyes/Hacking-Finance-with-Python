'''
Simple task to analyze spectrum of different maturities of payment
key-fact: inflation is 140% at the moment
'''
import pandas as pd
import numpy as np

precios = [10_614,14_518,17_890,21_596,25_570]
inflation = .109#1.40
monthly = inflation#(1 + inflation) ** (1 / 12) - 1

planes = pd.DataFrame(precios,columns=['Precios'])
planes['Dias'] = [i * 90 for i in range(len(precios))]
planes['Recargo'] = planes['Precios'] / planes['Precios'].values[0] - 1
planes['TNA'] = (1+planes['Recargo']) ** (360/planes['Dias']) - 1
planes['Cuota'] = planes['Precios'] / (planes['Dias']/30)
planes['InflacionAcum'] = (1 + monthly) ** (planes['Dias']/30) - 1
planes['Desc.Infl'] = planes['Precios'] / (1+planes['InflacionAcum'])
planes.replace([np.inf, -np.inf], 0, inplace=True)

pagos = []
for i in range(1,5):
    value = planes['Cuota'][i]
    maturity = planes['Dias'][i]//30
    print(f"value\t{value},\nmaturity\t{maturity}")
    pagos.append(sum([value / (1 + monthly) ** i for i in range(1,maturity+1)]))
    
planes['Pagos'] = [0] + pagos
planes['RRecargo'] = planes['Pagos'] / planes['Precios'].values[0] - 1
planes['TRealA'] = (1+planes['RRecargo']) ** (360/planes['Dias']) - 1


planes.to_csv('cuotas.csv')
