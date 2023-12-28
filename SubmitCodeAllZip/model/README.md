Basic Idea: 

Most of the methods in this project have a basic idea that the gold and other assets price data of the previous day will be used to predict the close price of gold in the next day. So we need to remove the first data point in the y data (gold close price) and the last data point in the X data (data of features in previous day).