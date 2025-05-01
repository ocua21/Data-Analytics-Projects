# Orion Cua
# FIN 320

# All Packages used in this program
import numpy as np
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import minimize
import math

# Cap Weighted Portfolio
def cap_weighted_portfolio (stockSymbols, startDate, endDate, startingPrice):
    '''
    :param stockSymbols: array of stock symbols
    :param startDate: start date of the portfolio
    :param endDate: end date of the portfolio
    :param startingPrice: starting investment of the portfolio
    :return: an array of the growth of the investment
    '''
    stockDataArr = []
    numDays = 0
    for stock in stockSymbols:
        stockData = web.DataReader(stock, "yahoo", startDate, endDate)
        stockDataArr.append(stockData)
        numDays = len(stockData)
    portfolioValue = startingPrice
    portfolioValues = []
    i = 1
    while i < numDays:
        stockMarketValues = []
        returns = []
        totalMarketValue = 0
        for stockData in stockDataArr:
            stockDataDF = pd.DataFrame(stockData)
            stockDataDF = stockDataDF[['Close', 'Volume']]
            marketValue = stockDataDF.iloc[i]['Close'] * stockDataDF.iloc[i]['Volume']
            stockReturn = stockDataDF['Close'].pct_change()
            stockReturn = stockReturn.iloc[i]
            returns.append(stockReturn)
            totalMarketValue += marketValue
            stockMarketValues.append(marketValue)
        s = 0
        newPortValue = 0
        for stockValue in stockMarketValues:
            stockPcnt = stockValue / totalMarketValue
            stockInvest = stockPcnt * portfolioValue
            newPortValue += stockInvest * (1 + returns[s])
            s += 1
        portfolioValue = newPortValue
        portfolioValues.append(portfolioValue)
        i += 1
    return portfolioValues

# Equal-Weighted Portfolio
def equally_weighted_portfolio (stockSymbols, startDate, endDate, startingPrice):
    '''
    :param stockSymbols: array of stock symbols
    :param startDate: start date of the portfolio
    :param endDate: end date of the portfolio
    :param startingPrice: starting investment of the portfolio
    :return: an array of the growth of the investment
    '''
    stockDataArr = []
    numStocks = 0
    numDays = 0
    for symbol in stockSymbols:
        stockData = web.DataReader(symbol, "yahoo", startDate, endDate)
        stockDataArr.append(stockData)
        numDays = len(stockData)
        numStocks += 1
    weight = 1 / numStocks
    i = 1
    portfolioValue = startingPrice
    portfolioValues = []
    while i < numDays:
        newPortValue = 0
        for stockData in stockDataArr:
            stockDataDF = pd.DataFrame(stockData)
            stockReturn = stockDataDF['Close'].pct_change()
            stockReturn = stockReturn.iloc[i]
            stockInvest = weight * portfolioValue
            newPortValue += stockInvest * (1 + stockReturn)
        portfolioValues.append(newPortValue)
        portfolioValue = newPortValue
        i += 1
    return portfolioValues

def msd_risk (weights, volatilityValues, numStocks):
    '''
    calculates mean squared difference of volatility of a portfolio
    :return:
    '''
    totalVolatility = 0
    i = 0
    while i < numStocks:
        totalVolatility += weights[i] * volatilityValues[i]
        i += 1
    pcntVol = []
    targetVol = 1/numStocks
    newVol = []
    i = 0
    while i < numStocks:
        pcntVol.append((weights[i] * volatilityValues[i])/totalVolatility)
        i += 1
    for vol in pcntVol:
        newVol.append((vol - targetVol)**2)
    return (sum(newVol))/numStocks

