import hug
import sys
import datetime
from hug_middleware_cors import CORSMiddleware
sys.path.append('../')
from Backend_Ouvidor.lib.database import database

db = database('../Backend_Ouvidor/database/banco.db').create()

api = hug.API(__name__)
api.http.add_middleware(CORSMiddleware(api))

@hug.get('/')
def show(maximum:hug.types.number=30, minimum:hug.types.number=0, output=hug.output_format.json):
    response = list()
    for row in db(db.log.date == datetime.datetime.now().strftime('%Y/%m/%d')).select(orderby=~db.log.id,limitby=(minimum, maximum)):
        response.append({'id':row.id,'date':row.date,'time':row.time,'phrase':row.phrase})
    return response

@hug.get('/search')
def find(q:hug.types.text,output=hug.output_format.json,day=datetime.datetime.now().strftime('%Y/%m/%d')):
    response = list()
    results = db((db.log.phrase.contains(q) & (db.log.date == day))).select()
    for row in results:
        response.append({'id':row.id,'date':row.date,'time':row.time,'phrase':row.phrase})
    return response
