import geopandas as gpd
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from osgeo import gdal
from subprocess import Popen, PIPE



#Please Enter your shapefile path below
shapefile=gpd.read_file(r'D:\Test\data.shp')

geom=shapefile['geometry']





del shapefile['ph_class']

#Variable to Predict
Predict=shapefile['S1_PH']

#Dropping Catogorical variables from shapefile and retaining numerical variables
features1=shapefile.drop(['dc','geology','georeg','landscape','LU','wetland','cental_cli','S1_PH','geometry'],axis=1)

# Code for correlation coefficients and plots uncomment below and use your columns names instead 

# plt.subplot(2,2,1)
# plt.scatter(shapefile['asp_cos'],shapefile['asp_sin'])
# x=pd.Series(shapefile['asp_cos'])
# y=pd.Series(shapefile['asp-sin'])
# cor=y.corr(x)
# print(cor)



# plt.subplot(2,2,2)
# plt.scatter(shapefile['asp_cos'],shapefile['asp_sin'])

# plt.subplot(2,2,3)
# plt.scatter(shapefile['asp_cos'],shapefile['BIO01_mean'])

# plt.subplot(2,2,4)
# plt.scatter(shapefile['asp_cos'],shapefile['BIO02_mean'])


features=np.array(features1)


# Split the data into training and testing sets

train_features, test_features, train_labels, test_labels = train_test_split(features,
                                                                            Predict, test_size = 0.25,
                                                                            random_state = 50)
print('Training Features Shape:', train_features.shape)
print('Training Labels Shape:', train_labels.shape)
print('Testing Features Shape:', test_features.shape)
print('Testing Labels Shape:', test_labels.shape)


# Instantiate model with 1000 decision trees
rf = RandomForestRegressor(n_estimators = 1100, random_state = 80,max_depth=20)
# Train the model on training data
rf.fit(train_features, train_labels);

# Use the forest's predict method on the test data
predictions = rf.predict(test_features)

print("Mean Squre Error")
print(mean_squared_error(test_labels,predictions))
print("R^2 Error")
print(r2_score(test_labels,predictions))

#Code for hyperparamter tuning.Uncomment below and change the parameters you like
# params={'max_depth': [10,20,30],
#         'n_estimators':[900, 1000, 1100],
#         'random_state':[70,75,80]}

# gridforest = GridSearchCV(rf, params, cv = 3, n_jobs = -1, verbose = 1)
# gridforest.fit(train_features, train_labels)
# print(gridforest.best_params_)

