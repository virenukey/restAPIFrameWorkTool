try:
    from api import Api
    import constructURL
    from dataRead import DataRead
    from paramParser import Paramparser
    from logger import Log
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
                auth=None, method=None, dataCount=0):
        
        try:
            url = constructURL.constURL(baseurl=baseurl, 
                                        path=path)
     
            req = Api(url=url)
            
            if params:
                    params = DataRead.readData(params)
                    params = DataRead.dataDict(params, dataCount)
                    
            if data:
                    data = DataRead.readData(data)
                    data = DataRead.dataDict(data, dataCount)
                    
            if json:
                json = DataRead.readData(json)
                json = DataRead.dataDict(json, dataCount)
              
            if method == 'get':
                resp = req.get(params=params)   
            elif method == 'post':
                resp = req.post(json=json, data=data)
            elif method == 'put':
                resp = req.put(params=params, json=json, data=data)
            else:
                resp = req.delete(params=params, json=json, data=data, body=body)
                
        except Exception as e:
            print ("Exception occurred during runner as", e)
        
        return resp