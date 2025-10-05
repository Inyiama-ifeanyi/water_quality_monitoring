# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 21:35:51 2025

@author: Ifeanyi
"""

import pandas as pd
import numpy as np

def clean_sensor_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()  # Make copy to avoid modifying original
    
    # Replace empty strings with NaN
    df['pH'] = df['pH'].replace('', np.nan)     
    df['turbidity'] = df['turbidity'].replace('', np.nan)
    
    # Drop rows with NaN in ph or turbidity
    df = df.dropna(subset=['pH', 'turbidity'])
    
    #Add filter for ph and turbidity values
    df = df[df['pH'].between(0, 14)]
    df = df[df['turbidity'] >= 0]
    
    return df