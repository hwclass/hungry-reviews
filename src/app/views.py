from flask import render_template, url_for, redirect, g, request, jsonify ##
from app import app
from .forms import ReviewForm
import json
from itertools import groupby
from collections import defaultdict

# rethink imports
import rethinkdb as r
from rethinkdb.errors import RqlRuntimeError, RqlDriverError

# rethink config
RDB_HOST =  'localhost'
RDB_PORT = 28015
DB_NAME = 'wolt'
TABLE_NAME = 'reviews'

# db setup; only run once
def dbSetup():
    connection = r.connect(host=RDB_HOST, port=RDB_PORT)
    try:
        r.db_create(DB_NAME).run(connection)
        r.db(DB_NAME).table_create('reviews').run(connection)
        print('Database setup completed')
    except RqlRuntimeError:
        print ('Database already exists.')
    finally:
        connection.close()
dbSetup()

# open connection before each request
@app.before_request
def before_request():
    try:
        g.rdb_conn = r.connect(host=RDB_HOST, port=RDB_PORT, db=DB_NAME)
    except RqlDriverError:
        abort(503, "Database connection could be established.")

# close the connection after each request
@app.teardown_request
def teardown_request(exception):
    try:
        g.rdb_conn.close()
    except AttributeError:
        pass

@app.route('/', methods = ['GET', 'POST'])
def index():
        form = ReviewForm()
        if form.validate_on_submit(): 
            r.table('reviews').insert({"user_id" : form.user_id.data, "point" : form.point.data, "optional_comment":form.optional_comment.data}).run(g.rdb_conn)
            return redirect(url_for('index'))
        reviews = list(r.table(TABLE_NAME).run(g.rdb_conn))
        return render_template('index.html', form = form, reviews = reviews)

@app.route('/api/v1.0/reviews', methods=['GET'])
def get_reviews():
    # grouped_list_of_reviews = list(r.table(TABLE_NAME).get_all('point', 'optional_comment').group('user_id').run(g.rdb_conn))
    # grouped_list_of_reviews = list(r.table(TABLE_NAME).map(r.row["user_id"]).distinct().run(g.rdb_conn))
    grouped_list_of_reviews = list(r.table(TABLE_NAME).run(g.rdb_conn))
    """
    for key, group in groupby(grouped_list_of_reviews, lambda x: x[0]):
        grouped_list_of_user_ids[key] = []
        print(111)
        for review_item in group:
            print(222)
            grouped_list_of_user_ids[key].append(review_item)
            print(grouped_list_of_user_ids[key])  
        grouped_list_of_reviews.append(grouped_list_of_user_ids[key])
    """
    """
    for key, group in groupby(grouped_list_of_reviews, lambda x: x[0]):
        for review in group:
            print("A %s is a %s" % (review[1], key))
        print(" ")
    """
    return jsonify({'reviews': grouped_list_of_reviews})














