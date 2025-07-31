#!/usr/bin/env python3
""" Python script that uses REST API  to return info about an
    employee's TODO list progress
"""
from requests import get
from sys import argv

emp_id = int(argv[1])


response = get('https://jsonplaceholder.typicode.com/todos/')
real = response.json()

lister = []
done_list = []
t_totl = 0
t_don = 0
for item in real:
    if item['userId'] == emp_id:
        lister.append(item)
        if item['completed'] == True:
            done_list.append(item)
            t_don += 1
        t_totl += 1

resp_1 = get('https://jsonplaceholder.typicode.com/users')
real_2 = resp_1.json()
for item in real_2:
    if item['id'] == emp_id:
        emp_name = item['name']
        break
print("Employee {} is done with tasks({}/{}):".format(emp_name,
                                                      t_don, t_totl))
for item in done_list:
    task_title = item['title']
    print("\t {}".format(task_title))
