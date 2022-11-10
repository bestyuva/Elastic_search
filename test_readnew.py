import json
from itertools import groupby
import pandas as pd

def test_keys():
    with open('jsonfile/elastic_data.json') as f:
        g42Groupingkeys = json.load(f)
    type(g42Groupingkeys)
    # Output: dict
    print(g42Groupingkeys.keys())
    # Output: dict_keys(['took', 'timed_out', '_shards', 'hits'])

def test_readData():
    with open('jsonfile/elastic_data.json') as access_json:
        read_content=json.load(access_json)
        access=read_content['hits']
    with open("jsonfile/hits_data.json", "w") as outfile:
            json.dump(access, outfile)

def test_keys1():
    with open('jsonfile/hits_data.json') as f:
        g42Groupingkeys1 = json.load(f)
    type(g42Groupingkeys1)
    print(g42Groupingkeys1.keys())
    # Output: dict_keys(['total', 'max_score', 'hits'])
def test_readChild():
    with open('jsonfile/hits_data.json') as child_json:
        read_content = json.load(child_json)
        child_access = read_content['hits']
#        print(child_access)
        print(type(child_access))
        # Output: <class 'list'>
#Finding total number of transactions and lINEAR GROUPING OF complete data
    for x in range(len(child_access)):
        dataframe = pd.DataFrame(child_access[x])
        print (dataframe) # table format creation for grouping
        #df_groupby_currency = dataframe.groupby('EUR')
        #df_groupby_customer_gender = dataframe.groupby('MALE')
        #df_groupby_day_of_week  = dataframe.groupby('Sunday')
    print(len(child_access))
    for x in range(len(child_access)):
        dataframe = pd.DataFrame(child_access[x])
        print (dataframe[dataframe['_source'] == 'Sunday']) # Group count for Sunday Purchase
# determined Columns: [_index, _id, _score, _source]
        print(dataframe[dataframe['_source'] == 'MALE'])  # Group count for Gender MALE
    print(len(child_access))