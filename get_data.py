"""
DATA 515
HW 4
Zicong Liang
"""

import os
import urllib3
urllib3.disable_warnings()


def get_data(url):
    """
    A function get_data.
    Downloads the data if it is not present locally;
    if the data are already present, then it takes no action.

    Inputs: url - a webpage to download the data
    Outputs: test - a statement to the action
    """
    website = urllib3.PoolManager()
    # get the file name
    filename = os.path.basename(url)
    try:
        # the data are already present, then it takes no action
        if os.path.exists(filename):
            print("You already have the file in directory.")
            print("Don't need to download it again!")
            test = "File exists"
        else:
            # download the file to the local directory
            file = website.request("GET", url)
            with open(filename, 'wb') as f:
                f.write(file.data)
                f.close()
            print("You have successfully download the file {}".format(filename))
            test = "File was successfully downloaded"
    except:
        print("Error, The url doesn't exist!")
        test = "URL does not exist"

    return test