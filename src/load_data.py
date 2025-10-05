# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 21:35:51 2025

@author: Ifeanyi
"""

import pandas as pd

def load_data(file_path):
  
    # For Handling Error
    try:
        df = pd.read_csv(file_path)     # use to load csv file
        return df
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        return pd.DataFrame()