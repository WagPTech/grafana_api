#!/usr/bin/python
# -*- coding: utf-8 -*-

#https://github.com/m0nhawk/grafana_api
#https://geektechstuff.com/2021/01/06/using-an-api-call-to-make-multiple-grafana-users-python/

import csv
import json
import requests

def create_admin_url():
    # grafana URL - does not need HTTP:// or slashes following the address
    grafana_url = '30.0.0.10:3000'
    # using the user API path
    api_path = '/api/admin/users'

#grafana_api = GrafanaFace(auth='eyJrIjoib3ZzOGthN2hoeGJMTGxEWFl5OTN6VklPUGpJV283cG0iLCJuIjoidXNlcnMiLCJpZCI6MX0=', host='http://30.0.0.10:3000/api/dashboards/home')
#curl -H "Authorization: Bearer eyJrIjoib3ZzOGthN2hoeGJMTGxEWFl5OTN6VklPUGpJV283cG0iLCJuIjoidXNlcnMiLCJpZCI6MX0=" http://30.0.0.10:3000/api/dashboards/home

    # DO NOT STORE CREDENTIALS in the program
    print("Requires an Grafana account with admin powers")
    #admin_username = input("Username: grafana_api")
    #admin_password = input("Password: grafana_api")
    admin_username = "grafana_api"
    admin_password = "grafana_api"



    # final URL
    url = 'http://'+admin_username+':'+admin_password+'@'+grafana_url+api_path
    return(url)
	
def create_account():
    url = create_admin_url()
    #url = "http://api_key:eyJrIjoiUXFjMjd1UkJKOHZVT2JCMEdPcjFkTWFQUHVUVHZJaHIiLCJuIjoidXNlcnMiLCJpZCI6MX0=@localhost:3000/api/org"
    with open ('csv_name.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)#, delimiter = '\t')
        for row in reader:
            name = row['nome']
            email = row['email']
            login = row['login']
            password = row['password']
            parameters = {"name":name,"email":email,"login":login,"password":password}
            #parameters = grafana_api.admin.create_user({"name":name,"email":email,"login":login,"password":password})
            print(parameters)
            headers = {"content-type": "application/json"}
            # data is a Python dictionary and needs explicitely converting to JSON
            print(url,headers,parameters)
            response = requests.post(url,headers=headers,data=json.dumps(parameters))
            print(response)
            print("username: "+name+" status: ")
            print(response.text)
            print(" ")
create_account()
