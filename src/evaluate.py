# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 21:35:51 2025

@author: Ifeanyi
"""

import pandas as pd

class WaterQualityEvaluator:
    def __init__(self, ph_range=(6.5, 8.5), turbidity_threshold=1.0):
        self.ph_range = ph_range
        self.turbidity_threshold = turbidity_threshold

    def is_safe(self, row: pd.Series) -> bool:
        """
        Determine if a row of water data is safe.
        Returns True if ph is within ph_range and turbidity is below threshold, False otherwise.
        """
        if pd.isna(row['ph']) or pd.isna(row['turbidity']):
            return False
        if not (self.ph_range[0] <= row['ph'] <= self.ph_range[1]):
            return False
        if row['turbidity'] >= self.turbidity_threshold:
            return False
        return True
    def evaluate_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Evaluate water safety for each row and add status column.
        """
        df = df.copy()
        def get_status(row):
            if pd.isna(row['pH']):
                return "❌ Unsafe (missing pH)"
            if pd.isna(row['turbidity']):
                return "❌ Unsafe (missing turbidity)"
            if row['pH'] < self.ph_range[0]:
                return "❌ Unsafe (pH too low)"
            if row['pH'] > self.ph_range[1]:
                return "❌ Unsafe (pH too high)"
            if row['turbidity'] >= self.turbidity_threshold:
                return "❌ Unsafe (turbidity too high)"
            return "✅ Safe"
        
        df['status'] = df.apply(get_status, axis=1)
        return df