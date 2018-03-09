#!/usr/bin/env python

import requests;
import json;
import argparse;

print("Your request:");

parser = argparse.ArgumentParser()
parser.add_argument("--pswd", help="that optional takes your github account", required=True);
parser.add_argument("--login", help="that optional takes your github login", required=True);
parser.add_argument("--repos",nargs="?", help="that optional argument has:\n \"rep_name\" and \"id_rep\"")
parser.add_argument("--pulls",nargs="?", help="that optional argument has:\n \"pull_title\" and \"pull_id\" and \"pull_updated\" and \"user\"")
args = parser.parse_args()

PASSWORD=args.pswd;
LOGIN=args.login;

repo_info = requests.get('https://api.github.com/user', auth=(LOGIN, PASSWORD))


#repo_info = requests.get('https://api.github.com/user', auth=(LOGIN, PASSWORD))
Pulls_info = requests.get('https://api.github.com/repos/alenaPy/devops_lab/pulls', auth=(LOGIN, PASSWORD))


json_dict = repo_info.json();
json_pulls = Pulls_info.json();



#print rep_name
args = parser.parse_args()
if args.repos == "rep_name":
    print("Rep_name = " + str(json_dict.get("login")));


#print rep_id
if args.repos == "rep_id":    
    print("ID = " + str(json_dict.get("id")));


#print rep_title
if args.pulls == "rep_title":    
    max_count = len(json_pulls);
    print(max_count);
    i = 0
    for i in range(max_count):
        print(str(json.dumps(json_pulls[i]["title"], sort_keys = True, indent = 4, ensure_ascii = False)));


#print pull_id
if args.pulls == "pull_id":    
    max_count = len(json_pulls);
    print("max_count" + str(max_count));
    i = 0
    for i in range(max_count):
        print(str(json.dumps(json_pulls[i]["id"], sort_keys = True, indent = 4, ensure_ascii = False)));


#print rep_updated
if args.pulls == "rep_updated":    
    max_count = len(json_pulls);
    print(max_count);
    i = 0
    for i in range(max_count):
        print(str(json.dumps(json_pulls[i]["updated_at"], sort_keys = True, indent = 4, ensure_ascii = False)));

