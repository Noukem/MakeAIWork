#!/usr/bin/env python

# Imports
import logging
import pandas as pd
import pickle
import sqlite3

# Hardening
from pathlib import Path
from sklearn.neighbors import KNeighborsRegressor

# TODO
# Voeg eigen model training toe

# Global configuration
<<<<<<< HEAD
logging.basicConfig(level=logging.DEBUG)
# Vervang bestandsnaam en maak mapje models aan
=======
logging.basicConfig(level=logging.INFO)
>>>>>>> 4c21a8afb1b1eca08f91560f22b7add390b23db3
exportFile = "../models/knn.pkl"

dbName = "../rest_server/medisch_centrum_randstad/db.sqlite3"
tableName = "data_with_bmi"

logging.info(f"Connect to {Path(dbName).name}")
dbConnection = sqlite3.connect(dbName)

logging.info("Load transformed data from database into dataframe")
dfWithBMI = pd.read_sql_query(
    f"SELECT length, lifespan FROM {tableName}", dbConnection)

logging.info("Close DB Connection")

logging.info("Preprocessing : remove rows with missing values")
f = dfWithBMI.dropna()
logging.debug(dfWithBMI.head())

logging.info("Feature Selection")

y = dfWithBMI['lifespan'].values
logging.debug(f"Y : {type(y)}")

X = dfWithBMI['length'].values
logging.debug(f"X : {type(X)}")

logging.info("Build Regression Model")

regressor = KNeighborsRegressor(n_neighbors=4, metric='euclidean')
regressor.fit(X.reshape(-1, 1), y)

logging.debug(f"Check with single value {regressor.predict([[185]])}")

pickle.dump(regressor, open(exportFile, 'wb'))
dbConnection.close()
