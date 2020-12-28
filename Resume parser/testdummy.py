import os
import argparse
from pprint import pprint
import io
import multiprocessing as mp
import urllib
from urllib.request import Request, urlopen
from pyresparser import ResumeParser
import json 

def get_remote_data():
    try:
        remote_file = 'https://www.omkarpathak.in/downloads/OmkarResume.pdf'
        print('Extracting data from: {}'.format(remote_file))
        req = Request(remote_file, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        _file = io.BytesIO(webpage)
        _file.name = remote_file.split('/')[-1]
        resume_parser = ResumeParser(_file)
        return [resume_parser.get_extracted_data()]
    except urllib.error.HTTPError:
        return 'File not found. Please provide correct URL for resume file.'


def get_local_data():
    skill=[]
    name=""
    dicte={"Name":"Number_of_skills"}
    for i in range(0,3):
        print("enter the name of Resume file")
        Resume_name=input()
        data = ResumeParser(Resume_name).get_extracted_data()
        
        for i in data.keys():
            if i=="skills":
                skill=data["skills"]
            if i=='name':
                    name=data[i]
    # count=list.count(temp)
        length=len(skill)
        # print(name,length)
        dicte.setdefault(name,length)
    print(dicte)
    with open('test.csv', 'w') as f:
        for key in dicte.keys():
            f.write("%s,%s\n" % (key, dicte[key]))


# for i in range()
get_local_data()
# get_local_data('ba-ex06.pdf')
 # with open("sample.json", "w") as outfile:  
    #     json.dump(data, outfile)
    # with open('test.csv', 'w') as f:
    #     for key in data.keys():
    #         f.write("%s,%s\n" % (key, data[key]))
    # print(data)