import json
import objectpath

#import jsonfile1

#Read the file
elastic=open('jsonfile/elastic_data.json','r')
jsondata=elastic.read()

#parsing


object=json.loads(jsondata)
list=(str(object['hits']))
print(len(list))
#print(list)

#for i in range(len(list)):
def item_generator(jsondata, user):
    if isinstance(jsondata, dict):
        for k, v in jsondata.items():
            if k == user:
                yield v
                print(v)
            else:
                yield from item_generator(v, user)
    elif isinstance(jsondata, list):
        for item in jsondata:
            yield from item_generator(item, user)
            print(item)