# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 21:35:51 2025

@author: Ifeanyi
"""

from load_data import load_data
from clean_data import clean_sensor_data
from evaluate import WaterQualityEvaluator

def main():
    df = load_data('../data/sensor_data.csv')
    if df.empty:
        print("No data loaded")
        return
    df = clean_sensor_data(df)
    evaluator = WaterQualityEvaluator()
    df = evaluator.evaluate_dataframe(df)
    for _, row in df.iterrows():
        print(f"Sensor {row['sensor_id']}: {row['status']}")
    
    # Bonus Task 3: Count safe vs. unsafe
    safe_count = len(df[df['status'].str.startswith('✅')])
    unsafe_count = len(df) - safe_count
    print(f"Safe lakes: {safe_count}, Unsafe lakes: {unsafe_count}")
    
    # Bonus Task 1: Save to results.csv
    df.to_csv('../data/results.csv', index=False)
    print("Results saved to ../data/results.csv")

if __name__ == "__main__":
    main()