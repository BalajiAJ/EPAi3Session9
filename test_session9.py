from session9 import *
from datetime import datetime
import pytest
from io import StringIO 
import sys
import time
import inspect
import os
import session9
import re
import math

def test_randomprofiles_namedtuple():
    assert bool(session9.randomprofiles_namedtuple()), 'no value true returned something is wrong'

def test_randomprofiles_namedtuple_docsrting():
    summaryprofilenamedtup = session9.randomprofiles_namedtuple()
    assert bool(summaryprofilenamedtup.__doc__), 'no docstring for named tuple  something is wrong'
def test_meancurrentlocation():
    summaryprofilenamedtup = session9.randomprofiles_namedtuple()
    assert str(type(summaryprofilenamedtup.meancurrentlocation)).__contains__('tuple'), "mean location needs to be a tuple"

def test_allvalues():
    summaryprofilenamedtup = session9.randomprofiles_namedtuple()
    assert bool(summaryprofilenamedtup.meancurrentlocation), "no value for mean current location"
    assert bool(summaryprofilenamedtup.averageage), "no value for average age"
    assert bool(summaryprofilenamedtup.largestbloodtype), "no value for largest blood type"
    assert bool(summaryprofilenamedtup.oldestpersonage), "no value for oldest person age"
    

def test_oldestage():
    summaryprofilenamedtup = session9.randomprofiles_namedtuple()
    assert summaryprofilenamedtup.averageage <= summaryprofilenamedtup.oldestpersonage, "average age cannot be more than oldest age"

def test_randomprofiles_dict():
    assert bool(session9.randomprofiles_dict()), 'no value true returned something is wrong'


def test_meancurrentlocation_dict():
    summaryprofilenameddict = session9.randomprofiles_dict()
    assert str(type(summaryprofilenameddict["meancurrentlocation"])).__contains__('tuple'), "mean location needs to be a tuple"

def test_allvalues_dict():
    summaryprofilenameddict = session9.randomprofiles_dict()
    assert bool(summaryprofilenameddict["meancurrentlocation"]), "no value for mean current location"
    assert bool(summaryprofilenameddict["averageage"]), "no value for average age"
    assert bool(summaryprofilenameddict["largestbloodtype"]), "no value for largest blood type"
    assert bool(summaryprofilenameddict["oldestpersonage"]), "no value for oldest person age"
    

def test_oldestage_dict():
    summaryprofilenameddict = session9.randomprofiles_dict()
    assert summaryprofilenameddict["averageage"] <= summaryprofilenameddict["oldestpersonage"], "average age cannot be more than oldest age"

def test_dict():
    summaryprofilenameddict = session9.randomprofiles_dict()
    assert str(type(summaryprofilenameddict)).__contains__('dict'), "should return a dictionary"

def test_top100companystock():
    assert bool(session9.top100companystock()), 'no value true returned something is wrong'

def test_top100companydata():
    assert bool(session9.top100companydata()), 'no value true returned something is wrong'

def test_top100companystock_high_check():
    top100companystock = session9.top100companystock()
    assert top100companystock.high >= top100companystock.close , "close cannot be greater than high value"
    assert top100companystock.high >= top100companystock.open , "open cannot be greater than high value"

def test_top100companystock_reasonable():
    top100companystock = session9.top100companystock()
    assert math.isclose(top100companystock.high,top100companystock.close,abs_tol=500), "close cannot be greater than high value"
    #assert top100companystock.high >= top100companystock.open , "open cannot be greater than high value"

def test_def_top100companydata():
    assert bool(session9.top100companydata()), 'no value true returned something is wrong'

def test_top100companystock_allvalues():
    top100companystock = session9.top100companystock()
    assert bool(top100companystock.high), "no value for high"
    assert bool(top100companystock.open), "no value for open"
    assert bool(top100companystock.close), "no value for close"

def test_top100companydata_allvalues():
    top100companydata = session9.top100companydata()
    assert bool(top100companydata[0].compname), "no value for compname"
    assert bool(top100companydata[0].marketcap), "no value for marketcap"
    assert bool(top100companydata[0].date1), "no value for date1"
    assert bool(top100companydata[0].scrip), "no value for scrip"
    assert bool(top100companydata[0].open), "no value for open"
    assert bool(top100companydata[0].close), "no value for close"
    assert bool(top100companydata[0].high), "no value for high"

def test_top100companystock_docstring():
    top100companystock = session9.top100companystock()
    assert bool(top100companystock.__doc__), 'no docstring for named tuple  something is wrong'
    assert bool(top100companystock.high.__doc__), 'no docstring for named tuple  something is wrong'
    assert bool(top100companystock.open.__doc__), 'no docstring for named tuple  something is wrong'
    assert bool(top100companystock.close.__doc__), 'no docstring for named tuple  something is wrong'

def test_top100companydata_docstring():
    top100companydata = session9.top100companydata()
    assert bool(top100companydata[0].__doc__), 'no docstring for named tuple  something is wrong'

def test_top100companydata_highlow_verify():
    top100companydata = session9.top100companydata()
    assert top100companydata[0].open <= top100companydata[0].high, "high must the highest value in a day"
if __name__ == '__main__':
    test_randomprofiles_namedtuple()