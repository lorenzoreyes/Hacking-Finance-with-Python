import time 
import pandas as pd 
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

flujos = [-80,10,10,10,10,10,10,10,10,100]
tasa = 0.1

def valor_actual_neto(flujos:list, tasa:float, periodos:int=0):
    """
    Calculo del Valor Actual Neto (VAN)
    El valor actual neto (VAN) es un criterio de inversión que consiste
    en actualizar los cobros y pagos de un proyecto o inversión para conocer
    cuanto se va a ganar o perder con esa inversión. 
    También se conoce como valor neto actual (VNA), 
    valor actualizado neto o valor presente neto (VPN)
    link concepto: https://economipedia.com/definiciones/valor-actual-neto.html
    
    Variables:
    flujos: list lista que contenga la serie de pagos
    tasa: float tasa para descontar los flujos 
    periodos: int cantidad de periodos del ejercicio 

    Formula Matematica:
    DCF = CFt / (1 + rate) ^ t 
    o Python
    dcf = flujos[i] / (1 + rate) ** i 
    
    VAN = suma(dcf)
    """
    periodos = len(flujos)
    flujo_descontado = [abs(flujos[0])] # abs abreviatura para valor absoluto de la inversion inicial
    tasa_descuento = [1]
    for i in range(1,periodos):
        dcf = flujos[i] / (1 + tasa) ** i
        # los guardo en las respectivas listas 
        flujo_descontado.append(dcf)
        tasa_descuento.append((1+tasa)**i)
    
    # suma acumulada de los valores actuales de los flujos
    valor_flujo_acumulado = [sum(flujo_descontado[:i]) for i in range(len(flujo_descontado))]    
    # sumo el flujo descontado con el valor total del acumulado = VAN
    valor_actual_neto = [sum(i) for i in zip(flujo_descontado,valor_flujo_acumulado)]
    
    # a fines de mostrar paso a paso al pasarlo en un diccionario
    ejercicio = {}
    for i in range(periodos):
        ejercicio[f'Periodo {i}'] =  {'Flujo': flujos[i],
                                      'Tasa': tasa,
                                      'Tasa Aplicada': tasa_descuento[i],
                                      'Valor Flujo en t Periodo': flujo_descontado[i],
                                      'Valor Flujo Acumulado': valor_flujo_acumulado[i],
                                      'Valor Actual Neto': valor_actual_neto[i]}    
    
    for k,v in ejercicio.items():
        print(f"{k}:\n{v}\n")
        
    # o dataframe para verlo formato excel    
    process = pd.DataFrame({'Periodo': range(0,10),
                            'Flujo': flujos,
                            'Tasa': tasa,
                            'Tasa Aplicada': tasa_descuento,
                            'Valor Flujo en t Periodo': flujo_descontado,
                            'Valor Flujo Acumulado': valor_flujo_acumulado,
                            'Valor Actual Neto': valor_actual_neto})

    # asi solamente devolvemos el proceso en formato excel
    return process   
        
        

df = valor_actual_neto(flujos, tasa)        
print(df)
