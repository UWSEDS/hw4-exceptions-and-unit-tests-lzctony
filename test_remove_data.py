"""
DATA 515
HW 4
Zicong Liang
"""

from remove_data import remove_data
import unittest
import os

url = "https://data.seattle.gov/resource/4xy5-26gy.csv"
filename = os.path.basename(url)


class TestGetData(unittest.TestCase):

    # remove file exists
    def testFileExists(self):

        if os.path.exists(filename):
            print("File exists")
        else:
            print("Create a file name", filename)
            f = open(filename, "w")

        print("Testing remove file exists.")
        result = remove_data(url)
        test = "File was successfully deleted"
        self.assertEqual(result, test)


    # remove file does not exist
    def testFileNotExists(self):

        # remove the file if exists before testing
        if os.path.exists(filename):
            os.remove(filename)

        print("Testing remove file does not exist.")
        result = remove_data(url)
        test = "Nothing to be deleted"
        self.assertEqual(result, test)


if __name__ == "__main__":
    unittest.main()
