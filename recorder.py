import threading
from datetime import datetime, timedelta
import socket
import os

import classes

duration = 1800  # 30 min to Seconds
tmp_duration = 1800  # 30 min to Seconds


def insert_recording(channel, now, end, filename):
    Recording = classes.Recording(channel_id=channel.id, start_time=now, end_time=end, path='/recording/' + filename)
    classes.Recording.query
    classes.db.session.add(Recording)
    classes.db.session.commit()


# the main worker function of the threads
def recorder(channel, debug=False):
    new_channel = classes.Channel.query.get(channel.id)
    # check if channel is deleted or active yet
    if new_channel:
        # restart thread every 30 minutes
        threading.Timer(tmp_duration, recorder, [channel, False]).start()
        # Datetime for now and after 30 minutes
        now = datetime.now()
        end = datetime.now() + timedelta(seconds=duration)
        start = now.strftime("%Y%m%d_%H%M%S")  # create datetime file format

        if channel.type == 'radio':  # the case of radio streams
            print('Start Record Radio Streaming : %s' % channel.name)
            # create the filename with stream information
            filename = str(channel.keyname) + '_' + socket.gethostname() + '_' + str(start) + '.aac'
            # command for radio streams
            cmd = 'ffmpeg -i "' + str(channel.url) + '" -acodec aac -ab 48000 -ar 22050 -ac 1 -t {1} ' \
                                                     'recordings/{0} '.format(str(filename), str(duration))
            if not debug:
                cmd += '> /dev/null 2>&1'  # this command hide terminal messages from python console
            os.system(cmd)
            # insert function on recording table
            insert_recording(channel, now, end, filename)

        elif channel.type == 'TV':  # the case of TV streams
            print('Start Record TV Streaming : %s' % channel.name)
            # create the filename with stream information
            filename = str(channel.keyname) + '_' + socket.gethostname() + '_' + str(start) + '.mp4'
            # command for TV streams
            cmd = 'ffmpeg -i "' + str(channel.url) + '" -r 10 -vcodec libx264 -movflags frag_keyframe -acodec aac -ab ' \
                                                     '48000 -ar 22050 -ac 1 -s 160x120 -t {1} ' \
                                                     'recordings/{0} '.format(str(filename), str(duration))
            if not debug:
                cmd += '> /dev/null 2>&1'  # this command hide terminal messages from python console
            os.system(cmd)
            # insert function on recording table
            insert_recording(channel, now, end, filename)


        else:
            print('Invalid Channel Type')
        return
    else: # Id channel is Deleted stop recording this in the future
        print(channel.name, " is deleted")
        return
