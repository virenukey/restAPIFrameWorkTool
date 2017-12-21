try:
    import pyexcel
    from runner import Runner
    import setupTest
    import argparse
except ImportError as e:
    print ("Import of module in test failed", e)


parser = argparse.ArgumentParser(description='to select particular url to test')   
parser.add_argument('-u','--urlNum', help='Description for foo argument', required=True)
args = parser.parse_args()
my_dict = {}
url = None
setuptest = setupTest.setupTest

def testSetup():
    fileName = setuptest['location']+'\\'+setuptest['fileName']
    my_dict = pyexcel.get_dict(file_name=fileName, name_columns_by_row=0)
    return my_dict

def testRun():
    try:
        my_dict = testSetup()
        if args.urlNum == 'all':
            for i, url in enumerate(my_dict['BaseUrl']):
                print ("Running test case %d" % (i+1))
                print ("Description: %s" %(my_dict['Description'][i]))
                try:
                    resp = Runner.runTest(baseurl=url, path=my_dict['Path'][i], params=my_dict['Params'][i], 
                                   body=my_dict['Body'][i], json=my_dict['Json'][i], data=my_dict['Data'][i], 
                                   files=None, auth=my_dict['Auth'][i], method=my_dict['Method'][i])
                
                    assert (my_dict['Expected'][i] == resp.status_code)
                except Exception as e:
                    print ("Test case %d failed" % (i+1))
                    continue
                else:
                    print ("Test case %d passed" % (i+1))
        else:
            try:
                a = int(args.urlNum)-1
                print ("Description: %s" %(my_dict['Description'][a]))
                resp = Runner.runTest(baseurl=my_dict['BaseUrl'][a], path=my_dict['Path'][a], params=my_dict['Params'][a], 
                                    body=my_dict['Body'][a], json=my_dict['Json'][a], data=my_dict['Data'][a], 
                                    files=None, auth=my_dict['Auth'][a], method=my_dict['Method'][a])
                
                assert (my_dict['Expected'][a] == resp.status_code)
            except Exception as e:
                    print ("Test case %d failed" % (a+1))
            else:
                    print ("Test case %d passed" % (a+1))
            
    except Exception as e:
        print ("caught exception during test run", e)
        
        
if __name__ == '__main__':
    testRun()
    