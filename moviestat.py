# coding=utf-8
from pymongo import MongoClient

def stat_movies():
    client = MongoClient()
    db = client['bechdel']
    coll = db['movies']
    n = 0

    years = coll.distinct('year')
    years.sort()
    print('Total years %d, min: %d, max: %d' % (len(years), years[0], years[-1]))
    print('---')

    # Печатает таблицу с фильмами
    print('year\ttotal\tr0\tr1\tr2\tr3')
    for y in years:
        total = coll.find({'year' : y}).count()
        r0 = coll.find({'year' : y, 'rating' : 0}).count()
        r1 = coll.find({'year' : y, 'rating' : 1}).count()
        r2 = coll.find({'year' : y, 'rating' : 2}).count()
        r3 = coll.find({'year' : y, 'rating' : 3}).count()
        prop = (100.0*float(r3)) / total
        print('%d\t%d\t%d\t%d\t%d\t%d\t%f%%' % (y, total, r0, r1, r2, r3, prop))

    countries = coll.distinct('production_countries.name')
    countries.sort()
    print('Total countries %d, min: %s, max: %s' % (len(countries), countries[0], countries[-1]))
    print('---')

    # Печатает таблицу с фильмами по странам
    print('country\ttotal\tr0\tr1\tr2\tr3')
    for y in countries:
        total = coll.find({'production_countries.name' : y}).count()
        r0 = coll.find({'production_countries.name' : y, 'rating' : 0}).count()
        r1 = coll.find({'production_countries.name' : y, 'rating' : 1}).count()
        r2 = coll.find({'production_countries.name' : y, 'rating' : 2}).count()
        r3 = coll.find({'production_countries.name' : y, 'rating' : 3}).count()
        prop = (100.0*float(r3)) / total
        print('%s\t%d\t%d\t%d\t%d\t%d\t%f%%' % (y, total, r0, r1, r2, r3, prop))


    # Печатает таблицу с фильмами по странам и годам
    print('year\tcountry\ttotal\tr0\tr1\tr2\tr3\tshare')
    for y in years:
	    for c in countries:
	        total = coll.find({'production_countries.name' : c, 'year' : y}).count()
	        r0 = coll.find({'production_countries.name' : c, 'year' : y, 'rating' : 0}).count()
	        r1 = coll.find({'production_countries.name' : c, 'year' : y, 'rating' : 1}).count()
	        r2 = coll.find({'production_countries.name' : c, 'year' : y, 'rating' : 2}).count()
	        r3 = coll.find({'production_countries.name' : c, 'year' : y, 'rating' : 3}).count()
	        prop = (100.0*float(r3)) / total if total > 0 else 0
	        print('%d\t%s\t%d\t%d\t%d\t%d\t%d\t%f%%' % (y, c, total, r0, r1, r2, r3, prop))


if __name__ == "__main__":
    stat_movies()