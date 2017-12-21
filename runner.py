try:
    from api import Api
    import constructURL
    from paramParser import Paramparser
except ImportError as e:
    print ("Import of module in test failed", e)
    
class Runner(object):
    resp = None
    @staticmethod
    def runTest(baseurl, path, params=None,
                body=None,
                json=None,
                data=None,
                files=None,
                auth=None, method=None):
        
        try:
            url = constructURL.constURL(baseurl=baseurl, 
                                        path=path)
            
            if params:
                params = Paramparser.parse(params)
            
            if json:
                json = Paramparser.parse(json)
                
            if data:
                data = Paramparser.parse(data)
            
            if body:
                body = Paramparser.parse(body)
                
            req = Api(url=url)
            
            if method == 'get':
                resp = req.get(params=params)
            elif method == 'post':
                resp = req.post(json=json, data=data)
            elif method == 'put':
                resp = req.put(params=params, json=json, data=data)
            else:
                resp = req.delete(params=params, json=json, data=data, body=body)
        except Exception as e:
            print ("Runner failed with exception", e)   
        
        return resp