from db_client import *
import hug

@hug.default_output_format()
def my_output_formatter(data):
    return "STRING:{0}".format(data)

@hug.get(output=hug.output_format.json)
def hello():
    return {'hello': 'world'}

@hug.get('/happy_birthday')
def happy_birthday(name, age:hug.types.number=1):
    """Says happy birthday to a user"""
    return "Happy {age} Birthday {name}!".format(**locals())

@hug.get(output=hug.output_format.json)
def authors():
	return {'data' : r.db('test').table('authors').run(db_connection)}

@hug.post()
def authors(body, output=hug.output_format.json):
	r.db(PROJECT_DB).table(PROJECT_TABLE).insert({"name":body["name"],"tv_show":body["tv_show"], "posts":[{"title": "Decommissioning speech", "db_connectionent": "The Cylon War is long over..."}]}).run(db_connection)
	return {'data' : r.db('test').table('authors').run(db_connection)}

@hug.get(output=hug.output_format.json)
def users():
	return {'data' : r.db('test').table('users').run(db_connection)}

@hug.get(output=hug.output_format.json)
def reviews():
	return {'data' : r.db('test').table('reviews').run(db_connection)}

@hug.not_found()
def authors():
    return {'Nothing': 'to see'}
