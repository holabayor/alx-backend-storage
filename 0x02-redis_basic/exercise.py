#!/usr/bin/env python
import redis
from uuid import uuid4
from typing import Union
''' Writing strings to Redis '''


class Cache():
    ''' Cache Class '''
    def __init__(self):
        ''' init Method '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' generate a random key (e.g. using uuid),
            store the input data in Redis using the random key
            return the key
        '''
        key = str(uuid4())
        self._redis.set(key, data)
        return key
