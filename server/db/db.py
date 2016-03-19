import os
import rethinkdb as r
from rethinkdb.errors import RqlRuntimeError, RqlDriverError


RDB_HOST = os.environ.get('RDB_HOST') or 'localhost'
RDB_PORT = os.environ.get('RDB_PORT') or 28015

PROJECT_DB = 'test'
PROJECT_TABLE = 'authors'

db_connection = r.connect(RDB_HOST,RDB_PORT)