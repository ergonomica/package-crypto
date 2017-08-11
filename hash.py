"""
[hash.py]

Provides the `hash` function, with various tools for hashing.
"""

import hashlib

def md5(string):
    m = hashlib.md5()
    m.update(string)
    return m.digest()

def sha256(string):
    s = hashlib.sha256()
    s.update(string)
    return s.digest()

def hash(argc):
    """hash: various hashing functions.
    
    Usage:
        hash (md5|sha256) FILE
        hash (md5|sha256) --string STRING
    """
    
    if argc.args['FILE']:
        if argc.args['md5']:
            return md5(open(argc.args['FILE']).read())

        elif argc.args['sha256']:
            return sha256(open(argc.args['FILE']).read())

    elif argc.args['--string']:
        if argc.args['md5']:
            return md5(argc.args['STRING'])

        elif argc.args['sha256']:
            return sha256(argc.args['STRING'])

exports = {"hash": hash}
