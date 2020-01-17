# author: Fanli Zhou
# date: 2020-01-16

"""This script downloads a data set and stores the data set as a csv file.

Usage: download_save_data.py <url> <path> 

Options:
<url>      URL to download the data set
<path>     Local file path to save the data set as a csv file
"""
import pandas as pd
from docopt import docopt
opt = docopt(__doc__)

def main(url, path):
  data = pd.read_csv(url)
  data.to_csv(path)


if __name__ == '__main__':
  main(opt['<url>'], opt['<path>'])
