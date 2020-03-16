import threading

import classes
from recorder import recorder

threads = []
all_channels = classes.Channel.query.all()
# Look up to the channel table in the DB and start recording any url found in there
for x in all_channels:
    t = threading.Thread(target=recorder, args=(x, False,))
    threads.append(t)
    t.start()
