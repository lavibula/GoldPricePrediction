
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


Analyzing the performance of *BITCOIN PRICE PREDICTION* models

**Overall**

Results from the data table show that the models with high performance in predicting Gold prices are: Linear Regression, Random Forest, GRU, KNN and Adaboost all have high R2 values ​​on both the training set and test set, RMSE and MAPE% indicate accurate prediction with minimal error. This proves the reason: Gold is often sought by investors as a safe haven asset. Among them, linear regression gives the best performance.

**Analysis of different types of models used**
*Experiments show:*

1. The machine learning models we use are Linear Regression and KNN. Linear regression achieved the best performance on the test set with an R2 of 0.9991, relatively low RMSE and MAPE% indicating that the model has high accuracy and low prediction error. It can be hypothesized that this is due to good data normalization and the presence of a linear relationship between different economic and market factors. Linear regression gives much better performance than KNN, because KNN usually does not perform well in high-dimensional datasets, in addition the KNN model is also sensitive to the number of neighbors which is difficult to determine in this case .

2. Ensemble learning models including bagging methods like Random Forest and boosting methods like AdaBoost, show good performance especially Random Forest method. This is because Random Forests typically use a large number of decision trees, each with relatively high depth, allowing them to learn complex rules and make effective use of relationships between object features physical. On the other hand, AdaBoost also work well but require adjusting the number and depth of trees for optimal results. The Random Forest model has high accuracy, slightly lower than Linear Regression.


3. Deep Learning models, here we use GRU (a type of recurrent neural network) which gives relatively good results, but not as good as Linear Regression or Random Forest, with an R2 value lower than 0.9706 and higher RMSE and MAPE% errors on the test set. GRU still has room for improvement, due to time and resource constraints, we have not been able to tune parameters or create more complex neural networks to maximize model performance.


**Conclusion**

Among the tested models, Linear Regression is the best model to predict gold prices based on this data, with accurate and stable performance on both the training and test sets. Random Forest shows high performance on the training set, but the results on the test set are slightly worse than the Linear Regression model. Other models such as GRU, KNN and Adaboost, although they have certain predictive ability, do not show optimal performance compared to the first two models. Deep learning models like GRU demonstrate good performance and have the potential for further improvements, but they require longer training times and resource-consuming parameter tuning.