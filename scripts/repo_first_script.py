""""
Script to make updates in github
"""
import click
import pandas as pd

class FilteringClass:
    """
    Class for filtering
    """

    def __init__(self, df):
        self.df = df

    def filterprice(self, price):
        """
        filter by price
        """
        return self.df[self.df["Price Starting With ($)"] < price]

@click.command(short_help="Parser to import dataset")
@click.option("-f", "--filename", required=True, help="File to import")
def main(filename):
    """
    This is the main function
    """

    df = pd.read_csv(filename)
    filter_instance = FilteringClass(df)
    result = filter_instance.filterprice(12)
    #import pdb;pdb.set_trace()
    print(result.shape)

if __name__ == "__main__":
    main()
