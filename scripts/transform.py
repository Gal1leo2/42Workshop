import pandas as pd
import os

def transform():
    staged_file = "data/staged/synthetic_dataset_clean.csv"
    df = pd.read_csv(staged_file)

    # Create new columns
    df['Price_after_discount'] = df['Price'] * (1 - df['Discount']/100)

    # Aggregate by category
    summary = df.groupby('Category').agg(
        avg_price=('Price_after_discount', 'mean'),
        avg_rating=('Rating', 'mean'),
        total_stock=('Stock', lambda x: (x=='In Stock').sum()),
        num_products=('row_id', 'count')
    ).reset_index()

    os.makedirs("output", exist_ok=True)
    summary.to_csv("output/retail_summary.csv", index=False)

if __name__ == "__main__":
    transform()
