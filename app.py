import os
import threading
from datetime import datetime
import time
import socket

import api

duration = 1800  # 30 min to Seconds
tmp_duration = 5  # 30 min to Seconds


def worker(channel):
    # %Y%m%d_%H:%M:%S
    now = datetime.now()
    s2 = now.strftime("%Y%m%d_%H%M%S")

    if channel.type == 'radio':
        print('Start Record Radio Streaming : %s' % channel.name)
        filename = str(channel.keyname) + '_' + socket.gethostname() + '_' + str(s2) + '.aac'
        cmd = 'ffmpeg -i "' + str(channel.url) + '" -acodec aac -ab 48000 -ar 22050 -ac 1 -t {1} ' \
                                                 'recordings/{0} '.format(str(filename), str(tmp_duration))
        cmd += '> /dev/null 2>&1'
        os.system(cmd)
    elif channel.type == 'TV':
        print('Start Record TV Streaming : %s' % channel.name)
        filename = str(channel.keyname) + '_' + socket.gethostname() + '_' + str(s2) + '.mp4'
        cmd = 'ffmpeg -i "' + str(channel.url) + '" -r 10 -vcodec libx264 -movflags frag_keyframe -acodec libfaac -ab ' \
                                                 '48000 -ar 22050 -ac 1 -s 160x120 -t {1} ' \
                                                 'recordings/{0} '.format(str(filename), str(tmp_duration))
        # cmd += '> /dev/null 2>&1'
        os.system(cmd)

    else:
        print('Invalid Channel Type')
    return


threads = []
all_channels = api.Channel.query.all()
for x in all_channels:
    t = threading.Thread(target=worker, args=(x,))
    threads.append(t)
    t.start()
