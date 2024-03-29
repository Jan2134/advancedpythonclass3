"""
Script to make updates in GitHub
"""

import click
import pandas as pd

if __name__ == "__main__":
    from filtering import FilteringClass
else:
    from scripts.filtering import FilteringClass

def load_dataset(filename):
    """
    Function to load dataset
    """
    extension = filename.rsplit(".", 1)[-1]
    if extension == "csv":
        return pd.read_csv(filename)
    raise TypeError(f"The extension is {extension}, not csv. Try again.")

@click.command(short_help="Parser to import dataset")
@click.option("-id", "--input", required=True, help="File to import")
@click.option("-f", "--filtering", is_flag=True, help="Filter data")
@click.option("-y", "--year", help="Filter data for year")
@click.option("-m", "--month", help="Filter data for month")
@click.option("-p", "--price", help="Filter data for price smaller than x")
def main(input, filtering, year, month, price):
    """
    This is the main function
    """
    df = load_dataset(input)

    if filtering:
        filter_description = "I am filtering for"
        filter_instance = FilteringClass(df)

        if year:
            print(filter_description + f" year {year}")
            df = filter_instance.filter_by_publish_year(int(year))

        if month:
            print(filter_description + f" month {month}")
            df = filter_instance.filter_by_publish_month(month)

        if price:
            print(filter_description + f" price {price}")
            df = filter_instance.filter_by_price(int(price))

    print(df.head())

if __name__ == "__main__":
    main()
