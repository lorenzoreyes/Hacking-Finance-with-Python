'''
We are illustrating how to calculate rates conversion
with Raw Python, no libraries needed just the formulas
'''
def annual_effective(rate,days):
    '''
    Convert annual rate into effective real rate
    rate: float = annual rate as reference
    days: int = days pending to calculate
    year convention assumed 365
    formula = (1 + rate / year) ** (year / days) - 1
    '''
    effective = (1 + rate / 365) ** (365 / days) -1
    return effective


def annual_months(rate,time):
    '''
    Convert annual rate into monthly 1 2 3... rate 
    rate: float = annual rate as reference
    time: int = frequency monthly, bi, quarter...
    formula = (1 + rate) ** (time /12) - 1
    '''
    monthly = (1 + rate) ** (time / 12) - 1
    return monthly

def months_annual(rate,time):
    '''
    Convert back to annualized rate
    rate: float = rate of reference
    time: int = frequency of the rate given
    formula = (1 + rate) ** (12 /time) - 1 
    '''
    annual = (1 + rate) ** (12 / time) - 1
    return annual 


def effective_annual(rate,days):
    '''
    Convert back to annual rate from effective real rate
    rate: float = annual rate as reference
    days: int = days pending to calculate
    year convention assumed 365
    formula = ((1 + rate/365) ** (365/days) - 1) * 100
    '''
    annual = ((1 + rate/365) ** (365/days) - 1) * 100 
    return annual
