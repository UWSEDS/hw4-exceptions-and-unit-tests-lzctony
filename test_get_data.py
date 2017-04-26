"""
DATA 515
HW 4
Zicong Liang
"""

from get_data import get_data
import unittest
import os

url = "https://data.seattle.gov/resource/4xy5-26gy.csv"
filename = os.path.basename(url)

class TestGetData(unittest.TestCase):

    # file is present locally
    def testFileLocally(self):

        if os.path.exists(filename):
            print("File exists")
        else:
            print("Create a file", filename)
            f = open(filename, "w")

        result = get_data(url)
        test = "File exists"
        self.assertEqual(result, test)

    # file is not present locally, and the URL points to a file that exists
    def testFileNotLocallyURLExists(self):

        # delete the file if exists
        if os.path.exists(filename):
            os.remove(filename)

        result = get_data(url)
        test = "File was successfully downloaded"
        self.assertEqual(result, test)

    # URL does not point to a file that exists. (2 pt)
    def testURLNotExists(self):

        # delete the file if exists
        if os.path.exists(filename):
            os.remove(filename)

        # this is a fake url that doesn't work
        fakeurl = "https://ata.seattle.gov/resource/4xy5-2.csv"
        result = get_data(fakeurl)
        test = "URL does not exist"
        self.assertEqual(result, test)


if __name__ == "__main__":
    unittest.main()
