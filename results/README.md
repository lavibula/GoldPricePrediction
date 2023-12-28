
General performance summary table of models:

SORT ACCORDING **R2_TEST**:

|                   |Train Set| Train Set|Train Set|Test Set|Test Set|Test Set|
|-------------------|-------|----------|---------|-------|----------|---------|
| **Model**         | **R2** | **RMSE** | **MAPE%**   | **R2**    | **RMSE**    | **MAPE%**  |
| Linear Regression | 0.9996 | 5.5715 | 0.2175%  | 0.9991 | 5.5907 | 0.2375% |
| Random Forest     |  *0.992* | 3.4621 | 0.1673% | 0.9911 | 9.5096| 0.3585% |
| GRU               | 0.9939 | 13.9366 | 0.69% | 0.9706 | 17.4278 | 0.71% |
| KNN               | 0.9964   | 13.8035     | 0.6741%        | 0.9520     | 21.8558    | 0.9189%  |
| Adaboost          | 0.9989    | 7.6105     | 0.3304%    | 0.9468     | 23.0224    | 0.9565%  |


Based on the general performance summary of the models => Analyze the performance results of the models *GOLD PRICE PREDICTION*:

**Overview**

Results from the data table show that the models have quite high performance in predicting Gold prices. Models such as Linear Regression, Random Forest, GRU, KNN and Adaboost all have high R2 values ​​on both the training and test sets, with Linear Regression giving the highest performance.

1. **Linear regression**
The best performance on the Test Set with R2 is 0.9991, indicating that the model is highly accurate in predicting gold prices, with an R2 index close to 1.
RMSE and MAPE% are also relatively low, indicating that the model has high accuracy and low prediction error.

2. **Random Forest**
The model has high accuracy. However, performance on the Test Set has an R2 of 0.9911, slightly lower than Linear Regression, and higher RMSE and MAPE% than Linear Regression, suggesting that the error of predictions can be large than the Linear Regression model.

3. **GRU** (a type of recurrent neural network) gives relatively good results, but not as good as Linear Regression or Random Forest, with an R2 value lower than 0.9706 and RMSE and MAPE errors % higher on test set.

4. **KNN** and **Adaboost** have lower performance than other models, as shown by lower R2 values ​​and higher RMSE and MAPE% errors on the test set and test set.

**Conclude**

Among the tested models, Linear Regression is the best model to predict gold prices based on this data, with accurate and stable performance on both the training and test sets. Random Forest shows high performance on the training set, but the results on the test set are slightly worse than the Linear Regression model. Other models such as GRU, KNN and Adaboost, although they have certain predictive ability, do not show optimal performance compared to the first two models.