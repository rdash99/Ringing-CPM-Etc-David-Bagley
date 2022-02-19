# todo - reimplement in Java to test speed of requests
import time
import requests
import json

import sqlite3
db = sqlite3.connect('Methods.db')
cur = db.cursor()


def createTable():
    try:
        cur.execute(
            "CREATE TABLE Methods (id integer PRIMARY KEY, library text, title text, name text, stage integer, placeNotation text, rows blob)")
        db.commit()
        print('Table created')
    except:
        pass


def dropTable():
    try:
        cur.execute("DROP TABLE if exists Methods")
        db.commit()
        print('Table dropped')
    except:
        pass


def getAllMethods():
    methods = []
    url = 'https://api.complib.org/method/search?perpage=0'
    data = requests.get(url).json()
    count = data['count']
    # return data
    print(count)
    print(len(data['methods']))

    # todo - speed up this process by using multiprocessing and split the data into chunks before processing then write each chunk to the database
    for method in data['methods']:
        id = method['id']
        library = method['library']
        title = method['title']
        name = method['name']
        stage = method['stage']
        placeNotation = method['placeNotation']
        rows = getMethodRows(id)
        entity = (id, library, title, name, stage, placeNotation, rows)

        methods.append(entity)
    print("done")


def getMethodRows(id):
    url = 'https://api.complib.org/method/{}/rows'.format(id)
    data = requests.get(url).json()
    rows = data['rows']
    # print(len(rows))
    return rows


start_time = time.time()
getAllMethods()
print("--- %s seconds ---" % (time.time() - start_time))
# getMethodRows(11795)
