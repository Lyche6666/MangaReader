# test_mangareader.py
"""
Tests for MangaReader module.
"""

import unittest
from mangareader import MangaReader

class TestMangaReader(unittest.TestCase):
    """Test cases for MangaReader class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MangaReader()
        self.assertIsInstance(instance, MangaReader)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MangaReader()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
