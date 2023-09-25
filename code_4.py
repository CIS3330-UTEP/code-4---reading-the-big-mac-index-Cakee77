import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

data = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    filtered_data = data[(data['date'].str.startswith(str(year))) & (data['iso_a3'] == country_code.upper())]
    mean_price = filtered_data['dollar_price'].mean()
    return round(mean_price, 2)

def get_big_mac_price_by_country(country_code):
    filtered_data = data[data['iso_a3'] == country_code.upper()]
    mean_price = filtered_data['dollar_price'].mean()
    return round(mean_price, 2)


def get_the_cheapest_big_mac_price_by_year(year):
    filtered_data = data[data['date'].str.startswith(str(year))]
    min_price_row = filtered_data.loc[filtered_data['dollar_price'].idxmin()]
    country_name = min_price_row['name']
    country_code = min_price_row['iso_a3']
    dollar_price = min_price_row['dollar_price']
    return f"{country_name}({country_code}): ${round(dollar_price, 2)}"


def get_the_most_expensive_big_mac_price_by_year(year):
    filtered_data = data[data['date'].str.startswith(str(year))]
    max_price_row = filtered_data.loc[filtered_data['dollar_price'].idxmax()]
    country_name = max_price_row['name']
    country_code = max_price_row['iso_a3']
    dollar_price = max_price_row['dollar_price']
    return f"{country_name}({country_code}): ${round(dollar_price, 2)}"

if __name__ == "__main__":
    year = int(input("Enter the year: "))
    country_code = input("Enter the country code (lowercase): ")

    print(f"Average Big Mac price in {year} for {country_code}: ${get_big_mac_price_by_year(year, country_code)}")
    print(f"Average Big Mac price in {country_code}: ${get_big_mac_price_by_country(country_code)}")
    print(f"Cheapest Big Mac in {year}: {get_the_cheapest_big_mac_price_by_year(year)}")
    print(f"Most expensive Big Mac in {year}: {get_the_most_expensive_big_mac_price_by_year(year)}")