from pymongo import MongoClient
from dont_add import db_info


client = MongoClient()
mongo_db = client.recipes
collection = mongo_db.recipes

# the code to search by contains filter

# results = collection.find({'Title': {'$regex': ".*Coffee.*"}})
# for entry in results:
#     pprint(entry)


def search_by_title(search):

    results = collection.find({'Title': {'$regex': f".*{search}.*"}})

    return results


def search_by_author(search):
    results = collection.find({'Author': {'$regex': f".*{search}.*"}})

    return results


def format_out_str(recipe):

    string = f'''
    Title : {recipe['Title']}
    -------------------------
    Author : {recipe['Description']}
    -------------------------
    Source Url : {recipe['Url']}
    -------------------------
    Ingredients : {recipe['Ingredents']}
    -------------------------
    Steps : {recipe['Steps']}
    '''
    return string






