try:
    from api import Api
    from requests.auth import HTTPBasicAuth, HTTPDigestAuth
    from requests_oauthlib import OAuth1
except ImportError as e:
    print ("Import of module in test failed", e)


class ApiAuth(Api):
    def __init__(self, url, auth):
        super(ApiAuth, self).__init__(url)
        self.auth = auth
        
    def httpBasicAuth(self):
        try:
            r = self.get(self.url, auth=HTTPBasicAuth(self.auth['user'], self.auth['pass']))
        except Exception as e:
            print ("Exception in GET HttpBasicAuth request", e)
        return r
    
    def httpDigestAuth(self):
        try:
            r = self.get(self.url, auth=HTTPDigestAuth(self.auth['user'], self.auth['pass']))
        except Exception as e:
            print ("Exception in GET HttpDigestAuth", e)
        return r
    
    def oAuth(self):
        try:
            r = self.get(self.url, auth=OAuth1(self.auth['apiKey'], self.auth['appSecret'], 
                        self.auth['oAuthToken'], self.auth['oAuthTokenSecret']))
        except Exception as e:
            print ("Exception in GET oAuth request", e)
        return r
    
    