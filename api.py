try:
    import requests
except ImportError as e:
    print ("Import of module in test failed", e)

class Api(object):
    def __init__(self, url):
        self.url = url
            
    def get(self, params=None, headers=None, cookies=None, 
            allow_redirects=False, auth=None, stream=None, timeout=None):
        r = None
        try:
            r = requests.get(self.url, params=params, headers=headers, cookies=cookies, 
                             allow_redirects=allow_redirects, auth=auth, 
                             stream=stream, timeout=timeout, verify=True)
        except Exception as e:
            print("Exception occurred in get request", e)
        return r
                    
    def post(self, data=None, json=None, headers=None, files=None, 
             timeout=None, auth=None):
        r = None
        try:
            r = requests.post(self.url, data=data, json=json, headers=headers, 
                              files=files, auth=auth, timeout=timeout, verify=True)
        except Exception as e:
            print("Exception occurred in post request", e)
        return r
    
    def put(self, data=None, json=None, headers=None, files=None, 
            timeout=None, auth=None):
        r = None
        try:
            r = requests.put(self.url, data=data, json=json, 
                             headers=headers, files=files, auth=auth, 
                             timeout=timeout, verify=True)
        except Exception as e:
            print("Exception occurred in put request", e)
        return r
    
    def delete(self):
        pass
        
        
        
    