# -*- coding: utf-8 -*-

import json,requests

def request_url_json_to_dict(url):
    r=requests.get(url)
    r.encoding='gb2312'
    dict_json=json.loads(r.text)
    return dict_json

def get_kit_url_by_requests():
    url='https://developer.apple.com/tutorials/data/documentation/technologies.json'
    dict_json=request_url_json_to_dict(url)
    dict_kit=dict_json["references"]
    dict_kit_url={}
    for i in dict_kit:
        try:
            kit_name=dict_kit[i]["title"]
            kit_url="https://developer.apple.com"+dict_kit[i]["url"]
            dict_kit_url[kit_name]=kit_url
        except:
            print('error : %s'%i)
    print(len(dict_kit_url))
    print(dict_kit_url)
    return dict_kit_url

def get_kit_permission_by_request():
    dict_kit_url=get_kit_url_by_requests()
    dict_kit_permissions={}
    for i in dict_kit_url:
        i=i.replace(" ","")
        print("sss"+i)
        url="https://developer.apple.com/tutorials/data/documentation/"+i+".json"
        print(url)
        try:
            list_permissions=[]
            dict_json=request_url_json_to_dict(url)
            dict_references = dict_json["references"]
            for i in dict_references.keys():
                if "information_property_list" in i:
                    list_permissions.append(dict_json["references"][i]["title"])
                    dict_kit_permissions[i]=list_permissions
        except:
            print('error : %s'%i)
    print(dict_kit_permissions)

get_kit_permission_by_request()

print("end")

