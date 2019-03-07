# coding=utf-8
from pymongo import MongoClient
import json

def imdb_merge():
    client = MongoClient()
    db = client['bechdel']
    movies = db['movies']
    imdb = db['imdb']
    n = 0
    nf = 0

    for c in movies.find():
        n += 1
        ttid = 'tt' + c['imdbid']
        r = imdb.find_one({'imdb_id' : ttid})
        if not r:
            nf += 1
        else:
            c['production_countries'] = json.loads(r['production_countries'].replace("'", '"'))
            movies.save(c)
        if n % 100 == 0:
            print('Total %d, not found %d' % (n, nf))


if __name__ == "__main__":
    imdb_merge()