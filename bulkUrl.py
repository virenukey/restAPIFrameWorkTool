try:
    import pyexcel
    from runner import Runner
    import setupTest
    import argparse
    from logger import Log
except ImportError as e:
    print ("Import of module in test failed", e)


parser = argparse.ArgumentParser(description='to select particular url to test')   
parser.add_argument('-u','--urlNum', help='Description for foo argument', required=True)
args = parser.parse_args()
my_dict = {}
url = None
setuptest = setupTest.setupTest
log = Log()

def testSetup():
    log.logger.warning("Getting test case file name")
    log.logger.info("Setting file location for test case")
    fileName = setuptest['location']+'\\'+setuptest['fileName']
    
    log.logger.warning("Reading test data from %s" % fileName)
    log.logger.info("Still reading test data from %s" % fileName)
    my_dict = pyexcel.get_dict(file_name=fileName, name_columns_by_row=0)
    return my_dict

def testRun():
    try:
        my_dict = testSetup()
        log.logger.warning("Into test case execution")
        log.logger.info("Executing test cases")
        if args.urlNum == 'all':
            log.logger.warning("Executing all Test cases")
            log.logger.info("Executing all test cases")
            for i, url in enumerate(my_dict['BaseUrl']):
                print ("Running test case %d" % (i+1))
                print ("Description: %s" %(my_dict['Description'][i]))
                try:
                    log.logger.warning("Executing test case %d" % (i+1))
    
                    resp = Runner.runTest(baseurl=url, path=my_dict['Path'][i], params=my_dict['Params'][i], 
                                   body=my_dict['Body'][i], json=my_dict['Json'][i], data=my_dict['Data'][i], 
                                   files=None, auth=my_dict['Auth'][i], method=my_dict['Method'][i])
                    
                    log.logger.warning("Verifying test case %d with expected result" % (i+1))
                    assert (my_dict['Expected'][i] == resp.status_code)
                except Exception as e:
                    log.logger.error("Test case %d failed" % (i+1))
                    log.logger.debug("Test case \"%s\" failed" % my_dict['Description'][i])
                    print ("Test case %d failed" % (i+1))
                    continue
                else:
                    log.logger.error("Test case %d passed" % (i+1))
                    log.logger.debug("Test case \"%s\" passed" % my_dict['Description'][i])
                    print ("Test case %d passed" % (i+1))
        else:
            try:
                a = int(args.urlNum)-1
                log.logger.warning("Executing test case %d" % (a+1))
                print ("Description: %s" %(my_dict['Description'][a]))
                print ("Running test case %d" % (a+1))
                resp = Runner.runTest(baseurl=my_dict['BaseUrl'][a], path=my_dict['Path'][a], params=my_dict['Params'][a], 
                                    body=my_dict['Body'][a], json=my_dict['Json'][a], data=my_dict['Data'][a], 
                                    files=None, auth=my_dict['Auth'][a], method=my_dict['Method'][a])
                
                log.logger.warning("Verifying test case %d with expected result" % (a+1))
                assert (my_dict['Expected'][a] == resp.status_code)
            except Exception as e:
                log.logger.error("Test case %d failed" % (a+1))
                log.logger.debug("Test case \"%s\" failed" % my_dict['Description'][a])
                print ("Test case %d failed" % (a+1))
            else:
                log.logger.error("Test case %d passed" % (a+1))
                log.logger.debug("Test case \"%s\" passed" % my_dict['Description'][a])
                print ("Test case %d passed" % (a+1))
            
    except Exception as e:
        print ("caught exception during test run", e)
        
        
if __name__ == '__main__':
    testRun()
    