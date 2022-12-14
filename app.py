#!/usr/bin/python3

import os
import json
import psycopg2

if __name__ == "__main__":
    path = os.getcwd()
    with open(path+'/'+'config.json') as file:
        conf = json.load(file)['postgresql']

    try:
        conn = psycopg2.connect(host=conf['host'], 
                                database=conf['database'], 
                                user=conf['user'], 
                                password=conf['password']
                                )
        print(f"[INFO] Success connect PostgreSQL .....")
    except:
        print(f"[INFO] Cant connect PostgreSQL .....")