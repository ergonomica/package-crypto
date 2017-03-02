"""
[crypto.py]

Cryptography.
"""

import hashlib

def _md5(string):
    m = hashlib.md5()
    m.update(string)
    return m.digest()

def _sha256(string):
    s = hashlib.sha256()
    s.update(string)
    return s.digest()

def md5(env, args, kwargs):
    """{string:}"""
    
    # hashing input
    if "string" in kwargs and kwargs["string"] in ["t", "true"]:
        return map(_md5, args)    
    else: # hashing files
        return [_md5(open(x).read()) for x in args]

def sha256(env, args, kwargs):
    """"""
    
    # hashing input
    if "string" in kwargs and kwargs["string"] in ["t", "true"]:
        return map(_sha256, args)    
    else: # hashing files
        return [_sha256(open(x).read()) for x in args]


verbs = {'md5':md5,
         'sha256':sha256,
        }
