
import unittest
from word_ladder import word_ladder as wl

class test_word_ladder(unittest.TestCase):
    
    def test_one(self):
        transformations = wl("hit", "cog", {"hot", "dot", "dog", "lot", "log", "cog"})
        self.assertEqual(transformations, 5)
        
    
    def test_two(self):
        transformations = wl("hit", "dog", {"hot", "dot", "dog", "lot", "log", "cog"})
        self.assertEqual(transformations, 4)
        
    
    def test_three(self):
        transformations = wl("hit", "cog", {"hot", "dot", "dog", "lot", "log"})
        self.assertEqual(transformations, 0)
        
    def test_four(self):
        transformations = wl("hit", "hit", {"hit"})
        self.assertEqual(transformations, 1)