import unittest
import twitterverse_functions as tf


class TestGetFilterResults(unittest.TestCase):
    '''Your unittests here'''
    def setUp(self):
        self.data_file = open('data.txt')
        self.data = tf.process_data(self.data_file)
    
    def tearDown(self):
        self.data_file.close()
    
    def test_empty_filter_query(self):
        '''test if the filter query does not contain commands    '''
        self.assertEqual(tf.get_filter_results(self.data, ['tomCruise'], 
                                              {}), ['tomCruise'])
    def test_empty_search_result(self):
        '''test if nothing was generated from the search_result  '''        
        self.assertEqual(tf.get_filter_results(self.data, [], 
                                              {'follower':'PerezHilton','following':'NicoleKidman','location-includes':'Los Angeles',
                                            'name-includes':'tom'}), [])
    def test_name_includes(self):
        '''test if the function filters appropriately when the option is 'name-includes' '''
        self.assertEqual(tf.get_filter_results(self.data, ['tomCruise','Tommy','tomas','bottOm'], 
                                              {'name-includes':'tom'}), ['tomCruise','tomas'])  
    def test_location_includes(self):
        '''test if the function filters appropriately when the option is 'location-includes' '''
        self.assertEqual(tf.get_filter_results(self.data, ['tomCruise'], 
                                               {'location-includes':'Los Angeles'}), ['tomCruise']) 
    def test_location_not_includes(self):
        '''test if the function filters appropriately when the option is 'location-includes' and the location
        does not match
        '''
        self.assertEqual(tf.get_filter_results(self.data, ['tomCruise'], 
                                               {'location-includes':'USA'}), [])
    def test_following_includes(self):
        '''test if the function filters appropriately when the option is 'following' '''
        self.assertEqual(tf.get_filter_results(self.data, ['tomCruise'], 
                                           {'following':'NicoleKidman'}), ['tomCruise'])
    def test_following_not_includes(self):
        '''test if the function filters appropriately when the option is 'following' and no users
        under the following dictionary match'''
        self.assertEqual(tf.get_filter_results(self.data, ['tomCruise'], 
                                           {'following':'Obama'}), [])   
    def test_follower_inclues(self):
        '''test if the function filters appropriately when the option is 'follower' '''
        self.assertEqual(tf.get_filter_results(self.data, ['tomCruise'], 
                                           {'follower':'PerezHilton'}), ['tomCruise'])   
    def test_follower_not_inclues(self):
        '''test if the function filters appropriately when the option is 'follower' and no users
        under the following dictionary match'''        
        self.assertEqual(tf.get_filter_results(self.data, ['tomCruise'], 
                                           {'follower':'q'}), [])   
    def test_all_filters(self):
        ''' test if the function filters appropriately when all the options are being called. '''
        self.assertEqual(tf.get_filter_results(self.data, ['tomCruise'], 
                                           {'follower':'PerezHilton','following':'NicoleKidman','location-includes':'Los Angeles',
                                            'name-includes':'tom'}), ['tomCruise'])    
if __name__ == '__main__':
    unittest.main(exit=False)
