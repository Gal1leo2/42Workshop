import pandas as pd
import os
import numpy as np

def stage():
    staged_file = "data/staged/synthetic_dataset.csv"
    df = pd.read_csv(staged_file)

    # Fill missing numerical columns with median
    df['Price'] = df['Price'].fillna(df['Price'].median())
    df['Rating'] = df['Rating'].fillna(df['Rating'].median())
    df['Discount'] = df['Discount'].fillna(0)

    # Fill missing categorical columns with mode
    df['Category'] = df['Category'].fillna(df['Category'].mode()[0])
    df['Stock'] = df['Stock'].fillna('Unknown')

    # Add row id
    df['row_id'] = np.arange(1, len(df)+1)

    df.to_csv("data/staged/synthetic_dataset_clean.csv", index=False)

if __name__ == "__main__":
    stage()
