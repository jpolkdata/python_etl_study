# https://www.startdataengineering.com/post/python-fp-v-oop/
# execute the script with this command
# py .\modules\01_oop\test_etl.py 

import polars as pl
from datetime import date

def get_monthly_sales(orders: pl.DataFrame) -> pl.DataFrame:
    return (
        orders
        .with_columns(pl.col("order_date").dt.truncate("1mo").alias("month"))
        .group_by(["month", "product_id", "region_id"])
        .agg([
            pl.col("sales_amount").sum().alias("total_sales"),
            pl.col("order_id").count().alias("order_count")
        ])
    )

def get_regional_sales(monthly_sales: pl.DataFrame) -> pl.DataFrame:
    return (
        monthly_sales
        .group_by(["month", "region_id"])
        .agg([
            pl.col("total_sales").sum().alias("regional_sales"),
            pl.col("order_count").sum().alias("regional_orders")
        ])
    )

if __name__ == "__main__":
    # Sample data as a dictionary
    data = {
        "order_id": [1, 2, 3, 4, 5, 6],
        "order_date": [
            date(2024, 1, 5),
            date(2024, 1, 15),
            date(2024, 2, 10),
            date(2024, 2, 28),
            date(2024, 3, 1),
            date(2024, 3, 20),
        ],
        "product_id": [101, 101, 102, 103, 101, 102],
        "region_id": [1, 1, 2, 2, 1, 2],
        "sales_amount": [100.0, 150.0, 200.0, 250.0, 175.0, 300.0],
    }

    # Convert the dictionary into a Polars DataFrame
    orders = pl.DataFrame(data)

    # Data transformations are applied as a series of individual transformations
    monthly_sales = get_monthly_sales(orders)
    regional_sales = get_regional_sales(monthly_sales)
    print(monthly_sales)
    print(regional_sales)
    # And so on
