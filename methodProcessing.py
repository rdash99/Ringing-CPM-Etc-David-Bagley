# todo - reimplement in Java to test speed of requests

import os
import time
import sqlite3
import requests
import multiprocessing
import json
import shutil


def createTable(cur, db):
    cur.execute(
        "CREATE TABLE Methods (id integer PRIMARY KEY, library text, title text, name text, stage integer, placeNotation text, rows text)")
    db.commit()
    #print('Table created')


def dropTable(cur, db):
    cur.execute("DROP TABLE if exists Methods")
    db.commit()
    #print('Table dropped')


def chunk(lst, amt):
    lstChunk = []
    for i in range(0, len(lst), amt):
        lstChunk.append(lst[i: i + amt])
    return lstChunk


def getAllMethods():
    methods = []
    url = 'https://api.complib.org/method/search?perpage=0'
    data = requests.get(url).json()
    count = data['count']
    # return data
    print(count)
    print(len(data['methods']))

    chunks = chunk(data['methods'], 500)
    print(len(chunks))
    # print(chunks[0])
    # print(processChunk(chunks[0]))

    processes = []

    chunkLength = len(chunks)
    i = 0

    for item in chunks:
        p = multiprocessing.Process(target=processChunk, args=(item, i,))
        p.name = str(i)
        p.start()
        processes.append(p)
        i += 1

    for process in processes:
        process.join()
    """ pool = multiprocessing.Pool(len(chunks))
    pool.map(processChunk, chunks)
    pool.close() """

    # todo - speed up this process by using multiprocessing and split the data into chunks before processing then write each chunk to the database
    """ for method in data['methods']:
        id = method['id']
        library = method['library']
        title = method['title']
        name = method['name']
        stage = method['stage']
        placeNotation = method['placeNotation']
        rows = getMethodRows(id)
        entity = (id, library, title, name, stage, placeNotation, rows)

        methods.append(entity) """

    print("First stage complete")

    writeToDatabase(chunkLength)
    print("done")


def getMethodRows(id):
    url = 'https://api.complib.org/method/{}/rows'.format(id)
    data = requests.get(url).json()
    rows = data['rows']
    # print(len(rows))
    return rows


def processChunk(chunk, name):
    db = sqlite3.connect('./data/{}.db'.format(name))
    cur = db.cursor()

    dropTable(cur, db)
    createTable(cur, db)

    items = []
    for item in chunk:
        id = item['id']
        library = item['library']
        title = item['title']
        name = item['name']
        stage = item['stage']
        placeNotation = item['placeNotation']
        rows = getMethodRows(id)
        entity = (id, library, title, name, stage, placeNotation, str(rows))

        cur.execute(
            "INSERT INTO Methods(id, library, title, name, stage, placeNotation, rows) VALUES(?, ?, ?, ?, ?, ?, ?)", entity)
        db.commit()

        items.append(entity)
    db.close()
    # return items


def writeToDatabase(numItems):
    db = sqlite3.connect('Methods.db')
    cur = db.cursor()
    dropTable(cur, db)
    createTable(cur, db)
    for i in range(numItems):
        cur.execute("ATTACH DATABASE './data/{}.db' AS db{}".format(i, i))
        db.commit()
        cur.execute("INSERT INTO Methods SELECT * FROM db{}.Methods".format(i))
        db.commit()
        cur.execute("DETACH DATABASE db{}".format(i))
        db.commit()

    db.close()
    cleanup()


def main():
    # dropTable()
    # createTable()
    start_time = time.time()
    getAllMethods()
    print("--- %s seconds ---" % (time.time() - start_time))
    # print(processChunk(data['methods']))
    # print(getMethodRows(1))


""" start_time = time.time()
getAllMethods()
print("--- %s seconds ---" % (time.time() - start_time)) """


def createDirectory(path):
    try:
        os.makedirs(path)
    except:
        pass


def removeDirectory(path):
    try:
        shutil.rmtree(path)
    except:
        pass


def cleanup():
    removeDirectory('./data')
    createDirectory('./data')


if __name__ == '__main__':
    createDirectory('./data')
    main()
# getMethodRows(11795)
