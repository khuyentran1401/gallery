# Trends Analysis
This is a datapane-compatible notebook which plots data from Google Trends.

It takes a single input query -- a search term -- and uses `PyTrends` to pull the information from Google, which is then plotted using Altair. 

<img width="800" alt="image" src="https://user-images.githubusercontent.com/3541695/81617218-ee666e80-93dc-11ea-9fb0-debf3036982e.png">

It also pulls the US geographic information from Google, and uses this to plot which states are most interested in a given query.

<img width="793" alt="image" src="https://user-images.githubusercontent.com/3541695/81617123-c119c080-93dc-11ea-9f77-22dcb13dc619.png">

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
- PyTrends
- vega_datasets