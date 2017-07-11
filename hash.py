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

def main(argc):
    """crypto: various hashing functions.
    
    Usage:
        crypto (md5|sha256) FILE
        crypto (md5|sha256) --string STRING
    """
    
    if argc.args['FILE']:
        if argc.args['md5']:
            return [md5(open(argc.args['FILE']).read()]

        elif argc.args['sha256']:
            return [sha256(open(x).read()]

    elif argc.args['--string']:
        if argc.args['md5']:
            return md5(argc.args['STRING'])

        elif argc.args['sha256']:
            return sha256(argc.args['STRING'])
