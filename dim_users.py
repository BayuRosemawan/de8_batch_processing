import os
import json
import psycopg2

if __name__ == "__main__":
    path = os.getcwd()
    print(path)
    with open(path+'/'+'config.json') as file:
        conf = json.load(file)['postgresql']
try:
    conn = psycopg2.connect(host=conf['host'], 
                            database=conf['database'], 
                            user=conf['user'], 
                            password=conf['password']
                            )