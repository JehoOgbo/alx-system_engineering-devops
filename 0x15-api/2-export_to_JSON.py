#!/usr/bin/python3
""" Python script that uses REST API  to return info about an
    employee's TODO list progress
"""
from requests import get
from sys import argv
import json

if __name__ == '__main__':
    emp_id = int(argv[1])

    response = get('https://jsonplaceholder.typicode.com/todos/')
    real = response.json()

    lister = []
    for item in real:
        if item['userId'] == emp_id:
            lister.append(item)

    resp_1 = get('https://jsonplaceholder.typicode.com/users')
    real_2 = resp_1.json()
    for item in real_2:
        if item['id'] == emp_id:
            emp_name = item['username']
            break

    new_list = []
    for item in lister:
        my_dict = {"task": item['title'], "completed": item["completed"],
                   "username": emp_name}
        new_list.append(my_dict)
    dicter = {emp_id: new_list}

    with open("{}.json".format(emp_id), mode="w", encoding="utf-8") as file:
        json.dump(dicter, file)
