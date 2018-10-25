from server import sio
from system.mysql import fnSql
import hashlib
from config import *


@sio.on('sendMessage')
def connect(sid, data):
    print('sendMessage')
    print(data)
