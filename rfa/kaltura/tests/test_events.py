"""Event handler testing"""

import unittest
from base import TestCase

from rfa.kaltura.events.events import modifyVideo

class ModifyVideoTests(TestCase):
    
    def testDescriptionChange(self):
        
        context = DummyContext()
        event = DummyEvent()
        
        modifyVideo(context,event)
        
        assertEqual(context.Description(), context.KalturaObject.getDescription())
        
        


class DummyKalturaObject(object):

    def __init__(self):
        self._name = "Dummy Title"
        self._description = "Dummy Description"
        self._partnerId = None
        self._categoriesIds = ''
        self._tags = ''
    
    def getName(self):
        return self._name
    
    def getDescription(self):
        return self._description
    
    def getPartnerId(self):
        return self._partnerId
    
    def getCategoriesIds(self):
        return self._categoriesIds
    
    def getTags(self):
        return self._tags

class DummyContext(object):
    
    def __init__(self):
        self.KalturaObject = DummyKalturaObject()
        self._title = "Dummy Title"
        self._description = "Dummy Description"
        self._partnerId = None
        self._categories = []
        self._tags = []
        
    def Title(self):
        return self._title
    
    def Description(self):
        return self._description
    
    def getPartnerId(self):
        return self._partnerId
    
    def getCategories(self):
        return self._categories
    
    def getTags(self):
        return self._tags
    
    def updateTags(self):
        pass
    
    def updateCategories(self):
        pass
    
    def _updateRemote(self, **kwargs):
        #simulate communication between Plone and Kaltura Server
        newDescription = kwargs.get('Description')
        if newDescription is not None:
            self.KalturaObject._description = newDescription
        

class DummyEvent(object):
    pass



def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(ModifyVideoTests),
        ))

if __name__ == "__main__":
    suite = test_suite()
    unittest.TextTestRunner(verbosity=2).run(suite)

