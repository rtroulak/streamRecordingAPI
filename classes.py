from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import Flask
app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///recs_bmat.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init my db
db = SQLAlchemy(app)
# Init Marshmallow as ma
ma = Marshmallow(app)


# Channels Class/Model
class Channel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    keyname = db.Column(db.Text)
    type = db.Column(db.Text)
    url = db.Column(db.Text)

    def __init__(self, name, keyname, type, url):
        # self.id = id
        self.name = name
        self.keyname = keyname
        self.type = type
        self.url = url


# Recording Class/Model
class Recording(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    channel_id = db.Column(db.Integer)
    start_time = db.Column(db.Text)  # i set this as datetime but we have an issue on sqlite with datetimes
    end_time = db.Column(db.Text)  # i set this as datetime but we have an issue on sqlite with datetimes
    path = db.Column(db.Text)

    def __init__(self, channel_id, start_time, end_time, path):
        self.channel_id = channel_id
        self.start_time = start_time
        self.end_time = end_time
        self.path = path


# Channels Schema
class ChannelSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'keyname', 'type', 'url')


# Recording Schema
class RecordingSchema(ma.Schema):
    class Meta:
        fields = ('id', 'channel_id', 'start_time', 'end_time', 'path')


# Init schema
channel_schema = ChannelSchema()
channels_schema = ChannelSchema(many=True)
recording_schema = RecordingSchema()
recordings_schema = RecordingSchema(many=True)

db.create_all()