# Risk Parity Portfolio
def risk_parity_portfolio (stockSymbols, startDate, endDate, startingPrice):
    '''
    :param stockSymbols: array of stock symbols
    :param startDate: the starting day of the portfolio
    :param endDate: the end date of the calculations
    :param startingPrice: initial investment of the portfolio
    :return: array of closing value of the portfolio each day
    '''
    newStartDate = datetime.datetime(startDate.year - 1, startDate.month, startDate.day)
    stocksData = pd.DataFrame()
    for symbol in stockSymbols:
        stocksData[symbol] = web.DataReader(symbol, "yahoo", newStartDate, endDate)['Adj Close']
    numStocks = len(stocksData.columns)
    returns = stocksData.pct_change()
    volatility = returns.rolling(252).std() * math.sqrt(252)
    volatility = volatility[252:]
    returns = returns[252:]
    numDays = len(volatility)
    portfolioValue = startingPrice
    portfolioValues = []
    initial = np.repeat(1 / numStocks, numStocks)
    sum_to_1 = {'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1}
    bounds = ((0.0, 1.0),) * numStocks
    i = 0
    while i < numDays:
        volArray = []
        dailyReturns = []
        for stock in stockSymbols:
            volArray.append(volatility[stock].iloc[i])
            dailyReturns.append(1 + returns[stock].iloc[i])
        weights = minimize(msd_risk, initial, args=(volArray, 5), method='SLSQP', constraints=(sum_to_1),
                           bounds=bounds)
        stockInvest = weights.x * portfolioValue
        newPortValue = sum(dailyReturns * stockInvest)
        portfolioValues.append(newPortValue)
        portfolioValue = newPortValue
        i += 1
    return portfolioValues

def annualized_return(portfolioValues):
    totalDays = len(portfolioValues)
    years = totalDays/252
    annual_return = (((portfolioValues[-1]/portfolioValues[0])**(1/years))-1) * 100
    return annual_return

def portfolio_volatility(portfolioValues):
    stockSeries = pd.Series(portfolioValues)
    returns = stockSeries.pct_change()
    returns = returns[1:]
    vol = returns.std() * math.sqrt(252)
    return vol

def sharpe_ratio(portfolioValues):
    stockSeries = pd.Series(portfolioValues)
    returns = stockSeries.pct_change()
    returns = returns[1:]
    s_ratio = returns.mean() / returns.std()
    return s_ratio

if __name__ == "__main__":
    SD = datetime.datetime(2015, 1, 1)
    ED = datetime.datetime(2021, 1, 1)
    stockSymbols = ['BBW', 'BA', 'CRI', 'IRBT', 'FLWS']
    startingInvestment = 100
    rp_portfolio = risk_parity_portfolio(stockSymbols, SD, ED, startingInvestment)
    cap_portfolio = cap_weighted_portfolio(stockSymbols, SD, ED, startingInvestment)
    ew_portfolio = equally_weighted_portfolio(stockSymbols, SD, ED, startingInvestment)
    rp_portfolio = np.array(rp_portfolio)
    cap_portfolio = np.array(cap_portfolio)
    ew_portfolio = np.array(ew_portfolio)
    print("RISK PARITY PORTFOLIO")
    print("Initial Value: $%0.2f" % startingInvestment)
    print("Final Value: $%0.2f" % (rp_portfolio[-1]))
    print("Annual Returns: %f percent" % annualized_return(rp_portfolio))
    print("Volatility: %f" % portfolio_volatility(rp_portfolio))
    print("Sharpe Ratio: %f" % sharpe_ratio(rp_portfolio))
    print("")
    print("CAP WEIGHTED PORTFOLIO")
    print("Initial Value: $%0.2f" % startingInvestment)
    print("Final Value: $%0.2f" % (cap_portfolio[-1]))
    print("Annual Returns: %f percent" % annualized_return(cap_portfolio))
    print("Volatility: %f" % portfolio_volatility(cap_portfolio))
    print("Sharpe Ratio: %f" % sharpe_ratio(cap_portfolio))
    print("")
    print("EQUAL WEIGHTED PORTFOLIO")
    print("Initial Value: $%0.2f" % startingInvestment)
    print("Final Value: $%0.2f" % (ew_portfolio[-1]))
    print("Annual Returns: %f percent" % annualized_return(ew_portfolio))
    print("Volatility: %f" % portfolio_volatility(ew_portfolio))
    print("Sharpe Ratio: %f" % sharpe_ratio(ew_portfolio))
    plt.figure(1)
    plt.plot(ew_portfolio, color = 'red')
    plt.plot(cap_portfolio, color = 'blue')
    plt.plot(rp_portfolio, color = 'green')
    plt.title('Portfolio Comparison from  ' + str(SD.date()) + ' to ' + str(ED.date()))
    plt.xlabel('Days')
    plt.ylabel('Price (USD)')
    plt.legend(['Equal-Weighted Portfolio', 'Cap-Weighted Portfolio', 'Risk Parity Portfolio'])
    plt.show()


