#!/usr/bin/env python

# Imports
import pandas as pd
import sqlite3
import csv
import logging

logging.basicConfig(level=logging.DEBUG)

# Global variables
# Relatief pad naar data
dbPath = "/data"

# Extract
# Sheets -> Collection

df = pd.read_csv('../../Projects/Project1/data/data.csv')

dbName = "../../Projects/Project1/data/data_new1.db"
tableName = "data_clean1"


logging.info("Extract from DB")

# Maak een verbinding met de SQLite DB
dbConnection = sqlite3.connect(dbName)

# Haal alle gegevens op uit de tabel rest_netlify_api en sla die op in een Pandas dataframe
# Zie notebook data_collection

dfFromDB = pd.read_sql_query(f"SELECT * FROM {tableName}", dbConnection)
pd.set_option('display.max_columns', 10)
# dfFromDB.drop(['id'], axis=1)

logging.info("Transform the data")

#verwijder non-numerieke- en null-waardes
for c in df.columns:
    df[c] = pd.to_numeric(df[c], errors='coerce')

df= df.dropna(axis=0)

# Sheets -> Data Selection

# outliers

def remove_outliers(df,columns,n_std):
    for col in columns:
        print('Working on column: {}'.format(col))
        
        mean = df[col].mean()
        sd = df[col].std()
        
        df = df[(df[col] <= mean+(n_std*sd))]
        
    return df

# Maak nieuw dataframes aan o.b.v. geselecteerde kolommen -> kopieer uit je notebook EDA
# Sheets - > Feature Extraction

# df_bmi

col_bmi = (df.mass/(df.length/100)**2)
df_bmi = df.drop(['length', 'mass'], axis=1)
df_bmi['bmi'] = col_bmi
 
logging.info("Load the transformed datasets as tables in the DB")  

# df_lifestyle

df_lifestyle = df[['exercise', 'smoking', 'alcohol', 'sugar', 'lifespan']]

# df_not_genetic

df_not_genetic = df.drop(['genetic'], axis = 1)
df_ng = df_not_genetic

# Zie notebook SQL Practicum
df.to_sql('new_table', con=dbConnection, index=False)

# Sluit database
con.close()
