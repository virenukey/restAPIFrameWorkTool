Framework tool for RESTFul API test
====================================

Framework for testing (RESTful) HTTP/HTTPS APIs
=================================================
This framework tool allows you to test for various REST URL APIs with various Input Parameters.
The test case can just be written to xlsx sheet and will be consumed by driver written in Python


Advantage of this framework
============================
Testing RESTful APIs generally involves two prediticable steps -

- Invoke the API end point
- Validate the response - headers, payload etc

Most of the time, end user or manual tester are not fond of doing programming or end user reluctant of doing coding to test their REST API.
For them, most easiest way, is to write test cases into Microsoft Excel tool with various input parameters and expected output.
This framework supports HTTP/HTTPS RestAPI calls including all available Authentication support (OAuth, HttpBasicAuth, HttpDigestAuth)


# Practical uses of "RESTFul API Test"
- Perform "integration" testing of internal and external API endpoints
- Examine and test complex response payloads
- You can simply use this framework to dump and analyze API responses - headers, payload etc.


Prerequisites
================
Using Python pip install following packages:
1. pip install pyexcel
2. pip install requests
3. pip install requests_oauthlib

Note: framework has been developed run and verified on 64 bit Windows platform. 
This framework tool is only meant for Windows platform as we are maintaining Microsoft Excel for data input

Components
===========
1. Class Api : This is base class wrapper for all Rest API methods (GET, POST, PUT, DELETE)
2. Class ApiAuth: This clild to Api for API authentications
3. scripts/testcase1.xlsx : This is file to define your test data for each test case with expected output
4. setupTest.py : This define path to your test data file
5. Runner.py : Main Engine to read data and run test case
6. scripts: Consists of individual test cases
7. bulkUrl.py : Driver file to drive and run test cases
8. constructURL: Constructs the REST URL

Example Test case
=================
Please refer following example test case to tests various REST URL in its individual methods e.g GET, POST..etc
- testcase1.xlsx

Run a test
==========
Individual test case can be run using command:
- python bulkUrl.py -u all (To verify all REST URLs mentioned in xlsx sheet)
- python bulkUrl.py -u 3 (To verify specific REST URL, in this case url number 3)


Limitations
=============
1. Need to incorporate REST DELETE methods
2. Neet to parse HTML and XLM responses

Enhancements
=============
1. Dynamic test data to be implemented e.g. to verify REST URL with various data combinations as a part of Parameters
2. Doc strings need to be implemented
3. Coding standards need to be implemented

# restAPIFrameWorkTool
