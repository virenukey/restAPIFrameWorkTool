import pyexcel
import setupTest
from babel._compat import itervalues, iterkeys

class DataRead(object):
       
    @staticmethod
    def readData(file):
        setuptest = setupTest.testData(file)
        fileName = setuptest['location']+'\\'+setuptest['fileName']
        my_dict = pyexcel.get_dict(file_name=fileName, name_columns_by_row=0)
        return my_dict
    
    @staticmethod
    def dataDict(my_dict, i):
        newdict = {}
        _len = len(my_dict) - 1
        try:
            for k in iterkeys(my_dict):
                if (_len < i):
                    break
                    
                else:
                    newdict[k] = my_dict[k][i]
        except Exception as e:
            print ("Exception in dataRead class with dataDict method, due to", e)    
            
        if newdict:
            a = [str(i) for i in itervalues(newdict)]
            print ("Verifying test case for value combination \"%s\"" % (','.join(a)))
            return newdict
        else:
            return None