import os
import argparse
from pprint import pprint
import io
import multiprocessing as mp
import urllib
from urllib.request import Request, urlopen
from pyresparser import ResumeParser
def get_local_data():
    data = ResumeParser('OmkarResume.pdf').get_extracted_data()
    return data
print(get_local_data())