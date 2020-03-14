import os
import threading
from datetime import datetime, timedelta
import time
import socket
from select import select

from sqlalchemy import (MetaData, Table, Column, Integer,
                        Date, select, literal, and_, exists)

import api

duration = 1800  # 30 min to Seconds
tmp_duration = 5  # 30 min to Seconds


def worker(channel, debug=False):
    # %Y%m%d_%H:%M:%S
    now = datetime.now()
    end = datetime.now() + timedelta(seconds=duration)
    start = now.strftime("%Y%m%d_%H%M%S")

    if channel.type == 'radio':
        print('Start Record Radio Streaming : %s' % channel.name)
        filename = str(channel.keyname) + '_' + socket.gethostname() + '_' + str(start) + '.aac'
        cmd = 'ffmpeg -i "' + str(channel.url) + '" -acodec aac -ab 48000 -ar 22050 -ac 1 -t {1} ' \
                                                 'recordings/{0} '.format(str(filename), str(tmp_duration))
        if not debug:
            cmd += '> /dev/null 2>&1'  # this command hide terminal messages from python console
        os.system(cmd)

        Recording = api.Recording(channel_id=channel.id, start_time=now, end_time=end, path='/recording/' + filename)
        api.Recording.query
        api.db.session.add(Recording)
        api.db.session.commit()
    elif channel.type == 'TV':
        print('Start Record TV Streaming : %s' % channel.name)
        filename = str(channel.keyname) + '_' + socket.gethostname() + '_' + str(start) + '.mp4'
        cmd = 'ffmpeg -i "' + str(channel.url) + '" -r 10 -vcodec libx264 -movflags frag_keyframe -acodec aac -ab ' \
                                                 '48000 -ar 22050 -ac 1 -s 160x120 -t {1} ' \
                                                 'recordings/{0} '.format(str(filename), str(tmp_duration))
        if not debug:
            cmd += '> /dev/null 2>&1'  # this command hide terminal messages from python console
        os.system(cmd)

    else:
        print('Invalid Channel Type')
    return


threads = []
all_channels = api.Channel.query.all()
for x in all_channels:
    t = threading.Thread(target=worker, args=(x, False,))
    threads.append(t)
    t.start()
