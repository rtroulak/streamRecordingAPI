import threading

import api
from recorder import recorder


threads = []
all_channels = api.Channel.query.all()
for x in all_channels:
    t = threading.Thread(target=recorder, args=(x, False,))
    threads.append(t)
    t.start()
