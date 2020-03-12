from sqlalchemy import create_engine
from flask import Flask, request, jsonify
from threading import Thread
import time
import app
import threading
import atexit
import os
import subprocess

duration = 1800  # 30 min to Seconds
tmp_duration = 5  # 30 min to Seconds

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///recs_bmat.db'
db_uri = app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///recs_bmat.db'
engine = create_engine(db_uri)


def worker(num):
    """thread worker function"""
    print('START Worker: %s' % num)
    time.sleep(tmp_duration)
    print('END Worker: %s' % num)
    return


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()


def exec_func(x):
    bashCommand = "cwm --rdf test.rdf --ntriples > test.nt"


def main(db):
    print("My Rec File is here")
