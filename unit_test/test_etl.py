# to run the tests run the command below
# pytest .\modules\01_oop\test_etl.py 

import polars as pl
from datetime import date
import pytest
from etl import get_monthly_sales, get_regional_sales

@pytest.fixture
def sample_orders():
    return pl.DataFrame({
        "order_id": [1, 2, 3, 4, 5, 6],
        "order_date": pl.Series(
            [date(2024, 1, 5),
            date(2024, 1, 15),
            date(2024, 2, 10),
            date(2024, 2, 28),
            date(2024, 3, 1),
            date(2024, 3, 20)], 
            dtype=pl.Date
        ),
        "product_id": [101, 101, 102, 103, 101, 102],
        "region_id": [1, 1, 2, 2, 1, 2],
        "sales_amount": [100.0, 150.0, 200.0, 250.0, 175.0, 300.0]
    })

def test_get_monthly_sales(sample_orders):
    result = get_monthly_sales(sample_orders)
    assert result.shape[0] > 0
    assert "month" in result.columns
    assert "total_sales" in result.columns
    assert "order_count" in result.columns

def test_get_monthly_sales(sample_orders):
    monthly = get_monthly_sales(sample_orders)
    regional = get_regional_sales(monthly)
    assert regional.shape[0] > 0
    assert "regional_sales" in regional.columns
    assert "regional_orders" in regional.columns