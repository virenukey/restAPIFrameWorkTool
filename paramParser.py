class Paramparser(object):
    @staticmethod
    def parse(param):
        param = param.encode('ascii')
        params = dict(x.split('=') for x in param.split('&'))
        return params