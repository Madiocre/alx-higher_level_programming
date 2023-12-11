from models.base import Base
import unittest

class TestBase(unittest.TestCase):
    '''Tests the Base class.'''

    def setUp(self):
        '''Imports module, instantiates class'''
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        '''Cleans up after each test_method.'''
        pass

    def test_A_nb_objects_private(self):
        '''Tests if nb_objects is private class attribute.'''
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_B_nb_objects_initialized(self):
        '''Tests if nb_objects initializes to zero.'''
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_C_instantiation(self):
        '''Tests Base() instantiation.'''
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})
        self.assertEqual(b.id, 1)

    def test_E_consecutive_ids(self):
        '''Tests consecutive ids.'''
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_F_id_synced(self):
        '''Tests sync between class and instance id.'''
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)
if __name__=='__main__':
	unittest.main()