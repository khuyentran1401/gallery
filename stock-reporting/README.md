[![Run on Datapane !](https://img.shields.io/badge/Datapane-Run%20script-1abc9c.svg)](https://datapane.com/leo/scripts/stock_analysis/)
[![View on Datapane !](https://img.shields.io/badge/Datapane-View%20sample%20report-ff69b4.svg)](https://datapane.com/leo/reports/stock_report_a9407a67/)

# Stock Reporting
This is a datapane-compatible notebook which takes a list of input stocks and plots the price from a period until today.

<img width="501" alt="image" src="https://user-images.githubusercontent.com/3541695/81616760-012c7380-93dc-11ea-8e7a-13ce12de50ad.png">

Depending on input parameters, it will either plot the actual price in USD, or the [z-score](https://en.wikipedia.org/wiki/Standard_score), so you can plot stocks with different prices on the same terms.

It also uses yfinance to pull the data, and Altair for plotting.

## Usage
Run the Jupyter Notebook to generate reports using `datapane`, or deploy it to Datapane.com if you want to let other people run it through their browser (make sure you're logged in first).

```
~/> datapane script deploy
```

## More information
Check the datapane.yaml for input parameter descriptions.

## Requirements

- pandas
- altair
- yfinance
- datapane
