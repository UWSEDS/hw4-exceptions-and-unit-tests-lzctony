"""
DATA 515
HW 4
Zicong Liang
"""

import os

def remove_data(url):
    """
    A function delete_data
    delete_data, removes the data if it is present locally.

    Inputs: url - a webpage to download the data
    Outputs: test - a statement to the action
    """
    # get the file name
    filename = os.path.basename(url)
    if os.path.exists(filename):
        os.remove(filename)
        print("You have successfully deleted the file {}".format(filename))
        test = "File was successfully deleted"
    else:
        print("Can't find the file to delete.")
        test = "Nothing to be deleted"
    return test