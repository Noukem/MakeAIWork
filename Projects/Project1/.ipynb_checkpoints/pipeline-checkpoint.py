#!/usr/bin/env python

# Imports
import pandas as pd
import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG)

# Global variables
# Relatief pad naar data
dbPath = "Data"

# Extract
# Sheets -> Collection
logging.info("Extract from DB")

# Maak een verbinding met de SQLite DB

# Haal alle gegevens op uit de tabel rest_netlify_api en sla die op in een Pandas dataframe
# Zie notebook data_collection

logging.info("Transform the data")
# Wat ga je doen met rijen die lege waarden bevatten?
# Sheets -> Data Selection

# Maak nieuw dataframes aan o.b.v. geselecteerde kolommen -> kopieer uit je notebook EDA
# Sheets - > Feature Extraction
 
logging.info("Load the transformed datasets as tables in the DB")  
# Zie notebook SQL Practicum

# Sluit database


