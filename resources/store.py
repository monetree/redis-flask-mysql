from flask_restful import Resource
from models.store import StoreModel
import random
from utils import Red


# here i just created some dummy data 
class Store(Resource):
    def get(self):
        loop = 640
        for i in range(loop):
            string ="abrtuoecdef12364747"
            name = ''.join(random.sample(string,len(string)))
            location = "japan"
            store = StoreModel(name, location)
            try:
                store.save_to_db()
            except:
                return {'message': "Internal server error"}, 500

        return store.json(), 201


class StoreList(Resource):
    def get(self):
        cache_key = "redis_key"
        # Here i added default cache key for redis data
        # cache key will be redis key and api rsult will be value
        # as redis supports data in key value foemat
        cacheData = Red.get(cache_key)
        if cacheData:
            return cacheData

        # I just added loop to make query multiple times same thing
        # In real life senario we will have to grab data from multiple collection and
        # have to do calculations on top of that
        # so i just added some loop by looking into real world senario

        loop = 30
        for i in range(loop):
            res = [i.json() for i in StoreModel.query.all()]
        us_counts = []
        uk_counts = []
        japan_counts = []
        india_counts = []

        data = res

        for i in data:
            if i["location"] == "usa":
                us_counts.append(i)

        for i in data:
            if i["location"] == "uk":
                uk_counts.append(i)

        for i in data:
            if i["location"] == "japan":
                japan_counts.append(i)

        for i in data:
            if i["location"] == "india":
                india_counts.append(i)
        api = {
            "usa_count": len(us_counts),
            "uk_counts": len(uk_counts),
            "japan_counts": len(japan_counts),
            "india_counts": len(india_counts),
            "data": [i.json() for i in StoreModel.query.all()][:10]
        }
        # finally after all calculations done
        # i am storing the data do redis db with out key
        # so that the next time when user will come it will
        # find the key in redis db hence it will return
        # instead of coming here
        Red.set(cache_key, api)
        return api