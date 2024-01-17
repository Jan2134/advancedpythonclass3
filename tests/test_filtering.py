"""
Run test for the filtering
"""

import unittest
import pandas as pd
from scripts.filtering import FilteringClass

class TestFilteringClass(unittest.TestCase):
    """
    Class to test filtering
    """
    def setUp(self):
        """
        Set up sample data
        """
        data_example = {
            "Price Starting With ($)": [10, 20, 30, 40, 50],
            "Publish Date (Year)": [2019, 2020, 2021, 2022, 2023],
            "Publish Date (Month)": ["January", "February", "March", "April", "May"]
        }
        self.df = pd.DataFrame(data_example)
        self.filter_instance = FilteringClass(self.df)

    def test_filter_by_price(self):
        """
        Test filter by price function
        """
        result = self.filter_instance.filter_by_price(30)
        expected_result = self.df[self.df["Price Starting With ($)"] < 30]
        pd.testing.assert_frame_equal(result, expected_result)

    def test_filter_by_publish_year(self):
        """
        Test filter by year function
        """
        result = self.filter_instance.filter_by_publish_year(2020)
        expected_result = self.df[self.df["Publish Date (Year)"] == 2020]
        pd.testing.assert_frame_equal(result, expected_result)

    def test_filter_by_publish_month(self):
        """
        Test filter by month function
        """
        result = self.filter_instance.filter_by_publish_month("March")
        expected_result = self.df[self.df["Publish Date (Month)"] == "March"]
        pd.testing.assert_frame_equal(result, expected_result)

if __name__ == '__main__':
    unittest.main()