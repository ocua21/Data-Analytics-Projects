# Investment Portfolio Analysis

**Purpose:** This project creates a tool that analyzes the performance of 3 distinct portfolio construction schemes (Cap-Weighted, Equal-Weighted, and Risk Parity). This tool will allow the user to input a list of stocks, start date, end date and investment amount and will return the performance of each portfolio in the given timeframe.

**Background:**

1. **Cap-Weighted Portfolio:** The weight of each asset is directly proportional to the market cap of the asset compared to the total market cap of the portfolio. Naturally, this scheme allows larger companies to control the majority of the portfolio with the smaller companies having smaller shares, leading to lower volatility.
2. **Equal-Weighted Portfolio:** Each asset will make up an equal amount of the portfolio. In a portfolio of n assets, each asset makes up 1/n of the entire portfolio. This portfolio is very diversified and allows for any assets to make an impact on the portfolio, which carries increased volatility/risk.
3. **Risk-Parity Portfolio:** Each asset will have an equal risk contributions to the portfolio. The size of each asset is ignored and instead the volatility is used to determine the weight. The overall risk of the portfolio is flexible and can be configured for each use case.

**Scope:**

1. **Create a function for each portfolio construction scheme that:**

   a. Takes a list of stock symbols, start date, end date and investment amount as inputs

   b. Extracts historical stock data from the web for each stock symbol

   c. Calculates the weight for each stock using the construction scheme

   d. Returns an array containing the portfolio value at the end of each day in the given timeframe

2. **Create functions to analyze the perfomance of each function**

   a. Annualized Rate of Return - A simple metric to determine the average annual return of the portfolio

   b. Portfolio Volatility - A metric that indicates the level of risk by taking the standard deviation of returns

   c. Sharpe Ratio - A widely used financial metric used to give insight into an investment’s returns versus the risk

4. **Test the Portfolio Construction Schemes using 3 test cases**

5. **Visualize the perfomances of each Portfolio Scheme over the same time period**

**RESULTS**

- **Test Case #1** Investing $100 into 5 random stocks [INSM, GS, EA, WMT, MGNI] from 1/1/2015 to 1/1/2021

![image](https://github.com/user-attachments/assets/1fe0cf21-1cc3-4297-b194-8a431861ea36)


![image](https://github.com/user-attachments/assets/1b419a30-eca8-49b6-91ce-88dd9175210a)

In this test case, the Cap-Weighted Portfolio had the best return in the 6-year span as well as the highest Sharpe Ratio


- **Test Case #2** Investing $100 into 3 well performing large cap stocks [WMT, AMZN, MSFT] and 2 well performing small cap stocks [IRBT, VXRT] from 1/1/2015 to 1/1/2021

![image](https://github.com/user-attachments/assets/841de0f1-2a3f-4f82-936a-72da62d126d8)


![image](https://github.com/user-attachments/assets/7076bdc8-4975-4afa-8b39-c03978e5f1ab)

In this test case, the Cap Weighted Portfolio performs the best due to the fact that the large majority of their returns comes from the well performing large cap stocks.

- **Test Case #3** Investing $100 into 2 poor performing large cap stocks [BBW, BA] along with 3 well performing small cap stocks [CRI, IRBT, FLWS] from 1/1/2015 to 1/1/2021

![image](https://github.com/user-attachments/assets/79a8f51b-aa6d-43fc-805f-f489a183fe80)

![image](https://github.com/user-attachments/assets/02dae0ac-9370-4166-aa1d-e1d843f45e38)

In this test case, since the large cap stocks performed poorly, it was the Cap Weighted Portfolio that suffered the most while the Risk Parity Portfolio  performed the best since the stocks within this portfolio did not perform well, so a portfolio with low volatility was be the best option. 
