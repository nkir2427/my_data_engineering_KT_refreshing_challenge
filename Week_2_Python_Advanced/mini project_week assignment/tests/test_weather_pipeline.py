
import pandas as pd

DATA_FILE = "data/processed/weather_clean.csv"

def load_data():
    return pd.read_csv(DATA_FILE)

def test_columns_exist():
    df = load_data()

    required_columns = [
        "time",
        "date",
        "temperature_c",
        "temperature_status",
        "humidity_pct",
        "precipitation",
        "is_raining",
        "wind_speed_kmh"
    ]

    for column in required_columns:
        assert column in df.columns

def test_temperature_no_nulls():
    df = load_data()
    assert df["temperature_c"].isnull().sum() == 0

def test_precipitation_non_negative():
    df = load_data()
    assert (df["precipitation"] >= 0).all()
