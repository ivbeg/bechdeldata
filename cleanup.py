# coding=utf-8
from pymongo import MongoClient

def cleanup():
    client = MongoClient()
    db = client['bechdel']
    coll = db['movies']
    n = 0
    # Для каждого фильма преобразуем строковые рейтирг и год в числовые
    for r in coll.find():
        n += 1
        r['year'] = int(r['year'])
        r['rating'] = int(r['rating'])
        coll.save(r)
        if n % 100 == 0:
            print('Processing %d' % (n))
    pass


if __name__ == "__main__":
    cleanup()