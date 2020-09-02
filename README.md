# Car Price Prediction

* Created a project to estimate the price of car to help buyers negotiate the price.
* Optimised Random forest regressor using GridSearchCV to get the best parameters.


## Code and Resource Used

* python version: 3.8
* Packages: pandas, numpy, sklearn, matplotlib, seaborn, pickle

## Model Building

* Used "Random Forest Regressor" model for training. 
* Created new colunms for "number of years car was used".
* Converted categorical variables into dummy variables.
* Split the data into train and test set of 8 : 2 ratio.
* Tried three different models and evaluated their accuracy by "Mean Squared Error".


## Productionization

* For productionization I used django API endpoint that was hosted locally.
* The API endpoint takes in the request with all the features about the car like "Year", "KMS driven", "Fuel type" etc.
* Depending on the input car price is returned in the response.
