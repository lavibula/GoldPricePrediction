# ***Multi Linear Regression Model Evaluation***


1. Model performance:
- Both Linear Regression, Ridge Reg with the best parameters, Lasso Reg with the best parameters all produce models with almost the same performance.
- The best model we trained was the SIMPLE Ridge regression model when the hyperparameters were simple adjusted: alpha = 0.5, solver='lsqr', the results are below:

| Metrics  | Train Set   | Test Set   |
|----------|-------------|------------|
| R2       | 0.9996      | 0.9991     |
| MSE      | 31.0418     | 31.2566    |
| RMSE     | 5.5715      | 5.5907     |
| MAE      | 3.2427      | 3.6209     |
| MAPE (%) | 0.2175      | 0.2375     |


2. Experiment:
We training with Lasso Regression and obtained Important features as below : ['GOLD_open', 'GOLD_low', 'copper', 'crude_oil', 'DXY', 'NLR'].
We tried training the model with the above input features but the model's performance did not improve much.