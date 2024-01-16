class FilteringClass:
    """
    Class for filtering
    """

    def __init__(self, df):
        self.df = df

    def filter_by_price(self, price):
        """
        filter by price
        """
        return self.df[self.df["Price Starting With ($)"] < price]
    
    def filter_by_publish_year(self, year):
        """
        filter books by given year
        """
        return self.df[self.df["Publish Date (Year)"]== year]
    
    def filter_by_publish_month(self, month):
        """
        filter books by given year
        """
        return self.df[self.df["Publish Date (Month)"]== month]