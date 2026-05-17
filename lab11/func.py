"""
Created on 5/1/2021

@author: razvan.vilceanu
"""
import time
import urllib.request
import gzip
import os

def mail_freq(file):
    try:
        with open(file) as fhand:
            from_lines = list(filter(lambda x: x.startswith("From:"), fhand))
            time.sleep(1)

            adresses = list(map(lambda x: x.split()[1], from_lines))
            time.sleep(1)

            from itertools import groupby

            sorted_adresses = sorted(adresses)
            time.sleep(1)

            agg_adresses = list(map(lambda x: (x[0], len(list(x[1]))), groupby(sorted_adresses)))
            time.sleep(1)

            final_adresses = sorted(agg_adresses, key=lambda x: x[1], reverse=True)
            time.sleep(1)

            return final_adresses
    except Exception as e:
        print("A aparut eroarea: ", e)



def download_files(url):
    time.sleep(0.5)
    head, tail = os.path.split(url)
    urllib.request.urlretrieve(url, tail)


    return None
