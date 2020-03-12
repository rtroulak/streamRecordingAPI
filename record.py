from sqlalchemy import create_engine
from flask import Flask, request, jsonify
from threading import Thread
import time
import app
import threading
import atexit
import os
import subprocess


POOL_TIME = 10 #Seconds

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///recs_bmat.db'
db_uri = app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///recs_bmat.db'
engine = create_engine(db_uri)



def table_channels():
    result = engine.execute('SELECT * FROM '
                            '"Channel"')
    for _r in result:
        # Set the next thread to happen
        yourThread = threading.Timer(POOL_TIME, exec_func(_r[0]), ())
        yourThread.start()
        urls = []
        # print(_r[0])

    return result


def exec_func(x):
    bashCommand = "cwm --rdf test.rdf --ntriples > test.nt"

def main(db):
    print("My Rec File is here")
    table_channels()
