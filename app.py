import os

from flask import request, jsonify
import threading

from classes import Channel, channel_schema, recordings_schema, Recording, recording_schema, db, channels_schema, app
from recorder import recorder


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


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
    threads = []
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
    if channel:  # update channel
        name = request.json['name']
        keyname = request.json['keyname']
        type = request.json['type']
        url = request.json['url']

        channel.name = name
        channel.keyname = keyname
        channel.type = type
        channel.url = url

        db.session.commit()
        threads = []
        if channel.id:
            t = threading.Thread(target=recorder, args=(channel, False,))
            threads.append(t)
            pid = threading.current_thread().ident
            t.start()

        return channel_schema.jsonify(channel)
    else:  # return not found 404 response
        return not_found()


# Update a Recording
@app.route('/recording/<id>', methods=['PUT'])
def update_recording(id):
    recording = Recording.query.get(id)
    if recording:  # delete row from db
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
    else:  # return not found 404 response
        return not_found()


# Delete Channel,  i use thrash instead of delete because of sorting in unit tests
@app.route('/channel/<id>', methods=['DELETE'])
def trash_channel(id):
    channel = Channel.query.get(id)
    if channel:  # delete row from db
        db.session.delete(channel)
        db.session.commit()
        return channel_schema.jsonify(channel)
    else:  # return not found 404 response
        return not_found()


# Delete Recording, i use thrash instead of delete because of sorting in unit tests
@app.route('/recording/<id>', methods=['DELETE'])
def trash_recording(id):
    recording = Recording.query.get(id)
    if recording:  # delete row from db
        db.session.delete(recording)
        db.session.commit()

        return recording_schema.jsonify(recording)
    else:  # return not found 404 response
        return not_found()


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/shutdown', methods=['POST'])
def will_shutdown():
    shutdown_server()
    return 'Server shutting down...'



if __name__ == '__main__':
    app.run()
