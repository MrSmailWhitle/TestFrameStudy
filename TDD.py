#! /usr/bin/env python
#coding=utf-8
class TestCase:
    def __init__(self,name):
        self.name=name
    def Setup(self):
        pass
    def run(self,result):
        result.testStart()
        self.Setup()
        try:    
            method=getattr(self,self.name)
            method()
        except:
            result.testFailed()
        self.teardown()
    def teardown(self):
        pass

class Havenrun(TestCase):
    def __init__(self,name):
        TestCase.__init__(self,name)
        self.havenrun=None
    def testmethod(self):
        self.havenrun=True
        self.log=self.log+"testmethod"
    def Setup(self):
        self.log="Setup"
        #self.isSetup=1
    def teardown(self):
        self.log=self.log+"teardown"
    def testBrokenMethod(self):
        raise Exception
class TestResult:
    def __init__(self):
        self.runcount=0
        self.errorcount=0
    def testStart(self):
        self.runcount=self.runcount+1
    def sumMary(self):
        return "%d run,%d failed"%(self.runcount,self.errorcount)
    def testFailed(self):
        self.errorcount=self.errorcount+1

class TestCaseTest(TestCase):
    def Setup(self):
        self.result=TestResult()
    def testSetup(self):
        self.test=Havenrun("Setup")
        self.test.run()
        print self.test.log
    def testmethod(self):
        self.test=Havenrun("testmethod")
        self.test.run()
        #print self.test.isSetup
        print self.test.log
        #assert("Setuptestmethodteardown"==self.test.log)
    def testResult(self):
        test=Havenrun("testmethod")
        result=test.run()
        print result.sumMary()
    def testFailedResult(self):
        test=Havenrun("testBrokenMethod")
        result=TestResult()
        test.run(result)
        print test.log
    def testFailedResultFormatting(self):
        result=TestResult()
        result.testStart()
        result.testFailed()
        print result.sumMary()
    def testSuite(self):
        suite=TestSuite()
        suite.add(Havenrun("testMethod")) 
        suite.add(Havenrun("testBrokenMethod"))
        result=TestResult()
        suite.run(result)
        print result.sumMary()
        
class TestSuite:
    def __init__(self):
        self.tests=[]
    def add(self,test):
        self.tests.append(test)
    def run(self,result):
        for test in self.tests:
            test.run(result)
            
#TestCaseTest("testSetup").run()
#TestCaseTest("testnewSetup").run()
#TestCaseTest("testResult").run()
#TestCaseTest("testFailedResult").run()
#TestCaseTest("testFailedResultFormatting").run()
#TestCaseTest("testSuite").run()
suite=TestSuite()
suite.add(TestCaseTest("testSetup"))
suite.add(TestCaseTest("testmethod"))
suite.add(TestCaseTest("testFailedResultFormatting"))
result=TestResult()
suite.run(result)
print result.sumMary()