import pandas as pd
import requests
from multiprocessing import Pool
import sqlite3
db = sqlite3.connect('Methods.db')
cur = db.cursor()

total = 0

def createTable():
    try:
        cur.execute("CREATE TABLE Methods (id integer PRIMARY KEY, library text, title text, name text, stage integer, rows blob)")
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


base_url = 'https://api.complib.org/'
def parseCSV(file, total):
    f = pd.read_csv(file)
    keep_col = ['id']
    new_f = f[keep_col]
    ids = []
    for index, rows in new_f.iterrows():
        id = rows.id
        ids.append(id)
        total +=1
        proccessData(id, total)
        #print(entities)
def proccessData(id, total):
    url = base_url + 'method/{}/rows'.format(id)
    #print(url)
    try:
        data = requests.get(url).json()
    except:
        data = requests.get(url).json()
    #print(data)
    id = int(data['id'])
    library = data['library']
    title = data['title']
    name = str(data['name'])
    stage = int(data['stage'])
    rows = str(data['rows'])
    entity = (id, library, title, name, stage, rows)
    #print(entity)
    storeData(entity, total)
    #return entity

def storeData(entity, total):
    try:
        cur.execute("INSERT INTO Methods(id, library, title, name, stage, rows) VALUES(?, ?, ?, ?, ?, ?)", entity)
        db.commit()
    except:
        pass
    total += 1
    #print('added')
    #print(total)

dropTable()
createTable()
parseCSV('tempData.csv', total)
print('finished')
db.close()