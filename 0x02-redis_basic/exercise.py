#!/usr/bin/env python
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
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

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        '''
            takes a key string argument and an optional Callable argument fn.
            This callable will convert the data back to the desired format
        '''
        value = self._redis.get(key)
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str):
        '''
            Get the string value
        '''
        value = self._redis.get(key)
        return value.decode('utf-8')

    def get_int(self, key: str):
        '''
            Get and parameterize the integer values
        '''
        value = self._redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except Exception:
            value = 0
        return value
