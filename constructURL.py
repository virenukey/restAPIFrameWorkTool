import re

def constURL(baseurl, path):
    if re.match(r'http:.*\/$', baseurl):
        r = baseurl+path
    elif re.match(r'^\/', path):
        r = baseurl+path
    else:
        r = baseurl+'/'+path
    return r