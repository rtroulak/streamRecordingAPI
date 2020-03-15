from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import threading

from recorder import recorder

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


# GET method functions for Select
# Get All Channels
@app.route('/channel', methods=['GET'])
def get_channels():
    all_channels = Channel.query.all()
    result = channels_schema.dump(all_channels)
    return jsonify(result)


# Get Single Channel
@app.route('/channel/<id>', methods=['GET'])
def get_channel(id):
    channel = Channel.query.get(id)
    return channel_schema.jsonify(channel)


# Get All Recordings
@app.route('/recording', methods=['GET'])
def get_recordings():
    all_recordings = Recording.query.all()
    result = recordings_schema.dump(all_recordings)
    return jsonify(result)


# Get Single Channel
@app.route('/recording/<id>', methods=['GET'])
def get_recording(id):
    recording = Recording.query.get(id)
    return recording_schema.jsonify(recording)


# Get Single Channel
@app.route('/channel/<channel_id>/recording', methods=['GET'])
def get_recording_channel(channel_id):
    all_recordings = Recording.query.filter_by(channel_id=channel_id)
    # all_recordings = Recording.query.all()
    result = recordings_schema.dump(all_recordings)
    return recordings_schema.jsonify(result)


# POST method functions for Create
# Create a new Channel
@app.route('/channel', methods=['POST'])
def add_channel():
    # id = request.json['id']
    name = request.json['name']
    keyname = request.json['keyname']
    type = request.json['type']
    url = request.json['url']

    new_channel = Channel(name, keyname, type, url)
    thread_channel = new_channel
    db.session.add(new_channel)
    db.session.commit()

    if new_channel.id:
        t = threading.Thread(target=recorder, args=(thread_channel, False,))
        threads.append(t)
        pid = threading.current_thread().ident
        t.start()

    return channel_schema.jsonify(new_channel)


# Create a new Recording
@app.route('/recording', methods=['POST'])
def add_recording():
    # id = request.json['id']
    channel_id = request.json['channel_id']
    start_time = request.json['start_time']
    end_time = request.json['end_time']
    path = request.json['path']

    new_recording = Recording(channel_id, start_time, end_time, path)

    db.session.add(new_recording)
    db.session.commit()

    return recording_schema.jsonify(new_recording)


# PUT method functions for update
# Update a Channel
@app.route('/channel/<id>', methods=['PUT'])
def update_channel(id):
    channel = Channel.query.get(id)

    name = request.json['name']
    keyname = request.json['keyname']
    type = request.json['type']
    url = request.json['url']

    channel.name = name
    channel.keyname = keyname
    channel.type = type
    channel.url = url

    db.session.commit()

    if channel.id:
        t = threading.Thread(target=recorder, args=(channel, False,))
        threads.append(t)
        pid = threading.current_thread().ident
        t.start()

    return channel_schema.jsonify(channel)


# Update a Recording
@app.route('/recording/<id>', methods=['PUT'])
def update_recording(id):
    recording = Recording.query.get(id)

    channel_id = request.json['channel_id']
    start_time = request.json['start_time']
    end_time = request.json['end_time']
    path = request.json['path']

    recording.channel_id = channel_id
    recording.start_time = start_time
    recording.end_time = end_time
    recording.path = path

    db.session.commit()

    return recording_schema.jsonify(recording)


# DELETE method functions for delete
# Delete Channel
@app.route('/channel/<id>', methods=['DELETE'])
def delete_channel(id):
    channel = Channel.query.get(id)
    db.session.delete(channel)
    db.session.commit()

    return channel_schema.jsonify(channel)


# Delete Recording
@app.route('/recording/<id>', methods=['DELETE'])
def delete_recording(id):
    recording = Recording.query.get(id)
    db.session.delete(recording)
    db.session.commit()

    return recording_schema.jsonify(recording)


# Look up to the channel table in the DB and start recording any url found in there
threads = []
all_channels = Channel.query.all()
for x in all_channels:
    t = threading.Thread(target=recorder, args=(x, False,))
    threads.append(t)
    t.start()

if __name__ == '__main__':
    app.run()
